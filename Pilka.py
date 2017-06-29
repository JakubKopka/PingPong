from Figura import Figura


class Pilka(Figura):

    def __init__(self, x, y, kolor, szerokosc, predkosc):
        super().__init__(x, y, kolor, szerokosc)
        self.kierunek = False
        self.odbicie = 'prosto'
        self.predkosc = predkosc