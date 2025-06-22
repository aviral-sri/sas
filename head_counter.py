import os
import sys
import json
import random
from ultralytics import YOLO

# Constants
MODEL_PATH = 'model/best.pt'
IMAGE_DIR = 'test_images'
OUTPUT_DIR = 'output'
OUTPUT_JSON = os.path.join(OUTPUT_DIR, 'result.json')

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def count_heads(image_path):
    try:
        model = YOLO(MODEL_PATH)
        results = model(image_path)

        boxes = results[0].boxes
        head_count = len(boxes)

        result = {
            "head_count": head_count,
            "image_used": image_path
        }

        with open(OUTPUT_JSON, 'w') as f:
            json.dump(result, f)

    except Exception as e:
        with open(OUTPUT_JSON, 'w') as f:
            json.dump({"error": str(e)}, f)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        image_path = sys.argv[1]
    else:
        image_number = random.randint(0, 54)
        image_path = os.path.join(IMAGE_DIR, f"{image_number}.jpg")

    count_heads(image_path)
