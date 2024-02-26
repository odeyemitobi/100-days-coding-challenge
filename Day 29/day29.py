def smash(words):
    if not words:
        return ""
    sentence = ""

    for word in words:
        sentence += word + " "

    sentence = sentence.rstrip()
    return sentence


user_input = input("Enter words separated by spaces: ")
word_list = user_input.split()

result = smash(word_list)

print("Merged Sentence:", result)
