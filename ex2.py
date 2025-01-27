#Write a Python program to find if a given string starts with a given
#character using Lambda.

start_with = lambda word, letter: word.startswith(letter)
word = "davit manukyan"
letter = "d"
result = start_with(word,letter)
print(result)


