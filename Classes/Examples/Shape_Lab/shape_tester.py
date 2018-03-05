import shape

def main():
    p1 = shape.Point(2,3)
    p2 = shape.Point(5,3)
    p3 = shape.Point(2,7)
    
    print("point1:",p1)
    print("point2:",p2)
    print("point3:",p3)
    
    print("distance from p1 to p2: ",p1.distance(p2))
    
    s1 = shape.Segment(p1, p2)
    s2 = shape.Segment(p2, p3)
    s3 = shape.Segment(p3, p1)
    
    print("segment 1:",s1)
    print("segment 2:",s2)
    print("segment 3:",s3)
    
    print("segment 1 length:",s1.length())
    print("segment 2 length:",s2.length())
    print("segment 3 length:",s3.length())
    
    t1 = shape.Triangle(s1, s2, s3)
    print("Triangle 1:",t1)
    print("perimeter =",t1.perimeter())
    print("area =",t1.area())
    
    print()
    
       
    
    t2 = shape.Triangle(shape.Segment(shape.Point(5,9), shape.Point(10,9)),
                        shape.Segment(shape.Point(5,9), shape.Point(5,21)),
                        shape.Segment(shape.Point(5,21), shape.Point(10,9)))
    print("Triangle 2:",t2)
    print("perimeter =",t2.perimeter())
    print("area =",t2.area())
    
    
    
    
if __name__ == "__main__":
    main()