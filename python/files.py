# working with files

def main():
    # printer()
    # copier()
    copy_binary()


def printer():
    # open takes an optional second argument
    # open('this.txt', 'r') #read only, default
    # open('this.txt', 'r+') #read and write
    # open('this.txt', 'w') #write, creates a file if not there, erases everything
    # open('this.txt', 'w+') #write and read
    # open('this.txt', 'a') #append a line at the end of the file
    # open('this.txt', 'rt') #read text, 'wt' write text
    # open('this.txt', 'wb') #write binary, 'rb' read binary
    fl = open('this.txt', 'r')
    for line in fl:
        print(line.rstrip())


def copier():
    # read and write text
    file_in = open('this.txt', 'rt')
    file_out = open('this-copy.txt', 'wt')
    for line in file_in:
        print(line.rstrip(), file=file_out)  # file_out.writelines(line)
        print("*", end="", flush=True)
    file_out.close()
    print("\nDone.")


def copy_binary():
    file_in = open('metag.png', 'rb')
    file_out = open('metag-copy.jpg', 'wb')

    while True:
        buf = file_in.read(10240)
        if buf:
            file_out.write(buf)
            print("#", end="", flush=True)
        else:
            break
    file_out.close()
    print("\nDone.")


if __name__ == '__main__':
    main()
