# -*- coding: cp1251 -*-
import os, re, sys

__description__ = 'Nmap Visual Graph'
__author__ = 'Storchak Sergey a.k.a ser-storchak'
__version__ = '1.4'
__date__ = '25.06.2015'

'''
Особенности программы:
- запуск с параметрами;
- парсит файл nmap.gnmap;
- не отображает узлы без открытых портов;
- не отображает порты со статусом "unknown";

Планируется:
- выбор графа;
- параметры по умолчанию;
- изменение имени выходного файла в dndTree.js;
- при завершении скрипта выдать ссылку на открытие файла с графом;
- оптимизация кода
'''

def title():
	print ("\n\t Nmap Visual Graph v1.4 ")
	print ("\t-------------------------\n")
	
def usage():
	title()
	print ("\n Usage: python nvg.py <gnmap file> <output file>\n")
	print (" Example: python nvg.py nmap.gnmap nmap.json\n")

if len(sys.argv) <= 2:
	usage()
	sys.exit(1)
else:
	title()
	
filepath_nmap = sys.argv[1]
filepath_result = sys.argv[2]

file = open(filepath_nmap, "r")
f = open(filepath_result, "w")
f.write("{\n\t\"name\": \"nmap\",")
f.write("\n\t\"children\": [{")
for y in file.readlines():
    pattern1 = r"Host: (?P<host>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) \(\)\sPorts"
    pattern2 = r"\d{1,5}/[a-z|]+/[a-z]+//[a-z-]+///"
    pattern3 = r"\d{1,5}/(unknown)/[a-z]+//"
    ip1 = re.compile (r"Host: (?P<host>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) \(\)\sPorts")
    ip2 = re.compile(r"\d{1,5}/[a-z|]+/[a-z]+//[a-z-]+///")
    check1 = re.match(pattern1, y)
    check2 = re.match(pattern2, y)
    r1 = ip1.findall(y)
    r2 = ip2.findall(y)
    r = r1 + r2
    if check1 or check2: # исключение узлов без открытых портов
        f.write("\n\t\t\"name\": \"%s\"," % r[0])
        del r[0]
        f.write("\n\t\t\"children\": [")
        a = 0
        for x in r:
            check3 = re.match(pattern3, x) # исключение портов со статусом "unknown"
            if not check3: 
                a +=1
                if a == len(r):  
                    f.write("{\n\t\t\t\"name\": \"%s\"" % x)
                    f.write("\n\t\t}]")
                else:
                    f.write("{\n\t\t\t\"name\": \"%s\"" % x)
                    f.write("\n\t\t}, ")
        f.write("\n\t}, {")
f.write("\n\t}]")
f.write("\n}")
f.close()
file.close()
'''
Удаление лишних символов
'''
with open(filepath_result, "r+") as d:
    pattern4 = r"},\s+}, {"
    zamena = r"}]"
    s = d.read()
    s = re.sub(pattern4, zamena, s)
    d.seek(0)
    d.write(s)
    d.truncate()
print ("\nГенерация файла завершена\n")    
