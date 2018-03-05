def substring(p, w):
    return p.count(w)

def substring_ignore_spaces(p, w):
    return p.replace(" ","").count(w)

def main():
    phrase = "How much wood could a woodchuck chuck" +\
             "If a wood chuck could chuck wood"
    print(substring(phrase,"wood"))                     # 4
    print(substring(phrase,"uck"))                      # 4
    print(substring(phrase,"woodchuck"))                # 1
    print(substring_ignore_spaces(phrase, "woodchuck"))  # 2
    print(substring_ignore_spaces(phrase, "woodc"))      # 3
    print(substring_ignore_spaces(phrase, "wordchuck")) # 0
    
main()