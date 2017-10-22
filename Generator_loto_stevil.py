#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def generator(neenako_stevilo):
    lista_stevil = []

    while True:
        if len(lista_stevil) == neenako_stevilo:
            break

        izbrano_stevilo = random.randint(1, 39)

        if izbrano_stevilo not in lista_stevil:
            lista_stevil.append(izbrano_stevilo)

    return sorted(lista_stevil)



print("Lotto generator števil.")

start = "da"

while start.lower() == "da" or start.lower() == "d":
    koliko_stevil = raw_input("Koliko števil si želite?: ")

    try:
        koliko_stevil_stevilo = int(koliko_stevil)
        print generator(koliko_stevil_stevilo)

        start = raw_input("Bi imel še več števil? (Da/Ne) ")
    except:
        print("Nisi vnesel števila.")
        start = raw_input("Boš poskusil še enkrat? (Da/Ne) ")

print("Program zaključen.")
