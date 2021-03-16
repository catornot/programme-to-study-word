from kivy.app import App
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock

import random

from kivy.core.window import Window
from kivy.graphics import (Color,Ellipse,Rectangle,Line)

score=0
#write your words in this tuple like like in the example 
words_backup=(

['Canada' , 'le village' ],
['Saskatchewan' , 'rivière au débit rapide' ],
['Winnipeg', 'eau sale' ],
['Ontario', 'lac magnifique' ],
['Toronto', 'lieu de rencontre'],

['Ottawa' , "commercer"  ],
['Québec', 'un passage étroit' ],
['Chicoutimi' , 'la fin des eaux profondes' ],
['Chibougamau' , 'lieu de rencontre' ],
["tu doit savoir comment ecricre les mot lieu",""],



)

class WindowManager(ScreenManager):
	pass

class QAscreen(Screen):
	global words_backup
	words=list(words_backup)
	word_num=0
	t1 = ObjectProperty(None)
	text11 = ObjectProperty(None)
	text12 = ObjectProperty(None)

	t2 = ObjectProperty(None)
	text21 = ObjectProperty(None)
	text22 = ObjectProperty(None)

	t3 = ObjectProperty(None)
	text31 = ObjectProperty(None)
	text32 = ObjectProperty(None)

	t4 = ObjectProperty(None)
	text41 = ObjectProperty(None)
	text42 = ObjectProperty(None)

	t5 = ObjectProperty(None)
	text51 = ObjectProperty(None)
	text52 = ObjectProperty(None)

	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		cloq1=[]
		cloq2=[]
		self.answers={}
		for x in range(5):
			try:
				poped=self.words[x+self.word_num][0]							
				cloq1.append(poped)
			except:
				pass

		for x in range(5):
			try:
				cloq2.append(self.words[x+self.word_num][1])
			except:
				pass
		# print(cloq2,
		# 	cloq1
		# 	)
		for x in range(5):
			self.answers[cloq2[x]]=cloq1[x]

		copy=cloq2		
		
		
		cloq2=[]
		copy2=cloq2

		num=[]
		for x in range(5):
			num.append(x+1)

		for x in range(5):
			if copy[0] != "":
				cloq2.append(str(num.pop(random.randint(0,len(num)-1)))+": "+str(copy.pop(0)))
			else:
				cloq2.append(copy.pop(0))
				print("got")

		list_of_strings=[]
		copy_answers={}

		copy2=[]
		for x in range(5):
			copy2.append(self.words[x+self.word_num][1])

		for x in range(5):
			if cloq2[x] != "":
				value=self.answers.get(copy2[x])
				copy_answers[value]=cloq2[x][0]
				list_of_strings.append(cloq2[x])
			else:
				value=self.answers.get(copy2[x])
				copy_answers[value]=cloq2[x]
				list_of_strings.append(cloq2[x])
			# index=list(cloq2.values()).index(copy2.pop(0))
			# string=str(index)+": "+str(cloq2[str(index)])
			# self.answers[str(x)]=string[0]
			# list_of_strings.append(string)
			# print(self.answers)
		self.answers=copy_answers

		new_list=[]
		for x in range(len(list_of_strings)):
			new_list.append(list_of_strings.pop(random.randint(0,len(list_of_strings)-1)))

		new_list2=[]
		for x in range(len(cloq1)):
			new_list2.append(cloq1.pop(random.randint(0,len(cloq1)-1)))

		try:

			self.text11 = new_list2[0]
			self.text12 = new_list[0]

			self.text21 = new_list2[1]
			self.text22 = new_list[1]


			self.text31 = new_list2[2]
			self.text32 = new_list[2]

			self.text41 = new_list2[3]
			self.text42 = new_list[3]

			self.text51 = new_list2[4]
			self.text52 = new_list[4]

			self.word_num += 5

		except:
			pass
		
		print(str(self.answers)+'\n')


	def correction(self):
		global score
		global words_backup

		if self.answers[self.text11] == self.t1.text:
			score = score + 1 

		if self.answers[self.text21] == self.t2.text:
			score = score + 1 

		if self.answers[self.text31] == self.t3.text:
			score = score + 1 

		if self.answers[self.text41] == self.t4.text:
			score = score + 1 

		if self.answers[self.text51] == self.t5.text:
			score = score + 1
		self.t1.text = "" 
		self.t2.text = "" 
		self.t3.text = "" 
		self.t4.text = "" 
		self.t5.text = "" 



		print(score)

		if self.word_num > 19:
			self.word_num = 0
			self.words = list(words_backup)
			sm.current = "score"
		try:
			cloq1=[]
			cloq2=[]
			self.answers={}
			for x in range(5):
				try:
					poped=self.words[x+self.word_num][0]							
					cloq1.append(poped)
				except:
					pass

			for x in range(5):
				try:
					cloq2.append(self.words[x+self.word_num][1])
				except:
					pass
			# print(cloq2,
			# 	cloq1
			# 	)
			for x in range(5):
				try:
					self.answers[cloq2[x]]=cloq1[x]
				except:
					self.answers["cloq2[x]"]="cloq1[x]"

			copy=cloq2		
			
			
			cloq2=[]
			copy2=cloq2

			num=[]
			for x in range(5):
				num.append(x+1)

			for x in range(5):
				if copy[0] != "":
					cloq2.append(str(num.pop(random.randint(0,len(num)-1)))+": "+str(copy.pop(0)))
				else:
					cloq2.append(copy.pop(0))
					print("got")

			list_of_strings=[]
			copy_answers={}

			copy2=[]
			for x in range(5):
				copy2.append(self.words[x+self.word_num][1])

			for x in range(5):
				if cloq2[x] != "":
					value=self.answers.get(copy2[x])
					copy_answers[value]=cloq2[x][0]
					list_of_strings.append(cloq2[x])
				else:
					value=self.answers.get(copy2[x])
					copy_answers[value]=cloq2[x]
					list_of_strings.append(cloq2[x])
				# index=list(cloq2.values()).index(copy2.pop(0))
				# string=str(index)+": "+str(cloq2[str(index)])
				# self.answers[str(x)]=string[0]
				# list_of_strings.append(string)
			# print(self.answers)
			self.answers=copy_answers

			new_list=[]
			for x in range(len(list_of_strings)):
				new_list.append(list_of_strings.pop(random.randint(0,len(list_of_strings)-1)))

			new_list2=[]
			for x in range(len(cloq1)):
				new_list2.append(cloq1.pop(random.randint(0,len(cloq1)-1)))

			# print(self.answers)
		

			self.text11 = new_list2[0]
			self.text12 = new_list[0]

			self.text21 = new_list2[1]
			self.text22 = new_list[1]


			self.text31 = new_list2[2]
			self.text32 = new_list[2]

			self.text41 = new_list2[3]
			self.text42 = new_list[3]

			self.text51 = new_list2[4]
			self.text52 = new_list[4]

			self.word_num += 5

		except:
			self.word_num = 0
			self.words = list(words_backup)
			sm.current = "score"
		
		print(str(self.answers)+'\n')

		# print(self.word_num,words_backup)




class MainMenu(Screen):
	pass

class Score(Screen):
	score1 = ObjectProperty(None)

	def on_enter(self):
		Clock.schedule_once(self.change_screen)

	def change_screen(self, dt):
		global score
		self.score1 = str(score-1)+"/?" # hey hey





Builder.load_file("app.kv")
sm = WindowManager()

screens = [MainMenu(name="mainmenu"),QAscreen(name="qa"),Score(name="score")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "mainmenu"
       
class histoireApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    histoireApp().run()
