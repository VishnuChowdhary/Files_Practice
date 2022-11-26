def reverse_string(text):
    wordlist = text.split()
    result = wordlist[::-1]
    return result


reversed_text = reverse_string('Vishnu Vardan')
print(reversed_text)
