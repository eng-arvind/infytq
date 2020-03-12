from string import digits
witnum = "arvind123kumar"
rev_digit = str.maketrans('','',digits)
rev = witnum.translate(rev_digit)
print(rev)