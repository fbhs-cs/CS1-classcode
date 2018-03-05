def substring(p, w):
    return p.lower().count(w.lower())

def substring_ignore_spaces(p, w):
    return substring(p.replace(" ",""),w)
    
    
    

def main():
    phrase = "How much WOOD could a woodchuck chuck" +\
             "If a wood chuck could chuck wood"
    print(substring(phrase,"wood"))                     # 4
    print(substring(phrase,"uck"))                      # 4
    print(substring(phrase,"woodchuck"))                # 1
    print(substring_ignore_spaces(phrase, "woodchuck"))  # 2
    print(substring_ignore_spaces(phrase, "woodc"))      # 3
    print(substring_ignore_spaces(phrase, "wordchuck")) # 0
    
main()