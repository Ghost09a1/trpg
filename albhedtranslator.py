#  Al Bhed cipher
english_to_al_bhed = {
    'a': 'y', 'b': 'p', 'c': 'l', 'd': 't', 'e': 'a', 'f': 'v', 'g': 'k', 'h': 'r',
    'i': 'e', 'j': 'z', 'k': 'g', 'l': 'm', 'm': 's', 'n': 'h', 'o': 'u', 'p': 'b',
    'q': 'x', 'r': 'n', 's': 'c', 't': 'd', 'u': 'i', 'v': 'j', 'w': 'f', 'x': 'q',
    'y': 'o', 'z': 'w', ' ': ' ',  
}

# text to Al Bhed
def text_to_al_bhed(text):
    translated_text = ""
    for char in text.lower():
        if char in english_to_al_bhed:
            translated_text += english_to_al_bhed[char]
        else:
            translated_text += char  # Keep non-alphabet 
    return translated_text

# Continuously ask for text and translate it to Al Bhed
while True:
    user_input = input("Enter text (or 'quit' to exit): ")
    
    if user_input.lower() == 'quit':
        break  # Exit loop 'quit'
    
    translated_text = text_to_al_bhed(user_input)
    print("Translated to Al Bhed:", translated_text)
