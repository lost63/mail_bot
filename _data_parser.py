import re
from html_table_parser import HTMLTableParser

def table_parser2(data):
	d={}
	p = HTMLTableParser()
	p.feed(data)
	for i in p.tables[0]:
		if re.findall("ID", str(i)) != [] and re.findall("ID", str(d)) == []: d["ID"] = i[(i.index("ID")+1)].replace(" ","")
		if re.findall("Что напомнить", str(i)) != [] and re.findall("Что напомнить", str(d)) == []: d["Что напомнить"] = i[(i.index("Что напомнить")+1)]
		if re.findall("Когда напомнить", str(i)) != [] and re.findall("Когда напомнить", str(d)) == []: d["Когда напомнить"] = i[(i.index("Когда напомнить") + 1)]
	if re.findall("ID", str(d)) == []: d["ID"] = 'нет данных'
	if re.findall("Что напомнить", str(d)) == []: d["Что напомнить"] = 'нет данных'
	if re.findall("Когда напомнить", str(d)) == []: d["Когда напомнить"] = 'нет данных'
	return d
