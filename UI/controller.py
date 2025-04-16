import flet as ft

from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # other attributes
        self._mese = 0

    def handle_umidita_media(self, e):
        self._view.lst_result.controls.clear()
        if self._mese == 0:
            self._view.create_alert("Seleziona un mese prima di procedere")
            return
        localita = self._model.getUmiditaMedia(self._mese)
        self._view.lst_result.controls.append(ft.Text("L'umidità media nel mese selezionato è:"))
        for l in localita:
            self._view.lst_result.controls.append(ft.Text(f"{l}: {localita[l]}"))
        self._view.update_page()



    def handle_sequenza(self, e):
        self._view.lst_result.controls.clear()
        if self._mese == 0:
            self._view.create_alert("Seleziona un mese prima di procedere")
            return
        costo, sequenza = self._model.calcolaSequenza(self._mese)
        self._view.lst_result.controls.append(ft.Text(f"La seuqnza ottima ha costo {costo} ed é:"))
        for situazione in sequenza:
            self._view.lst_result.controls.append(ft.Text(str(situazione)))
        self._view.update_page()









    def read_mese(self, e):
        self._mese = int(e.control.value)
        print(self._mese)

