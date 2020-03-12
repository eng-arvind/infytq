string1 = input()
sub_string1 = input()


def check(string, sub_string):
    if string.find(sub_string) == -1:
        print("does not match")
    else:
        print("founded")


check(string1, sub_string1)
