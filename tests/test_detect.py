import os
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_detect_objects():
    image_path = os.path.join(os.path.dirname(__file__), "test_image3.jpg")

    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    response = client.post(
        "/detect/",
        files={"file": ("test_image3.jpg", image_data, "image/jpeg")}
    )

    assert response.status_code == 200
    assert "detections" in response.json()
