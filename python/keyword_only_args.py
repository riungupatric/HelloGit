# keyword-only arguments to help ensure code clarity
def confidential_info(name, age, *, reveal=False):
    if reveal:
        return f"My name is {name} and I am {age} years old."
    else:
        return


def main():
    result = confidential_info('Patrick Riungu', 32, reveal=True)
    print(result)


if __name__ == '__main__':
    main()
