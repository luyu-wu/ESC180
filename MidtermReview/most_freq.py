def most_frequent(faves):
    dict = {}
    for i in faves:
        dict[i]=0
    for i in faves:
        dict[i] += 1

    max,ind = 0, "N/A"
    for i in dict:
        if dict[i] > max:
            max = dict[i]
            ind = i
    return ind

print(most_frequent(["candy", "costumes", "midterms", "candy"]))
