#!/bin/python3
'''
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,GOOGLE

 would have it's logo with the letters G,O,E
 '''
if __name__ == '__main__':
    word=sorted([ _ for _ in input()])
    word_counter={}
    for _ in word:
        word_counter[_]=word.count(_)
    top_letter = dict(sorted(word_counter.items(), key=lambda x: x[1],reverse=True))
    for each in range(3):
        print ( list(top_letter.keys())[each], list(top_letter.values())[each])
