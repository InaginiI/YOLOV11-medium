from ultralytics import YOLO

# Senin eğittiğin modeli yükle
model = YOLO("best.pt")

# Test resimlerinde tahmin yap
results = model.predict(source="test_images", show=True, save=True, project="runs/predict")

print("Tahminler tamamlandı! Sonuçlar runs/predict klasöründe.")
