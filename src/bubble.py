#!/usr/bin/env python3

##
## EPITECH PROJECT, 2023
## whorkshop-sort
## File description:
## bubble
##

import time
import sys

def bubble_sort(array: list):
    start_time = time.time() # Je débute le chrono
    len_array: int = len(array) # Je recup la longueur

    # Vous devez refaire le bubble sort
    # Vous comparez chaque element avec son voisin et les echanger si nécessaire


    end_time = time.time()  # Enregistre le temps de fin
    return array, end_time - start_time

def main(): # Pas besoin de toucher au main
    try:
        input_numbers = sys.stdin.readline().strip()
        numbers = [int(x) for x in input_numbers.split()]
    except ValueError:
        print("Le fichier contient des valeurs non numériques.")
        return

    result, time = bubble_sort(numbers)
    print(f"New list: {result}")
    print(f"Time to sort: {time}")

if __name__ == "__main__":
    main()

