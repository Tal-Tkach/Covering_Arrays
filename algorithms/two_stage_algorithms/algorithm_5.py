from algorithms.two_stage_algorithms.two_stage import TwoStage
from algorithms.two_stage_algorithms.two_stage_algorithms_helpers import get_N_for_LLL
from utils.covering_arrays_generators import get_randomized_covering_array_in_memory, generate_random_k_values_array, \
    t_columns_of_k_generator, generator_for_full_covering_array_with_k_columns


class Algorithm5(TwoStage):
    def _initiate_algorithm(self):
        self.n = get_N_for_LLL(self.t, self.k, self.v)

    def _first_stage(self):
        self.A = get_randomized_covering_array_in_memory(self.n, self.k, self.v)

    def _second_stage(self):
        all_covered = False
        self.test_result.second_stage_loops = 0
        while not all_covered:
            all_covered = True
            # Iterating all the possible combinations of t columns of values from v
            for cols, values in self.cols_values_generator():
                if not self.is_covered(cols, values):
                    self.randomized_interaction_columns(cols)
                    all_covered = False
                    break
            self.test_result.second_stage_loops += 1

    def cols_values_generator(self):
        for c in t_columns_of_k_generator(self.k, self.t):  # All the possible columns combinations
            for v in generator_for_full_covering_array_with_k_columns(self.t,self.v):  # All cartesian product of possible values for t columns
                yield c, v

    def randomized_interaction_columns(self, cols):
        for row in range(self.n):
            # Generate a new random values for the t columns
            new_interaction = next(generate_random_k_values_array(self.t, self.v))
            # Sets the t columns in the new row with the values from the uncovered interaction
            for i in range(len(cols)):
                self.A[row][cols[i]] = new_interaction[i]

    def is_covered(self, cols, values):
        for row in self.A:
            # Validate all values of the the current row in the specified columns match the interaction values
            if all((row[cols[j]] == values[j] for j in range(self.t))):
                return True
        return False
