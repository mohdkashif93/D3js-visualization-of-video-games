f = open('data/vgsales.csv','r')

genre_keys = ['Action','Sports','Platform','Racing','Puzzle','Role-Playing','Adventure',
'Fighting','Misc','Shooter','Strategy','Simulation']
'''
dict_genre = {}
c = 0
for i in f:
	i =  i.split(',')
	if(c!=0):
		print i[4]
		print float(i[-1])
		if i[4] in genre_keys:
			if i[4] in dict_genre.keys():
				dict_genre[i[4]] += float(i[-1])
			else:
				print i[4]
				dict_genre[i[4]] = float(i[-1])
	c = c + 1
print dict_genre

res_dict1 = []
for i in dict_genre.keys():
	r = {}
	r['category'] = i
	r['measure'] = dict_genre[i]
	res_dict1.append(r)
print res_dict1
'''

plat_keys = ['Wii','NES','3DS','2600','DC','DS','GB','GBA','GC',
'GEN','N64','NES','PC','PS2','PS3','PS4','PSP','PSV','SAT','SCD',
'SNES','WiiU','X360','XB','XOne']
'''
dict_plat = []
c = 0
for i in f:
	i =  i.split(',')
	if(c!=0):
		print i[2]
		print float(i[-1])
		if i[2] in plat_keys and i[4] in genre_keys:
			r1 = {}
			r1['group'] = i[4]
			if i[4] in genre_keys:
				r1['category'] = i[2]
				r1['measure'] = float(i[-1])
			dict_plat.append(r1)
	c = c + 1
'''
'''
dict_plat_group = {}
c = 0
for i in f:
	i =  i.split(',')
	if(c!=0):
		print i[2]
		print float(i[-1])
		if i[2] in plat_keys and i[4] in genre_keys:
			if i[2]+','+i[4] in dict_plat_group.keys():
				dict_plat_group[i[2]+','+i[4]] += float(i[-1])
			else:
				dict_plat_group[i[2]+','+i[4]] = float(i[-1])
	c = c + 1

print dict_plat_group

f = open('data/new_line','w')
f.write('[')
for i in dict_plat_group.keys():
	j = i.split(',')
	#{ group: "Steve", category: "Mangos", measure: 1822.6467 }, 
	f.write('{group:"'+j[1]+'", category:"'+j[0]+'", measure:')
	f.write(str(dict_plat_group[i]))
	f.write('},')
f.write(']')
'''
#{ group: "Steve", category: 2014, measure: 7035 }

#year_keys = ['1984','1985','1986','1987','1988','1989','1990','2000','2001','2002',
#'2003','2004','2005',]
year_keys = ['2006','2007','2008','2009','2010','2011',
'2012','2013','2014','2015']

dict_plat_line = {}
c = 0
for i in f:
	i =  i.split(',')
	if(c!=0):
		print i[3]
		print float(i[-1])
		if i[3] in year_keys and i[4] in genre_keys:
			if i[3]+','+i[4] in dict_plat_line.keys():
				dict_plat_line[i[3]+','+i[4]] += float(i[-1])
			else:
				dict_plat_line[i[3]+','+i[4]] = float(i[-1])
	c = c + 1

print dict_plat_line

f = open('data/new_line_3','w')
f.write('[')
for i in dict_plat_line.keys():
	j = i.split(',')
	#{ group: "Steve", category: "Mangos", measure: 1822.6467 }, 
	f.write('{group:"')
	f.write(j[1])
	f.write('", category:"'+j[0]+'", measure:')
	f.write(str(dict_plat_line[i]))
	f.write('},')
f.write(']')
