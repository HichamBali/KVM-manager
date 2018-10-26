from Tkinter import *
import libvirt 
import sys
import os
conn = libvirt.open()
choix=8

while choix != 5 :  
	print "programme de gestion des machines virtuelles ; veuillez entrer votre choix"
	print " 0) Nom de la machine hyperviseur "
	print " 1) lister les machines virtuelles"
	print " 2) demarrer une machine"
	print " 3) Arreter une machine "
	print " 4) l'adresse IP d'une machine virtuelle donnee"
	print " 5) quitter"
	choix=raw_input(" Tapper un numero ")
	choix=int(choix)
	if choix==0 :
		B=conn.getHostname()
		print "La machine hyperviseur "+B
	if choix==1 : 
		print "Lister les machines virtuelle"+str(conn.listDefinedDomains())
	if choix==2 : 
		print "Lister les machines virtuelle"+ str(conn.listDefinedDomains())
		A = raw_input ("Quel machine voullez vous demarrer [tappez le nom de la machine]")
		print A
		rhel=conn.lookupByName(A)
		rhel.create()
		os.system("virt-viewer " + rhel.name() + " &")
	if choix==3 :
		print "Lister les machines virtuelle"+str(conn.listDomainsID())
		A = int(raw_input ("Quel machine voullez vous Arreter [ tappez le nom de la machine ]"))
		rhel = conn.lookupByID(A)
		rhel.destroy()
	if choix==5 : 
		break

		


	  

