def adjc(sentence):
    ch = []
    temp = None
    for i in sentence:
        if(temp != i):
            ch.append(i)
            temp = i
    return ''.join(ch)

sentence = input("Enter the string - ")
print(adjc(sentence))
