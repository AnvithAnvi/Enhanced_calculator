import os
import pandas as pd
from app.history import History
from app.calculation import Calculation

def test_add_and_to_dataframe(tmp_path):
    h = History()
    calc = Calculation(2, 3, "add", 5)
    h.add(calc)
    df = h.to_dataframe()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1

def test_load_from_csv(tmp_path):
    file = tmp_path / "test.csv"
    pd.DataFrame([{"operand1":1,"operation":"add","operand2":2,"result":3,"timestamp":"2025-01-01"}]).to_csv(file, index=False)
    h = History()
    h.load_from_csv(file)
    assert len(h._history) == 1
