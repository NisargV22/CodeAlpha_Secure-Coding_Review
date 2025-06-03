def read_file():
    filename = input("Enter the filename to read: ")

    # No validation or restriction — allows reading any file on the system
    with open(filename, 'r') as f:
        data = f.read()
        print("File contents:\n", data)

if __name__ == "__main__":
    read_file()
