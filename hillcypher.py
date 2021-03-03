def encrypt(message,a,b,c,d):
    try:
        '''this func accepts a message with 2x2 key and returns the encrypted CyperText'''
    
        dic = {}
        list = []
        answer = []
        nums = 0
        
        # Created dictionary where A = 0 to Z = 25
        for i in range(ord('A'), ord('Z') + 1):
            dic[chr(i)] = nums+len(dic)
        
        # Removing White Space
        message = (message.replace(" ","")).upper() 
        length = len(message)
        
        
        # Adding a Dummy Alphabet if length is Odd
        if len(message)%2!=0:
            message = message + 'A'
        else:
            message = message
        
        
        # Adding Numbers of alphabets to a list
        for i in range(len(message)):
            list.append(dic[message[i]])

        
        # Matrics Multiplication
        R1V1 = []
        R1V2 = []
        R2V1 = []
        R2V2 = []
        for x in range(len(list)):
            if x%2==0:
                R1V1.append(a*list[x])
                R2V1.append(c*list[x])
            elif x%2!=0:
                R1V2.append(b*list[x])
                R2V2.append(d*list[x])
    
    
        for y in range(len(R1V1)):
            first = R1V1[y]+R1V2[y]
            if first > 26:
                for key,value in dic.items():
                    if value == first%26:
                        answer.append(key)
            else:
                for key,value in dic.items():
                    if value == first:
                        answer.append(key)
    
            second = R2V1[y]+R2V2[y]
            if second > 26:
                for key,value in dic.items():
                    if value == second%26:
                        answer.append(key)
            else:
                for key,value in dic.items():
                    if value == second:
                        answer.append(key)
        
        # Removing Dummy Alphabet if the length was Odd
        if length%2!=0:
            answer.pop()
    
        for ans in answer:
            print(ans)
            
    except Exception as e:
        print('Error Occured, insert Message first then Key')
        
        
def decrypt(message,a,b,c,d):
    try:
        '''this func accepts CypherText with 2x2 key and decrypts the Message'''
        dic = {}
        list = []
        nums = 0
        answer = []

        # Created dictionary where A = 0 to Z = 25
        for i in range(ord('A'), ord('Z') + 1):
            dic[chr(i)] = nums+len(dic)

        # Removing White Space
        message = (message.replace(" ","")).upper()
        length = len(message)

        # Adding a Dummy Alphabet if length is Odd
        if len(message)%2!=0:
            message = message + 'A'
        else:
            message = message

        # Adding Numbers of alphabets to a list
        for i in range(len(message)):
            list.append(dic[message[i]])

        # determenent of Key
        det = (a*d)-(b*c)


        def modular_inverse(det):
            for x in range(1,26):
                if ((det%26) * (x%26)) % 26 == 1:
                    return x

        # Taking moduler inverse of the determenent
        det = modular_inverse(det)

        # Taking inverse of Key and Multiplying determenent with Key
        a,b,c,d = (d*det), (-b*det), (-c*det), (a*det)

        # Taking modulus of the inversed Key
        a,b,c,d = a%26, b%26, c%26, d%26


        # Matrics Multiplication
        R1V1 = []
        R1V2 = []
        R2V1 = []
        R2V2 = []
        for x in range(len(list)):
            if x%2==0:
                R1V1.append(a*list[x])
                R2V1.append(c*list[x])
            elif x%2!=0:
                R1V2.append(b*list[x])
                R2V2.append(d*list[x])
    
        # Matrics Addition    
        for y in range(len(R1V1)):
            first = R1V1[y]+R1V2[y]
            if first > 26:
                for key,value in dic.items():
                    if value == first%26:
                        answer.append(key)
            else:
                for key,value in dic.items():
                    if value == first:
                        answer.append(key)
    
            second = R2V1[y]+R2V2[y]
            if second > 26:
                for key,value in dic.items():
                    if value == second%26:
                        answer.append(key)
            else:
                for key,value in dic.items():
                    if value == second:
                        answer.append(key)

        # Removing Dummy Alphabet if the length was Odd
        if length%2!=0:
            answer.pop()
    
        for ans in answer:
            print(ans)
    except Exception as e:
        print('Error Occured, insert CypherText first then Key')

#Uzaif_Ahmed
