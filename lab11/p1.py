def all_combinations(n, L, start_list = None):
    if start_list == None:
        start_list = []
    if n == 0:
        return start_list.copy()
    else:
        res = []
        for num in L:
            start_list.append(num)
            res.append(all_combinations(n-1, L, start_list))
            start_list.pop()
        return res

print(all_combinations(2,[1,2,3]))
    
