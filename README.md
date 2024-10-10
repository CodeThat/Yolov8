# YOLOv8 Object Detection

This repository contains multiple Python scripts that implement object detection using the YOLOv8 model. The scripts cover a range of functionalities, including live detection from a webcam, video file processing, image prediction, downloading images from Google, benchmarking, validating the model, and training.

## Contents

- `main.py`: Runs YOLOv8 live detection using a webcam.
- `benchmark.py`: Benchmarks the YOLOv8 model on a GPU.
- `download_images.py`: Downloads images from Google Images based on provided keywords.
- `predict.py`: Processes a video file and performs object detection on each frame.
- `predict_images.py`: Predicts objects in images and videos, displaying results.
- `train.py`: Trains the YOLOv8 model using specified datasets.
- `val.py`: Validates the YOLOv8 model and retrieves performance metrics.

## Prerequisites

Before running the scripts, ensure you have the following prerequisites installed:

- Python 3.8 or higher
- Required libraries:
    ```bash
    pip install ultralytics opencv-python simple-image-download Pillow
    ```

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/YourUsername/yolo-object-detection.git
   ```

2. Navigate to the project directory:

   ```bash
   cd yolo-object-detection
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Live Detection

Run the `main.py` script to perform live object detection using your webcam:

```bash
python main.py --webcam-resolution 1280 720
```

### 2. Benchmarking

To benchmark the YOLOv8 model on a GPU, run:

```bash
python benchmark.py
```

### 3. Downloading Images

Use the `download_images.py` script to download images from Google Images. Customize the `keywords` list in the script to specify what you want to download.

```bash
python download_images.py
```

### 4. Video Processing

Process a video file for object detection using the `predict.py` script:

```bash
python predict.py
```

### 5. Image Prediction

Predict objects in images and display results using the `predict_images.py` script. Update the source as needed:

```bash
python predict_images.py
```

### 6. Model Training

Train the YOLOv8 model using a dataset specified in the `train.py` script:

```bash
python train.py
```

### 7. Model Validation

Validate the YOLOv8 model and retrieve performance metrics using the `val.py` script:

```bash
python val.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Prerequisites

Before running the scripts, ensure you have the following prerequisites installed:

- Python 3.8 or higher
- Required libraries:
    ```bash
    pip install ultralytics opencv-python simple-image-download Pillow
    ```

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/YourUsername/yolo-object-detection.git
   
2. Navigate to the project directory
  cd yolo-object-detection

