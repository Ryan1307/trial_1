#!usr/bin/python3
import os
import re
    
def main():
    #os.chdir('C:\\Users\\saint\\Desktop\\Trial\\')
    file_name = 'pride_and_prejudice_test.txt'
    contents = []
    with open(file_name) as file:
        for lines in file:
            data = lines.split("\n")
            s = re.split('[^\w]+',data[0])
            contents.append(s)
    contents = [item for sublist in contents for item in sublist]
    contents = list(filter(lambda a: a != '', contents))
    print(contents)
if __name__ == "__main__":
    main()
