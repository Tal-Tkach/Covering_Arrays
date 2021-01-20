from algorithms.two_stage_algorithms.two_stage import TwoStage
from algorithms.two_stage_algorithms.two_stage_algorithms_helpers import get_N_for_LLL, \
    validate_at_most_p_interaction_not_covered
from utils.covering_arrays_generators import get_randomized_covering_array_in_memory, generate_random_k_values_array, \
    t_columns_of_k_generator, generator_for_full_covering_array_with_k_columns


class Algorithm5(TwoStage):
    def _initiate_algorithm(self):
        self.n = get_N_for_LLL(self.t, self.k, self.v)

    def _first_stage(self):
        self.A = get_randomized_covering_array_in_memory(self.n, self.k, self.v)

    def _second_stage(self):
        self.test_result.second_stage_loops = 0
        is_stage_finished = False
        while not is_stage_finished:
            self.test_result.second_stage_loops += 1
            is_stage_finished, uncovered_interactions = validate_at_most_p_interaction_not_covered(self.A, self.t,
                                                                                                   self.k, self.v,
                                                                                                   0)
            if uncovered_interactions:
                self.randomized_interaction_columns(uncovered_interactions[0].cols)

    def randomized_interaction_columns(self, cols):
        for row in range(self.n):
            # Generate a new random values for the t columns
            new_interaction = next(generate_random_k_values_array(self.t, self.v))
            # Sets the t columns in the new row with the values from the uncovered interaction
            for i in range(len(cols)):
                self.A[row][cols[i]] = new_interaction[i]
