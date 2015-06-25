# nvg
Nmap Visual Graph

Usage: python grep.py 'gnmap file' 'output file'

Example: python grep.py nmap.gnmap nmap.json

### Инструкция по использованию:
запустить сканирование портов, указать для файла nmap.gnmap путь, где находится основной скрипт

nmap -sU -sT -oG nmap.gnmap <ip-диапазон>

После окончания сканирования запустить скрипт в интерпретаторе Python 3.4

python grep.py nmap.gnmap nmap.json

В итоге в папке должны быть следующие файлы: script.py, nmap.gnmap, graph.html, dndTree.js, nmap.json(генерируется скриптом)
