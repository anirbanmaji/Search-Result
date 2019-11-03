from django.shortcuts import render
import cx_Oracle
import re

def home(request):
    return render(request, 
    			'home.html',)




def update(request):
	query = request.GET['search_query']

	username = "c##anirban"
	password = "proscenium"
	servicename = "orcl"

	con = cx_Oracle.connect(username+"/"+password+'@localhost/'+servicename)
	cur = con.cursor()

	cur.execute("select max(FREQUENCY) from WORD_FREQUENCY")
	max_freq = int(cur.fetchone()[0])

	def sorting_key(f_tuple):
		word = f_tuple[0]
		reg_starting_with_query = re.compile('^'+query+'.*')
		if re.match(reg_starting_with_query, word) != None:
			return max_freq - len(word)
		else:
			return f_tuple[1]

	word_freq_list_unsorted = []
	word_freq_list_sorted = []

	
	cur.execute("select * from WORD_FREQUENCY where word like '%"+query+"%'")
	word_freq_list_unsorted = cur.fetchall()
	word_freq_list_sorted = sorted(word_freq_list_unsorted, key = sorting_key, reverse = True)

	only_25_sorted = word_freq_list_sorted[:25]

	return render(request, 'newpage.html',{'query':only_25_sorted})