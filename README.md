# nvg
Nmap Visual Graph

Usage: python nvg.py 'gnmap file' 'output file'

Example: python nvg.py nmap.gnmap nmap.json

### Инструкция по использованию:
запустить сканирование портов

nmap -sU -sT -oG nmap.gnmap 'ip-диапазон'

После окончания сканирования запустить скрипт в интерпретаторе Python 3.4

python nvg.py /путь/к/файлу/nmap.gnmap /путь/к/файлу/nmap.json

В итоге в папке должны быть следующие файлы: nvg.py, nmap.gnmap, graph.html, dndTree.js, nmap.json(генерируется скриптом)

Запустить graph.html
