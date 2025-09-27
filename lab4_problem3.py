def generate_hats(num_students):
    import random
    hats = []
    for i in range(num_students):
        if random.random() < 0.5:
            hats.append('W')
        else:
            hats.append('B')
    return hats

def count_white_hats(hats,s_i):
    c = 0
    for i in range(len(hats)):
        if hats[i] == 'W' and i != s_i:
            c += 1
    return c   
def make_guesses(hats):
    guesses = []
    for i in range(len(hats)):          
        white = count_white_hats(hats,i)
  
        if white % 2 == 1:
            guesses.append('B')
        else:
            guesses.append('W')
    return guesses


def are_all_guesses_correct(hats, guesses):
    for i in range(len(hats)):
        if hats[i] != guesses[i]:
            return False
    return True
    
if __name__ == "__main__":
    num_students = 12
    hats = generate_hats(num_students)
    print("Hats: ", hats)
    guesses = make_guesses(hats)
    print("Guesses:", guesses)
    if are_all_guesses_correct(hats, guesses):
        print("All guesses correct!")
    else:
        print("Not all guesses correct.")
