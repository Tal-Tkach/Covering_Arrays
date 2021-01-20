from itertools import combinations, product

import numpy as np


# Generates a random k items array with each item chosen randomly from between 0 and v
def generate_random_k_values_array(k: int, v: int):
    yield np.random.randint(low=0, high=v, size=k, dtype=np.uint8)


# Generates a full covering array with k columns and each cell has one of the values of v
def generator_for_full_covering_array_with_k_columns(k: int, v: int):
    yield from product(range(v), repeat=k)


# Generates all the ways to chose t indices from k indices
def t_columns_of_k_generator(k: int, t: int):
    yield from combinations(range(k), t)


# Returns a random array with n rows of k item where each item chosen randomly from v
def get_randomized_covering_array_in_memory(n: int, k: int, v: int):
    return [next(generate_random_k_values_array(k, v)) for _ in range(n)]
