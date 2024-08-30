from ultralytics import YOLO

# Carregar modelo
model = YOLO('model/simple_ai_v1.0.pt')

# Inferencia do modelo
results = model(source='inference/video01.mov', show=True, conf=0.75, save=True)