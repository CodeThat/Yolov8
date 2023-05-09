from ultralytics.yolo.utils.benchmarks import benchmark

# Benchmark on GPU
benchmark(model='yolov8n.pt', imgsz=640, half=False, device=0)
