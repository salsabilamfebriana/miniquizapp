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

        # Dictionary GIF untuk tiap generasi
        gif_dict = {
            "Pre-Boomer (lahir sebelum 1946)": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHZkNnB4a3QwcnZqdWhrN2t4ZnZ0aDhoOTZkYmRqNnJsZzYxcHI0eCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/50rJushu3URtS/giphy.gif",
            "Baby Boomers (1946–1964)": "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdXZ6bDdsM3UwNTZ6OGRpOHdpNjI2bWp0NjZwZzZybDk3Z2dtYmU2dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MZiqcOmikf3VMVRhBs/giphy.gif",
            "Generasi X (1965–1980)": "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3NHphbHhndnNlcDB5dTN4ZmdnZzR3NzRkN3U0aXVtdGJmcTZweGUyMyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/2MMuVJhA6SPZaODIUK/giphy.gif",
            "Generasi Y / Milenial (1981–1996)": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWNtZXp1Nml5MW55Mm5mN3V5N3p4MTFjejZ4bzIxaDh4NW1oYWlrdSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/SxMMNyNTMGw2uwqSNl/giphy.gif",
            "Generasi Z (1997–2012)": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2ZqN3YzcjV1YzU1YzI2dWw1ZXJwbGkxdTJ4NzdicjVzNHBzdWNyNiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/KvGWFRpWTd23ANVr57/giphy.gif",
            "Generasi Alpha (2013–2025)": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWwxdHVzbGZjeG55NnlpMWFndThqdG91YTc3em9rYnAxZHR3eHhsbSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Y2KvXNRs7wCs5sWKrp/giphy.gif"
        }

        # Tampilkan hasil
        st.success(f"{nama}, berdasarkan jawabanmu, kamu termasuk: **{generasi}**")
        st.balloons()
        # Tampilkan GIF sesuai generasi
        st.image(gif_dict[generasi], use_container_width=True)




