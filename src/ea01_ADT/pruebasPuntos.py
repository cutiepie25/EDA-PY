import math
from point2DCartesian import Point2DCartesian
from point2DPolar import Point2DPolar


if __name__=="__main__":
    p1 = Point2DCartesian(0,0)
    p2 = Point2DPolar(1, math.pi/4)
    p3 = Point2DCartesian(p2.getX(), p2.getY())

    print(p1)
    print(p2)    
    print(p3)

    assert p1!=p2, 'p1 y p2 deben ser distintos'
    assert p2==p3, 'p2 y p3 deben ser iguales'    
    assert p3!=p1, 'p3 y p1 deben ser distintos'

    assert p2.getX()==math.sqrt(2)/2, "la componente x de p2 debe ser raiz(2)/2"

    assert abs(p2)==1, "La magnitud de p2 debe ser la unidad"
    assert abs(p3)==1, "La magnitud de p3 debe ser la unidad"    

    