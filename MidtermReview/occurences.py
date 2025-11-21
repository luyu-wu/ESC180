def count_occurrences(list,n):
    c = 0
    for i in list:
        if i == n:
            c+=1
    return c

print(count_occurrences(["candy", "costumes", "midterms", "candy"], "candy"))
