#!/usr/bin/python
# -*- coding: UTF-8 -*-

# MODULES

import os

# COULEURS

VERT="\033[1;32m"
NORMAL="\033[0;39m"
ROUGE="\033[1;31m"
ROSE="\033[1;35m"
BLEU="\033[1;34m"
BLANC="\033[0;02m"
BLANCLAIR="\033[1;08m"
JAUNE="\033[1;33m"
CYAN="\033[1;36m"

# FONCTIONS
def bienvenue():
	print "-----[JEU DE LA ROULETTE]-----"
	print "    Bienvenue sur le jeu !    "
	print "       Cree par Arthur        "
	print "           Jouons !           "
	print "------------------------------"
	

def fdebug(message):
	if "d" in debug :
		print(ORANGE + message + NORMAL)
def ferror(message):
	if "d" in debug :
		print(ROUGE + message + NORMAL)
	
def testtaille(min,max):
	global nombre
	test = 0
	while test is not "1" : 
		nombre = input (VERT + "Choisis un nombre compris entre 1 et 50 ! >>" + NORMAL) #on demande un nombre
		
		try : # On vérifie que c'est bien un nombre
			int(nombre)
		except :
			print "Ce n'est pas un nombre"
			ferror("Pas un nombre (" + nombre + ")")
		else :
			test1 = "1"
		
		if test1 == "1" :
			test2 = 0
			test3 = 0
			if nombre <= max :
				test2 = "1"
			else :
				print "Ton nombre est trop grand !"
				#ferror("Trop grand (" + str(nombre) + " > " + str(max) + ")")
				
			if min <= nombre :
				test3 = "1"
			else :
				print "Ton nombre est trop petit !"
				#ferror("Trop petit (" + str(nombre) + " < " + str(min) + ")")
			if test2 and test3 == "1" :
				fdebug("Ok !")
				test = "1"
		
# MAIN

bienvenue()
debug = "c"
debug = raw_input("Tape entrée pour jouer !")
testtaille(1,50)

print "tout vas bien"