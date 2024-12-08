# 'The quick brown fox jumps over the lazy dog.'
# input : "The quick brown fox jumps over the lazy dog."
# output : "dog. lazy the over jumps fox brown quick The "

sentense= "The quick brown fox jumps over the lazy dog."
# rev_sen= sentense.split()
# rev_sen=rev_sen[::-1]
# output=" ".join(rev_sen)
#
# print(output)

def rev_sent(sentense):
    temp = sentense.split()
    temp = temp[::-1]
    output = " ".join(temp)
    return output

print(rev_sent(sentense))