import streamlit as st
import pandas as pd

def app():
    st.subheader('Jual beli e-book')
    st.write('Selamat datang di halaman pembelian e-book')


    # Data persediaan buku
    book_data = {
        "Title": ["Buku A", "Buku B", "Buku C"],
        "Author": ["Penulis A", "Penulis B", "Penulis C"],
        "size": [20, 25 , 18  ]
    }

    # Konversi data menjadi DataFrame pandas
    df = pd.DataFrame(book_data)

    st.table(df)

# Fungsi untuk menampilkan detail buku
    def display_book_details(book):
        st.write(f"**{book['Title']}**")
        st.write(f"Penulis: {book['Author']}")
        st.write(f"size: {book['size']} mb")

    # Sidebar dengan daftar buku
    selected_book = st.sidebar.selectbox("Pilih Buku", df["Title"])

    # Cari buku yang dipilih
    selected_book_info = df[df["Title"] == selected_book].iloc[0]

    # Tampilkan detail buku yang dipilih
    st.header(f"Detail Buku: {selected_book_info['Title']}")
    display_book_details(selected_book_info)

    # Fungsi untuk memproses pembelian
    def process_purchase(book, quantity):
        st.success(f"Terimakasih sudah mendownload {book['Title']} !")

    # Input jumlah buku yang akan dibeli


    # Tombol untuk melakukan pembelian
    if st.button("Download"):
        process_purchase(selected_book_info)