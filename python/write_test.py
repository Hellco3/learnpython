comment = []
for number in range(10):
    comment.append(str(number))
print(comment)
with open ('write_test.txt','w',encoding= 'utf-8') as f1:
    f1.writelines(comment)
with open ('write_test.txt','r',encoding = 'utf-8') as f2:
    file_content = f2.readline()
print(file_content)
