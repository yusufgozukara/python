sentence=input("write a sentence: ")
result={word:sentence.count(word) for word in sentence}
print(result)
