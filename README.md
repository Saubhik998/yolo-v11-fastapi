
# YOLOv11 FastAPI Object Detection API

A lightweight, containerized API that uses YOLOv11 (Ultralytics) for real-time object detection on uploaded images. Built with FastAPI, it processes image files and returns detected objects along with bounding box coordinates and confidence scores.

##  Features

- Object detection using YOLOv11 nano model (`yolo11n.pt`)
- Unit testing with `pytest`
- Docker support
- FastAPI for blazing-fast performance
- Dependency management via `requirements.txt`

---

## Project Structure

```
yolo-v11-fastapi/
│
├── app/
│   ├── main.py          # FastAPI app with /detect endpoint
│   ├── yolo_model.py    # YOLO model integration
│
├── tests/
│   └── test_detect.py   # Unit test for the API
│
├── Dockerfile           # Docker container definition
├── requirements.txt     # Python dependencies
├── .gitignore           # Git ignored files
└── README.md
```

---

## Running Tests

```bash
pytest
```

Ensure you have a `test_image.jpg` in the `tests/` folder for the test to work.

---

## 🔧 Local Development

### 1. Clone the Repository

```bash
git clone https://github.com/Saubhik998/yolo-v11-fastapi.git
cd yolo-v11-fastapi
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API

```bash
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000/docs` for Swagger UI.

---

## Docker Usage

### Build the Docker Image

```bash
docker build -t yolo-v11-api .
```

### Run the Container

```bash
docker run -p 8000:8000 yolo-v11-api
```

Then open `http://localhost:8000/docs` to test.

---

##Sample Request

You can test the `/detect/` endpoint using [Swagger UI](http://localhost:8000/docs) or using `curl`:

```bash
curl -X POST "http://localhost:8000/detect/" -F "file=@test_image.jpg"
```

---

## Model Info

This project uses the **YOLOv11 Nano** model (`yolo11n.pt`) by Ultralytics, ideal for fast and lightweight inference.



