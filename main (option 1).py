def function():
    k = int(input("Введите сдвиг (если нужно дешифровать, сдвиг введите с минусом) \n"))
    t= input("Введите текст \n")
    
    result = ''
    
    for i in range(len(t)):
        if t[i] in russian_alphabet.upper():
            result += russian_alphabet[(russian_alphabet.upper().index(t[i]) + k) % len(russian_alphabet)].upper()
        
        elif t[i] in russian_alphabet:
            result += russian_alphabet[(russian_alphabet.index(t[i]) + k) % len(russian_alphabet)]
            
            
        elif t[i] in english_alphabet.upper():
            result += english_alphabet[(english_alphabet.upper().index(t[i]) + k) % len(english_alphabet)].upper()
            
        elif  t[i] in english_alphabet:
            result += english_alphabet[(english_alphabet.index( t[i]) + k) % len(english_alphabet)]
            
        else:
            result += t[i]
            
    return result


english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
russian_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
print(function())





