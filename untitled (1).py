import streamlit as st
import pandas as pd

# Menu Pengguna
def menu_pengguna():
    st.subheader("Menu Pengguna")
    option = st.selectbox("Pilih Menu", ["Lihat Menu Katering", "Pesan Makanan","Invoice", "Status", "Keluar"])

    if option == "Lihat Menu Katering":
        st.write("Menu Katering: ")
        st.write("1. Nasi Goreng")
        st.write("2. Ayam Penyet")
        st.write("3. Sate")
    elif option == "Pesan Makanan":
        makanan = st.selectbox("Pilih makanan yang ingin dipesan", ["Nasi Goreng", "Ayam Penyet", "Sate"])
        jumlah = st.number_input("Jumlah Porsi", min_value=1, value=1) # Tambahkan input jumlah
        metode_pembayaran = ["Transfer Bank", "GoPay", "OVO"]
        metode = st.selectbox("Pilih Metode Pembayaran", ["Gopay", "Transfer Bank", "Ovo"])
        st.write(f"Anda memesan: {makanan}, Jumlah: {jumlah} Porsi")
        st.write(f"Anda memesan: {makanan}")
        metode = st.selectbox("Pilih Metode Pembayaran", metode_pembayaran)
        st.write(f"Metode Pembayaran: {metode}")
        if metode == "Transfer Bank":
            st.write("Silakan transfer ke rekening BCA 1234567890 a/n Katering Enak")
        elif metode == "GoPay":
            st.write("Silakan bayar melalui GoPay ke nomor 081234567890")

        harga_makanan = {"Nasi Goreng": 15000, "Ayam Penyet": 20000, "Sate": 25000}
        total_harga = harga_makanan[makanan] * jumlah
        st.write(f"Total Pembayaran: Rp {total_harga:,}")
        total_harga = harga_makanan[makanan] * jumlah
        st.write(f"Total Pembayaran: Rp {total_harga:,}")
        st.write(f"Status Pemesanan: {status_pemesanan}")
        st.write("Invoice:")
        st.write(f"Makanan: {makanan}")
        st.write(f"Jumlah: {jumlah} Porsi")
        st.write(f"Total Harga: Rp {total_harga:,}")
        st.write(f"Metode Pembayaran: {metode}")
        st.write(f"Tanggal Pesanan: {tanggal_pesanan}")
        st.write(f"Waktu Pesanan: {waktu_pesanan}")



    elif option == "Keluar":
        st.write("Terima kasih telah menggunakan layanan kami!")
        st.stop()

# Menu Admin
def menu_admin():
    st.subheader("Menu Admin")
    option = st.selectbox("Pilih Menu", ["Tambah Menu Makanan", "Lihat Pesanan", "Keluar"])

    if option == "Tambah Menu Makanan":
        makanan_baru = st.text_input("Masukkan nama makanan baru")
        if st.button("Tambah"):
            st.write(f"Menu makanan '{makanan_baru}' telah ditambahkan.")
    elif option == "Lihat Pesanan":
        # Contoh pesanan
        st.write("Pesanan Hari Ini:")
        st.write("1. Nasi Goreng - 2 Porsi")
        st.write("2. Sate - 1 Porsi")
        st.stop()
    elif option == "Keluar":
        st.write("Keluar dari aplikasi.")
        st.stop()

# Fungsi Login Admin
def login_admin():
    st.subheader("Login Admin")
    email = st.text_input("Masukkan Email:")
    password = st.text_input("Masukkan Password:", type="password")

    if st.button("Login"):
        if email == "admin@example.com" and password == "admin123":
            st.success("Login berhasil!")
            menu_admin()
        else:
            st.error("Email atau password salah. Coba lagi.")

# Fungsi Utama
def main():
    st.title("Aplikasi Katering")

    # Pilih tipe pengguna
    tipe_user = st.selectbox("Pilih Tipe Pengguna", ["Pengguna", "Admin"])

    if tipe_user == "Pengguna":
        menu_pengguna()
    elif tipe_user == "Admin":
        login_admin()

if __name__ == "__main__":
    main()