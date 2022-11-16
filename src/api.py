from flask import Flask
from flask_restful import Api, Resource
from python_champions.index import list_of_champs
from python_items.index import list_of_items
from get_dict import get_json_champ, get_json_item

app = Flask(__name__)
api = Api(app)


class ChampionData(Resource):
    def get(self):
        return {"listOfChampions": list_of_champs}


class ItemData(Resource):
    def get(self):
        return {"listOfItems": list_of_items}


api.add_resource(ChampionData, "/getInitChampions")
api.add_resource(ItemData, "/getInitItems")

if __name__ == "__main__":
    app.run(debug=True)
