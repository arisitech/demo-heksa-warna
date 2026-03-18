import tkinter as tk

def tampilkan_jendela_warna(kode_hex, nama_warna=""):
    # 1. Membuat jendela utama
    root = tk.Tk()
    root.title(f"Visualisasi Warna Hex: {kode_hex}")
    
    # 2. Mengatur ukuran jendela (Lebar x Tinggi)
    root.geometry("400x300")
    
    # 3. Mengubah warna latar belakang jendela menggunakan KODE HEX
    # Inilah bagian di mana Python menggunakan heksa untuk warna!
    root.configure(bg=kode_hex)
    
    # 4. Menambahkan label teks di tengah
    # Kita buat teksnya putih agar terlihat di latar belakang gelap
    label = tk.Label(root, text=f"{nama_warna}\n{kode_hex}", 
                     fg="white", bg=kode_hex, font=("Helvetica", 24, "bold"))
    label.pack(expand=True)
    
    # 5. Menjalankan aplikasi
    print(f"Menampilkan jendela dengan warna latar: {kode_hex}")
    root.mainloop()

# --- Area Uji Coba ---

# Silakan ganti kode hex di bawah ini dengan warna favorit Anda!

# Contoh 1: Biru Langit (Sky Blue)
tampilkan_jendela_warna("#3498DB", "Biru Langit")

# Contoh 2: Oranye Terang (Vibrant Orange)
#tampilkan_jendela_warna("#FF5733", "Oranye")

# Contoh 3: Hijau Neon (Lime Green)
# tampilkan_jendela_warna("#32CD32", "Hijau Neon")