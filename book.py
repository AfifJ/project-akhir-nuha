import streamlit as st
import pandas as pd
from firebase_admin import firestore

import firebase_admin
from firebase_admin import credentials

# Use a service account.
cred = credentials.Certificate('fir-nuha-firebase-adminsdk-pab87-c48ad1e9a4.json')

if not firebase_admin._apps:
  app = firebase_admin.initialize_app(cred)

# Use a service account.
db = firestore.client()

def app():
    st.subheader('Jual beli e-book')
    st.write('Selamat datang di halaman pembelian e-book')


    docs = db.collection("daftar-buku").stream()

    listJudul = []
    listPenulis = []
    listLink = []
    for doc in docs:
      docData = doc.to_dict()
      listJudul.append(docData['judul'])
      listPenulis.append(docData['penulis'])
      listLink.append(docData['linkDownload'])
      st.write(doc.id)

    book_data = {
        "Judul": listJudul,
        "Penulis": listPenulis,
        "Link Download": listLink
    }

    df = pd.DataFrame(book_data)
    st.dataframe(
      df,
      hide_index=True,
    )
    
    with st.expander("Tambah Buku"):
      judul = st.text_input("Judul")
      penulis = st.text_input("Penulis")
      link = st.text_input("Link Download")



      tambah = st.button("Tambah")
      
      if tambah:
        try:
          data = {"judul": f"{judul}", "penulis": f"{penulis}", "linkDownload": f"{link}"}
          db.collection("daftar-buku").document().set(data)
          st.rerun()
        except Exception as e:
          st.warning(f"Menambahkan gagal {e}")