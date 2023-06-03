# =[Modules dan Packages]========================

from flask import Flask, request, jsonify
from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import pickle
import nltk
import joblib
import pickle
from joblib import load

# import package untuk phishing detection
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer

# import package untuk safebot
from process import preparation, generate_response

# download nltk
preparation()

# =[Variabel Global]=============================

app = Flask(__name__, static_url_path='/static')
model = None

# =[Routing]=====================================

# [Routing untuk Halaman Utama atau Home]


@app.route("/")
def beranda():
    return render_template('index.html')

# [Routing untuk Halaman Utama atau Home]


@app.route("/chatbot")
def chatbot():
    return render_template('chatbot.html')

# Routing for API phishing


@app.route("/api/deteksi", methods=['POST'])
def apiDeteksi():
    # Nilai default untuk string input
    text_input = ""

    if request.method == 'POST':
        # Set nilai string input dari pengguna
        text_input = request.form['data']
        hasil = model.predict([text_input])

        if (hasil == "bad"):
            hasil_prediksi = "Terindikasi URL Phishing. Note: Jangan mengklik atau mengunjungi link tersebut. Sebaiknya Anda menghapus email atau pesan yang berisi link tersebut, atau mengabaikan link tersebut jika terdapat di dalam pesan atau situs web lain."
        elif (hasil == "good"):
            hasil_prediksi = "Tidak terindikasi URL phishing (URL Aman). Note: Tetaplah waspada dan hati-hati ketika mengklik link tersebut. Pastikan bahwa Anda hanya mengklik link dari sumber yang terpercaya, seperti situs web resmi atau email yang Anda harapkan dari pengirim yang dikenal. "
        # Return hasil prediksi dengan format JSON
        return jsonify({
            "data": hasil_prediksi,
        })

# Routing for API response chatbot


@app.route("/get")
def get_bot_response():
    user_input = str(request.args.get('msg'))
    result = generate_response(user_input)
    return result

# =[Main]========================================


if __name__ == '__main__':

    # Load model phishing yang telah ditraining
    model = load('model_phishing_lr.model')

    # Run Flask di localhost
    app.run(host="localhost", port=5000, debug=True)
