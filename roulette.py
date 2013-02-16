#!/usr/bin/python
# -*- coding: UTF-8 -*-


################ IMPORTATIONS ################
import os
import time
import sys

from random import randrange
from math import ceil
##############################################
 
################## COULEURS ##################

VERT="\033[1;32m"
NORMAL="\033[0;39m"
ROUGE="\033[1;31m"
ROSE="\033[1;35m"
BLEU="\033[1;34m"
BLANC="\033[0;02m"
BLANCLAIR="\033[1;08m"
JAUNE="\033[1;33m"
CYAN="\033[1;36m"

##############################################

def bienvenue():
	print "-----[JEU DE LA ROULETTE]-----"
	print "    Bienvenue sur le jeu !    "
	print "       Cree par Arthur        "
	print "           Jouons !           "
	print "------------------------------"

def progressbar():
	toolbar_width = 70

	# setup toolbar
	sys.stdout.write("[%s]" % (" " * toolbar_width))
	sys.stdout.flush()
	sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

	for i in xrange(toolbar_width):
		time.sleep(0.1) # do real work here
		# update the bar
		sys.stdout.write("-")
		sys.stdout.flush()
	sys.stdout.write("\n")


def partie():
	global continuer_partie
	global argent
	while continuer_partie: # Tant qu'on doit continuer la partie on demande a l'utilisateur de saisir le nombre sur lequel il va miser
		nombre_mise = -1
		while nombre_mise < 0 or nombre_mise > 49:
			nombre_mise = input(VERT + "Tapez le nombre sur lequel vous voulez miser (entre 0 et 49) : >>>" + NORMAL)
			# On convertit le nombre mise
			try:
				nombre_mise = int(nombre_mise)
			except ValueError:
				print(ROUGE + "Vous n'avez pas saisi de nombre" + NORMAL)
				nombre_mise = -1
				continue
			if nombre_mise < 0:
				print(ROUGE + "Ce nombre est negatif" + NORMAL)
			if nombre_mise > 49:
				print(ROUGE + "Ce nombre est superieur a 49" + NORMAL)
 
		# A present, on selectionne la somme A miser sur le nombre
		mise = 0
		while mise <= 0 or mise > argent:
			mise = input(VERT + "Tapez le montant de votre mise : >>>" + NORMAL)
			# On convertit la mise
			try:
				mise = int(mise)
			except ValueError:
				print(ROUGE + "Vous n'avez pas saisi de nombre" + NORMAL)
				mise = -1
				continue
			if mise <= 0:
				print(ROUGE + "La mise saisie est negative ou nulle." + NORMAL)
			if mise > argent:
				print(ROUGE + "Vous ne pouvez miser autant, vous n'avez que" + argent + "$" + NORMAL)
 
		# Le nombre mise et la mise ont ete selectionnes par
		# l'utilisateur, on fait tourner la roulette
		numero_gagnant = randrange(50)
		print(BLEU + "La roulette tourne... " + NORMAL ) 
 		progressbar()
 		print(BLEU + "... et s'arrête sur le numero : " + JAUNE + str(numero_gagnant) + NORMAL)
		# On etablit le gain du joueur
		if numero_gagnant == nombre_mise:
			print(VERT + "Felicitations ! Vous obtenez " + str(mise * 3) + "$ !" + NORMAL)
			argent += mise * 3
		elif numero_gagnant % 2 == nombre_mise % 2: # ils sont de la même couleur
			mise = ceil(mise * 0.5)
			print(VERT + "Vous avez mise sur la bonne couleur. Vous obtenez " + str(mise) + "$" + NORMAL)
			argent += mise
		else:
			print(JAUNE + "Vous perdez votre mise : vous n'avez pas mise sur la bonne couleur ni sur le bon chiffre" + NORMAL)
			argent -= mise
 
		# On interrompt la partie si le joueur est ruine
		if argent <= 0:
			print(ROUGE + "Vous êtes ruine ! C'est la fin de la partie." + NORMAL)
			continuer_partie = False
		else:
			# On affiche l'argent du joueur
			print(VERT + "Vous avez a present " + str(argent) + "$" + NORMAL)
			quitter = raw_input(BLEU + "Souhaitez-vous quitter le casino (o/n) ? >>>" + NORMAL)
			if quitter == "o" or quitter == "O":
				print(ROUGE + "Vous quittez le casino avec vos gains." + NORMAL)
				continuer_partie = False

################### MAIN ####################
bienvenue()

# Declaration des variables de depart
argent = 1000 # On a 1000 $ au debut du jeu
global argent
continuer_partie = True # Booleen qui est vrai tant qu'on doit continuer la partie

print(VERT + "Vous vous installez devant la roue avec exactement " +  str(argent) + "$." + NORMAL)


partie()
#############################################