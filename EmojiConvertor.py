msg = input(">")
emoji = {
    ":)": "😊",
    ":(": "☹️",
    ":D": "😁",
    ";)": "😉",
    ":P": "😝",
    ":o": "😮",
    ":|": "😑",
    ":/": "😕",
    ":'(": "😥",
    ":*": "😘"
}
output = ""
words = msg.split(" ")
for word in words:
    output += emoji.get(word, word) + " "
    # We used get method bcz words are not in dictionary, so we return words as it is
print(output)
