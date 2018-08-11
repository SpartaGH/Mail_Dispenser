import smtplib as sl
import re

def verifnomb():
    quant = input("Nombre de mails à envoyer ?")
    return int(quant)

#TODO à tester
def triMail(File fb, File fe, File fa):
    temp = ''
    #on verifie pour chaque adresse du fichier brut si elle n'est pas dans le fichier envoyé
    with open(fb , 'r'):
        with open(fe, 'r'):
            for line in fb :
                if not re.match(line,fe):
                    #Si ce n'est pas le cas, on ajoute cette adresse a un string temp
                    temp = temp + line
    with open(fa , 'w'):
        #on copie le temp dans fa
        #TODO
            
#TODO a retester            
def envoieMail(File file):
    
    #choisir le nb de mail à envoyé
    nbmail=verifnomb()
    while type(nbmail) != int:
        nbmail=verifnomb()

    with open(file, 'r') as f:
        
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
            if n==nbmail+1:
                break
            else:
                msg = ("msg test n°"+str(n)).encode()
                client = str(line)  #controle avec des regex si chaque ligne est bien un mail valide
                regexMail = '^[a-z0-9._-]+@[a-z0-9._-]{2,}\.[a-z]{2,4}$'
                if re.match(regexMail,client):
                    server.sendmail(email, client, msg)
                    print("Email n°"+str(n)+" envoyé à "+str(client)+", msg : "+(msg).decode())
                    n=n+1
                else:
                    print("Mail illisible : "+str(client))

        
        print(str(nbmail)+" email(s) ont/a été envoyé.")
        #Quit
        server.quit()

def main():
    
    #On s'occupe de trié les adresses
    fileMailBrut = 'liste.txt'
    fileMailEnvoye = 'mailEnvoye.txt'
    fileMailAEnvoye = 'mailAEnvoye.txt
    
    triMail(fileMailBrut,fileMailEnvoye,fileMailAEnvoye)
    
    #Puis ensuite on envoie les mails contenue dans la liste des mails à envoyé
    envoieMail(fileMailAEnvoye)
    
    
main()