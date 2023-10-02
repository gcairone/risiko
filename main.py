import risk as rk

P = rk.Partita()

for i in range(29):
    P.place_tank(P.players[i % 4].terr[i % 10].name, 3)

P.stampa_pl()
P.chipossoattaccare("Afghanistan")

"""
P.attack("Ontario", "Alberta", 3)  # p1
P.attack("India", "China", 3)  # p1
P.stop()
P.stop()
P.stop()
P.stop()

P.attack("Venezuela", "Brazil", 3)  # p1
P.attack("Venezuela", "Brazil", 3)  # p1
P.attack("Venezuela", "Brazil", 3)  # p1
P.stop()
P.stop()
P.stop()
P.stop()



P.attack("Kamchatka", "Alaska", 3)  # p1
P.attack("Kamchatka", "Alaska", 2)  # p1
P.stop()
P.stop()
P.stop()
P.stop()

P.reinforce([k.name for k in P.players[0].card_terr], ["East_US"], [15])
"""
# ordine: pinopino, gino, tob, tricheco
# un turno: [reinforce], [attack...], stop
