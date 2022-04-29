# solving complex problem through divide and concur

def remove_underscore(text):
    if not text:
        return text
    if '_' in text:
        text1 = text.replace('_', ' ')
        return text1
    return text


def remove_hyphen(text):
    if not text:
        return text
    if '-' in text:
        text1 = text.replace('-', ' ')
        return text1
    return text


def pascalCase(text):
    # remove hyphen
    t1 = remove_hyphen(text)

    # remove underscore
    t2 = remove_underscore(t1)

    # cammelCase
    words = [x for x in t2.split(' ')]
    result = words[0]
    for i in range(1, len(words)):
        result += words[i].title()
    print(result)


s0 = "The_Cat-was_Savage"
s1 = "the-Cat_is_Hungry"
s2 = ""
pascalCase(s0)
pascalCase(s1)
pascalCase(s2)
# print(remove_hyphen(remove_underscore(s)))
