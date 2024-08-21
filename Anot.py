symbol_direct = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
import random
def convert(numb): # Konwertacja liczb
    
    if numb in symbol_direct:
        
        return symbol_direct.index(numb)
    return symbol_direct[int(numb)]


text = list(input("Hello! This program encrypts or decrypts texts in swap style. \n\nType your text: "))
lng_txt = len(text)
key_source = list(input("\nEnter key: "))
if "R" in key_source: # Funkcja losowania kluczu 
    
    key_source.remove("R")
    random_time = int("".join(key_source))
    key_source.clear()
    for time in range(random_time): 
        
        x = convert(random.randint(0, 35))
        key_source.append(x)


key_work = [convert(x) for x in key_source] 
key_source = "".join(map(str, key_source))
if input("\nYou want to encrypt or decrypt? (e/d)") == "e":
    
    text = ['_' if x == ' ' else x for x in text]
else:
    
    text = [' ' if x == '_' else x for x in text]
    key_work.reverse()

    
for key in key_work:
    
    key = int(key) - 1
    if key < 1:
        
        continue

    for x in range(0, lng_txt, key + 1):
        
        y = x + key

        if y < lng_txt: 
            
            text[x], text[y] = text[y], text[x]


print("\nComplete! Result: ", "".join(text), "\nCryptkey: ", key_source)
input()