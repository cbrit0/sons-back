from flask import Flask, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify(
        phone_names=phone_names,
        final_prices=final_prices)

response = requests.get("https://catalogo.movistar.cl/tienda/celulares/apple")

soup = BeautifulSoup(response.text, "html.parser")

phones = [phone for phone in soup.find_all("div", class_="product-item-info")]
phone_names = [phone.find("h2").text.strip() for phone in phones]
final_prices = [phone.find("span", class_="divCon-plan-txt-valor-sinLabel").text.strip() for phone in phones]

CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
