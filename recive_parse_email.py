import re
import _sqlite
import _email2
import datetime
from datetime import datetime
import _data_parser

def write_data_to_sql(id_, from_,  subject, content, content_type):
	d={}
	#   0                1                  2                3                     4                         5
	d["ID"] = " "; d["Что напомнить"] = " "; d["статус"] = ' '; d["дата"] = ' '; d['Когда напомнить'] = ' '; d['адрес почты'] = ' '
	if re.findall(r'Что ты можешь', subject) != [] or re.findall(r'что ты можешь', subject) != []:
		status = "well_to_know"
		_sqlite.insert_data_sql("test_db", "'"+d["ID"]+"', '"+d["Что напомнить"]+"', '"+status+"', '"\
		+str(datetime.now().strftime('%d.%m.%y  %H:%M:%S'))+"', '"+d['Когда напомнить']+"', '"+from_+"'")
	if re.findall(r'Напомни_', subject) != [] or re.findall(r'напомни_', subject) != []:
		d=_data_parser.table_parser2(content)
		status='remind'
		_sqlite.insert_data_sql("test_db", "'" + d["ID"] + "', '" + d["Что напомнить"] + "', '" + status + "', '" \
		+ str(datetime.now().strftime('%d.%m.%y  %H:%M:%S')) + "', '" + d['Когда напомнить'] + "', '" + from_ + "'")
	# Далее может быть конструкнуция по другим совпадениям и действиям с ними

# Проверяем почту через модуль _email2, записываем данные в k
k=_email2.check_email_box()

# обрабатыаем входящую почту и формируем перечень сообщений для удаления
sublist_to_delete=[]; list_to_delete=[]
for i in k:
	#Обработанные данные на основании загловка сообщения, записываем в БД
	write_data_to_sql(i[0], i[1],  i[2], i[3], i[4])
	#Формируем список сообщений для удаления
	if re.findall(r'Что ты можешь', str(i[2])) != [] or re.findall(r'что ты можешь', str(i[2])) != [] or re.findall(r'Напомни_', str(i[2])) != []:
		sublist_to_delete.append(i[0]);	sublist_to_delete.append(i[2])
		list_to_delete.append(sublist_to_delete)
#Удаляем обработанные сообщения по средством модуля _email2
_email2.delete_several_email(list_to_delete)


