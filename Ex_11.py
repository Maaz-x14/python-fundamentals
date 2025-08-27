def emoji_conv(msg):
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
    return output


message = input(">")
print(emoji_conv(message))