def get_split(line, N):
    #print(line,N)
    return_list = []
    str = line.split()
    for word in str:
        #print(word)
        return_list.append(word)
    return return_list



return_list = get_split('I am a good boy',1)
print(return_list)
for word in return_list:
    print(word)