from app.calculation import Calculation

def test_calculation_str():
    c = Calculation(2, 3, "add", 5)
    s = str(c)
    assert "add" in s and "=" in s
