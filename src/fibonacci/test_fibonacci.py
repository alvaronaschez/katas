import json

import pytest

from .fibonacci import (
    recursive_fibonacci,
    iterative_fibonacci,
    generator_fibonacci,
)

with open("test_data.json") as json_file:
    test_data = json.load(json_file)

benchmark_test_data = [x for x in test_data if x[0] in {10, 100, 1000}]


@pytest.fixture(autouse=True, scope="function")
def clean_cache():
    yield
    recursive_fibonacci.cache_clear()


@pytest.mark.benchmark
@pytest.mark.parametrize("n,expected", test_data)
@pytest.mark.parametrize(
    "fibonacci", [recursive_fibonacci, iterative_fibonacci, generator_fibonacci]
)
def test_fibonacci(fibonacci, n, expected):
    assert expected == fibonacci(n)


@pytest.mark.benchmark
@pytest.mark.parametrize("n,expected", benchmark_test_data)
@pytest.mark.parametrize(
    "fibonacci", [recursive_fibonacci, iterative_fibonacci, generator_fibonacci]
)
def test_fibonacci_benchmark(fibonacci, n, expected, benchmark):
    assert expected == benchmark(fibonacci, n)
