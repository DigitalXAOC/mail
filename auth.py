import poplib
with open('userinfo') as uinfo:
    data=uinfo.readlines()
    data=[i.rstrip() for i in data]
    print(data)

'''    E=poplib.POP3(data[0])
    E.user(data[1])
    E.pass_(data[2])
    print(E.retr(1)[1])
    E.quit()
'''
