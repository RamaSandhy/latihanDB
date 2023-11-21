import tkinter as tk
from tkinter import messagebox
import sqlite3

# Fungsi untuk memprediksi prodi berdasarkan nilai
def hasil_prediksi():
    # Mendapatkan nilai dari entry
    nama_siswa = entry_nama.get()
    nilai_biologi = float(entry_biologi.get())
    nilai_fisika = float(entry_fisika.get())
    nilai_inggris = float(entry_inggris.get())

    # Memprediksi prodi berdasarkan nilai tertinggi
    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
        prediksi_fakultas = "Kedokteran"
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        prediksi_fakultas = "Teknik"
    elif nilai_inggris > nilai_biologi and nilai_inggris > nilai_fisika:
        prediksi_fakultas = "Bahasa"
    else:
        prediksi_fakultas = "Tidak dapat diprediksi"

    # Menampilkan hasil prediksi di label
    label_hasil.config(text=f"Hasil Prediksi: {prediksi_fakultas}")

    # Menyimpan data ke SQLite
    simpan_data(nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prediksi_fakultas)

# Fungsi untuk menyimpan data ke SQLite
def simpan_data(nama_siswa, biologi, fisika, inggris, prediksi_fakultas):
    try:
        # Membuat atau membuka koneksi ke database SQLite
        connection = sqlite3.connect("data_siswa.db")
        cursor = connection.cursor()

        # Membuat table jika belum ada
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS nilai_siswa (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_siswa TEXT,
                biologi REAL,
                fisika REAL,
                inggris REAL,
                prediksi_fakultas TEXT
            )
        ''')

        # Menyimpan data ke dalam tabel
        cursor.execute('''
            INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
            VALUES (?, ?, ?, ?, ?)
        ''', (nama_siswa, biologi, fisika, inggris, prediksi_fakultas))

        # Commit perubahan dan tutup koneksi
        connection.commit()
        connection.close()

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

# Membuat GUI
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")

# Membuat label judul
label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Helvetica", 16))
label_judul.grid(row=0, column=0, columnspan=2, pady=10)

# Membuat entry untuk nama siswa
label_nama = tk.Label(root, text="Nama Siswa:")
label_nama.grid(row=1, column=0, sticky="e", pady=5)
entry_nama = tk.Entry(root)
entry_nama.grid(row=1, column=1, pady=5)

# Membuat entry untuk nilai biologi
label_biologi = tk.Label(root, text="Nilai Biologi:")
label_biologi.grid(row=2, column=0, sticky="e", pady=5)
entry_biologi = tk.Entry(root)
entry_biologi.grid(row=2, column=1, pady=5)

# Membuat entry untuk nilai fisika
label_fisika = tk.Label(root, text="Nilai Fisika:")
label_fisika.grid(row=3, column=0, sticky="e", pady=5)
entry_fisika = tk.Entry(root)
entry_fisika.grid(row=3, column=1, pady=5)

# Membuat entry untuk nilai inggris
label_inggris = tk.Label(root, text="Nilai Inggris:")
label_inggris.grid(row=4, column=0, sticky="e", pady=5)
entry_inggris = tk.Entry(root)
entry_inggris.grid(row=4, column=1, pady=5)

# Membuat button untuk hasil prediksi
button_prediksi = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
button_prediksi.grid(row=5, column=0, columnspan=2, pady=10)

# Membuat label untuk hasil prediksi
label_hasil = tk.Label(root, text="Hasil Prediksi:")
label_hasil.grid(row=6, column=0, columnspan=2, pady=5)

# Menjalankan aplikasi
root.mainloop()