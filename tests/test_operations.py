import pytest
from app.operations import OperationFactory

@pytest.mark.parametrize("a,b,op,expected", [
    (2, 3, "add", 5),
    (5, 2, "subtract", 3),
    (2, 3, "power", 8),
    (9, 2, "root", 3),
    (10, 3, "modulus", 1)
])
def test_operations(a, b, op, expected):
    func = OperationFactory.create(op)
    assert round(func(a, b), 2) == expected
