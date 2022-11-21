from python_champions.Aatrox import Aatrox
from python_champions.Ahri import Ahri
from python_champions.Akali import Akali
from python_champions.Seraphine import Seraphine
from get_dict import get_json_champ
from jsonpickle import encode, decode

# Initialise ALL available champions 
aatrox = Aatrox(get_json_champ("Aatrox"))
ahri = Ahri(get_json_champ("Ahri"))
akali = Akali(get_json_champ("Akali"))
seraphine = Seraphine(get_json_champ("Seraphine"))


list_of_py_champs = [aatrox, ahri, akali, seraphine]

# ENCODING (decoding) all champs
aatrox = decode(encode(aatrox, unpicklable=False))
ahri = decode(encode(ahri, unpicklable=False))
akali = decode(encode(akali, unpicklable=False))
seraphine = decode(encode(seraphine, unpicklable=False))

list_of_champs = [aatrox, ahri, akali, seraphine]




