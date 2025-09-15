# Kapalı Yol Tespiti (YOLOv11m)

Bu proje, YOLOv11m kullanılarak eğitilmiş **kapalı yol tespiti modeli** içerir.  
Model `best.pt` dosyası ile birlikte gelir, böylece tekrar eğitim yapmanıza gerek kalmaz.

---

## 🚀 Kurulum (Detaylı)

### 1. Python ve Ortam Hazırlığı

- **Python 3.8+** kurulu olmalı.
- Sanal ortam kullanmanız önerilir:

```bash
python -m venv yolov11-env
source yolov11-env/bin/activate # (Linux/Mac)
yolov11-env\Scripts\activate    # (Windows)
```

### 2. Depoyu Klonlayın

```bash
git clone https://github.com/InaginiI/YOLOV11-medium.git
cd YOLOV11-medium
```

### 3. Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```
- `requirements.txt` dosyasında PyTorch, OpenCV ve diğer gereklilikler yer almaktadır.

### 4. Model Dosyası Kontrolü

- `best.pt` dosyasının ana dizinde olduğundan emin olun.
- Aksi takdirde, modeli indirmeniz veya eğitmeniz gerekir.

### 5. Test Görsellerini Hazırlayın

- Tahmin yapmak istediğiniz görselleri `test_images/` klasörüne ekleyin.
- Örnek: `test_images/yol1.jpg`, `test_images/yol2.png`

---

## 🔎 Kullanım

### Temel Kullanım

```bash
python predict.py
```

Tahminler, `test_images/` klasöründeki tüm görseller için çalıştırılır. Sonuçlar `runs/predict/` klasörüne kaydedilecektir.

### Komut Satırı ile Örnek Kullanım

```bash
python predict.py --source test_images/
```
- `--source` ile farklı bir klasördeki görselleri de kullanabilirsiniz.

### Sonuçların İncelenmesi

- Çıktılar: `runs/predict/exp/` klasöründe, orijinal resimlerin üzerine modelin çizdiği kutucuklar ile kaydedilmiş halleri bulunur.
- Örnek çıktı dosya yolu: `runs/predict/exp/yol1.jpg`

### Örnek Çıktı Açıklaması

- Her tahmin edilen görsel üzerinde kapalı yol alanları kutucuk ile işaretlenir.
- Kutucukların etiket bilgisi ve olasılık skorları görselin üzerinde gösterilir.

---

## 🎞️ Video Tahmini ve Görüntü Ön İşleme

Son güncellemelerle birlikte, artık video dosyaları üzerinde kapalı yol tespiti ve görüntü ön işleme desteği de eklenmiştir.

### Video Tahmini

Bir video üzerinde tahmin çalıştırmak için:

```bash
python predict.py --source path/to/video.mp4
```
- Video dosyasının yolunu `--source` parametresi ile belirtebilirsiniz.
- Sonuçlar, `runs/predict/exp` altında kare kare işlenmiş ve kutucuklar eklenmiş olarak kaydedilir.

### Görüntü Ön İşleme

Kodda yer alan otomatik ön işleme adımları sayesinde giriş görselleriniz, model için uygun boyuta ve biçime dönüştürülür. Bu işlemler otomatik olarak `predict.py` içinde çalışır, ekstra bir işleme gerek yoktur.

---

## 📄 Ek Bilgiler

- Daha fazla test için farklı resimleri veya videoları `test_images/` klasörüne ekleyebilirsiniz.
- Model ve kodlar üzerinde değişiklik yapmak için `predict.py` ve `models/` klasörünü inceleyiniz.

---

## 🛠️ Destek

Sorularınız için GitHub Issues üzerinden iletişime geçebilirsiniz.
