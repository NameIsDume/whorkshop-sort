#!/usr/bin/env python3

##
## EPITECH PROJECT, 2023
## whorkshop-sort
## File description:
## insertion
##

import time
import sys

def insertion_sort(array: list):
    start_time = time.time() # Je débute le chrono
    len_array: int = len(array) # Je recup la longueur

    # Première étape on pense que la première valeur est déjà bonne
    # Parcours la liste on considère chaque élément comme une clé à insérer dans la portion triée
    # À chaque boucle, on compare la clé avec les éléments de la portion triée
    # Déplace les éléments plus grands que la clé vers la droite pour faire de la place à la clé à sa bonne position
    # On repète jusqu'a ce que tout soit bon

    end_time = time.time()  # Enregistre le temps de fin
    return array, end_time - start_time

def main(): # Pas besoin de toucher au main
    try:
        input_numbers = sys.stdin.readline().strip()
        numbers = [int(x) for x in input_numbers.split()]
    except ValueError:
        print("Le fichier contient des valeurs non numériques.")
        return

    result, time = insertion_sort(numbers)
    print(f"New list: {result}")
    print(f"Time to sort: {time}")

if __name__ == "__main__":
    main()