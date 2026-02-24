def word_frequency(sentence):
    words = sentence.split()
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


print(word_frequency("python django python api django"))