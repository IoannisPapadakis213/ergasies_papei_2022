import random

def check(d):
  global mikroi
  global mesaioi
  global megaloi
  if d==1 and mikroi > 0:
    mikroi-=1
    return True
  elif d==2 and mesaioi > 0:
    mesaioi-=1
    return True
  elif d==3 and megaloi > 0:
    megaloi-=1
    return True
  else:
    return False
#ΟΡΙΖΟΥΜΕ ΤΙΣ ΘΕΣΕΙΣ
theseis=["th1","th2","th3","th4","th5","th6","th7","th8","th9"]
# οριζουμε τα μεγέθη των δακτύλιων
daktylioi=[1,2,3]
sum_moves=0

for i in range(100):
  #ΜΗΔΕΝΙΖΟΥΜΕ ΤΙΣ ΘΕΣΕΙΣ ΓΙΑ ΚΑΘΕ ΠΑΙΧΝΙΔΙ
  th1=th2=th3=th4=th5=th6=th7=th8=th9=0
  moves=0
  gamerunning = False
  mikroi=9
  mesaioi=9
  megaloi=9
  while gamerunning != True:
    spot = random.choice(theseis)
    ring= random.choice(daktylioi)
    if spot=="th1":
      if th1==0 and check(ring):
          th1=ring
          moves+=1
      elif th1==1 and check(ring) and ring!=1:
        th1=ring
        moves+=1
      elif th1==2 and check(ring) and ring!=2:
        th1=ring
        moves+=1
      elif th1==3 and check(ring) and ring!=3:
        th1=ring
        moves+=1

    elif spot=="th2":
      if th2==0 and check(ring):
          th2=ring
          moves+=1
      elif th2==1 and check(ring) and ring!=1:
        th2=ring
        moves+=1
      elif th2==2 and check(ring) and ring!=2:
        th2=ring
        moves+=1
      elif th2==3 and check(ring) and ring!=3:
        th2=ring
        moves+=1
    

    elif spot=="th3":
      if th3==0 and check(ring):
          th3=ring
          moves+=1
      elif th3==1 and check(ring) and ring!=1:
        th3=ring
        moves+=1
      elif th3==2 and check(ring) and ring!=2:
        th3=ring
        moves+=1
      elif th3==3 and check(ring) and ring!=3:
          th3=ring
          moves+=1

    elif spot=="th4":
      if th4==0 and check(ring):
          th4=ring
          moves+=1
      elif th4==1 and check(ring) and ring!=1:
        th4=ring
        moves+=1
      elif th4==2 and check(ring) and ring!=2:
        th4=ring
        moves+=1
      elif th4==3 and check(ring)and ring!=3:
          th4=ring
          moves+=1

    elif spot=="th5":
      if th5==0 and check(ring):
          th5=ring
          moves+=1
      elif th5==1 and check(ring) and ring!=1:
        th5=ring
        moves+=1
      elif th5==2 and check(ring) and ring!=2:
        th5=ring
        moves+=1
      elif th5==3 and check(ring) and ring!=3:
        th5=ring
        moves+=1

    elif spot=="th6":
      if th6==0 and check(ring):
          th6=ring
          moves+=1
      elif th6==1 and check(ring) and ring!=1:
        th6=ring
        moves+=1
      elif th6==2 and check(ring) and ring!=2:
        th6=ring
        moves+=1
      elif th6==3 and check(ring) and ring!=3:
        th6=ring
        moves+=1

    elif spot=="th7":
      if th7==0 and check(ring):
          th7=ring
          moves+=1
      elif th7==1 and check(ring) and ring!=1:
        th7=ring
        moves+=1
      elif th7==2 and check(ring) and ring!=2:
        th7=ring
        moves+=1
      elif th7==3 and check(ring) and ring!=3:
        th7=ring
        moves+=1

    elif spot=="th8":
      if th8==0 and check(ring):
          th8=ring
          moves+=1
      elif th8==1 and check(ring) and ring!=1:
        th8=ring
        moves+=1
      elif th8==2 and check(ring) and ring!=2:
        th8=ring
        moves+=1
      elif th8==3 and check(ring) and ring!=3:
        th8=ring
        moves+=1

    elif spot=="th9":
      if th9==0 and check(ring):
          th9=ring
          moves+=1
      elif th9==1 and check(ring) and ring!=1:
        th9=ring
        moves+=1
      elif th9==2 and check(ring) and ring!=2:
        th9=ring
        moves+=1
      elif th9==3 and check(ring) and ring!=3:
        th9=ring
        moves+=1

    
#--------ΕΛΕΓΧΟΙ-------
#ΠΡΩΤΗ ΣΕΙΡΑ ΟΡΙΖΟΝΤΙΑ
    if th1!=0 and th2!=0 and th3!=0:
      if th1==1 and th2==1 and th3==1:
        gamerunning = True
      elif th1==2 and th2==2 and th3==2:
        gamerunning = True
      elif th1==3 and th2==3 and th3==3:
        gamerunning = True
      elif th1==1 and th2==2 and th3==3:
        gamerunning = True
      elif th1==3 and th2==2 and th3==1:
        gamerunning = True
#ΔΕΥΤΕΡΗ ΣΕΙΡΑ ΟΡΙΖΟΝΤΙΑ
    if th4!=0 and th5!=0 and th6!=0:
      if th4==1 and th5==1 and th6==1:
        gamerunning = True
      elif th4==2 and th5==2 and th6==2:
        gamerunning = True
      elif th4==3 and th5==3 and th6==3:
        gamerunning = True
      elif th4==1 and th5==2 and th6==3:
        gamerunning = True
      elif th4==3 and th5==2 and th6==1:
        gamerunning = True
#ΤΡΙΤΗ ΣΕΙΡΑ ΟΡΙΖΟΝΤΙΑ
    if th7!=0 and th8!=0 and th9!=0:
      if th7==1 and th8==1 and th9==1:
        gamerunning = True
      elif th7==2 and th8==2 and th9==2:
        gamerunning = True
      elif th7==3 and th8==3 and th9==3:
        gamerunning = True
      elif th7==1 and th8==2 and th9==3:
        gamerunning = True
      elif th7==3 and th8==2 and th9==1:
        gamerunning = True
#ΠΡΩΤΗ ΣΕΙΡΑ ΚΑΘΕΤΑ
    if th1!=0 and th4!=0 and th7!=0:
      if th1==1 and th4==1 and th7==1:
        gamerunning = True
      elif th1==2 and th4==2 and th7==2:
        gamerunning = True
      elif th1==3 and th4==3 and th7==3:
        gamerunning = True
      elif th1==1 and th4==2 and th7==3:
        gamerunning = True
      elif th1==3 and th4==2 and th7==1:
        gamerunning = True
#ΔΕΥΤΕΡΗ ΣΕΙΡΑ ΚΑΘΕΤΑ
    if th2!=0 and th5!=0 and th8!=0:
      if th2==1 and th5==1 and th8==1:
        gamerunning = True
      elif th2==2 and th5==2 and th8==2:
        gamerunning = True
      elif th2==3 and th5==3 and th8==3:
        gamerunning = True
      elif th2==1 and th5==2 and th8==3:
        gamerunning = True
      elif th2==3 and th5==2 and th8==1:
        gamerunning = True
#ΤΡΙΤΗ ΣΕΙΡΑ ΚΑΘΕΤΑ 
    if th3!=0 and th6!=0 and th9!=0:
      if th3==1 and th6==1 and th9==1:
        gamerunning = True
      elif th3==2 and th6==2 and th9==2:
        gamerunning = True
      elif th3==3 and th6==3 and th9==3:
        gamerunning = True
      elif th3==1 and th6==2 and th9==3:
        gamerunning = True
      elif th3==3 and th6==2 and th9==1:
        gamerunning = True
#ΠΡΩΤΗ ΣΕΙΡΑ ΔΙΑΓΩΝΙΑ
    if th1!=0 and th5!=0 and th9!=0:
      if th1==1 and th5==1 and th9==1:
        gamerunning = True
      elif th1==2 and th5==2 and th9==2:
        gamerunning = True
      elif th1==3 and th5==3 and th9==3:
        gamerunning = True
      elif th1==1 and th5==2 and th9==3:
        gamerunning = True
      elif th1==3 and th5==2 and th9==1:
        gamerunning = True
#ΔΕΥΤΕΡΗ ΣΕΙΡΑ ΔΙΑΓΩΝΙΑ
    if th3!=0 and th5!=0 and th7!=0:
      if th3==1 and th5==1 and th7==1:
        gamerunning = True
      elif th3==2 and th5==2 and th7==2:
        gamerunning = True
      elif th3==3 and th5==3 and th7==3:
        gamerunning = True
      elif th3==1 and th5==2 and th7==3:
        gamerunning = True
      elif th3==3 and th5==2 and th7==1:
        gamerunning = True
#ΕλΕΓΧΟΣ ΔΙΑΘΕΣΙΜΟΤΗΤΑΣ ΔΑΚΤΥΛΙΩΝ
    if mikroi==0 and mesaioi==0 and megaloi==0:
      gamerunning = True
  sum_moves+=moves
print("ΜΕΣΟΣ ΟΡΟΣ ΚΙΝΗΣΕΩΝ:",sum_moves/100)