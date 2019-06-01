import os
import re
    
def main():
    os.chdir('C:\\Users\\saint\\Desktop\\Trial\\')
    file_name = 'pride_and_prejudice_test.txt'

    contents = []
    content_1 = []
    t = []
    t2 = []
    with open(file_name) as file:
        for lines in file:
            data = lines.split("\n")
            contents.append(data)
    for i in range(len(contents)):
        content_1.append(contents[i][0])
    for t in content_1:
        s = re.split('[^\w]+',t)
        t2.append(s)
    t3 = tuple(t2)
    conts = set(t3)
    print (t2)
    count_key = {}
    length_unique = (len(conts))
    dict1={}
    for i in range(length_unique):
        element = conts[i]
        if element not in list(dict1.keys()):
            count = 1
            dict1[element] = count
        else:
            dict1[element] = count + 1
    # print(dict1)    
    

if __name__ == "__main__":
    main()
