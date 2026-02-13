from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=data)

@app.route("/")
def home():
    return "Servidor rodando"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Recebido:", data)

    mensagem = f"""
📌 NOVO SINAL
📊 Dados:
{data}
"""
    send_telegram(mensagem)

    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
