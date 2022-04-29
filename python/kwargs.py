# keyword arguments (kwargs)
def main():
    addr = dict(Town="Nyeri", City="Nairobi", Country="Kenya", Zipcode=10001)
    #address(Town="Nyeri", City="Nairobi", Country="Kenya", Zipcode=10001)
    address(**addr)


def address(**kwargs):
    if len(kwargs):
        for keyword in kwargs:
            print(f"{keyword} : {kwargs[keyword]}")
    else:
        print("Address is empty")


if __name__ == '__main__':
    main()
