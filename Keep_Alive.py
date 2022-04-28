from flask import Flask
from threading import Thread
from dotenv import load_dotenv

load_dotenv()

app = Flask('')

@app.route('/')
def main():
  return "O bot está online!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()