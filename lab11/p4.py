from p3 import get_response
def chat():
    hist = ""
    while True:
        ques = input("Q: ")
        hist += "\nQ: "+ques
        ans = get_response(hist)
        print(ans)
        hist += "\nA: "+ans
    
if __name__=="__main__":
    chat()
