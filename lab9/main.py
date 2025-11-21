## PROBLEM 1
import urllib
import requests
custom_headers = {
    "User-Agent": "MyPythonApp/1.0",
    "Authorization": "Bearer your_auth_token",
    "Accept": "application/json"
}
def dict_to_str(d):
    ret = ""
    for key in d:
        ret+=str(key) + ", "+str(d[key])+"\n"
    return ret


def dict_to_str_sorted(d):
    arr = list(d.keys())
    arr.sort()        
    ret = ""
    for key in arr:
        ret+=str(key) + ", "+str(d[key])+"\n"
    return ret

'''
f = open("data2.txt")
text = f.read()

lines = text.lower().split("\n")

for (i,v) in zip(range(len(lines)),lines):
    if v.lower().find('lol') != -1:
        print("Line",i,": "+v)
'''
# Load sick man
words = open("text.txt", encoding="latin-1").read().lower().split()

def word_counts(words):
    d = {}
    for i in words:
        d[i] = 0
    for i in words:
        d[i] = d[i] + 1
    return d
print("\n\nWord Counts\n")
print(word_counts(words))

def keyf(n):
    return n[1]
def sort_frequency(freq):
    return sorted(freq.items(),key=keyf,reverse=True) # sort by second index # items returns tuples of each kv

print("\n\nFrequency Sorted\n")

print(sort_frequency(word_counts(words)))

print("\n\nFrequency Sorted - Pride and Prejudice\n")
pride = open("prejudice.txt", encoding="latin-1").read().lower().split()
print(sort_frequency(word_counts(pride))[:10])

def top10(L):
    L.sort()
    return L[:10]

print("\n\n Frequency Sorted Top 10\n")
print(sort_frequency(word_counts(words))[:10])

def searchResults(term):
    print("Scraping https://ca.search.yahoo.com/search;_ylt=Av3YHOEya_QRKgRTD8kMWgst17V_?p="+urllib.parse.quote(term)+"&amp;toggle=1&amp;cop=mss&amp;ei=UTF-8&amp;fr=yfp-t-715&amp;fp=1")

    page = requests.get("https://ca.search.yahoo.com/search;_ylt=Av3YHOEya_QRKgRTD8kMWgst17V_?p="+urllib.parse.quote(term)+"&amp;toggle=1&amp;cop=mss&amp;ei=UTF-8&amp;fr=yfp-t-715&amp;fp=1", headers=custom_headers).text
    #f.close()
    ind = page.find("000 search results")+3
    i = 1
    while page[ind-i] != " ":
        i+=1
    return int(page[ind-i:ind].replace(",","")) # return int of search results

def choose_variant(L):
    max_n, string = 0,""
    for i in L:
        num = searchResults(i)
        if num > max_n:
            string = i
            max_n = num
    return string

print(choose_variant(["top ranked school uoft", "top ranked school waterloo"]))
#print(searchResults("Hello world"))


# Problem 4
f = open("ccc.txt")
text = f.read()

lines = text.split("\n")
schools = []
for line in lines:
    prov = line.find(", ")
    if  prov > 0: # check if student line
        # Names are all caps
        words = line.split()
        word_i = 0
        while words[word_i][1:] != words[word_i][1:].lower():
            word_i += 1
        s_i = line.find(words[word_i-1])+len(words[word_i-1])+1 # start index
        e_i = prov
        schools.append(line[s_i:e_i])

print(sort_frequency(word_counts(schools))[:10])
