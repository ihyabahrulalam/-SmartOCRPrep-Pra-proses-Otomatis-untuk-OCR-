import cv2
import numpy as np

def preprocess_image(image_path):
    # Membaca gambar
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Mengecek jika gambar terbaca
    if image is None:
        print(f"Error: Tidak dapat membaca gambar di {image_path}")
        return None

    # Filtering: Gaussian blur untuk mengurangi noise
    image = cv2.GaussianBlur(image, (5, 5), 0)

    # Thresholding: Ubah gambar menjadi biner (hitam-putih)
    _, image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

    # Normalisasi: Mengubah ukuran gambar (jika perlu)
    image = cv2.resize(image, (1000, 1000))  # Ukuran bisa disesuaikan

    return image
