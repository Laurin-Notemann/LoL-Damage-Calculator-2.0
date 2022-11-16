from jsonpickle import encode, decode
from get_dict import get_json_item
from python_items.LiandrysAnguish import LiandrysAnguish
from python_items.LudensTempest import LudensTempest

# Initialise ALL available items + ENCDODING (decoding)
liandrys = decode(encode(LiandrysAnguish(get_json_item("6653"))))
ludens = decode(encode(LudensTempest(get_json_item("6655"))))

list_of_items = [liandrys, ludens]