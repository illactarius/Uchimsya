from manga import Manga
import json

def dobavlenie(manga_l):
	"""функция добавления новой манги в справочник"""
	name = input("Заносим новую мангу\nВведи название: ")
	glav = input('Введи количество глав: ')
	prochitan = input('Сколько глав прочитано? ')
	y = input('Манга закончена? (y/n) ')
	genre = input('Введи жанры через пробел ')
	genres = genre.split()
	if y == y:
		m = Manga(name,glav,prochitan,True,genres)
	else:
		m = Manga(name,glav,prochitan,False,genres)
	manga_l.append(m)


def sohranenie_mangi(manga_l):
	"""функция сохранения текущего списка манги в файл"""
	save_manga={}
	for i in range(0,len(manga_l)):#использую словарь для построчного занесения даннх класса
		save_manga[i] = [manga_l[i].name,manga_l[i].glavi,manga_l[i].prochitano,manga_l[i].ongoing,manga_l[i].genres]
		with open('mangalist.json','w') as f:
			json.dump(save_manga,f)
	print('манга сохранена')

def otkritie_mangi():
	"""функция для открытия внешнего файла для справочника"""
	manga_l = []
	save_manga = {}
	with open('mangalist.json') as f:
		save_manga = json.load(f)#присваиваем данные из файла словарю
	for i in save_manga:#переносим данные справочника в список экземпляров класса Manga
		buf = Manga(save_manga[i][0],save_manga[i][1],save_manga[i][2],save_manga[i][3],save_manga[i][4])
		manga_l.append(buf)
	return manga_l
"""
manga_list=otkritie_mangi()
dobavlenie(manga_list)
sohranenie_mangi(manga_list)
for i in range(0,len(manga_list)):
	manga_list[i].manga_info()
end=input('end')
"""