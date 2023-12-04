#!/usr/bin/env python3

##
## EPITECH PROJECT, 2023
## whorkshop-sort
## File description:
## quick
##

import sys
import time

def quick_sort(array):
    # Choix du pivot, on choisit le premier, le dernier ou un élément médian de la liste
    # Réorganise la liste pour que tous les éléments plus petits que le pivot soient à gauche, et tous les éléments plus grands à droite. Après, le pivot est à sa position finale.
    # Récursivité l'algorithme de tri rapide aux sous-listes à gauche et à droite du pivot jusqu'à ce que toute la liste soit triée.


def main():
    try:
        input_numbers = sys.stdin.readline().strip()  # Lecture de la ligne depuis stdin
        numbers = [int(x) for x in input_numbers.split()]  # Conversion en liste d'entiers
    except ValueError:
        print("Le fichier contient des valeurs non numériques.")
        return

    start_time = time.time()
    result = quick_sort(numbers)
    end_time = time.time()
    final_time = end_time - start_time
    print(f"New list: {result}")
    print(f"Time to sort: {final_time}")

if __name__ == "__main__":
    main()