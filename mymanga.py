from manga import Manga
from funkcii import dobavlenie,sohranenie_mangi,otkritie_mangi

print('Добро пожаловать')
my_list = otkritie_mangi()
while True:
	print('Выберите операцию:\nДля просмотра списка аниме введите "s"\nДля добавления нового введите "u"\nДля работы с конкретным введите его название')
	v = input('Для выхода введите "q"\n')
	if v == "q":
		#print('Cписок сохранён')
		sohranenie_mangi(my_list)
		break
	elif v == 'u':
		dobavlenie(my_list)
	elif v == 's':
		for i in range(0,len(my_list)):
			my_list[i].manga_info()
	else:
		ind = -5
		for i in range(0,len(my_list)):
			if my_list[i].name.lower() == v.lower():
				ind = i
		if ind >=0:
			while True:
				print('Выберите действие введя цифру:')
				action = input('0)Получить информацию о манге\n1)Обновить количество вышедших глав\n2)Обновить количество прочитанных глав\n3)Если манга кончилась\n4)Для выхода\n')
				if action == '1':
					print(f'сейчас глав {my_list[ind].glavi}')
					update_glavi = input('Введите число вышедших глав\n')
					my_list[ind].update_glav(update_glavi)
				elif action == '2':
					print(f'сейчас прочитано глав {my_list[ind].prochitano}')
					prochitano_glavi = input('Введите количество прочитанных глав\n')
					my_list[ind].update_reading(prochitano_glavi)
				elif action == '3':
					my_list[ind].manga_end()
				elif action == '0':
					my_list[ind].manga_info()
				elif action == '4':
					break
				else:
					print('введено не правильное значение')
			else:
				print('такой манги в списке нет либо название введено не правильно')


end=input('end')



