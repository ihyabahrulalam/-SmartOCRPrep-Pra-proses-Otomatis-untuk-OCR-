import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import os
from preprocessing import preprocess_image
from utils import save_image

class SmartOCRPrepGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SmartOCRPrep - OCR Preprocessing")
        self.root.geometry("400x300")

        self.input_dir = 'input'
        self.output_dir = 'output'

        # Membuat folder input dan output jika belum ada
        if not os.path.exists(self.input_dir):
            os.makedirs(self.input_dir)
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        # Label
        self.label = tk.Label(root, text="Pilih Gambar untuk Diproses", font=("Arial", 14))
        self.label.pack(pady=20)

        # Tombol Pilih Gambar
        self.select_button = tk.Button(root, text="Pilih Gambar", command=self.select_image, font=("Arial", 12))
        self.select_button.pack(pady=10)

        # Progress Bar
        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="indeterminate")
        self.progress.pack(pady=10)

        # Tombol Mulai Proses
        self.process_button = tk.Button(root, text="Proses Gambar", state=tk.DISABLED, command=self.process_image, font=("Arial", 12))
        self.process_button.pack(pady=10)

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png")])
        if file_path:
            self.selected_image = file_path
            self.process_button.config(state=tk.NORMAL)

    def process_image(self):
        try:
            self.progress.start()

            # Mendapatkan nama file dan path
            filename = os.path.basename(self.selected_image)
            output_path = os.path.join(self.output_dir, filename)

            # Pra-proses gambar
            processed_image = preprocess_image(self.selected_image)

            if processed_image is None:
                raise Exception("Gambar tidak dapat diproses!")

            # Simpan gambar hasil pra-pemrosesan
            save_image(processed_image, output_path)

            # Tampilkan pesan sukses
            messagebox.showinfo("Sukses", f"Gambar telah diproses dan disimpan di {output_path}")

        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {e}")
        finally:
            self.progress.stop()
            self.process_button.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = SmartOCRPrepGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
