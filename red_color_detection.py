import cv2
import numpy as np

# Test görüntüsü (kırmızı kare)
img = np.ones((300, 300, 3), dtype=np.uint8) * 255
cv2.rectangle(img, (100, 100), (200, 200), (0, 0, 255), -1)

# HSV'ye çevir
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Kırmızı renk aralığı (HSV)
lower_red = np.array([0, 100, 100])     # Alt sınır
upper_red = np.array([10, 255, 255])    # Üst sınır

# Maske oluştur (sadece kırmızılar beyaz)
mask = cv2.inRange(hsv, lower_red, upper_red)

# Sonucu göster
cv2.imshow('Orijinal', img)
cv2.imshow('Kırmızı Maske', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()