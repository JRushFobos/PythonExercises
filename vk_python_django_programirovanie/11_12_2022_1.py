def hello_in_text1(text):
    if 'hi' in text.lower():
        return True
    else:
        return False



def hello_in_text2(text):
    return 'hi' in text.lower()

print(hello_in_text1('hi'))
print(hello_in_text1('h'))
print(hello_in_text2('hi'))
print(hello_in_text1('h'))