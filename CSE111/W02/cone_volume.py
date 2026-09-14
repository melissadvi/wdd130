import math
def main():
    if_radius = 2.8
    if_height = 3.2
    if_volume = cone_volume(if_radius,if_height)
    print("This programs computes the volume of a right circular cone.")
    print("For example, if the radius of a")
    print(f"cone is {if_radius} and the height is {if_height}")
    print(f"then the volume is {if_volume:.1f}")
    print()

    radius = float(input("Please enter the radius of the cone: "))
    height = float(input("Please enter the height of the cone: "))
    volume = cone_volume(radius, height)
    print(f"Radius: {radius}")
    print(f"Height: {height}")
    print(f"Volume: {volume:.1f}")

def cone_volume(radius, height):
    volume = math.pi * radius ** 2 * height / 3
    return volume
main()