def a(data):
    s = str(data['新闻名']) + str(data['新闻地址'])
    s = s.replace('\'', '').replace('[', ' ').replace(']', ' ')
    s = s + '\n'
    with open('网易.txt', 'a+') as ff:
        ff.write(s)
    ff.close()
    return 0
