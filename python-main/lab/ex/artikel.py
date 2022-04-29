
artik = {
            11:{"name" : "Bildschirm Belinea", "price":499.5},
            12:{"name":"PC Tastatur Swiss German", "price": 35.00},
            13:{"name":"Logitec Maus", "price":17.25},
            14:{"name":"USB Hub", "price":25.70},
            15:{"name":"Lautsprecher X66-12", "price":87.90} 
}

print(artik)

min_p=min([a["price"] for a in artik.values()])

artik_red = {}


