def high(x):
    x=x.split()
    import string
    alphabet = list(string.ascii_lowercase)
    list_numbers = []
    current_word_sum = 0
    for word in x:
        current_word_sum = 0
        for letter in word:
            value=alphabet.index(letter)+1
            current_word_sum += value
        list_numbers.append(current_word_sum)
    index=list_numbers.index(max(list_numbers))
    return x[index]