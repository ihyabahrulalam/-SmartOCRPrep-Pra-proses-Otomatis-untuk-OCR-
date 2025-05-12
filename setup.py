from cx_Freeze import setup, Executable
import os

# Menentukan file atau folder tambahan yang perlu disertakan
include_files = [
    ("input", "input"),
    ("output", "output")
]

# Setup cx_Freeze
setup(
    name="SmartOCRPrep",
    version="1.0",
    description="Aplikasi Preprocessing Otomatis untuk OCR",
    options={
        "build_exe": {
            "packages": ["tkinter", "cv2", "os"],
            "include_files": include_files
        }
    },
    executables=[Executable("gui.py", base="Win32GUI")]
)
