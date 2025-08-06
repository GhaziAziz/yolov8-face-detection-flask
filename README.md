# yolov8-face-detection-flask
A real-time face detection app using YOLOv8 and Flask, integrated with webcam support and trained on custom friend dataset.

here is a link my drive here is the training process val test train and many more
https://drive.google.com/drive/folders/1rr4judrbWJkfr-z6Me23LYs-2vaa5Say?usp=sharing

## 📁 Project Structure
app.py – Flask app to run the web interface and detection.
static/ – Stores uploaded images and CSS.
templates/ – HTML files for the front-end.
runs/detect/ – YOLOv8 inference results.
models/best.pt – Trained YOLOv8 model.
data.yaml – Dataset configuration.
train/, val/, test/ – Dataset splits.
utils/ – Any helper scripts or functions.


## 🛠️ Installation
bash
git clone https://github.com/your-username/yolov8-face-detection-flask.git
cd yolov8-face-detection-flask
pip install -r requirements.txt
🚀 Run the App
bash
python app.py



---

### 🧠 **Model Training**
Describe how to train the model using YOLOv8:
md
## 🧠 Model Training

1. Prepare your dataset (train, val, test) in YOLO format.
2. Create `data.yaml` with class names and paths.
3. Train with:

bash
yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=100 imgsz=640



---

### 📸 **Webcam & Image Upload**
md
## 📸 Features
- Live webcam face detection.
- Upload images for face detection.
- Real-time results with bounding boxes.


flask
ultralytics
opencv-python


## 📄 License

MIT License

## 🙏 Credits

- Ultralytics for YOLOv8
- Flask team
- Dataset created using X-AnyLabeling

