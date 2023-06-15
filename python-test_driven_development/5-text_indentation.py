#!/usr/bin/python3
def text_indentation(text):
    if not isinstance (text, str):
        raise TypeError("text must be a string")
    punctuation_marks = ['.', '?', ':']
    lines = []
    result = ''

    for char in text:
        result += char
        if char in punctuation_marks:
            lines.append(result.strip())
            result = ''
    lines.append(result.strip())
    for line in lines:
        print(line)
        print()