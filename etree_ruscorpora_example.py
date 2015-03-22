from xml.etree import ElementTree
from urllib.request import urlopen

url = 'http://search.ruscorpora.ru/search.xml?sort=gr_tagging&out=normal&dpp=1000&spd=1000&seed=13407&env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&text=lexgramm&mode=main&lang=ru&nodia=1&parent1=0&level1=0&lex1=&gramm1=A&sem1=t%3Aphysq%3Acolor&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&level2=0&min2=1&max2=1&lex2=&gramm2=S&sem2=r%3Aabstr+%26+t%3Apsych%3Aemot&sem-mod2=sem&sem-mod2=sem2&flags2=&m2='

fixed_url = url.replace('search.xml', 'dump.xml')
tree = ElementTree.parse(urlopen(fixed_url))

##for word in tree.findall('.//document//word'):
##    token = word.get('text')
##    lemmas = []
##    for element in word.findall('.//el[@name="lex"]//el-atom'):
##        lemmas.append(element.text)
##    print(token + ':', ', '.join(lemmas))

for word in tree.findall('.//word[@target]'):
    for atom in word.findall('.//el-atom'):
        if atom.text == 'r:abstr':
            print(word.get('text'))

# Задача: написать все леммы одного слова на одной строке
#
# Следующая задача: приписать в начале каждой строки
# словоформу, она лежит так: <word text="стакана" code="-1">
#
##скованный: скованный, сковать
##чёрным: черные, черный, черная
##отчаянием: отчаяние
#
# Следующая: вывести те из словоформ, помеченных, как
# входящие в ответ, которые при этом обладают
# семантическим признаком t:plant
# в ответе: <word text="грустью" target="1" queryPosition="1" code="-1">
#
# Пример выдачи:
##скованный, сковать
##черные, черный, черная
##отчаяние
##я
##видеть
##мой
##погибший, погибнуть
##товарищ
##и
##десятка, десяток
##побить
##они
##враг

print("PROFIT!")
