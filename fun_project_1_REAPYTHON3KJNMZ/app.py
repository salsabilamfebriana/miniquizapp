# import streamlit as st
# from streamlit import session_state as state

# # Judul aplikasi
# st.title("Aplikasi Quiz Sederhana")

# # Teks biasa
# st.write("Selamat datang di aplikasi quiz!")

# # Input teks
# name = st.text_input("Siapa nama Anda?", "Salsa")

# # Tombol
# if st.button("Mulai Quiz"):
#     st.write(f"Halo, {name}! Ayo kita mulai kuisnya.")

# question = "Apa ibu kota Indonesia?"
# options = ["Jakarta", "Bandung", "Surabaya"]

# answer = st.radio(question, options)

# if st.button("Submit Jawaban"):
#     if answer == "Jakarta":
#         st.success("Jawaban kamu benar!")
#     else:
#         st.error("Jawaban salah, coba lagi!")

# score = 0

# qna = {
#     "1 + 1 = ?": "2",
#     "Hewan berkaki 8?": "Laba-laba",
#     "Bahasa pemrograman populer untuk AI?": "Python"
# }

# for q, a in qna.items():
#     user_answer = st.text_input(q, key=q)
#     if user_answer:
#         if user_answer.lower() == a.lower():
#             st.success("Benar!")
#             score += 1
#         else:
#             st.warning("Salah!")

# if st.button("Lihat Skor"):
#     st.write(f"Skor akhir kamu adalah: {score} dari {len(qna)}")

import streamlit as st

# Judul aplikasi
st.title("Quiz Prediksi Generasi")

# Input nama peserta
nama = st.text_input("Masukkan nama kamu", "")

# Tombol mulai quiz: nyalakan flag di session_state
if st.button("Mulai Quiz"):
    if nama:
        st.session_state.quiz_started = True
        st.success(f"Halo, {nama}! Yuk, isi beberapa pertanyaan berikut untuk melihat kamu termasuk generasi apa.")
    else:
        st.warning("Silakan isi nama terlebih dahulu sebelum memulai quiz.")

# Hanya tampilkan quiz jika flag sudah nyala
if st.session_state.get("quiz_started"):

    hp = st.radio("HP yang kamu gunakan sehari-hari:", [
        "Samsung", "iPhone", "Xiaomi", "Oppo", "Lainnya"
    ], key="hp")

    nonton = st.radio("Bagaimana biasanya kamu nonton film?", [
        "Di bioskop",
        "Aku gonta-ganti saluran TV sampai ketemu acara yang menarik",
        "Streaming di HP atau laptop"
    ], key="nonton")

    karir = st.radio("Yang tertulis di CV kamu 20 tahun lagi:", [
        "Satu pekerjaan tetap. Jabatanku naik di satu perusahaan saja.",
        "Lima pekerjaan atau lebih yang unik dan menarik. Pilihanku selalu terbuka dan aku senang mencoba hal baru!",
        "Founder perusahaan besar dari nol. Aku suka menjadi Leader!"
    ], key="karir")

    waktu = st.radio("Mana yang lebih kamu suka, melakukan perjalanan ke masa lalu atau masa depan?", [
        "Ke masa lalu!",
        "Ke masa sekarang",
        "Ke masa depan"
    ], key="waktu")

    if st.button("Lihat Hasil Generasi Kamu"):
        skor = 0

        if hp in ["iPhone"]:
            skor += 2
        elif hp in ["Samsung"]:
            skor += 1
        elif hp in ["Xiaomi", "Oppo","Lainnya"]:
            skor += 0

        if nonton == "Streaming di HP atau laptop":
            skor += 2
        elif nonton == "Di bioskop":
            skor += 1

        if karir == "Founder perusahaan besar dari nol. Aku suka menjadi Leader!":
            skor += 2
        elif karir == "Lima pekerjaan atau lebih yang unik dan menarik. Pilihanku selalu terbuka dan aku senang mencoba hal baru!":
            skor += 1

        if waktu == "Ke masa depan":
            skor += 2
        elif waktu == "Ke masa sekarang":
            skor += 1

        if skor <= 2:
            generasi = "Pre-Boomer (lahir sebelum 1946)"
        elif skor <= 4:
            generasi = "Baby Boomers (1946–1964)"
        elif skor <= 6:
            generasi = "Generasi X (1965–1980)"
        elif skor <= 7:
            generasi = "Generasi Y / Milenial (1981–1996)"
        elif skor <= 8:
            generasi = "Generasi Z (1997–2012)"
        else:
            generasi = "Generasi Alpha (2013–2025)"

        st.success(f"{nama}, berdasarkan jawabanmu, kamu termasuk: **{generasi}**")
        st.balloons()
        




