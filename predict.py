import cv2
import numpy as np
import os
from ultralytics import YOLO

# =============================
# --- Ön İşleme Fonksiyonları ---
# =============================

TARGET_SIZE = (960, 544)

def gray_world_white_balance(img):
    """Gray World Beyaz Dengesi"""
    result = img.copy().astype(np.float32)
    avg_b = np.mean(result[:,:,0])
    avg_g = np.mean(result[:,:,1])
    avg_r = np.mean(result[:,:,2])
    avg_gray = (avg_b + avg_g + avg_r) / 3
    result[:,:,0] = np.minimum(result[:,:,0] * (avg_gray / avg_b), 255)
    result[:,:,1] = np.minimum(result[:,:,1] * (avg_gray / avg_g), 255)
    result[:,:,2] = np.minimum(result[:,:,2] * (avg_gray / avg_r), 255)
    return result.astype(np.uint8)

def adjust_gamma(image, gamma=1.2):
    """Gamma düzeltme"""
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                    for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)

def preprocess_image(img):
    """Tüm ön işlemleri uygula"""
    # Yeniden boyutlandır
    img = cv2.resize(img, TARGET_SIZE)

    # 1. Beyaz Dengesi
    img_wb = gray_world_white_balance(img)

    # 2. LAB + CLAHE
    lab = cv2.cvtColor(img_wb, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    img_clahe = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

    # 3. Gamma Correction
    final = adjust_gamma(img_clahe, gamma=1.2)

    return final

# =============================
# --- YOLO Modeli Tahmini ---
# =============================

model = YOLO("best.pt")  # Eğittiğin model # FARKLI MODELE GECERKEN BURADAN ISMINI DEGİSTİR 

# ------------- RESİMLER -------------
# input_dir = "test_images"
# output_dir = "runs/preprocessed_predict"
# os.makedirs(output_dir, exist_ok=True)

# for filename in os.listdir(input_dir):
#     if filename.lower().endswith((".jpg", ".png", ".jpeg")):
#         img_path = os.path.join(input_dir, filename)

#         # Görseli oku ve ön işleme uygula
#         img = cv2.imread(img_path)
#         processed = preprocess_image(img)

#         # YOLO ile tahmin yap
#         results = model.predict(processed, save=False, show=False)

#         # Tahmin sonucunu çizdir
#         annotated = results[0].plot()

#         # Kaydet
#         save_path = os.path.join(output_dir, filename)
#         cv2.imwrite(save_path, annotated)
#         print(f"[OK] Tahmin tamamlandı -> {save_path}")

# print("✅ Tüm görseller işlendi ve tahmin sonuçları kaydedildi.")

# ------------- VİDEO -------------
video_path = "video.mp4"  # test etmek istediğin video
cap = cv2.VideoCapture(video_path)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("runs/preprocessed_predict/output_video.mp4", fourcc, 20.0, TARGET_SIZE)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Ön işleme uygula
    frame_processed = preprocess_image(frame)

    # YOLO tahmini
    results = model.predict(frame_processed, save=False, show=False)
    annotated = results[0].plot()

    # Kaydet ve göster
    out.write(annotated)
    cv2.imshow("Tahmin", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
print("🎥 Video işlendi ve runs/preprocessed_predict/output_video.mp4 olarak kaydedildi.")
