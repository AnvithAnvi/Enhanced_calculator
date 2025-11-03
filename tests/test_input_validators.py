import pytest
from app.input_validators import validate_number
from app.exceptions import ValidationError

def test_valid_number():
    assert validate_number("5") == 5.0

def test_invalid_number():
    with pytest.raises(ValidationError):
        validate_number("abc")

def test_exceeds_max():
    with pytest.raises(ValidationError):
        validate_number("999999999")
