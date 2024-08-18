def rot13(s):
    result = []
    
    for char in s:
        if 'A' <= char <= 'Z':  
            shifted = ord(char) + 13
            if shifted > ord('Z'): 
                shifted -= 26
            result.append(chr(shifted))
        elif 'a' <= char <= 'z':  
            shifted = ord(char) + 13
            if shifted > ord('z'):  
                shifted -= 26
            result.append(chr(shifted))
        else:  
            result.append(char)
    
    return ''.join(result)


input_string = input()
print(rot13(input_string))
