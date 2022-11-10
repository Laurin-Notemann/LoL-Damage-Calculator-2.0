from flask import Flask
from flask_restful import Api, Resource
from src.python_champions.Aatrox import Aatrox
from src.python_champions.Ahri import Ahri
from src.python_champions.Akali import Akali
from src.python_champions.Seraphine import Seraphine
from src.python_champions.get_dict import get_dict


aatrox = Aatrox.Aatrox(get_dict("Aatrox"), 1000)
ahri = Ahri.Ahri(get_dict("Ahri"))
akali = Akali.Akali(get_dict("Akali"), 1000)
seraphine = Seraphine.Seraphine(get_dict("Seraphine"), 1000)


app = Flask(__name__)
api = Api(app)


class DamageData(Resource):
    def get(self):
        return {"names": [aatrox.champion_name, ahri.champion_name, akali.champion_name, seraphine.champion_name]}
    


api.add_resource(DamageData, "/data")

if __name__ == "__main__":
    app.run(debug=True)
    