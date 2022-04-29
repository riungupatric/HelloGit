# handle exceptions safely
import sys
import datetime


def main():
    age = input("Enter your age : ")

    try:
        years = int(age)
        future_age = years/1
    except ValueError:
        print("Error: Please enter a valid age number")
    except ZeroDivisionError:
        print("Error: can't divide by zero")
    except:
        print(f"you have an error: {sys.exc_info()}")
    else:
        print(f"You will be {years + 10} in {datetime.date.today().year + 10}")

    # age can't be negative years or more that 150 years
    try:
        if years <= 0:
            raise TypeError("Age can't be zero or less!")
        elif years > 150:
            raise TypeError("Impossible age, you're prolly dead")
    except TypeError as e:
        print(f"Age error: {e}")


if __name__ == '__main__':
    main()
