from utils.models import Algorithm
from utils.covering_arrays_generators import get_randomized_covering_array_in_memory, \
    generator_for_full_covering_array_with_k_columns
from algorithms.two_stage_algorithms.two_stage_algorithms_helpers import log, binom


class Algorithm1(Algorithm):
    def __exec(self):
        v_pow_t = pow(self.v, self.t)
        N = int((log(binom(self.k, self.t)) + self.t * log(self.v)) / (log(v_pow_t / (v_pow_t - 1))))
        covered = False
        self.A = list()
        self.test_result.first_stage_loops = 0
        while not covered:
            self.test_result.first_stage_loops += 1
            self.A = get_randomized_covering_array_in_memory(N, self.k, self.v)  # in memory as in algorithm
            covered = True
            for i in generator_for_full_covering_array_with_k_columns(self.k, self.v):
                did_find_cover = False
                for c in self.A:
                    amount_covered = 0
                    for index in range(self.k):
                        if c[index] == i[index]:
                            amount_covered += 1
                    if amount_covered >= self.t:
                        did_find_cover = True
                        break
                if not did_find_cover:
                    covered = False
                    break

    def run(self):
        self.__exec()
        self.test_result.first_stage_row_count = len(self.A)
        self.test_result.total_row_count = self.test_result.first_stage_row_count
        self.test_result.save()
