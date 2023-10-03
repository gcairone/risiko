import networkx as nx
import random as rd

# la classe networkx non sarebbe strettamente necessaria per i grafi, pero' puo' servire per diverse analytics



# classe giocatore, instanziare con nome, contiene una lista di territori posseduti (scelta all-inizio e variabile
# attraverso le conquiste), contiene una lista di carte territorio che serve per i rinforzi
class Player:
    def __init__(self, nom):
        self.name = nom
        self.terr = []
        # carte territorio che il giocatore tiene per rinforzi
        self.card_terr = []
        # obiettivo, di tipo obiettivo
        self.obiettivo = None

    def num_terr(self):
        return len(self.terr)

    def __str__(self):
        # nonostante la stampa dell'istanza Player stampi una lista di stringhe, terr e' una lista di oggetti di tipo
        # territory
        nomiterr = [i.name for i in self.terr]
        a = str(self.name) + " " + str(nomiterr)
        return a


# classe territorio, istanziata con nome e nome del continente, contiene un campo con il numero di carri armati,
# contiene un owner che e' di tipo player, contiene un attributo per i rinforzi
class Territory:
    def __init__(self, nom, cont):
        self.name = nom
        self.continent = cont
        self.owner = None
        #
        self.tanks = 0
        # attributo (fante, cannone, cavaliere)
        self.attribute = rd.Random(42).choice(["fante", "cannone", "cavaliere"])

    def __str__(self):
        a = str(self.name) + " -- " + str(self.owner.name) + " " + str(self.tanks)
        return a

# classe obiettivo, un membro tipo e un membro generico
class Obiettivo:
    def __init__(self, tipo, arg):
        self.tipo = tipo
        if tipo == 'conq_n_territori':
            # arg è il numero di territori
            self.n = arg
        if tipo == 'elim_giocatore':
            # arg è l'indice del giocatore tra 0 e 5
            self.pl = arg
        if tipo == 'conq_due_continenti':
            # arg è la lista di nomi di continenti
            self.l_cont = arg
        if tipo == 'conq_continenti_piu_scelta':
            # arg è la lista di nomi di continenti
            self.l_cont = arg
    def __str__(self):
        stringa = ''
        if self.tipo == 'conq_n_territori':
            stringa = 'Conquistare ' + str(self.n) + 'territori'
        if self.tipo == 'elim_giocatore':
            stringa = 'Eliminare giocatore ' + str(self.pl)
        if self.tipo == 'conq_due_continenti':
            stringa = 'Conquistare ' + self.l_cont[0] + ' e ' + self.l_cont[1] 
        if self.tipo == 'conq_continenti_piu_scelta':
            stringa = 'Conquistare ' + self.l_cont[0] + ', ' + self.l_cont[1] + ' e un terzo continente a scelta'
        return stringa

# conq_n_territori (n), elim_giocatore (pl), conq_due_continenti (l_cont), conq_continenti_piu_scelta (l_cont)


# update the board, instanzia i territori e i collegamenti
def update_board():
    # elenco territori
    Alaska = Territory("Alaska", "North_America")
    Northwest_Territories = Territory("Northwest_Territories", "North_America")
    Greenland = Territory("Greenland", "North_America")
    Alberta = Territory("Alberta", "North_America")
    Ontario = Territory("Ontario", "North_America")
    Quebec = Territory("Quebec", "North_America")
    West_US = Territory("West_US", "North_America")
    East_US = Territory("East_US", "North_America")
    Central_America = Territory("Central_America", "North_America")
    Venezuela = Territory("Venezuela", "South_America")
    Peru = Territory("Peru", "South_America")
    Brazil = Territory("Brazil", "South_America")
    Argentina = Territory("Argentina", "South_America")
    Iceland = Territory("Iceland", "Europe")
    Scandinavia = Territory("Scandinavia", "Europe")
    Great_Britain = Territory("Great_Britain", "Europe")
    North_Europe = Territory("North_Europe", "Europe")
    West_Europe = Territory("West_Europe", "Europe")
    South_Europe = Territory("South_Europe", "Europe")
    Ukraine = Territory("Ukraine", "Europe")
    North_Africa = Territory("North_Africa", "Africa")
    Egypt = Territory("Egypt", "Africa")
    Congo = Territory("Congo", "Africa")
    East_Africa = Territory("East_Africa", "Africa")
    South_Africa = Territory("South_Africa", "Africa")
    Madagascar = Territory("Madagascar", "Africa")
    Urals = Territory("Urals", "Asia")
    Siberia = Territory("Siberia", "Asia")
    Yakutia = Territory("Yakutia", "Asia")
    Chita = Territory("Chita", "Asia")
    Kamchatka = Territory("Kamchatka", "Asia")
    Japan = Territory("Japan", "Asia")
    Mongolia = Territory("Mongolia", "Asia")
    Afghanistan = Territory("Afghanistan", "Asia")
    Middle_East = Territory("Middle_East", "Asia")
    India = Territory("India", "Asia")
    China = Territory("China", "Asia")
    Siam = Territory("Siam", "Asia")
    Indonesia = Territory("Indonesia", "Australia")
    New_Guinea = Territory("New_Guinea", "Australia")
    East_Australia = Territory("East_Australia", "Australia")
    West_Australia = Territory("West_Australia", "Australia")

    ...
    # Riempire questo con le carte territori (classe non nome)
    cards = [Alaska, Northwest_Territories, Greenland, Alberta, Ontario, Quebec, West_US, East_US,
             Central_America,
             Venezuela, Peru, Brazil, Argentina, Iceland, Scandinavia, Great_Britain, North_Europe, West_Europe,
             South_Europe, Ukraine,
             North_Africa, Egypt, Congo, East_Africa, South_Africa, Madagascar, Urals, Siberia, Yakutia, Chita,
             Kamchatka, Japan, Mongolia,
             Afghanistan, Middle_East, India, China, Siam, Indonesia, New_Guinea, East_Australia, West_Australia]
    # elenco collegamenti
    edges = [
        ("Alaska", "Northwest_Territories"),
        ("Alaska", "Alberta"),
        ("Alaska", "Kamchatka"),
        ("Northwest_Territories", "Greenland"),
        ("Northwest_Territories", "Alberta"),
        ("Northwest_Territories", "Greenland"),
        ("Northwest_Territories", "Ontario"),
        ("Greenland", "Quebec"),
        ("Greenland", "Iceland"),
        ("Quebec", "Ontario"),
        ("Ontario", "Alberta"),
        ("Ontario", "Greenland"),
        ("Quebec", "East_US"),
        ("Alberta", "West_US"),
        ("Ontario", "West_US"),
        ("East_US", "West_US"),
        ("East_US", "Central_America"),
        ("Ontario", "East_US"),
        ("West_US", "Central_America"),
        ("Central_America", "Venezuela"),
        ("Venezuela", "Peru"),
        ("Venezuela", "Brazil"),
        ("Brazil", "Peru"),
        ("Brazil", "Argentina"),
        ("Brazil", "North_Africa"),
        ("Argentina", "Peru"),
        ("Iceland", "Scandinavia"),
        ("Iceland", "Great_Britain"),
        ("Scandinavia", "Great_Britain"),
        ("Scandinavia", "North_Europe"),
        ("Scandinavia", "Ukraine"),
        ("Great_Britain", "North_Europe"),
        ("Great_Britain", "West_Europe"),
        ("North_Europe", "West_Europe"),
        ("North_Europe", "South_Europe"),
        ("North_Europe", "Ukraine"),
        ("West_Europe", "South_Europe"),
        ("West_Europe", "North_Africa"),
        ("South_Europe", "North_Africa"),
        ("South_Europe", "Egypt"),
        ("South_Europe", "Middle_East"),
        ("South_Europe", "Ukraine"),
        ("North_Africa", "Egypt"),
        ("North_Africa", "Congo"),
        ("North_Africa", "East_Africa"),
        ("Congo", "East_Africa"),
        ("Congo", "South_Africa"),
        ("East_Africa", "Madagascar"),
        ("East_Africa", "Egypt"),
        ("Madagascar", "South_Africa"),
        ("South_Africa", "East_Africa"),
        ("Urals", "Siberia"),
        ("Siberia", "Yakutia"),
        ("Urals", "Ukraine"),
        ("Siberia", "Yakutia"),
        ("Siberia", "Mongolia"),
        ("Siberia", "China"),
        ("Siberia", "Chita"),
        ("Urals", "China"),
        ("Yakutia", "Kamchatka"),
        ("Yakutia", "Chita"),
        ("Chita", "Mongolia"),
        ("Chita", "Kamchatka"),
        ("Kamchatka", "Alaska"),
        ("Kamchatka", "Japan"),
        ("Kamchatka", "Mongolia"),
        ("Japan", "Mongolia"),
        ("Mongolia", "China"),
        ("Afghanistan", "China"),
        ("Afghanistan", "Middle_East"),
        ("Afghanistan", "Ukraine"),
        ("Afghanistan", "Urals"),
        ("Middle_East", "India"),
        ("Middle_East", "Egypt"),
        ("Middle_East", "China"),
        ("Middle_East", "Ukraine"),
        ("India", "Siam"),
        ("India", "China"),
        ("Siam", "Indonesia"),
        ("Siam", "China"),
        ("Indonesia", "New_Guinea"),
        ("Indonesia", "West_Australia"),
        ("New_Guinea", "East_Australia"),
        ("East_Australia", "West_Australia"),
        ("New_Guinea", "West_Australia"),
    ]
    g = nx.Graph(edges)

    ...
    return cards, g


# carica i giocatori, da qui, funzione chiamata automaticamente quando viene istanziata una partite
def update_players():
    p = []
    # istanziamento giocatori
    p1 = Player("p1")
    p2 = Player("p2")
    p3 = Player("p3")
    p4 = Player("p4")
    ...
    # aggiunti
    p.append(p1)
    p.append(p2)
    p.append(p3)
    p.append(p4)
    ...
    return p


# carica num obiettivi dalle possibili carte obiettivo
def update_obiettivi():
    lista_obiettivi = []
    lista_obiettivi.append(Obiettivo('conquistare_n_territori', 18))
    lista_obiettivi.append(Obiettivo('conquistare_n_territori', 24))
    lista_obiettivi.append(Obiettivo('elim_giocatore', 0))
    lista_obiettivi.append(Obiettivo('elim_giocatore', 1))
    lista_obiettivi.append(Obiettivo('elim_giocatore', 2))
    lista_obiettivi.append(Obiettivo('elim_giocatore', 3))
    lista_obiettivi.append(Obiettivo('elim_giocatore', 4))
    lista_obiettivi.append(Obiettivo('elim_giocatore', 5))
    lista_obiettivi.append(Obiettivo('conq_due_continenti', ['North_America', 'Africa']))
    lista_obiettivi.append(Obiettivo('conq_due_continenti', ['Asia', 'Africa']))
    lista_obiettivi.append(Obiettivo('conq_due_continenti', ['Europe', 'Australia']))
    lista_obiettivi.append(Obiettivo('conq_continenti_piu_scelta', ['North_America', 'Africa']))
    lista_obiettivi.append(Obiettivo('conq_continenti_piu_scelta', ['Asia', 'Africa']))
    lista_obiettivi.append(Obiettivo('conq_continenti_piu_scelta', ['Europe', 'Australia']))
    ...
    rd.shuffle(lista_obiettivi)
    return lista_obiettivi


# questa funzione viene chiamata al posto della precedente nel caso in cui la precedente ha un numero di giocatori
# non adatto
def default_player():
    p = []
    # istanziamento giocatori
    p1 = Player("p1")
    p2 = Player("p2")
    # aggiunti
    p.append(p1)
    p.append(p2)
    return p


# funzione che prende in input numero dadi in attacco e in difesa, restituisce due interi che indicano i tanks persi
def dadi(a, d):
    att, dif = [], []
    pa = 0
    pd = 0
    for ii in range(a): att.append(rd.Random(42).randint(1, 6))
    for ii in range(d): dif.append(rd.Random(43).randint(1, 6))
    att.sort(reverse=True)
    dif.sort(reverse=True)
    # print(att, dif)
    for ii in range(min(a, d)):
        if att[ii] <= dif[ii]:
            pa += 1
        else:
            pd += 1
    return pa, pd


# classe partita, senza la sua istanza non si puo' fare nulla
class Partita:
    def __init__(self):
        # Numeri non negat per indicare turni di giocatori, negativi indicano fase di posizionamento (-10, -11 ...
        # inizialmente -1
        # poi viene portato a -10, avrà valore -10-i quando è turno dell'i-esimo player per fare pos. armate iniz.
        # Quando finisce la fase preparatoria viene messo a ZERO, avrà valore i per l'i-esimo giocatore
        self.status = -1
        self.players = update_players()
        if len(self.players) < 2 or len(self.players) > 6:
            self.players = default_player()
        self.territories, self.Plancia = update_board()

        # associare obiettivi a persone
        obiettivi = update_obiettivi()
        for o in obiettivi:
            if o.tipo == 'eliminare_giocatore' and o.pl >= len(self.players):
                o = Obiettivo('conquistare_n_territori', 24)
        for i in range(len(self.players)):
            self.players[i].obiettivo = obiettivi[i]
        # comunicarli
        for pl in self.players:
            print(pl.name, pl.obiettivo)
        
        # creazione mazzo di carte
        self.cards = self.territories.copy()
        # aggiunta jolly
        J1 = Territory(None, None)
        J1.attribute = "j"
        J2 = Territory(None, None)
        J2.attribute = "j"
        self.cards.append(J1)
        self.cards.append(J2)
        rd.Random(42).shuffle(self.cards)

        # oggetto che serve solo per la fase di posizionamento iniziale, contiene un elemento per ogni player, che dice
        # quante armate il giocatore puo' ancora mettere sul suo territorio
        self.tanks_players = []
        # l'i-esimo è vero se nell'ultimo turno il giocatore i-esimo ha conquistato un territorio
        # questa cosa determina il fatto che si possa prendere una carta terr. per rinforzo
        self.recent_conquer = [False for player in self.players]
        self.can_reinforce = [False for player in self.players]
        self.just_won = [False for player in self.players] # se ha appena vinto, serve per lo spostamento dopo la vittoria
        self.att_dif = (None, None) # territorio attaccato e difeso (oggetti non nomi)
        self.gioc_eliminati = [] # lista di giocatori eliminati (non nomi)
        self.gioc_ragg_ob = [] # lista ordinata giocatori che hanno raggiunto l'obiettivo
        # distribuisci le carte
        new = self.territories.copy()
        rd.Random(42).shuffle(new)
        # kesimo player a cui metterlo
        k = 0
        # distribuizione territori
        while len(new) > 0:
            new[0].owner = self.players[k]
            self.players[k].terr.append(new[0])
            new.pop(0)
            k += 1
            k %= len(self.players)

        # determina quante armate per persona
        num = 35 - 5 * (len(self.players) - 3)
        for _ in range(len(self.players)):
            self.tanks_players.append(num)
        # metti un'armata in ogni territorio
        for player in self.players:
            for terr in player.terr:
                terr.tanks += 1
                self.tanks_players[self.players.index(player)] -= 1
        self.status = -10


    def verifica(self):
        # non pensa lei a togliere giocatori eliminati
        # verifica il compimento degli obiettivi, mettendo i giocatori che hanno compiuto l'obiettivo in
        # set_v, verifica quali sono i "nuovi vincitori", li comunica, li toglie da players e li mette nella classifica

        set_v = set()
        for pla in self.players:
            if pla.obiettivo.tipo == 'conq_n_territori':
                if pla.obiettivo.n <= len(pla.terr):
                    set_v.add(pla)
            if pla.obiettivo.tipo == 'elim_giocatore':
                if pla.obiettivo.pl in self.gioc_eliminati:
                    set_v.add(pla)


            # controllo continenti
            lista_c = []
            if [terry.continent for terry in pla.terr].count("North_America") == 9:
                lista_c.append("North_America")
            if [terry.continent for terry in pla.terr].count("South_America") == 4:
                lista_c.append("South_America")
            if [terry.continent for terry in pla.terr].count("Europe") == 7:
                lista_c.append("Europe")
            if [terry.continent for terry in pla.terr].count("Africa") == 6:
                lista_c.append("Africa")
            if [terry.continent for terry in pla.terr].count("Asia") == 12:
                lista_c.append("Asia")
            if [terry.continent for terry in pla.terr].count("Australia") == 4:
                lista_c.append("Australia")


            if pla.obiettivo.tipo == 'conq_due_continenti':
                if len(lista_c) >= 2 and set(pla.obiettivo.l_cont) <= set(lista_c):
                    set_v.add(pla)
            if pla.obiettivo.tipo == 'conq_continenti_piu_scelta':
                if len(lista_c) >= 3 and set(pla.obiettivo.l_cont) <= set(lista_c):
                    set_v.add(pla)

        
        # al momento set_v è il nuovo insieme dei giocatori che hanno raggiunto un'obiettivo
        # invece self.gioc_ragg_ob è il vecchio insieme
        if len(set_v - set(self.gioc_ragg_ob)) > 0:
            print((set_v - set(self.gioc_ragg_ob)), "ha vinto")
        
        # elimina i giocatori che hanno vinto da players e mettili in gioc_ragg_ob
        for pl in set_v - set(self.gioc_ragg_ob):
            self.players.remove(pl)
            self.gioc_ragg_ob.append(pl)
        
        if len(self.players) == 0:
            print("----------")
            print("---FINE---")
            print("----------")
            print("CLASSIFICA:")
            print(self.gioc_ragg_ob)

    # posiziona n tanks nel territorio dal nome ter, funzione valida solo per la fase preparatoria
    def place_tank(self, ter, n):
        if n > 3 or n < 1: n = 1
        if self.status > -10:
            print("Non si può posizionare in questa fase")
            return
        if ter not in [terry.name for terry in self.players[- self.status - 10].terr]:
            print("Questo non è un tuo territorio")
            return  # se non esiste "ter"
        # se n > tanks che si possono mettere
        if n > self.tanks_players[- self.status - 10]:
            self.territories[[terry.name for terry in self.territories].index(ter)].tanks += self.tanks_players[
                - self.status - 10]
            self.tanks_players[- self.status - 10] = 0
            # se siamo all'ultimo giocatore, riparti dal primo
            if self.status == - 10 - len(self.players) + 1:
                self.status = -10
            else:
                self.status -= 1
            # controlla se è finita la fase preparatoria
            if self.tanks_players == [0 for a in self.tanks_players]:
                print("FINE FASE PREP")
                self.status = 0
                print("-------", self.players[0].name, "-------")
            return
        # metti n tanks nel territorio dal nome terr
        # [terry.name for terry in self.territories].index(ter) sarebbe l'indice che corrisponde a ter
        self.territories[[terry.name for terry in self.territories].index(ter)].tanks += n
        self.tanks_players[- self.status - 10] -= n
        if self.status == - 10 - len(self.players) + 1:
            self.status = -10
        else:
            self.status -= 1
        # controlla se e' finita la fase preparatoria
        if self.tanks_players == [0 for a in self.tanks_players]:
            print("FINE FASE PREP")
            self.status = 0
            print("-------", self.players[0].name, "-------")


    def chipossoattaccare(self, t_att_n):
        print("")
        # dato t_att ovvero il nome di un territorio, restituisce una lista di territori che puoi attaccare da lì
        if self.status < 0:
            print("Informazione non disponibile in questa fase")
            return
        
        list_nomi_ter = [t.name for t in self.players[self.status].terr] # lista di nomi dei territori del giocatore
        if t_att_n not in list_nomi_ter:
            print("Non è un territorio da cui puoi attaccare")
            return
        list_neigh = list(nx.neighbors(self.Plancia, t_att_n)) # contiene nomi
        list_neigh = [t for t in list_neigh if t not in list_nomi_ter]
        print(list_neigh)
        l_t = [t.name for t in self.territories] # lista nomi di tutti i terr
        list_tanks = [self.territories[l_t.index(t_n)].tanks for t_n in list_neigh]
        print(list_tanks)

    # attacca da t_att_name a t_dif_name con na dadi
    def attack(self, t_att_name, t_dif_name, na):  # in input il nome del territorio, non l'istanza della classe
        # verifica che i nomi territori esistano, e crea variabili con i proprietari
        if t_att_name not in [terry.name for terry in self.territories]:
            print("Non è un territorio")
            return
        if t_dif_name not in [terry.name for terry in self.territories]:
            print("Non è un territorio")
            return
        t_att = self.territories[[terry.name for terry in self.territories].index(t_att_name)]
        t_dif = self.territories[[terry.name for terry in self.territories].index(t_dif_name)]
        i_att, att = self.players.index(t_att.owner), t_att.owner
        i_dif, dif = self.players.index(t_dif.owner), t_dif.owner
        # verifica che il prop di att sia al giusto turno
        if self.status != i_att:
            print("Non si può attaccare da questo territorio")
            return
        # verifica che attaccante e difensore non siano lo stesso
        if i_dif == i_att:
            print("Attaccante e difensore coincidono")
            return
        # verifica il confine
        if not self.Plancia.has_edge(t_att_name, t_dif_name):
            print("Territori non confinanti")
            return
        # verifica che il numero di dadi e' nel range giusto
        if na >= t_att.tanks:
            print("Numero di dadi troppo elevato")
            return
        if na < 1 or na > 3:
            print("Numero di dadi non compreso tra 1 e 3")
            return
        # poni can_reinforce a false
        self.can_reinforce[self.status] = False
        # poni just_won a False
        self.just_won = [False for player in self.players]
        # stampa commento
        print("Attacco:", t_att_name.upper(), t_att.tanks, t_dif_name.upper(), t_dif.tanks, "(", t_dif.owner.name, ")",
              end='\n')
        # attacca
        # la difesa e' obbligata a difendere con il massimo
        if t_dif.tanks >= 3:
            nd = 3
        else:
            nd = t_dif.tanks
        pa, pd = dadi(na, nd)
        t_att.tanks -= pa
        t_dif.tanks -= pd
        # controlla se il territorio difeso e' stato sconfitto
        contr = 0
        if t_dif.tanks == 0:
            self.recent_conquer[self.status] = True
            t_dif.owner = att
            att.terr.append(t_dif)
            dif.terr.remove(t_dif)
            t_dif.tanks = na
            t_att.tanks -= na
            contr = 1
            self.just_won[self.status] = True
            self.att_dif = (t_att, t_dif)
            # verifica se il giocatore che ha perso il territorio è stato eliminato
            if len(dif.terr) == 0:
                print(dif.name, "ELIMINATO")
                self.players.remove(dif)
                self.gioc_eliminati.append(dif)
            # verifica il raggiungimento degli obiettivi
            self.verifica()
        # else:
        # self.recent_conquer[self.status] = False
        print("        ", t_att_name.upper(), t_att.tanks, t_dif_name.upper(), t_dif.tanks, end='\n')
        if contr == 1: print("Conquistato")
        contr = 0
    

    def sposta(self, n):
        # spostamento dopo aver vinto un attacco
        # n sono i tanks che si vogliono spostare dall'attacco alla difesa (negativo se il contrario)
        if not self.just_won[self.status]:
            print("Non puoi spostare")
            return
        if n >= self.att_dif[0].tanks:
            print("n troppo alto")
            return
        if n <= - self.att_dif[1].tanks:
            print("n troppo basso")
            return
        self.att_dif[0].tanks -= n
        self.att_dif[1].tanks += n
        self.just_won[self.status] = False
        print(self.att_dif[0].name, self.att_dif[0].tanks)
        print(self.att_dif[1].name, self.att_dif[1].tanks)
        
    # serve a finire un turno di attacchi e passare al successivo, non si puo' passare da un turno a un altro senza
    # questa funzione, perche' la funzione attack puo' essere invocata quanto si vuole
    # ho aggiunto la possibilità di fare spostamenti
    def stop(self, sp_da=None, sp_a=None, n=0):  # ferma gli attacchi e prendi la carta
        if self.status < 0:
            print("Fase di preparazione in corso, non si può fermare un turno adesso")
            return
        # controllo se si può fare lo spostamento
        if (sp_a is not None and 
            sp_da is not None and
            sp_a in [t.name for t in self.players[self.status].terr] and
            sp_da in [t.name for t in self.players[self.status].terr] and
            self.Plancia.has_edge(sp_da, sp_a) and
            n < self.territories[[terry.name for terry in self.territories].index(sp_da)].tanks):

            self.territories([terry.name for terry in self.territories].index(sp_da)).tanks -= n
            self.territories([terry.name for terry in self.territories].index(sp_a)).tanks += n

        # mette a False just_won
        self.just_won = [False for player in self.players]
        # se ha conquistato almeno un territorio, prende una carta
        if self.recent_conquer[self.status]:
            self.players[self.status].card_terr.append(self.cards.pop())
            print("Carta: ", self.players[self.status].card_terr[-1].attribute, end='\n')
            self.recent_conquer[self.status] = False
        self.can_reinforce[self.status] = False

        # passa al giocatore successivo
        self.status += 1
        self.status %= len(self.players)
        self.can_reinforce[self.status] = True
        print("")
        print("-------", self.players[self.status].name, "-------", end='\n')


    def cosapossorinforzare(self):
        if not self.can_reinforce[self.status]:
            print("Non si possono fare rinforzi adesso")
            return
        # stampa le carte che hai con il segno
        print('Carte:')
        for c in self.players[self.status].card_terr:
            print(c.name, c.attribute)
        # continenti
        lista_c = []
        conto = 0
        if [terry.continent for terry in self.players[self.status].terr].count("North_America") == 9:
            lista_c.append("North_America")
            conto += 5
        if [terry.continent for terry in self.players[self.status].terr].count("South_America") == 4:
            lista_c.append("South_America")
            conto += 3
        if [terry.continent for terry in self.players[self.status].terr].count("Europe") == 7:
            lista_c.append("Europe")
            conto += 5
        if [terry.continent for terry in self.players[self.status].terr].count("Africa") == 6:
            lista_c.append("Africa")
            conto += 3
        if [terry.continent for terry in self.players[self.status].terr].count("Asia") == 12:
            lista_c.append("Asia")
            conto += 7
        if [terry.continent for terry in self.players[self.status].terr].count("Australia") == 4:
            lista_c.append("Australia")
            conto += 4
        print("Continenti completi:")
        print(lista_c, conto)
        # n territori
        print("Inoltre hai", self.players[self.status].num_terr(), 
              "territori, quindi ti spettano", int(self.players[self.status].num_terr() / 3),
              "armate")
        

    def reinforce(self, rinf, terr_r, tanks_r):
        """
        prende in input

        -rinf: una lista di nomi associati alle carte rinforzo che vuole usare (non territori da
        rinforzare), determina quali univocamente tris si vogliono usare e dunque quante armate si hanno.
        Si fa in modo da verificare prima la presenza di tris con valore piu' alto, in modo da massimizzare
        le armate ricevute dai tris (non esattamente se si tiene conto che un tris puo' essere reso piu' conveniente di
        altro in base ai +2, l'alternativa sarebbe un algoritmo piu' complesso)

        -terr_r: una lista di nomi di territori che vuole rinforzare,

        -tanks_r: una lista di numeri di carri armati da mettere in
        terr_r[i]

        attenzione: se la summa di terr_r e' diversa dei tanks disp., la mossa non viene eseguita
        """
        # controlli input
        # terr è la lista dei territori (istanze, non nomi) del giocatore in turno
        terr = self.players[self.status].terr
        # card_terr è la lista delle carte del giocatore in turno
        card_terr = self.players[self.status].card_terr

        # controlla che rinf è sottoinsieme di card_terr
        for tr in rinf:
            if tr not in [terry.name for terry in card_terr]:
                print("Non tutte le carte scelte sono disponibili")
                return
        # controlla che terr_r è sottoinseme di terr
        for tr in terr_r:
            if tr not in [terry.name for terry in terr]:
                print("Non possiedi tutti i territori scelti")
                return
        # controlla compatibilita' di lunghezza tra gli argomenti
        if not len(terr_r) == len(tanks_r):
            print("Numero di territori diverso da lunghezza della lista dei rinforzi")
            return
        # controlla se puoi fare rinforzi (in base al fatto che non abbia gia' fatto un attacco nel turno)
        if not self.can_reinforce[self.status]:
            print("Non si possono fare rinforzi adesso")
            return
        # rinforzi dovuti ai terr. posseduti
        tanks = int(len(terr) / 3)
        # print("Contr1", tanks)
        # rinforzi dovuti ai continenti
        if [terry.continent for terry in terr].count("North_America") == 9: tanks += 5
        if [terry.continent for terry in terr].count("South_America") == 4: tanks += 3
        if [terry.continent for terry in terr].count("Europe") == 7: tanks += 5
        if [terry.continent for terry in terr].count("Africa") == 6: tanks += 3
        if [terry.continent for terry in terr].count("Asia") == 12: tanks += 7
        if [terry.continent for terry in terr].count("Australia") == 4: tanks += 4
        # rinforzi dovuti alla presenza di tuoi territori nelle carte
        for tr in rinf:
            if tr in [terri.name for terri in terr]:
                tanks += 2
        # print("Contr2", tanks)
        # -----------------------------------------------------------------------------------------------------------
        # crea rinf_t (lista di territori) a partire da rinf (lista di nomi)
        rinf_t = [self.territories[[terri.name for terri in self.territories].index(t)] for t in rinf]
        # lista di attributi associati a rinf
        attr = [terri.attribute for terri in rinf_t]
        # print("Contr3")
        # controllo due jolly e un altro
        card_terr_copy = card_terr
        selfcards_copy = self.cards
        if len(attr) > 2 and attr.count("j") == 2:
            self.cards.append(card_terr.pop(attr.index("j")))
            attr.remove("j")
            self.cards.append(card_terr.pop(attr.index("j")))
            attr.remove("j")
            self.cards.append(card_terr.pop())
            attr.pop()
            tanks += 12
        # controllo tris diversi
        if "fante" in attr and "cavaliere" in attr and "cannone" in attr:
            self.cards.append(card_terr.pop(attr.index("fante")))
            attr.remove("fante")
            self.cards.append(card_terr.pop(attr.index("cavaliere")))
            attr.remove("cavaliere")
            self.cards.append(card_terr.pop(attr.index("cannone")))
            attr.remove("cannone")
            tanks += 10
        # controllo tre cavalieri
        # print("Contr4", tanks)
        if attr.count("cavaliere") == 3:
            self.cards.append(card_terr.pop(attr.index("cavaliere")))
            attr.remove("cavaliere")
            self.cards.append(card_terr.pop(attr.index("cavaliere")))
            attr.remove("cavaliere")
            self.cards.append(card_terr.pop(attr.index("cavaliere")))
            attr.remove("cavaliere")
            tanks += 8
        # controllo tre cannoni
        if attr.count("fante") == 3:
            self.cards.append(card_terr.pop(attr.index("fante")))
            attr.remove("fante")
            self.cards.append(card_terr.pop(attr.index("fante")))
            attr.remove("fante")
            self.cards.append(card_terr.pop(attr.index("fante")))
            attr.remove("fante")
            tanks += 6
        # controllo tre fanti
        if attr.count("cannone") == 3:
            self.cards.append(card_terr.pop(attr.index("cannone")))
            attr.remove("cannone")
            self.cards.append(card_terr.pop(attr.index("cannone")))
            attr.remove("cannone")
            self.cards.append(card_terr.pop(attr.index("cannone")))
            attr.remove("cannone")
            tanks += 4
        # print("Rinforzi:", tanks)  # -------------------------------------------------------------------------
        # una volta contati i tanks da mettere
        if not tanks == sum(i for i in tanks_r):
            print("Numero non adatto")
            print("Il numero adatto sarebbe", tanks)
            self.cards = selfcards_copy
            self.players[self.status].card_terr = card_terr_copy
            return

        # metti i tanks
        for i in range(len(tanks_r)):
            self.territories[[terry.name for terry in self.territories].index(terr_r[i])].tanks += tanks_r[i]

        print("Rinforzo:", terr_r, tanks_r)
        # à print("         ", tanks)
        self.can_reinforce[self.status] = False  


    def stampa_pl(self):
        for player in self.players:
            print(player)


    def stampa_ter(self):
        for terry in self.territories:
            print(terry)



