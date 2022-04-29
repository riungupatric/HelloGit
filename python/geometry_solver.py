import math


class Geometry(object):
    @staticmethod
    def area_of_circle(radius):
        ans = math.pi * radius**2
        return (ans)

    @staticmethod
    def area_of_rect(length, width):
        return length * width

    @staticmethod
    def volume_of_rect(length, width, depth):
        return (length * width * depth)

    @staticmethod
    def volume_of_sphere(radius):
        """This method calculates the volume of a sphere given its radius

        Args:
            radius (number): an integer or a float 

        Returns:
            number: an integer or a float
        """
        vol = (4/3)*(math.pi * radius**3)
        return (vol)
    # todo: consider adding more volume methods latter

    # main function
    # *entry point to the program
    # prints a simple menu -  you make a choice and supply the values


def main():
    running = True
    while running:
        print("Welcome to the Geometry Solver GAME!!!")
        print("Select the solution you want:")
        print("1) Area of a circle.")
        print("2) Area of a rectangle.")
        print("3) Volume of a rectangle.")
        print("4) Volume of a sphere.")
        print("x) Exit")
        print()

        # processing user input
        choice = input("Enter your choice : ")
        if choice == "1":
            radius = input("Enter the radius : ")
            ans = Geometry.area_of_circle(float(radius))
            print(f"Area of your circle is: {ans}")
            print()
        elif choice == "2":
            leng = float(input("Enter length : "))
            wid = float(input("Enter width : "))
            ans = Geometry.area_of_rect(leng, wid)
            print(f"Area of your rectangle is : {ans}")
            print()
        elif choice == "3":
            l = float(input("Enter length : "))
            w = float(input("Enter Width : "))
            d = float(input("Enter Depth : "))
            ans = Geometry.volume_of_rect(l, w, d)
            print(f"Volume of your sphere is {ans}")
            print()
        elif choice == "4":
            r = float(input("Enter radius : "))
            ans = Geometry.volume_of_sphere(r)
            print(f"Volume of your sphere is {ans}")
            print()
        elif choice == "x":
            running = False


if __name__ == "__main__":
    main()
