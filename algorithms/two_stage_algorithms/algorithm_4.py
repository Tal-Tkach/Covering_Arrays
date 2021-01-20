from dataclasses import dataclass, field
from typing import List

from algorithms.two_stage_algorithms.two_stage import TwoStage
from algorithms.two_stage_algorithms.two_stage_algorithms_helpers import validate_at_most_p_interaction_not_covered, \
    get_n_and_p_for_randomized_first_stage
from utils.covering_arrays_generators import get_randomized_covering_array_in_memory
from utils.covering_arrays_generic import Interaction


@dataclass
class Algorithm4(TwoStage):
    uncovered_interactions: List[Interaction] = field(default_factory=list)

    def _initiate_algorithm(self):
        self.n, self.p = get_n_and_p_for_randomized_first_stage(self.k, self.t, self.v)

    def _first_stage(self):
        self.test_result.first_stage_loops = 0
        is_stage_finished = False
        while not is_stage_finished:
            self.test_result.first_stage_loops += 1
            self.A = get_randomized_covering_array_in_memory(self.n, self.k, self.v)
            is_stage_finished, self.uncovered_interactions = validate_at_most_p_interaction_not_covered(self.A, self.t,
                                                                                                        self.k, self.v,
                                                                                                        self.p)
        self.test_result.uncovered_interactions_first_stage = len(self.uncovered_interactions)

    def _second_stage(self):
        # Adding all the missed interactions from stage 1 to the result array
        for interaction in self.uncovered_interactions:
            temp_interaction = [0] * self.k
            for i in range(len(interaction.cols)):
                temp_interaction[interaction.cols[i]] = interaction.values[i]
            self.A.append(temp_interaction)
