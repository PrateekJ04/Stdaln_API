
def reverse_and_swapcase():
    sentence=input("Enter a valid sentence: ")
    rev_sentense=sentence.split(" ")[::-1]
    #x=rev_sentense

    #swap_case=' '.join(x.swapcase() for x in rev_sentense)
    sent_rev=' '.join(x for x in rev_sentense)
    return sent_rev

output=print(reverse_and_swapcase())

#Need to check
