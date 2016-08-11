import random
import string
from random import randint
import math


phrase = 'Gage Krumbach'
population = 200
mutation = 25 #percent
ran_phrases = []
complete = 0
CHAR = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 ";:=-_+\/!@#$%^&*(),.??><'


def title():
	header = ""
	for i in range(len(phrase) - 5):
		header += " "
	print("Phrase" + header + " Fitness - Generation")

class Random_Phrase():
	
	def __init__(self):
		self.ran_phrase = []
		self.fitness = 0
	
	def make_rand_phrase(self):
		for i in range(len(phrase)):
			self.ran_phrase.append(random.choice(CHAR))
		


def make_pop():
	for i in range(population):
		generator = Random_Phrase()
		generator.make_rand_phrase()
		
		ran_phrases.append(generator)

		
def calc_fitness():
	for i in range(population):
		for x in range(len(phrase)):
			if ran_phrases[i].ran_phrase[x] == phrase[x]:
				ran_phrases[i].fitness += 1
				
def calc_fitness_two():
	for i in range(population):
		for x in range(len(phrase)):
			letter = ran_phrases[i].ran_phrase[x]
			
			if letter == phrase[x]:
				ran_phrases[i].fitness += 25
			
			elif letter.lower == phrase[x] or letter.upper == phrase[x]:
				ran_phrases[i].fitness += 15
			
			else:
				dist = abs(CHAR.find(phrase[x]) - CHAR.find(letter))
				ran_phrases[i].fitness += int(dist / 88 * 10)
				


def print_top():
	for i in range(len(phrase)):
		print(max(ran_phrases, key=lambda o: o.fitness).ran_phrase[i], end='')
		
	print("    ", max(ran_phrases, key=lambda o: o.fitness).fitness, " - ", index_loop)
	

	
def new_generation():
	temp_generation = []
	mate_1 = None
	mate_2 = None
	

	for i in range(population):
		mate_1 = None
		mate_2 = None
		#new random values
		pop_int_index = randint(0, population - 1)
		fitness_int = randint(0, max(ran_phrases, key=lambda o: o.fitness).fitness)
		
		#find mate 1
		while mate_1 == None:
			if ran_phrases[pop_int_index].fitness >= fitness_int:
				mate_1 = ran_phrases[pop_int_index]
			else:
				pop_int_index = randint(0, population - 1)
		
		#new random values
		pop_int_index = randint(0, population - 1)
		fitness_int = randint(0, max(ran_phrases, key=lambda o: o.fitness).fitness)

		#find mate 2
		while mate_2 == None:
			if ran_phrases[pop_int_index].fitness >= fitness_int:
				mate_2 = ran_phrases[pop_int_index]
			else:
				pop_int_index = randint(0, population - 1)
		
		#combine mates
		child_phrase = mate_1.ran_phrase[0:int(len(phrase)/2)] + mate_2.ran_phrase[int(len(phrase)/2): len(phrase)]
		child = Random_Phrase()
		child.ran_phrase = child_phrase
		temp_generation.append(child)
		
		#mutation
		if random.randint(0, 100) < mutation:
			child.ran_phrase[randint(0, len(phrase) - 1)] = random.choice(CHAR)

	
	
	global ran_phrases
	ran_phrases = temp_generation
	

def test_if_done():
	old = complete
	max_fit = max(ran_phrases, key=lambda o: o.fitness).fitness
	global complete
	complete = max_fit
	if old != complete:
		print_top()

		
index_loop = 0
title()
make_pop()
while complete != len(phrase):
	calc_fitness_two()
	test_if_done()
	new_generation()
	index_loop += 1

print("FINISH")