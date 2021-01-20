import unittest
import uuid

from algorithms.algorithm_1 import Algorithm1
from algorithms.brute_force import BruteForce
from algorithms.two_stage_algorithms.algorithm_4 import Algorithm4
from algorithms.two_stage_algorithms.algorithm_5 import Algorithm5
from algorithms.two_stage_algorithms.algorithm_5_v2 import Algorithm5 as Algorithm5V2
from utils.models import TestResult


class TestAlgorithms(unittest.TestCase):
    times_to_run_test_suite = 10
    k1 = 10
    k2 = 41
    t1 = 3
    t2 = 5
    v1 = 3
    v2 = 5

    def test_algorithms_performance(self):
        for t in range(self.t1, self.t2, 1):
            for v in range(self.v1, self.v2, 1):
                for test in self.tests:
                    for k in range(self.k1, self.k2, 5):
                        for i in range(self.times_to_run_test_suite):
                            test_result = TestResult(id=str(uuid.uuid4()), t=t, k=k, v=v,
                                                     algorithm_name=test.__func__.__name__)
                            test.__func__(t=t, k=k, v=v, test_result=test_result)

    @staticmethod
    def brute_force(t: int, k: int, v: int, test_result: TestResult):
        BruteForce(t=t, k=k, v=v, test_result=test_result).run()

    @staticmethod
    def algorithm_1(t: int, k: int, v: int, test_result: TestResult):
        Algorithm1(t=t, k=k, v=v, test_result=test_result).run()

    @staticmethod
    def algorithm_4(t: int, k: int, v: int, test_result: TestResult):
        Algorithm4(t=t, k=k, v=v, test_result=test_result).run()

    @staticmethod
    def algorithm_5(t: int, k: int, v: int, test_result: TestResult):
        Algorithm5(t=t, k=k, v=v, test_result=test_result).run()

    @staticmethod
    def algorithm_5_v2(t: int, k: int, v: int, test_result: TestResult):
        Algorithm5V2(t=t, k=k, v=v, test_result=test_result).run()

    tests = [brute_force, algorithm_1, algorithm_4, algorithm_5, algorithm_5_v2]
