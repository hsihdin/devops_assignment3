import pytest  
from area import calculate_area_square  

def test_calculate_area_square():  
    assert calculate_area_square(2)==4  
    assert calculate_area_square(3)==10
    # test with last 2 digits of student id    
    assert calculate_area_square(77)==5929

          
def test_calculate_area_square_negative():  
    with pytest.raises(TypeError):  
        calculate_area_square(-2)  
  
def test_calculate_area_square_string():  
    with pytest.raises(TypeError):  
        calculate_area_square("2")  
  
def test_calculate_area_square_list():  
    with pytest.raises(TypeError):  
        calculate_area_square([2])
