def encrypt(message,a,b,c,d):
    '''this func accepts a message with 2x2 key and returns the encrypted CyperText'''
    
    dic = {}
    list = []
    answer = []
    nums = 0
    for i in range(ord('A'), ord('Z') + 1):
        dic[chr(i)] = nums+len(dic)
    
    message = (message.replace(" ","")).upper()
    length = len(message)
    
    if len(message)%2!=0:
        message = message + 'A'
    else:
        message = message
    
    for i in range(len(message)):
        list.append(dic[message[i]])

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
    
    if length%2!=0:
        answer.pop()
    
    for ans in answer:
        print(ans)
#Uzaif_Ahmed