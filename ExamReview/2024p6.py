def is_palindrome(game_str):
    for i in range(len(game_str)//2):
        if game_str[i] != game_str[-i-1]:
            return False
    return True

print(is_palindrome("racecar"))

def can_win(game_str):
