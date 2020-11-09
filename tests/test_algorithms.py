import time
import unittest
from dataclasses import dataclass

from utils import generator_for_full_covering_array_of_points, failing_find_right_triangle_in_10_points_array, \
    working_find_right_triangle_in_10_points_array


@dataclass
class Counter:
    failed_count: int = 0


def benchmark(func):
    def wrapper(*args, **kwargs):
        ts = time.time()
        func(*args, **kwargs)
        te = time.time()
        print(f'{args[0]._testMethodName} executed in {(te - ts) * 1000} ms')

    return wrapper


def measure_success_rate(func):
    def wrapper(*args, **kwargs):
        counter = Counter()
        func(*args, counter=counter, **kwargs)
        print(
            f'caught failing in {(counter.failed_count / TestAlgorithms.times_to_run_test_suite) * 100}% of the tests')

    return wrapper


class TestAlgorithms(unittest.TestCase):
    times_to_run_test_suite = 1000
    number_of_points_in_test_list = 3
    min_x_for_point = 0
    max_x_for_point = 2
    min_y_for_point = 0
    max_y_for_point = 2

    @benchmark
    @measure_success_rate
    def test_brute_force(self, counter: Counter):
        for i in range(self.times_to_run_test_suite):
            for points_list in generator_for_full_covering_array_of_points(self.number_of_points_in_test_list,
                                                                           self.min_x_for_point, self.max_x_for_point,
                                                                           self.min_y_for_point, self.max_y_for_point):
                failing_algorithm_result = failing_find_right_triangle_in_10_points_array(points_list)
                working_algorithm_result = working_find_right_triangle_in_10_points_array(points_list)
                if failing_algorithm_result != working_algorithm_result:
                    counter.failed_count += 1
                    break
