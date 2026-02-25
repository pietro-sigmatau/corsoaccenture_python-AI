prodotti = {
    {'id': 1, 'nome': "PC", 'prezzo': 999.0},
    {'id': 2, 'nome': "monitor", 'prezzo': 699.0},
    {'id': 3, 'nome': "mouse", 'prezzo': 99.0},
    {'id': 4, 'nome': 'tastiera', 'prezzo': 129.0}
}

#dizionario per id, preparazione dei dati, si crea l'indice

indice={p["id"]: p for p in prodotti}

print(indice)