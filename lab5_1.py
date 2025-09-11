"""
    1. WAP to find the longest Word in a given sentence
"""

sentence = "Write a program"
words = sentence.split()
longest_word = ""
max_length = 0
for word in words:
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word
print(longest_word)