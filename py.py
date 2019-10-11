# fh = open('txt.txt')
# lst = list()
# for line in fh:
#     lst = lst + line.split()
#     lst.sort()
    
# words2 = list()
# for word in lst:
#     if word not in words2:
#         words2.append(word)
# print(words2)


fh = open('txt.txt')
lst = list()
for line in fh:
    lst = lst + line.split()
    lst.sort()

words2 = list()
for word in lst:
    if word not in words2:
        words2.append(word)
print(words2)
