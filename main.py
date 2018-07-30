import smtplib
import re

def verifnomb():
	quant = input("Nombre de mails à envoyer ?")
	return quant

# while True:
# 		if type(verifnomb()) != int:
# 			verifnomb()
# 		else
# 			break

def main():

	#fichier = input("Nom fichier ?")
	fichier = 'liste.txt'

	#choisir le nb de mail à envoyé
	for(nbmail=null; type(nbmail) != int; nbmail=verifnomb())

	with open(fichier, 'r') as f:
	    
		#Login
		server = smtplib.SMTP('smtp-gmail.com', 465)	#je connais pas cette fonction, je vais te faire confiance
		server.starttls()
		email = 'louisph54300@gmail.com'
		mdp = 'v#OKIF9QuxSpYM5Z'
		server.login(email, mdp)
		print(server.noop()) #Retourne code connexion (refusé/accépté)
		

		#boucle sur chaque ligne -> 1 mail
		n=1
		for line in f:
			 
			msg = "msg test n°"n
			client = str(line)	#controle avec des regex si chaque ligne est bien un mail valide
        regexMail = "^[a-z0-9._-]+@[a-z0-9._-]{2,}\.[a-z]{2,4}$"
			if re.match(regexMail,client):
            server.sendmail("sp email", client, msg)
            print("Email n°"n" envoyé à "client", msg : "msg)
            n++
        else:
            print("Mail illisible : "client)

		#Quit
		server.quit()


main()
