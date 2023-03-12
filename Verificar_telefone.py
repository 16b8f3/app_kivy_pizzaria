import re 

regex = '^\(?[1-9]{2}\)? ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$'

def check(telefone):  
    if (re.findall(regex, telefone)): 
        return 0
    else:  
        return 1