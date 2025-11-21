from PIL import Image, ImageFilter

# Load gambar yang sudah dibuat dari pycairo
img = Image.open("assets/bg_utama.png")

# Tambahkan efek blur (semakin besar radius = semakin blur)
blurred = img.filter(ImageFilter.GaussianBlur(radius=8))

# Simpan hasilnya
blurred.save("assets/bg_utama_blur.png")

print("Background blur berhasil dibuat → assets/bg_utama_blur.png")
