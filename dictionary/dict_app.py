import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word , data.keys())) > 0:
        yn = input("Did you mean %s? \nEnter Y if yes, else N for No: " % get_close_matches(word , data.keys())[0])

        if yn == 'Y' or yn == 'y':
            return data[get_close_matches(word , data.keys())[0]]
        elif yn == "N" or yn == 'n':
            return "Try Again"
    else:
        return "Word Doesn't Exist, Try Again."

user_input = input("Enter a word: ")

ans = translate(user_input)

if type(ans) == list:

    for i in ans:
        print(i)
else:
    print(ans)

