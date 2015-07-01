
def escaping_input(text):
    return text.replace('"', '\"')

a = '"'

b = escaping_input(a)

print(b)
