code_str = 'print("Hello, World!")'
exec(code_str)

def make_sum_fn(n):
    code_str = 'def sum'+str(n)+'(*args):\n sum = 0;\n for i in args:\n  sum += i;\n return sum'
    #print(code_str)
    exec(code_str,globals())
    
make_sum_fn(3)
print(sum3(1,2,3))
