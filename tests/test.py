from my_area import Myarea
def  calc_area():
    """
    to make sure that def  calc_area is working
    """
    assert Myarea.calc_area(3,4)==12,'incorrect'
    assert Myarea.calc_area(5,6)==30,'incorrect'
    assert Myarea.calc_area(7,4)==28,'incorrect'