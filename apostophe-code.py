APOSTROPHE = '\''
RIGHT_MARK = '’'

morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
         "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
         "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
         "-.--", "--.."]

# flatten a 2D list
flatten = lambda l: [item for sublist in l for item in sublist]

# :text: a message made up of [a-zA-Z]
def to_morse(message):
    m = [morse[ord(c)-97] for c in message.lower()]
    return flatten(m)


# :message: a message to encode
# :source: a source text with apostrophes
def insert_morse(message, source):
    # a list of dots and dashes
    morse = to_morse(message)
    # a list of the two types of apostrophes
    secret = [APOSTROPHE if m == '.' else RIGHT_MARK for m in morse]
    inserted = []
    for c in source:
        if len(secret) > 0 and (c == APOSTROPHE or c == RIGHT_MARK):
            inserted.append(secret.pop(0))
        else:
            inserted.append(c)
    return ''.join(inserted)

# :source: a source encoded via insert_morse
def retrieve_morse(source):
    morse = []
    for c in source:
        if c == APOSTROPHE:
            morse.append('.')
        elif c == RIGHT_MARK:
            morse.append('-')
    return ''.join(morse)


source_text = 'Hello \'\' World, \'\' no \'\' secrets \' here!'
secret = 'cat'

encoded_message = insert_morse(secret, source_text)
retrieved_message = retrieve_morse(encoded_message)

print(encoded_message) # Hello ’' World, ’' no '’ secrets ’ here!
print(retrieved_message) # -.-..--
