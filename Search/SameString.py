# Function to compare two strings using ==
def areStringsSame(s1, s2):
    return s1 == s2


def main():
    s1 = "hello"
    s2 = "hello"

    # Call the areStringsSame function to compare strings
    if areStringsSame(s1, s2):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()