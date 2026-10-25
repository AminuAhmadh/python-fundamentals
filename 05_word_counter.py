# program to count the occurrences of each word in a string of sentence(s)

from collections import Counter

print("Word Counter...")
sentence = input("Write a sentence: ")
print()

words_list = [word for word in sentence.split()]
for word, times in Counter(words_list).items():
    print(f"The Word '{word}' appears {times} times")