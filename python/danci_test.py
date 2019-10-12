import requests

url = 'https://www.shanbay.com/api/v1/vocabtest/category/'
res = requests.get(url)
js_link = res.json()
number = int(input('''请输入对应词库的标号：1.GMAT,2.考研,3.高考,4.四级,
5.六级,6.英专,7.托福,8.GRE,9.雅思,10.任意:'''))
ciku = js_link['data'][number-1][0]
url_1 = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+ciku
res_ciku = requests.get(url_1)
js_ciku = res_ciku.json()
lists = js_ciku['data']
known_list = []
unknown_list = []
knownkey_list = []
n = 0
for words in lists:
    word = words['content']
    print(word)
    judge = input('认识请输入1，不认识请按任意键跳过')
    if judge == '1':
        known_list.append(word)
        knownkey_list.append(n)
    else:
        unknown_list.append(word)
    n += 1
print ('现在我们来检测一下，你有没有真正掌握它们：')
wrong_words = []
right_num = 0
for y in knownkey_list:
    print('\n\n'+'A:'+lists[int(y)]['definition_choices'][0]['definition'])
    #我们改用A、B、C、D，不再用rank值，下同
    print('B:'+lists[int(y)]['definition_choices'][1]['definition'])
    print('C:'+lists[int(y)]['definition_choices'][2]['definition'])
    print('D:'+lists[int(y)]['definition_choices'][3]['definition'])
    xuanze = input('请选择单词\"'+lists[int(y)]['content']+'\"的正确翻译(填写字母即可):')
    dic = {'A':lists[int(y)]['definition_choices'][0]['rank'],'B':lists[int(y)]['definition_choices'][1]['rank'],'C':lists[int(y)]['definition_choices'][2]['rank'],'D':lists[int(y)]['definition_choices'][3]['rank']} 
    #我们创建一个字典，搭建起A、B、C、D和四个rank值的映射关系。
    if dic[xuanze] == lists[int(y)]['rank']:
    #此时dic[xuanze]的内容，其实就是rank值，此时的代码含义已经和之前的版本相同了。
        right_num += 1
    else:
        wrong_words.append(lists[int(y)]['content'])
print(wrong_words)