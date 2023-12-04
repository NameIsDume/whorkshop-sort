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
    start_time = time.time() # Je début le chrono
    len_array: int = len(array) # Je recup la longueur

    for i in range(len_array):
        for j in range(0, len_array-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    end_time = time.time()  # Enregistre le temps de fin
    return array, end_time - start_time

def main():
    try:
        input_numbers = sys.stdin.readline().strip()  # Lecture de la ligne depuis stdin
        numbers = [int(x) for x in input_numbers.split()]  # Conversion en liste d'entiers
    except ValueError:
        print("Le fichier contient des valeurs non numériques.")
        return

    result, time = bubble_sort(numbers)
    print(f"New list: {result}")
    print(f"Time to sort: {time}")

if __name__ == "__main__":
    main()

