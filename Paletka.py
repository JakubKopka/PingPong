from Figura import Figura
class Paletka(Figura):
    def __init__(self, x, y, kolor, wysokosc, szerokosc, czlowiek):
        super().__init__(x,y,kolor, szerokosc)
        self.wysokosc = wysokosc
        self.punkty = 0
        self.czlowiek = czlowiek