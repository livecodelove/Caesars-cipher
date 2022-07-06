def function():
    print('This decoder uses a shift equal to the length of each word')
    words = input('Enter the text you want to decode \n').split()
    
    result = ''
    for i in words:
       k = len(i)
       if not i.isalpha():
          for j in range(len(i)):
              if i[j] in ',.!?:':
                  k -= 1
       for j in range(len(i)):
           if i[j] not in ',.!?:':
                if i[j] in english_alphabet.upper():
                    result += english_alphabet[(english_alphabet.upper().index(i[j]) + k) % len(english_alphabet)].upper() 
                elif  i[j] in english_alphabet:
                    result += english_alphabet[(english_alphabet.index(i[j]) + k) % len(english_alphabet)]    
           else:
               result += i[j]
       result += ' '
    return result


english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(function())
