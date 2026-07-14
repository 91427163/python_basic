#method one (reverse by slicing)
def reverse_slicing(txt):

    return txt[-1::-1]

#method two (reverse by loop)
def reverse_loop(txt):

    rev_txt = ""
    for char in range(len(txt)-1, -1,-1):
        rev_txt += txt[char]
    return rev_txt

#Testing the Function
txt = input("Please Enter Your Text : ")
print(f"Original: {txt}")
print(f"Slicing: {reverse_slicing(txt)}")
print(f"Loop: {reverse_loop(txt)}")
