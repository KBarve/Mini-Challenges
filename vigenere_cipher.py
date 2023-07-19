import string
def validate(key,line):
    check = True
    temp = key
    temp2 = line
    "".join(temp)
    "".join(temp2)
    if temp.isalnum() and temp2.isalnum():
        check = False
        
    return check
    
def to_keystream(key,length):
    keystream = []
    repetition = (max(len(key),length))//(min(len(key),length))
    extra = (max(len(key),length))%(min(len(key),length))
    for i in range(repetition):
        for j in range(len(key)):
            keystream.append(key[j])
    for i in range(extra):
        keystream.append(key[i])
    return keystream

def shift_list(keystream):
    keystream.lower()
    shift = []
    for i in range(len(keystream)):
        shift.append(letters.index(keystream[i]))
    return shift
    
def replace(key_list,line,reference):
    for i in range(len(line)):
        line
        position = reference.index(line[i])
        new_position = position+key_list[i]
        if new_position>=len(reference):
            new_position -= len(reference)
        line[i]=reference[new_position]

def encode(key, line):
    letters = list(string.ascii_lowercase)
    capitals = list(string.ascii_uppercase)
    keystream = to_keystream(key,len(line))
    keys_list = shift_list(keystream)
    
    replace(keys_list,line,letters) 
    return ''.join(line)

if __name__ == "__main__":
    key = list(input("Enter key: "))
    line = list(input("Enter line: "))
    if validate:
        print("Invalid input")
    else:
        result = encode(key,line)
        print(result)
