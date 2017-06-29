import pygame, sys, time
from random import randint
from Pilka import Pilka
from Paletka import Paletka


class Gra():

    def __init__(self):
        pygame.font.init()

        self.okienko_wysokosc = 720
        self.okienko_szerokosc = 1000
        self.okienko_tlo = (255, 255, 204)
        self.paletka_dol_kolor = (255, 0, 0)
        self.paletka_gora_kolor = (255, 100, 200)
        self.pilka_kolor = (0, 0, 0)
        self.szybkosc_pilki = 1
        self.szerokosc_pilki = 15
        self.szerokosc_paletki = 150
        self.wysokosc_paletki = 20
        pygame.init()

        self.pilka_start_y = self.okienko_wysokosc / 2
        self.pilka_start_x = self.okienko_szerokosc / 2
        self.paletka_dol = Paletka(self.okienko_szerokosc / 2 - (self.szerokosc_paletki / 2), 650, self.paletka_dol_kolor, self.wysokosc_paletki,
                                   self.szerokosc_paletki, True)
        self.paletka_gora = Paletka(self.okienko_szerokosc / 2 - (self.szerokosc_paletki / 2), 50, self.paletka_gora_kolor,
                                    self.wysokosc_paletki, self.szerokosc_paletki, False)
        self.pilka = Pilka(self.okienko_szerokosc / 2, self.okienko_wysokosc / 2, self.pilka_kolor, self.szerokosc_pilki, self.szybkosc_pilki)

        self.okienko = pygame.display.set_mode((self.okienko_szerokosc, self.okienko_wysokosc))

        pygame.display.update()


    def zdarzenie(self):
        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                self.paletka_dol.punkty = 0
                self.paletka_gora.punkty = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                if self.paletka_gora.czlowiek:
                    self.paletka_gora.czlowiek = False
                else:
                    self.paletka_gora.czlowiek = True

    def nowa_gra(self):
        self.pilka.x = self.pilka_start_x
        self.pilka.y = self.pilka_start_y
        self.paletka_gora.x = self.pilka_start_x - self.paletka_gora.szerokosc / 2
        self.paletka_dol.x = self.pilka_start_x - self.paletka_dol.szerokosc / 2
        time.sleep(1)


    def wejscie(self):
        # Koniec pojedyńczej gry
        if self.pilka.y == 0:
            self.pilka.odbicie = 'prosto_dol'
            self.paletka_dol.punkty += 1
            self.nowa_gra()
        if self.pilka.y >= self.okienko_szerokosc - 200:
            self.pilka.odbicie = 'prosto_gora'
            self.paletka_gora.punkty += 1
            self.nowa_gra()

        keys = pygame.key.get_pressed()
        # Sterowanie paletka dół
        if (keys[pygame.K_LEFT]):
            if self.paletka_dol.x > 0:
                self.paletka_dol.x -= 1
        if (keys[pygame.K_RIGHT]):
            if self.paletka_dol.x < self.okienko_szerokosc - self.paletka_dol.szerokosc:
                self.paletka_dol.x += 1

        # Sterowanie paletka góra
        if (keys[pygame.K_a]):
            if self.paletka_gora.x > 0:
                self.paletka_gora.x -= 1
        if (keys[pygame.K_d]):
            if self.paletka_gora.x < self.okienko_szerokosc - self.paletka_gora.szerokosc:
                self.paletka_gora.x += 1

        if self.paletka_gora.czlowiek:
            # sterowanie poprzez człowieka
            # górna paletka
            if self.pilka.x >= self.paletka_gora.x and self.pilka.x <= self.paletka_gora.x + self.szerokosc_paletki and self.paletka_gora.y + self.paletka_gora.wysokosc + self.pilka.szerokosc == self.pilka.y:
                if self.pilka.x <= self.paletka_gora.x + self.szerokosc_paletki / 3:
                    self.pilka.odbicie = 'lewo_gora'
                    self.pilka.kierunek = False
                elif self.pilka.x <= self.paletka_gora.x + 2 * self.szerokosc_paletki / 3:
                    self.pilka.odbicie = 'prosto_gora'
                    self.pilka.kierunek = False
                elif self.pilka.x <= self.paletka_gora.x + self.szerokosc_paletki:
                    self.pilka.odbicie = 'prawo_gora'
                    self.pilka.kierunek = False
        else:
            # sterowanie komputer
            self.paletka_gora.x = self.pilka.x - self.paletka_gora.szerokosc / 2
            x = randint(0, 2)
            # górna paletka
            if self.pilka.x >= self.paletka_gora.x and self.pilka.x <= self.paletka_gora.x + 130 and self.paletka_gora.y + self.paletka_gora.wysokosc + self.pilka.szerokosc == self.pilka.y:
                if x == 1:
                    self.pilka.odbicie = 'lewo_gora'
                    self.pilka.kierunek = False
                if x == 2:
                    self.pilka.odbicie = 'prosto_gora'
                    self.pilka.kierunek = False
                if x == 0:
                    self.pilka.odbicie = 'prawo_gora'
                    self.pilka.kierunek = False

        # Dolna palteka
        if self.pilka.x >= self.paletka_dol.x and self.pilka.x <= self.paletka_dol.x + self.szerokosc_paletki and self.paletka_dol.y - self.pilka.szerokosc == self.pilka.y:
            if self.pilka.x <= self.paletka_dol.x + self.szerokosc_paletki / 3:
                self.pilka.odbicie = 'lewo_dol'
                self.pilka.kierunek = True
            elif self.pilka.x <= self.paletka_dol.x + 2 * self.szerokosc_paletki / 3:
                self.pilka.odbicie = 'prosto_dol'
                self.pilka.kierunek = True
            elif self.pilka.x <= self.paletka_dol.x + self.szerokosc_paletki:
                self.pilka.odbicie = 'prawo_dol'
                self.pilka.kierunek = True

        # lewa scianka
        if self.pilka.x == 0:
            if self.pilka.kierunek:
                self.pilka.odbicie = 'lewa_scianka_od_dolu'
            else:
                self.pilka.odbicie = 'lewa_scianka_od_gory'

        # prawa scianka
        if self.pilka.x == self.okienko_szerokosc - self.pilka.szerokosc:
            if self.pilka.kierunek:
                self.pilka.odbicie = 'prawa_scianka_od_dolu'
            else:
                self.pilka.odbicie = 'prawa_scianka_od_gory'

        # Odbicie piłki
        if self.pilka.odbicie == 'lewo_dol' or self.pilka.odbicie == 'prawa_scianka_od_dolu':
            self.pilka.y -= self.pilka.predkosc
            self.pilka.x -= self.pilka.predkosc
        elif self.pilka.odbicie == 'prosto_dol':
            self.pilka.y -= self.pilka.predkosc
        elif self.pilka.odbicie == 'prawo_dol' or self.pilka.odbicie == 'lewa_scianka_od_dolu':
            self.pilka.y -= self.pilka.predkosc
            self.pilka.x += self.pilka.predkosc
        elif self.pilka.odbicie == 'prosto_gora':
            self.pilka.y += self.pilka.predkosc
        elif self.pilka.odbicie == 'prawo_gora' or self.pilka.odbicie == 'lewa_scianka_od_gory':
            self.pilka.y += self.pilka.predkosc
            self.pilka.x += self.pilka.predkosc
        elif self.pilka.odbicie == 'lewo_gora' or self.pilka.odbicie == 'prawa_scianka_od_gory':
            self.pilka.y += self.pilka.predkosc
            self.pilka.x -= self.pilka.predkosc
        else:
            self.pilka.y += self.pilka.predkosc


    def rysowanie(self):
        self.okienko.fill(self.okienko_tlo)
        pygame.draw.rect(self.okienko, self.paletka_dol.kolor,
                         (self.paletka_dol.x, self.paletka_dol.y, self.paletka_dol.szerokosc, self.paletka_dol.wysokosc))
        pygame.draw.rect(self.okienko, self.paletka_gora.kolor,
                         (self.paletka_gora.x, self.paletka_gora.y, self.paletka_gora.szerokosc, self.paletka_gora.wysokosc))
        pygame.draw.circle(self.okienko, self.pilka.kolor, (int(self.pilka.x), int(self.pilka.y)), self.pilka.szerokosc, self.pilka.szerokosc)
        font = pygame.font.SysFont("consolas", 72)
        text = font.render(str(self.paletka_gora.punkty) + ' : ' + str(self.paletka_dol.punkty), True, (0, 0, 0))
        self.okienko.blit(text,
                     (self.okienko_szerokosc / 2 - text.get_width() // 2, self.okienko_wysokosc / 2 - text.get_height() // 2))

        pygame.display.flip()


    def main(self):
        while True:
            self.zdarzenie()
            self.wejscie()
            self.rysowanie()

