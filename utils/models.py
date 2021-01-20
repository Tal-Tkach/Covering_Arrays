import os

from dataclasses import dataclass

from tinydb import TinyDB

if not os.path.exists('../results'):
    os.mkdir('../results')

db = TinyDB('../results/db.json')


@dataclass
class TestResult:
    t: int
    k: int
    v: int
    id: str
    algorithm_name: str = ''
    stage: int = 1
    first_stage_row_count: int = 0
    uncovered_interactions_first_stage: int = 0
    first_stage_loops: int = 0
    second_stage_row_count: int = 0
    second_stage_loops: int = 0
    total_row_count: int = 0

    def save(self):
        db.insert(vars(self))


@dataclass
class Algorithm:
    t: int
    k: int
    v: int
    test_result: TestResult

    def run(self):
        raise NotImplementedError()
