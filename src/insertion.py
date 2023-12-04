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
    start_time = time.time() # Je début le chrono
    len_array: int = len(array) # Je recup la longueur

    for i in range(1, len_array):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

    end_time = time.time()  # Enregistre le temps de fin
    return array, end_time - start_time

def main():
    try:
        input_numbers = sys.stdin.readline().strip()  # Lecture de la ligne depuis stdin
        numbers = [int(x) for x in input_numbers.split()]  # Conversion en liste d'entiers
    except ValueError:
        print("Le fichier contient des valeurs non numériques.")
        return

    result, time = insertion_sort(numbers)
    print(f"New list: {result}")
    print(f"Time to sort: {time}")

if __name__ == "__main__":
    main()