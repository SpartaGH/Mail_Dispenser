import smtplib

def verifnomb():
	quant = input("Nombre de mails à envoyer ?")
	return quant

# while True:
# 		if type(verifnomb()) != int:
# 			verifnomb()
# 		else
# 			break

def main():

	fichier = input("Nom fichier ?")
	#fichier = 'liste.txt'

	#choisir le nb de mail à envoyé
	for(nbmail=null; type(nbmail) != int; nbmail=verifnomb())

	with open(fichier, 'r') as f:
	    
		#Login
		server = smtplib.SMTP('smtp-mail.outlook.com', 587)	#je connais pas cette fonction, je vais te faire confiance
		server.starttls()
		email = ''
		mdp = ''
		server.login(email, mdp)
		print(server.noop()) #Retourne code connexion (refusé/accépté)
		

		#boucle sur chaque ligne -> 1 mail
		n=1
		for line in f:
			 
			msg = "msg test n°"n
			client = str(line)	#faut controler avec des regex si chaque ligne est bien un mail valide
			server.sendmail("sp email", client, msg)	#c'est quoi sp email ?
				
			print("Email n°"n" envoyé.")
			n++

		#Quit
		server.quit()


main()