import re
import _sqlite
import _email2
import datetime
from datetime import timedelta
from datetime import datetime
import path

def adresses_from(list_):
	x2=re.findall('<(.*?)>', list_)
	if x2!=[]:
		x1=re.findall('<(.*?)>', list_)[0]
	else:
		x1=list_
	return x1

def check_sql_requests_action_by_one():
	check_exist = _sqlite.sql_row_names("test_db")
	for i in check_exist:
		if i[2]=='well_to_know':
			name='Bot'
			f = open(path.path+'template_what_you_can.html', 'r')
			html=f.read()
			html = html.replace('{_data_}', name)
			_email2.send_email('что я могу', html, adresses_from (i[5]))
			_sqlite.delete_data_sql("test_db", 'data_last_modify', i[3])
		if i[2]=='remind':
			try:
				time_o = datetime.strptime(i[4], '%d.%m.%y %H:%M')
				time_error = ' '
			except:
				time_o = datetime.strptime('01.01.30 00:00', '%d.%m.%y %H:%M')
				time_error = 'error_time_format'
			if time_o <= datetime.now() and i[2] == 'remind' or time_error == 'error_time_format':
				_email2.send_email('Напоминание ' + i[0]+' '+time_error, i[1], adresses_from(i[5]))
				_sqlite.delete_data_sql("test_db", 'data_last_modify', i[3])
		if i[2] == 'YOUR PARSER':
			#Различные другие совпадени и действия с ними
			pass

check_sql_requests_action_by_one()







