players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}
list = []
for key, value in players.items():
    k1 ,k2 = key
    v1,v2,v3 = value
    list.append((k1,k2,v1,v2,v3))
print(list)
# TODO здесь писать код
