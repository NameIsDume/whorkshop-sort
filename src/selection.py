#!/usr/bin/env python3

##
## EPITECH PROJECT, 2023
## whorkshop-sort
## File description:
## selection
##

import sys
import time

def selection_sort(array: list):
    len_array = len(array)
    start_time = time.time()

    # Toute la liste est considérée comme non triée
    # On parcourt la liste à partir de la première position jusqu'à end - 1
    # Sélectionne l'élément le plus petit dans la partie non triée de la liste
    # L'élément le plus petit trouvé échange la première position de la partie non triée
    # Répètition jusqu'à ce que toute la liste soit triée.

    end_time = time.time()
    return array, end_time - start_time

def main():
    try:
        input_numbers = sys.stdin.readline().strip()  # Lecture de la ligne depuis stdin
        numbers = [int(x) for x in input_numbers.split()]  # Conversion en liste d'entiers
    except ValueError:
        print("Le fichier contient des valeurs non numériques.")
        return

    result, time = selection_sort(numbers)
    print(f"New list: {result}")
    print(f"Time to sort: {time}")

if __name__ == "__main__":
    main()