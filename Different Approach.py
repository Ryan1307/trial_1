#!usr/bin/python3
from collections import Counter

def word_count(fname):
    with open(fname) as f:
        return Counter(f.read().split())
    
def main():
    filename = 'pride_and_prejudice_test.txt'
    print("Number of words in the file :",word_count(filename))
    

if __name__ == "__main__":
    main()
