# Smart Attendance System (SAS)

A computer vision-based attendance system that uses YOLO (You Only Look Once) for head detection to count and manage attendance. The system is designed to help enforce attendance limits by accurately counting the number of people in a given space.

## Features

- 🎯 Accurate head detection using YOLOv8 model
- 📊 Processes single images with head count results
- 📝 JSON output for easy integration with other systems
- 🚀 Efficient processing with support for GPU acceleration
- 🛠️ Simple command-line interface

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- CUDA-compatible GPU (recommended for better performance)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd SAS
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

To process a specific image:
```bash
python head_counter.py path/to/your/image.jpg
```

To process a random test image from the test_images directory:
```bash
python head_counter.py
```

### Output

The system generates a JSON file at `output/result.json` with the following structure:
```json
{
    "head_count": 5,
    "image_used": "test_images/3.jpg"
}
```

## Project Structure

```
SAS/
├── head_counter.py      # Main script for head counting
├── model/
│   └── best.pt         # YOLO model weights
├── output/              # Output directory for results
├── test_images/         # Sample test images
└── requirements.txt     # Project dependencies
```

## Integration with Web Applications

### Flask API Example

```python
from flask import Flask, request, jsonify
import subprocess
import json
import os

app = Flask(__name__)


@app.route('/count_heads', methods=['POST'])
def count_heads():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    image = request.files['image']
    temp_path = f"temp_{image.filename}"
    image.save(temp_path)
    
    try:
        # Run the head counter
        result = subprocess.run(
            ['python', 'head_counter.py', temp_path],
            capture_output=True,
            text=True
        )
        
        # Read and return the result
        with open('output/result.json') as f:
            result_data = json.load(f)
        
        return jsonify(result_data)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        # Clean up temporary file
        if os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == '__main__':
    app.run(debug=True)
```

## Extending the System

### Future Enhancements

1. **Real-time Video Processing**:
   - Add support for video streams
   - Implement frame skipping for better performance
   - Add tracking for more accurate counting

2. **Attendance Management**:
   - Integrate with a database for attendance records
   - Add user authentication
   - Implement capacity alerts

3. **Web Interface**:
   - Create a dashboard for monitoring
   - Add real-time updates
   - Support for multiple camera feeds

## Performance Considerations

- For production use, ensure you have a CUDA-enabled GPU
- The model works best with clear, well-lit images
- Processing time depends on image resolution and hardware

## Troubleshooting

1. **Model not found**:
   - Ensure `model/best.pt` exists in the correct location
   - Check file permissions

2. **Dependency issues**:
   - Create a virtual environment
   - Reinstall requirements: `pip install -r requirements.txt`

3. **Performance issues**:
   - Reduce image resolution before processing
   - Use GPU acceleration if available
   - Close other resource-intensive applications

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- YOLOv11 by Ultralytics
- OpenCV for image processing
- Python community for awesome libraries
