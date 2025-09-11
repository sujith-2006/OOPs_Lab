"""
    4. WAP to reverse words in a sentence.
"""
sentence = "I Love Python"
words = sentence.split()
reversed_words = words[::-1]
reversed_sentence = "".join(reversed_words)
print(reversed_sentence)
