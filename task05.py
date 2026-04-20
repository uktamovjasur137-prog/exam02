words ={}
def  count_words(text: str) -> dict:
    for word in text.split():
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words

x = count_words("salom salom dunyo")
print(x)