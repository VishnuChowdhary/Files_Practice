def animal_crackers(text):
    word_list = text.split()
    return word_list[0][0] == word_list[1][0]


result = animal_crackers('An Ant')
print(result)
