# dic = {Key1:Value1, Key2:Value2, ...}
dic = {'name':'pey', 'phone':'01011111111', 'birth':'1111'}
print(dic['name'])

#add
dic['grade'] = '99'
#delete
del dic['phone']
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())

print(dic.get('name'))          # == print(dic['name'])
print(dic.get('nokey'))
print(dic.get('nokey', 'default value'))

print('name' in dic)
print('email' in dic)

dic.clear()
print(dic)
