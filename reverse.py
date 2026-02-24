def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ""
    
    for i in range(len(words) - 1, -1, -1):
        reversed_sentence += words[i] + " "
    
    return reversed_sentence.strip()


print(reverse_words("I am learning Django"))