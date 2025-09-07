# QUESTION 2
course = "Praxis"

if course == "Praxis":
    print("Carrick")
elif course == "CIV":
    print("Bentz")

# QUESTION 3
def greet_instructor(course:str,greeting:str):
    if course == "Praxis":
        return greeting+"Carrick"
    elif course == "CIV":
        return greeting+"Bentz"
