import cv2

def save_image(image, output_path):
    # Mengecek jika gambar valid
    if image is None:
        print(f"Error: Tidak ada gambar untuk disimpan di {output_path}")
        return

    # Menyimpan gambar yang telah diproses
    cv2.imwrite(output_path, image)
    print(f"Gambar disimpan di {output_path}")
