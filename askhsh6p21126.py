import random

#ΠΟΝΤΟΙ ΜΑΥΡΟΥ 
black_p=0
#ΠΟΝΤΟΙ ΛΕΥΚΟΥ
white_p =0
for q in range(100):
    #ΔΗΜΙΟΥΡΓΙΑ ΤΗΣ ΣΚΑΚΙΕΡΑΣ ΚΑΙ ΤΟΠΟΘΕΤΗΣΗ ΠΙΟΝΙΩΝ
    th=["0"]*(61)
    th+=["Queen"]
    th+=["Bishop"]
    th+=["Rook"]
    #ΜΕΣΩ ΤΗΣ RANDOM ΑΛΛΑΖΟΥΜΕ ΤΙΣ ΘΕΣΕΙΣ ΤΩΝ ΠΙΟΝΙΩΝ
    random.shuffle(th)
    board=[]
    for i in range(8):
        board+=[th[8*i:8*i+8]]

    for i in range(8):
        for j in range(8):
            #ΒΡΙΣΚΩ ΤΗΝ ΒΑΣΙΛΙΣΣΑ
          if board[i][j]=="Queen":
            for k in range(8):
                #ΒΡΙΣΚΩ ΤΟΝ ΠΥΡΓΟ ΚΑΙ ΑΝ ΕΙΝΑΙ ΚΑΘΕΤΑ Η ΟΡΙΖΟΝΤΙΑ
                if board[k][j]=="Rook":
                    black_p+=1
                    white_p+=1
                if board[k][i]=="Rook":
                    black_p+=1
                    white_p+=1
                    #ΒΡΙΣΚΩ ΤΟΝ ΑΞΙΩΜΑΤΙΚΟ ΚΑΙ ΑΝ ΕΙΝΑΙ ΚΑΘΕΤΑ Η ΟΡΙΖΟΝΤΙΑ
                if board[k][j]=="Bishop":
                    black_p+=1
                if board[k][i]=="Bishop":
                    black_p+=1
                    #ΒΡΙΣΚΩ ΤΟΝ ΑΞΙΩΜΑΤΙΚΟ ΚΑΙ ΑΝ ΕΙΝΑΙ ΔΙΑΓΩΝΙΑ
                if k+j-i>=0 and k+j-i<8 and board[k][k+j-i]=="Bishop":
                    black_p+=1
                    white_p+=1
                if -k+j+i>=0 and -k+j+i<8 and board[k][-k+i+j]=="Bishop":
                    black_p+=1
                    white_p+=1
                    #ΒΡΙΣΚΩ ΤΟΝ ΠΥΡΓΟ ΚΑΙ ΑΝ ΕΙΝΑΙ ΔΙΑΓΩΝΙΑ
                if k+j-i>=0 and k+j-i<8 and board[k][k+j-i]=="Rook":
                    black_p+=1
                if -k+j+i>=0 and -k+j+i<8 and board[k][-k+i+j]=="Rook":
                    black_p+=1
             

                
print ("ΤΑ ΜΑΥΡΑ ΚΕΡΔΙΣΑΝ " ,black_p," ΦΟΡΕΣ")
print ("ΤΑ ΑΣΠΡΑ ΚΕΡΔΙΣΑΝ " ,white_p," ΦΟΡΕΣ")