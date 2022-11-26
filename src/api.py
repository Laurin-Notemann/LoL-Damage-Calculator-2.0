from flask import Flask, request
from python_champions.index import list_of_champs
from python_items.index import list_of_items
from additemstochampions import update_champion

app: Flask = Flask(__name__)

posted_data: dict = {}


@app.route("/getInitData/<string:res>", methods=["GET"])
def calcDat(res: str):
    if request.method == "GET":
        if res == "champs":
            return {"listOfChampions": list_of_champs}
        elif res == "items":
            return {"listOfItems": list_of_items}


@app.route("/sendData", methods=["POST"])
def sendData():
    if request.method == "POST":
        posted_data: dict = request.get_json(force=True)
        update_champion(posted_data)
        return posted_data


if __name__ == "__main__":
    app.run(debug=True)
