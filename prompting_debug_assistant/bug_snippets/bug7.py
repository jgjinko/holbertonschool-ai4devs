# bug7.py
# Type: Logic Error

"""
Simple program that calculates the area of a rectangle, but uses
width and height interchangeably leading to wrong results when the
values differ.
"""

def calc_area(width, height):
    # BUG: multiplies width by itself instead of width*height
    return width * width


def main():
    w = float(input("Enter width: "))
    h = float(input("Enter height: "))
    area = calc_area(w, h)
    print(f"Area: {area}")

    if w == h:
        print("Hey, it's a square!")
    else:
        print("That's a rectangle.")

    # simple loop to show incremental changes
    for i in range(3):
        print(f"Iteration {i+1}")


if __name__ == "__main__":
    main()
