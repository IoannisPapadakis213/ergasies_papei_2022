import random

print("Συμφωνα με το αρχείο card_game_24_11_2021")
wins1=wins2=draws=0
for i in range(100):
    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    player1=[]
    sum1=0
    while sum1<16:
        sum1=0
        player1.append(xartia.pop())
        # print (player1)
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
        #print(sum1)
    if sum1>21:
        #print("P2 wins!")
        wins2+=1
    else:

        #print("P2 joins the game") #let me add one more player
        player2=[]
        sum2=0
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            # print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
            #print(sum2)
        if sum2>21:
            sum2=0
        if sum1>sum2:
            #print("P1 wins!")
            wins1+=1
        elif sum2>sum1:
            #print("P2 wins!")
            wins2+=1
        else:
            #print("draw!")
            draws+=1

print("ΠΡΙΝ ΤΟ ΠΟΙΡΑΓΜΑ ΤΩΝ ΧΑΡΤΙΩΝ")
print("Ο ΠΡΩΤΟΣ ΠΑΙΚΤΗΣ ΕΧΕΙ ",wins1,"ΝΙΚΕΣ")
print("Ο ΔΕΥΤΕΡΟΣ ΠΑΙΚΤΗΣ ΕΧΕΙ ",wins2, "ΝΙΚΕΣ")
print("ΟΙ ΙΣΟΠΑΛΙΕΣ ΕΙΝΑΙ",draws)


print("---------------------------------------------------------")
print("META TO ΠΟΙΡΑΓΜΑ ΤΩΝ ΧΑΡΤΊΩΝ:")

wins1=wins2=draws=0
for i in range(100):
    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    player1=[]
    sum1=0
    found=True
    while sum1<16:
        sum1=0
        #οσο η συνθηκη ειναι αληθης
        if found:  
            num = len(xartia)
            #Η reversed()συνάρτηση 
            # επιστρέφει έναν επαναλήπτη που έχει πρόσβαση στη δεδομένη ακολουθία με την αντίστροφη σειρά.
            for card in reversed(xartia):
                num = num -1
                #εαν η πρωτη καρτα ειναι το 10 η μια απο τις φιγουρες προσθεσε την στα χαρτια του παικτη 1 και σταματησε
                if card[0]==10 or card[0]in figures:
                    player1.append(xartia.pop(num))
                    found=False
                    break
        else:
            player1.append(xartia.pop())
        # print (player1)
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
        #print(sum1)
    if sum1>21:
        #print("P2 wins!")
        wins2+=1
    else:
        #print("P2 joins the game") #let me add one more player
        player2=[]
        sum2=0
        found=True
        while sum2<16:
            sum2=0
            if found: #if its the first card ,search in the list xartia backwards until you find not10 or notJ or notQ or notK ,so that is the starting card
                num = len(xartia)
                for card in reversed(xartia):
                    num = num -1
                    #αυτη την φορα θελουμε το αντιθετο απο το προηγουμενο(εαν η πρωτη καρτα
                    #  δεν ειναι το 10 η φιγουρα να το προσθετει στον παικτη 2)
                    if not(card[0]==10 or card[0] in figures):
                        player2.append(xartia.pop(num))
                        found=False
                        break
            else:
                player2.append(xartia.pop())
            # print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
            #print(sum2)
        if sum2>21:
            sum2=0
        if sum1>sum2:
            #print("P1 wins!")
            wins1+=1
        elif sum2>sum1:
            #print("P2 wins!")
            wins2+=1
        else:
            #print("draw!")
            draws+=1

print("O ΠΡΩΤΟΣ ΠΑΙΚΤΗΣ ΕΧΕΙ ",wins1 ,"ΝΙΚΕΣ")
print("Ο ΔΕΥΤΕΡΟΣ ΠΑΙΚΤΗΣ ΕΧΕΙ",wins2,"ΝΙΚΕΣ")
print("ΟΙ ΙΣΟΠΑΛΙΕΣ ΕΙΝΑΙ ",draws)