import os
from preprocessing import preprocess_image
from utils import save_image

def main():
    input_dir = 'input'
    output_dir = 'output'

    # Pastikan folder output ada
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Memproses semua gambar di folder input
    for filename in os.listdir(input_dir):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            # Pra-proses gambar
            processed_image = preprocess_image(input_path)
            
            # Simpan hasilnya ke output folder
            save_image(processed_image, output_path)
            print(f"Proses {filename} selesai. Gambar disimpan di {output_path}")

if __name__ == "__main__":
    main()
