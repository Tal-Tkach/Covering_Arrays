from dataclasses import dataclass, field
from typing import List

from utils.models import Algorithm


@dataclass
class TwoStage(Algorithm):
    n: int = 0
    p: int = 0
    A: List = field(default_factory=list)

    def _initiate_algorithm(self):
        raise NotImplementedError()

    def _first_stage(self):
        raise NotImplementedError()

    def __first_stage_exec(self):
        self.test_result.stage = 1
        self._first_stage()
        self.test_result.first_stage_row_count = len(self.A)
        self.test_result.save()

    def _second_stage(self):
        raise NotImplementedError()

    def __second_stage_exec(self):
        self.test_result.stage = 2
        self._second_stage()
        self.test_result.total_row_count = len(self.A)
        self.test_result.second_stage_row_count = self.test_result.total_row_count - self.test_result.first_stage_row_count
        self.test_result.save()

    def run(self):
        self._initiate_algorithm()
        self.__first_stage_exec()
        self.__second_stage_exec()
