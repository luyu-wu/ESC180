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
    pass

def build_semantic_descriptors_from_files(filenames):
    pass

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    pass


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    pass

print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))
