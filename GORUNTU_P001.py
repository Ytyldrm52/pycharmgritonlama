"""import cv2

# Resmi yükle
image_path = 'D:/pythonprojekt/pythonprojekt/resimler/beyaz.jpg'  # Buraya resminizin dosya yolunu yazın
image = cv2.imread(image_path)

# Gri tonlamaya dönüştür
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Sonucu göster
cv2.imshow('Gri Tonlama', gray_image)
cv2.waitKey(0)  # Bir tuşa basana kadar bekle
cv2.destroyAllWindows()  # Pencereleri kapat"""



import cv2
import os

# Resmin dosya yolunu oluştur
image_path = os.path.join('D:\pythonprojekt\pythonProject/resimler/manzara.jpg')
image = cv2.imread(image_path)

# Resmin yüklendiğini kontrol et
if image is None:
    print("Resim yüklenemedi. Lütfen dosya yolunu kontrol edin.")
else:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gri Tonlama', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()