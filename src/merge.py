#!/usr/bin/env python3

##
## EPITECH PROJECT, 2023
## whorkshop-sort
## File description:
## merge
##

import sys
import time

def merge_sort(array: list):
    # Divise la liste non triée en deux moitiés jusqu'à ce que chaque sous-liste contienne un seul élément (une seule valeur est toujours triée).
    # Trie récursivement chaque sous-liste
    # Fusionne les sous-listes triées pour faire une liste unique triée.
    # Compare les éléments des sous-listes et les place dans le bon ordre.

    return array

def main():
    try:
        input_numbers = sys.stdin.readline().strip()  # Lecture de la ligne depuis stdin
        numbers = [int(x) for x in input_numbers.split()]  # Conversion en liste d'entiers
    except ValueError:
        print("Le fichier contient des valeurs non numériques.")
        return

    start_time = time.time()
    result = merge_sort(numbers)
    end_time = time.time()
    final_time = end_time - start_time

    print(f"New list: {result}")
    print(f"Time to sort: {final_time}")

if __name__ == "__main__":
    main()