def generate(digits=8):
    '''This function accepts the size and returns a strong password'''
    import random
    def num():
        a = chr(random.randrange(48,57))
        return a
    def low():
        b = chr(random.randrange(97,122))
        return b
    def symb1():
        c = chr(random.randrange(58,64))
        return c
    def upr():
        d = chr(random.randrange(65,90))
        return d
    def symb2():
        e = chr(random.randrange(33,47))
        return e
    
    def list_to_string(s):
        st = ""
        random.shuffle(s)
        for x in s:
            st+=x
        return st
    
    collect = []
    
    for i in range(digits-6):
        collect.append(num())
        collect.append(low())
        collect.append(symb1())
        collect.append(upr())
        collect.append(symb2())
        
    return list_to_string(collect[:digits])