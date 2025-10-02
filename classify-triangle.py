def classify_triangle(a, b, c):
    """Classify a triangle as Equilateral, Isosceles, Right, or Scalene."""
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "Right"
    else:
        return "Scalene"

def test_equilateral():
    """Test case for equilateral triangle classification."""
    assert classify_triangle(3, 3, 3) == "Equilateral"

def test_isosceles():
    """Test case for isosceles triangle classification."""
    assert classify_triangle(4, 4, 5) == "Isosceles"
    assert classify_triangle(5, 4, 5) == "Isosceles"
    assert classify_triangle(4, 5, 5) == "Isosceles"

def test_right():
    """Test case for right triangle classification."""
    assert classify_triangle(3, 4, 5) == "Right"
    assert classify_triangle(5, 12, 13) == "Right"

def test_scalene():
    """Test case for scalene triangle classification."""
    assert classify_triangle(4, 5, 6) == "Scalene"
    assert classify_triangle(2, 3, 4) == "Scalene"


if __name__ == "__main__":
    a = float(input("Enter the length of the first side of the triangle:"))
    b = float(input("Enter the length of the second side of the triangle:"))
    c = float(input("Enter the length of the third side of the triangle:"))


    triangle_type = classify_triangle(a, b, c) + " Triangle"
    print(triangle_type)