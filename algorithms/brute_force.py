from utils.models import Algorithm
from utils.covering_arrays_generators import generator_for_full_covering_array_with_k_columns


class BruteForce(Algorithm):
    def __exec(self):
        self.A = [_ for _ in generator_for_full_covering_array_with_k_columns(self.k, self.v)]

    def run(self):
        self.__exec()
        self.test_result.first_stage_row_count = len(self.A)
        self.test_result.total_row_count = self.test_result.first_stage_row_count
        self.test_result.save()
