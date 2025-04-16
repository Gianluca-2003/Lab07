from database.meteo_dao import MeteoDao

class Model:
    def __init__(self):
        self.n_soluzioni = 0
        self.costo = 100000000
        self.soluzione = []



    def getUmiditaMedia(self, mese):
        return MeteoDao.getUmiditaMedia(mese)



    def calcolaSequenza(self, mese):
        situazioni = MeteoDao.getSituazioniPrimiGiorni(mese)
        #print(situazioni)
        self.soluzione = []
        self.costo = 1000000
        self.costo, self.soluzione = self.ricorsione(situazioni, [])
        print(self.costo)
        print(self.soluzione)
        return self.costo, self.soluzione


    def make_candidati(self, lista_situazioni,parziale):
        candidati = []
        for situazione in lista_situazioni:
            if situazione.data.day == len(parziale) +1:
                candidati.append(situazione)
        return candidati


    def calcolaGiorniDiFila(self,parziale):
        count = 0
        ultima = parziale[-1].localita
        if parziale[-2].localita == ultima:
            count += 1
        if parziale[-3].localita == ultima:
            count += 1
        return count


    def calcolaCosto(self,parziale):
        costo = 0
        #1) fattore dovuto all'umidita
        for situazione in parziale:
            costo += situazione.umidita
        #2) contributo di 100 se cambi
        n_citta = 0
        citta = parziale[0].localita
        for situazione in parziale:
            if situazione.localita != citta:
                costo += 100
                citta = situazione.localita

        return costo







    def is_valid(self,parziale,situazione):
        #primo vincolo: non puo stare piu di sei giorni
        counter = 0
        posti = []
        for s in parziale:
            posti.append(s.localita)
            if situazione.localita == s.localita:
                counter += 1
        if counter == 6:
            return False
        #secondo vincolo devo stare almeno 3 giorni in una citta prima di poter cambiare
        if len(parziale) == 0:
            return True
        if len(parziale) < 3:
            if parziale[-1].localita != situazione.localita:
                return False
        if len(parziale) >= 3:
            if parziale[-1].localita != situazione.localita:
                n_uguali = self.calcolaGiorniDiFila(parziale)
                if n_uguali < 2:
                    return False
        return True



    def ricorsione(self, lista_situazioni, parziale):
        if len(parziale) >= 15:
            self.n_soluzioni += 1
            costo = self.calcolaCosto(parziale)
            if self.costo > costo:
                self.costo = costo
                self.soluzione = list(parziale)
            return self.costo ,self.soluzione
            #print(parziale)
        else:
            candidati = self.make_candidati(lista_situazioni, parziale)
            for situazione in candidati:
                if self.is_valid(parziale,situazione):
                    parziale.append(situazione)
                    self.ricorsione(lista_situazioni, parziale)
                    parziale.pop()
            return self.costo, self.soluzione




if __name__ == '__main__':
    my_model = Model()
    my_model.calcolaSequenza(2)


















