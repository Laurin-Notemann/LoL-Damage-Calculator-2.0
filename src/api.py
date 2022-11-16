from flask import Flask
from flask_restful import Api, Resource
import jsonpickle
from python_champions.A import Aatrox, Ahri, Akali
from python_champions.S import Seraphine
from get_dict import get_dict_champ, get_dict_item



aatrox = jsonpickle.encode(Aatrox(get_dict_champ("Aatrox"), 1000), unpicklable=False)
ahri = jsonpickle.encode(Ahri(get_dict_champ("Ahri")), unpicklable=False)
akali = jsonpickle.encode(Akali(get_dict_champ("Akali"), 1000), unpicklable=False)
seraphine = jsonpickle.encode(Seraphine(get_dict_champ("Seraphine"), 1000), unpicklable=False)



aatrox = jsonpickle.decode(aatrox)
ahri = jsonpickle.decode(ahri)
akali = jsonpickle.decode(akali)
seraphine = jsonpickle.decode(seraphine)


app = Flask(__name__)
api = Api(app)

test = {"champion_id": 1}

class DamageData(Resource):
    def get(self):
        return {"listOfChampions": [aatrox, ahri, akali, seraphine]}
    




api.add_resource(DamageData, "/data")

if __name__ == "__main__":
    app.run(debug=True)
    