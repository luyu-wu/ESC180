import math

def norm(vec):    
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] ** 2
    
    return math.sqrt(sum_of_squares)

def cosine_similarity(vec1, vec2):
    sum = 0
    for i in vec1:
        if i in vec2:
           sum += vec1[i]*vec2[i] 

    return sum/(norm(vec1)*norm(vec2))


def build_semantic_descriptors(sentences):
    d = {}
    for sentence in sentences:
        # unique words in the sentence
        unique = []
        seen = set()
        for w in sentence:
            if w not in seen:
                seen.add(w)
                unique.append(w)

        for i in range(len(unique)):
            w1 = unique[i]
            if w1 not in d:
                d[w1] = {}

            for j in range(len(unique)):
                if i == j:
                    continue
                w2 = unique[j]

                if w2 not in d[w1]:
                    d[w1][w2] = 1
                else:
                    d[w1][w2] += 1
    
    print("Finish building Descriptors")
    return d


def build_semantic_descriptors_from_files(filenames):
    sentences = []
    for i in filenames:
        file = open(i, "r", encoding="latin1")
        string = file.read().lower()
        file.close()

        string = string.replace("\n"," ")
        string = string.replace("?",".").replace("!",".")
        string = string.replace(",","").replace("-","").replace("--"," ")
        string = string.replace(":","").replace(";","")
        for sentence in string.split('.'):
            arr = []
            for word in sentence.split():
                arr.append(word)
            sentences.append(arr)
    print("Finished building sentences...")
    return build_semantic_descriptors(sentences)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    best = -2 # similarity
    bestWord = choices[0]
    for testWord in choices:
        if testWord in semantic_descriptors and word in semantic_descriptors:
            res = similarity_fn(semantic_descriptors[word],semantic_descriptors[testWord])
            if res > best:
                best = res
                bestWord = testWord
    return bestWord


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    tests = open(filename, "r", encoding="latin1").read().split("\n")
    correct, incorrect = 0,0
    for i in tests:
        words = i.split()
        if len(words) != 4:
            continue
        res = most_similar_word(words[0],words[1:],semantic_descriptors,cosine_similarity)
        if res == words[1]:
            correct += 1
            
    return correct/(len(tests))

if __name__ == "__main__":
    print("Building Decorators")
    sem_descriptors = build_semantic_descriptors_from_files(["wp.txt", "sw.txt"])
    # print(sem_descriptors["stroll"])
    print("Finish Building")
    res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
    print(res, "of the guesses were correct")

    # print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))
    #print(build_semantic_descriptors([["i", "am", "a", "sick", "man"],["i", "am", "a", "spiteful", "man"],["i", "am", "an", "unattractive", "man"],["i", "believe", "my", "liver", "is", "diseased"],["however", "i", "know", "nothing", "at", "all", "about", "my","disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]])["man"])
    #print(build_semantic_descriptors_from_files(["test2.txt","test2.txt"]))
