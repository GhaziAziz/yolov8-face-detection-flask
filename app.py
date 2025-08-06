from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO

app = Flask(__name__)
model = YOLO("best.pt")  # or your full path to .pt file

cap = cv2.VideoCapture(0)

def gen_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            results = model(frame)[0]
            annotated_frame = results.plot()
            _, buffer = cv2.imencode('.jpg', annotated_frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
