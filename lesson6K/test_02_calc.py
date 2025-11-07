import pytest
from calc_02 import Calc

@pytest.mark.parametrize ('inTime, result', [(45, 45)])
def test_time_wait(inTime, result):
    calc = Calc(inTime)
    calc.web()
    res = calc.time_Wait()
    calc.Quit()
    assert result == res
    
    
