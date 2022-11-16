from flask import Flask
from flask_restful import Api, Resource
from jsonpickle import encode, decode
from python_champions.A import Aatrox, Ahri, Akali
from python_champions.S import Seraphine
from python_items.L import LiandrysAnguish, LudensTempest
from get_dict import get_json_champ, get_json_item


# Initialise ALL available champions + ENCODING (decoding)
aatrox = decode(
    encode(Aatrox(get_json_champ("Aatrox"), 1000), unpicklable=False))
ahri = decode(encode(Ahri(get_json_champ("Ahri")), unpicklable=False))
akali = decode(encode(Akali(get_json_champ("Akali"), 1000), unpicklable=False))
seraphine = decode(
    encode(Seraphine(get_json_champ("Seraphine"), 1000), unpicklable=False))

# Initialise ALL available items + ENCDODING (decoding)
liandrys = decode(encode(LiandrysAnguish(get_json_item("6653"))))
ludens = decode(encode(LudensTempest(get_json_item("6655"))))

app = Flask(__name__)
api = Api(app)


class ChampionData(Resource):
    def get(self):
        return {"listOfChampions": [aatrox, ahri, akali, seraphine]}


class ItemData(Resource):
    def get(self):
        return {"listOfItems": [liandrys, ludens]}


api.add_resource(ChampionData, "/getInitChampions")
api.add_resource(ItemData, "/getInitItems")

if __name__ == "__main__":
    app.run(debug=True)
