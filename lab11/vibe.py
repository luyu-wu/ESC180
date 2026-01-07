from p3 import get_response
# P5
prompt = "generate a Python function (named fun(n)) that outputs the factorial of the input n. Generate only code (do not include ```python header)."

code = get_response(prompt)

# P6

def fact(n):
    if n == 1:
        return n
    return n*fact(n-1)

test_cases = [
    {"input": 3, "expected_output": fact(3)},
    {"input": 4, "expected_output": fact(4)},
    {"input": 5, "expected_output": fact(5)},
    {"input": 6, "expected_output": fact(6)},
    {"input": 7, "expected_output": fact(7)},
]


def check_result(generated_code,test_cases):
    exec(generated_code, globals())
    passing, failing = 0,0
    for i in test_cases:
        if fun(i['input'] == i['expected_output']):
            passing += 1
        else:
            failing -= 1
    return passing, failing

print(code)
if input("Run? (input NO to not): ") == "NO":
    exit()
print("\nPassing   |   Failing")
print(check_result(code,test_cases))
