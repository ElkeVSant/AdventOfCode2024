#!/usr/bin/env python

def main():
    list1 = []
    list2 = []
    with open("day1/input.txt") as lists:
        for loc in lists:
            loc1, loc2 = loc.split()
            list1.append(int(loc1))
            list2.append(int(loc2))
    print(distance(list1, list2))
    print(compare(list1, list2))

def distance(list1, list2):
    difs = [abs(loc1-loc2) for loc1, loc2 in zip(sorted(list1), sorted(list2))]
    return sum(difs)

def compare(list1, list2):
    similarity = [loc*list2.count(loc) for loc in list1]
    return sum(similarity)
    
if __name__=="__main__":
    main()
