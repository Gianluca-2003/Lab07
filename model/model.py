from database.meteo_dao import MeteoDao

class Model:
    def __init__(self):
        self._umidita = None
        self._risultati = [float("inf"), []]
        self._conteggio = {"Milano": 0, "Torino": 0, "Genova": 0}

    def getUmiditaMedia(self, mese):
        return MeteoDao.getUmiditaMedia(mese)

    def getUmiditaMesePrimiGiorni(self, mese):
        return MeteoDao.getUmiditaMesePrimiGiorni(mese)

    def calcolaPercorsoMinimoCosto(self, umidita):
        self._umidita = umidita
        self._risultati = [float("inf"), []]
        self._conteggio = {"Milano": 0, "Torino": 0, "Genova": 0}
        self._ricorsione([], 0, 0)
        print("\n✅ Miglior sequenza trovata con costo:", self._risultati[0])
        for citta, data, umid in self._risultati[1]:
            print(f"{data} - {citta}: Umidità = {umid}%")
        return self._risultati[0], self._risultati[1]

    def _ricorsione(self, parziale, giorno, costo):
        if giorno == 15:
            if costo < self._risultati[0]:
                self._risultati[0] = costo
                self._risultati[1] = list(parziale)
                print(f"\n🎯 Nuova miglior sequenza trovata! Costo: {costo}")
                for citta, data, umid in parziale:
                    print(f"{data} - {citta}: {umid}%")
            return
        citta_ordinate = sorted(self._umidita.keys(), key=lambda c: self._umidita[c][giorno][1])
        for citta in citta_ordinate:
            if self._conteggio[citta] >= 6:
                continue

            if len(parziale) >= 3 and parziale[-1][0] != citta:
                ultime3 = [entry[0] for entry in parziale[-3:]]
                if ultime3 != [parziale[-1][0]] * 3:
                    continue
            elif 0 < len(parziale) < 3 and parziale[-1][0] != citta:
                continue

            data, umid = self._umidita[citta][giorno]
            nuovo_costo = costo + umid
            if len(parziale) > 0 and parziale[-1][0] != citta:
                nuovo_costo += 100
            print(f"Giorno {giorno + 1}: provo {citta} - {data} (umidità={umid}%) costo attuale = {nuovo_costo}")

            parziale.append((citta, data, umid))
            self._conteggio[citta] += 1

            self._ricorsione(parziale, giorno + 1, nuovo_costo)

            parziale.pop()
            self._conteggio[citta] -= 1
















