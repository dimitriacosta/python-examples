def string_encode(word):
    count = {}
    result = ''
    for character in word.lower():
        count.setdefault(character, 0)
        count[character] += 1

    for character in word.lower():
        if count[character] > 1:
            result += ')'
        else:
            result += '('

    print("Evaluating: %s" % word)
    return result

print(string_encode("din"))
print(string_encode("recede"))
print(string_encode("Success"))
