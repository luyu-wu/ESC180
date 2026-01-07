'''Semantic Similarity'''
'''NOTES FOR SHIRLEEN
- Check for Runtime Complexity
- Debug
-actually input the files and test the code
- clean up the code
'''

'''Imports'''
import math
import random

'''Functions'''
def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as
    described in the handout for Project 3. (GIVEN; By Prof. Guerzhoy)

    The norm is basically the magnitude
    '''
    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    '''Calculate cosine similarity, between the two vector using the provided formula(the dot product)'''

    #for each of the items in the dictionary, if they are the same, you add them together, or else you ignore them
    #we only need to check one of the list, because if a key in v2 is not in v1, we don need to concern ourselves with it

    #then go through each of the common words for the dotproduct
    numerator = 0
    for word in vec1.keys():
        if word in vec2.keys():
            numerator += vec1[word] * vec2[word]

    #the we need to find the magnitude of both of the vectors
    denom = norm(vec1) * norm(vec2)

    return numerator/denom


def build_semantic_descriptors(sentences):
    '''Returns the semantic descriptor, which is basically the number of times a word appears in the same sentence with a different word, as a dictionary'''

    #I think there is somethinbg wrong with this code, but ngl idk how I can debug this...
    semantic_d = {}
    for sentence in sentences: #run-time complexity should be ok here...Since this is for sentence in sentence, the rest of the code would run according to the number of sentences...Which should still be 0(n)
        unique = []
        seen = set()
        for w in sentence:
            if w not in seen:
                seen.add(w)
                unique.append(w)
        sentence = unique 
        for w1 in sentence:
            for w2 in sentence:
                if w1 != w2: #make sure that 'I' doesnt get put in the dictionary that says 'I' as well...would that have matter??
                    if w1 not in semantic_d.keys():
                        semantic_d[w1] = {w2: 1}
                        #add the word if it is not in the semantic yet
                    else:
                        if w2 not in semantic_d[w1].keys():
                            semantic_d[w1][w2] = 1
                            #if the second word appears with the first word for the first time add the word into the dictionary
                        else:
                            semantic_d[w1][w2] += 1 #or else just add


    return semantic_d

def build_semantic_descriptors_from_files(filenames):
    '''Provided a list of filenames. Open each of them and create and return a single dictionary that houses the semantic descirptor for all the words within the file'''

    #First turn the sentences in the file to a list of list for each sentences
    words = []
    for i in range(len(filenames)):
        file = open(filenames[i], "r", encoding="latin1").read().replace('!', '.').replace('?', '.') #and this also replaces all the other end-sentence punctuations into a fullstop so then I can just use the fullstop to split the text later
        #would it be ok to use a for loop here?
        for punctuations in [',', ':', ';', '-', '--']:
            file = file.replace(punctuations, '')
            #now it should just be lower case with the three major sentence-ending puntuations.
        file = file.lower().split('.') #now it is splitted into sentences
        #then we split the words within each sentences
        for i in range(len(file)):
            file[i] = file[i].split()

        words.extend(file) #extend to the bigger database
    return build_semantic_descriptors(words)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    '''Pick the most similar word base on the cosine similarity'''
    #initiate the maximum set ups
    cur_max, cur_max_word = -2, ""

    if word not in semantic_descriptors.keys():
        return random.choice(choices) #if the word is not in the semantic... then it just pick a random guess

    #find the word vector for the given word within the semantic
    #only if the word is in the semantic...
    word_vector = semantic_descriptors[word]

    #try out each of the choices
    for choice in choices: #this should go in order of index, so IDK why it is not doing that
        #if choice not in semantic_descriptors[word]:
        #    similarity = -1
        #else:
        similarity = similarity_fn(word_vector, semantic_descriptors[choice])

        #then compare
        if similarity > cur_max: #only replace if it is larger than
            cur_max = similarity
            cur_max_word = choice

    return cur_max_word #return the maximum


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    '''We would first have to divide the file 'filename' into lines...Right?? Because they just give you the lines'''
    #read file
    with open(filename, 'r') as test_file:
        test_file = test_file.read()

    #split into each of the test questions
    test_file = test_file.split('\n')
    #initiate score setup
    total = len(test_file)
    score = 0

    #run the test
    for i in range(len(test_file)):
        test_file[i] = test_file[i].split()

    for test in test_file:
        if test != []:
            guess = most_similar_word(test[0], test[2:], semantic_descriptors, similarity_fn)

            if guess == test[1]:
                score += 1

    return (score / total) * 100 #calculate the percentage


if __name__ == '__main__':
    filenames = ['wp.txt', 'sw.txt']
    semantic_descriptors = build_semantic_descriptors_from_files(filenames)
    print(run_similarity_test('test.txt', semantic_descriptors, cosine_similarity))
    #on the very very bright side there are no more errors, something is just wrong with the construction of my code which is something else that is harder to fix...

