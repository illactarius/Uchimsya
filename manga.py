class Manga():
	'''класс для манги'''
	def __init__(self,name,glavi,prochitano,ongoing = False,genres=[]):
		'''инициируем атрибуты имя, всего глав, прочитано глав, завершенность и жанры'''
		self.name = name
		self.glavi = glavi
		self.prochitano = prochitano
		self.ongoing = ongoing
		self.genres = genres
	def manga_end(self):
		"""функция заканчивающая мангу"""
		self.ongoing = False
	def update_glav(self,count):
		"""функция обновляющая количество вышедших глав"""
		if self.ongoing:
			self.glavi = count
		else:
			print('неча обновлять законченную мангу')
	def manga_status(self):
		"""функция сообщающая закончилась ли манга"""
		if self.ongoing:
			print('Манга продолжается')
		else:
			print('Манга закончилась')
	def update_reading(self,chapter):
		"""функция обновляющая количество прочитанных глав"""
		self.prochitano = chapter
	def manga_info(self):
		"""функция, выводящая информацию по прочитанным главам"""
		genress =''
		for genre in self.genres:
			genress +=f' {genre}' 
		if self.ongoing:
			print(f'Манга {self.name.title()} в жанрах {genress.lstrip()} продолжается:\nСейчас глав {self.glavi}, прочитано {self.prochitano}')
		else:
			print(f'Манга {self.name.title()} в жанрах {genress.lstrip()} закончена:\nВсего глав {self.glavi}, прочитано {self.prochitano}')

#naruto = Manga('Naruto',700,200,False,['сёнен','фентези','боевик'])
#naruto.manga_info()
