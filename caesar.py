import string

def replace(key,line,array,index):
    position = array.index(line[index])
    new_position = position+key
    if new_position>=26:
        new_position -= 26 
    line[index]=array[new_position]

def encode(key, line):
    letters = list(string.ascii_lowercase)
    capitals = list(string.ascii_uppercase)
    for i in range(len(line)):
        if line[i].isalnum():
            if line[i].islower():
                replace(key,line,letters,i) 
            else:
                replace(key,line,capitals,i)
    return ''.join(line)

if __name__ == "__main__":
    key = abs(int(input("Enter key: ")))
    line = list(input("Enter line: "))

    result = encode(key,line)
    print(result)

