from itertools import combinations, product
from typing import List
from random import randint


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x},{self.y})"


def is_right_triangle(p1: Point, p2: Point, p3: Point):
    # Distance between p1 and p2
    d1 = (int(pow((p2.y - p1.x), 2)) + int(pow((p2.y - p1.x), 2)))

    # Distance between p2 and p3
    d2 = (int(pow((p3.y - p2.x), 2)) + int(pow((p3.y - p2.x), 2)))

    # Distance between p3 and p1
    d3 = (int(pow((p1.y - p3.x), 2)) + int(pow((p1.y - p3.x), 2)))

    # Validating Pythagoras a^2 = b^2 + c^2 for all possible root point
    if any([d1 == d2 + d3, d2 == d1 + d3, d3 == d1 + d2]):
        return True

    return False


def is_fail_right_triangle(p1: Point, p2: Point, p3: Point):
    # Distance between p1 and p2
    d1 = (int(pow((p2.y - p1.x), 2)) + int(pow((p2.y - p1.x), 2)))

    # Distance between p2 and p3
    d2 = (int(pow((p3.y - p2.x), 2)) + int(pow((p3.y - p2.x), 2)))

    # Distance between p3 and p1
    d3 = (int(pow((p1.y - p3.x), 2)) + int(pow((p1.y - p3.x), 2)))

    # Validating Pythagoras a^2 = b^2 + c^2 only p1 as root point
    if d1 == d2 + d3:
        return True

    return False


# Performance : O(n^3) given the n is the length of the array
def working_find_right_triangle_in_10_points_array(points: List[Point]):
    every_3_points_set = combinations(points, 3)
    for three_points_set in every_3_points_set:
        if is_right_triangle(*three_points_set):
            return True
    return False


# Performance : O(n^3) given the n is the length of the array
def failing_find_right_triangle_in_10_points_array(points: List[Point]):
    n = len(points)
    for i in range(n):  # Iterate over all the points
        for j in range(n - i, n):  # Iterate only over the points after the first checking point
            for h in range(n - j, n):  # Iterate only over the points after the first and second checking points
                if is_fail_right_triangle(points[i], points[j], points[h]):
                    return True
    return False


# Generates a random point with min_x<=x<max_x and min_y<=y<max_y
def generate_random_point(min_x: int, max_x: int, min_y: int, max_y: int):
    # # To reduce time skipping validations
    # if max_x < min_x or max_y < min_y:
    #     raise ValueError("Invalid input")
    return Point(randint(min_x, max_x), randint(min_y, max_y))


# Generates a random points array with n points
def generate_random_points_array(k: int, min_x: int, max_x: int, min_y: int, max_y: int):
    # # To reduce time skipping validations
    # if k <= 0 or max_x < min_x or max_y < min_y:
    #     raise ValueError("Invalid input")
    points = list()
    for i in range(k):
        points.append(generate_random_point(min_x, max_x - 1, min_y, max_y - 1))
    return points


# Generates a random points array with n points
def generator_for_random_points_covering_array(n: int, k: int, min_x: int, max_x: int, min_y: int, max_y: int):
    # # To reduce time skipping validations
    # if n<=0 or k <= 0 or max_x < min_x or max_y < min_y:
    #     raise ValueError("Invalid input")
    for i in range(n):
        yield generate_random_points_array(k, min_x, max_x, min_y, max_y)


def generator_for_full_covering_array_of_points(k: int, min_x: int, max_x: int, min_y: int, max_y: int):
    all_kind_of_points = list()
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            all_kind_of_points.append(Point(x, y))

    yield from product(all_kind_of_points, repeat=k)
