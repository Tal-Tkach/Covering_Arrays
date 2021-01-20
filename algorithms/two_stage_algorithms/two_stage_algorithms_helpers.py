import math
from typing import List

import scipy.special

from utils.covering_arrays_generators import t_columns_of_k_generator, generator_for_full_covering_array_with_k_columns
from utils.covering_arrays_generic import Interaction

binom = scipy.special.binom
log = math.log


def get_N_for_LLL(t: int, k: int, v: int):
    v_pow_t = pow(v, t)
    t_from_k = binom(k, t)
    t_from_k_minus_t = binom(k - t, t)
    dividend = log(t_from_k - t_from_k_minus_t) + t * log(v) + 1
    divisor = log(v_pow_t / (v_pow_t - 1))
    return math.ceil(dividend / divisor)


def get_n_and_p_for_randomized_first_stage(k: int, t: int, v: int):
    t_from_k = binom(k, t)
    v_pow_t = pow(v, t)
    denom = log(v_pow_t / (v_pow_t - 1))
    nume = log(t_from_k) + t*log(v) + log(denom)
    n = math.ceil(nume / denom)
    p = 1/denom
    return n, p


def validate_at_most_p_interaction_not_covered(A: List, t: int, k: int, v: int, p: int):
    uncovered_interaction: List[Interaction] = list()
    is_stage_finished = True
    for cols_to_check in t_columns_of_k_generator(k, t):  # Iterate over the interactions all t columns out of k
        # Each t-tuple value possible
        covered_interactions = {i: False for i in generator_for_full_covering_array_with_k_columns(t, v)}
        for row in A:  # Iterate over the entire random array to find which interactions are cover
            temp_cover = [row[cols_to_check[i]] for i in range(t)]
            covered_interactions.pop(tuple(temp_cover), None)  # Setting the current row interaction value as covered

        for interaction, is_interaction_covered in covered_interactions.items():
            uncovered_interaction.append(Interaction(cols=cols_to_check, values=interaction))
        if len(uncovered_interaction) > p:
            is_stage_finished = False
            break
    return is_stage_finished, uncovered_interaction
