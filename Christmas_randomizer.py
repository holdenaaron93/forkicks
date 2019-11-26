import smtplib as ml
import random

def notify(username,password,receive):

    #List of everyone's email address, emails must be oldest to youngest (exluding nicoles this year)
    #to = ['holden.les@gmail.com','sterlingholden@gmail.com','holden.deric@gmail.com',
          #'harrisonholden@gmail.com','hooley.lauren@gmail.com','holden.amanda.m@gmail.com',
          #'holdenaaron93@gmail.com','malieaholden@gmail.com']
    to = ['holdenaaron93@gmail.com']



#sends an email to each person with the they drew for christms
    for i in range(len(to)):
        body1 = 'Merry Christmas everyone! \n\nFor christmas this year you have '
        body2 = ' \nIf you drew the same person as last year, let me know and we can do a redraw.\n\nThanks,\nRobo-Elf'
        body = body1 + receive[i] + body2

        server = ml.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(username,password)
        server.sendmail(username,to[i],body)
        server.quit()
    print('Emails Sent')



#Takes the list of names and shuffles them. It returns the shuffled list
def randomize():

    giver = ['Les & Terry!', 'Sterling & Mia!', 'Deric & Korin!', 'Harrison & Natalie!', 'Dirk & Lauren!',
             'Derick & Amanda!', 'Aaron and Melanie!', 'Maliea! (aka The Lone wolf)']

    receive = giver[:]
    test = True


    #makes sure no one has their name
    while test:

        random.shuffle(receive)

        if receive[0] == giver[0]:
            test = True
        elif giver[1] == receive[1]:
            test = True
        elif giver[2] == receive[2]:
            test = True
        elif giver[3] == receive[3]:
            test = True
        elif giver[4] == receive[4]:
            test = True
        elif giver[5] == receive[5]:
            test = True
        elif giver[6] == receive[6]:
            test = True
        elif giver[7] == receive[7]:
            test = True
        else:
            test = False

    return (receive)




#main function
def main():
    username = input('Gmail Username')
    password = input('Password')
    receive = randomize()
    notify(username,password,receive)


main()


