from jsonpickle import encode, decode
from get_dict import get_json_item
from python_items.LiandrysAnguish import LiandrysAnguish
from python_items.LudensTempest import LudensTempest
from python_items.Item import Item

# Initialise ALL available items + ENCDODING (decoding)

liandrys: LiandrysAnguish = LiandrysAnguish(get_json_item("6653"))
liandrys.set_mythic_stats()
ludens: LudensTempest = LudensTempest(get_json_item("6655"))
ludens.set_mythic_stats()

list_of_py_items: list[Item] = [liandrys, ludens]

liandrys = decode(encode(liandrys, unpicklable=False))
ludens = decode(encode(ludens, unpicklable=False))

list_of_items: list[Item] = [liandrys, ludens]
