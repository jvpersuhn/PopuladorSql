def lerJson(Arquivo):
    f = open(Arquivo,'r',encoding='utf8')
    ret = []
    for i in f:
        s = i.strip()
        if s == '{' or s == '[':
            continue
        else:
            ret.append(i)
    
    a = open('Novo.txt','x')
    for i in ret:
        a.write(i)

def Salvar(Arquivo):
    f = open(Arquivo,'r')
    dic = {}
    ret = []
    for i in f:
        s = i.replace(',','')
        s = s.replace('"','')
        s.strip()
        s = s.split(':')
        s[0].strip()
        if s[0] != '\n' or s[0] != ']' :
            if s[0] == '}':
                ret.append(dic)
            else:
                try:
                    dic[s[0]] = s[1].strip()
                except IndexError as e:
                    print(e)

#lerJson('Dados.txt')
Salvar('Novo.txt')