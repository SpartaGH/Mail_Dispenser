import smtplib as sl
import re

def verifnomb():
    quant = input("Nombre de mails à envoyer ?")
    return int(quant)

def main():

    #fichier = input("Nom fichier ?")
    fichier = 'liste.txt'

    #choisir le nb de mail à envoyé
    nbmail=verifnomb()
    while type(nbmail) != int:
        nbmail=verifnomb()

    with open(fichier, 'r') as f:
        
        #Login
        print("test1")
        #☻ça bug au niveau de la connexion
        server = sl.SMTP('smtp.gmail.com', 587)    #je connais pas cette fonction, je vais te faire confiance
        #server.set_debuglevel(1)
        server.starttls()
        #print('q')
        email = 'louisph54300@gmail.com'
        mdp = 'root2540'
        server.login(email, mdp)
        #print("test2")

        #boucle sur chaque ligne -> 1 mail
        n=1
        for line in f:
            
            msg = ("msg test n°"+str(n)).encode()
            client = str(line)  #controle avec des regex si chaque ligne est bien un mail valide
            regexMail = '^[a-z0-9._-]+@[a-z0-9._-]{2,}\.[a-z]{2,4}$'
            if re.match(regexMail,client):
                server.sendmail(email, client, msg)
                print("Email n°"+str(n)+" envoyé à "+str(client)+", msg : "+(msg).decode())
                n=n+1
            else:
                print("Mail illisible : "+str(client))

        #Quit
        server.quit()

main()
