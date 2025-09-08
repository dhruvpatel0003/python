from math import pow

def classify_triangle(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    elif pow(a, 2) + pow(b, 2) == pow(c, 2) or pow(a, 2) + pow(c, 2) == pow(b, 2) or pow(b, 2) + pow(c, 2) == pow(a, 2):
        return "Right"
    else:
        return "Scalene"

def test_equilateral():
    assert classify_triangle(3, 3, 3) == "Equilateral"

def test_isosceles():
    assert classify_triangle(4, 4, 5) == "Isosceles"
    assert classify_triangle(5, 4, 5) == "Isosceles"
    assert classify_triangle(4, 5, 5) == "Isosceles"

def test_right():
    assert classify_triangle(3, 4, 5) == "Right"
    assert classify_triangle(5, 12, 13) == "Right"

def test_scalene():
    assert classify_triangle(4, 5, 6) == "Scalene"
    assert classify_triangle(2, 3, 4) == "Scalene"


if __name__ == "__main__":
    a = input("Enter the length of the first side of the triangle:")
    b = input("Enter the length of the second side of the triangle:")
    c = input("Enter the length of the third side of the triangle:")

    triangleType = classify_triangle(a, b, c) + " Triangle"
    print(triangleType)