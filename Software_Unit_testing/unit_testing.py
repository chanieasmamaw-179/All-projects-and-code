import pytest
from main import my_sum

def tes1(num):
    assert my_sum([1,2,3]) == True
    
def test2(num):
    assert my_sum([0]) == True
    
def test3(num):
    assert my_sum([None]) == True
    