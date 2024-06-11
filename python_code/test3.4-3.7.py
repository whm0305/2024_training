#练习3.4-3.7 列表名单
invitation_list = ['Wang','Li','Dou','Fang','Xu']
#嘉宾名单
print("---嘉宾名单---")
for name in invitation_list:
    message = f"Dear {name},I would like to invite you to my dinner party!"
    print(message)
#修改名单
print("---修改名单---")
absentName = 'Dou'
invitation_list.remove(absentName)
print(f"Dear {absentName} can't attend my party")
invitation_list.append('He')
for name in invitation_list:
    message = f"Dear {name},I would like to invite you to my dinner party!"
    print(message)
#添加嘉宾
print("---添加嘉宾---")
addName = ['Bao','Zhang','Yang']
invitation_list.insert(0,addName[0])
invitation_list.insert(3,addName[1])
invitation_list.append(addName[2])
for name in invitation_list:
    message = f"Dear {name},I would like to invite you to my dinner party!"
    print(message)
#缩短名单
print("---缩短名单---")
#错误写法
#for name in invitation_list:
#    if len(invitation_list)>2:
#        name = invitation_list.pop()
#        message = f"Sorry,dear {name},my party cancel"
#        print(message)
#修正写法
for _ in range(len(invitation_list)-2): #循环长度-2次，保留两个
    name = invitation_list.pop()
    message = f"Sorry, dear {name}, my party has been cancelled."
    print(message)
for name in invitation_list:
    message = f"Dear {name},I would like to invite you to my dinner party!"
    print(message)
#错误写法
#for index in range(len(invitation_list)):
#    del invitation_list[index]    #循环会按照原来的len，删除元素后索引会超过
#修正写法
del invitation_list[0]
del invitation_list[0]
#或
#for _ in range(len(invitation_list)):
#    del invitation_list[0]
print("---最终名单---")
print(invitation_list)
