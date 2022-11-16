from python_champions.Aatrox import Aatrox
from python_champions.Ahri import Ahri
from python_champions.Akali import Akali
from python_champions.Seraphine import Seraphine
from get_dict import get_json_champ
from jsonpickle import encode, decode

# Initialise ALL available champions + ENCODING (decoding)
aatrox = decode(encode(Aatrox(get_json_champ("Aatrox"), 1000), unpicklable=False))
ahri = decode(encode(Ahri(get_json_champ("Ahri")), unpicklable=False))
akali = decode(encode(Akali(get_json_champ("Akali"), 1000), unpicklable=False))
seraphine = decode(encode(Seraphine(get_json_champ("Seraphine"), 1000), unpicklable=False))

list_of_champs = [aatrox, ahri, akali, seraphine]
