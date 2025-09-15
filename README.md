# Kapalı Yol Tespiti (YOLOv11m)

Bu proje, YOLOv11m kullanılarak eğitilmiş **kapalı yol tespiti modeli** içerir.  
Model `best.pt` dosyası ile birlikte gelir, böylece tekrar eğitim yapmanıza gerek kalmaz.  

---

## 🚀 Kurulum

git clone https://github.com/InaginiI/YOLOV11-medium.git
cd YOLOV11-medium
pip install -r requirements.txt
python predict.py

##🔎 Kullanım

Test etmek istediğiniz görselleri test_images/ klasörüne ekleyin.
Örneğin:

test_images/
├── yol1.jpg
├── yol2.png


Aşağıdaki komutla tahmin çalıştırın:

python predict.py


Sonuçlar otomatik olarak runs/predict/ klasörüne kaydedilecektir.

Orijinal resimlerin üzerine modelin çizdiği kutucuklar ile kaydedilmiş halleri bulunur.

Örnek yol:

runs/predict/exp/yol1.jpg
