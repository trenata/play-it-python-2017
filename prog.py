import wiringpi
import time
from time import sleep

wiringpi.wiringPiSetup()
wiringpi.mcp23017Setup(65, 0x20)
wiringpi.mcp23017Setup(81, 0x24)
wiringpi.mcp23017Setup(97, 0x26)

for i in range(65,109):
        wiringpi.pinMode(i,1)

first = True

def general(be):
        mat = [[0 for i in range(6)] for j in range(6)]
        if be.upper() == "EM":
                mat[3][1] = 1
                mat[4][1] = 1
        elif be.upper() == "AM":
                mat[1][0] = 1
                mat[2][1] = 1
                mat[3][1] = 1
        elif be.upper() == "DM":
                mat[0][0] = 1
                mat[2][1] = 1
                mat[1][2] = 1
        elif be.upper() =="CM":
                mat[0][2] = 1
                mat[4][2] = 1
                mat[1][3] = 1
                mat[2][4] = 1
                mat[3][4] = 1
        elif be.upper() =="GM":
                mat[0][2] = 1
                mat[1][2] = 1
                mat[2][2] = 1
                mat[5][2] = 1
                mat[3][5] = 1
                mat[4][5] = 1
        elif be.upper() =="FM":
                mat[0][0] = 1
                mat[1][0] = 1
                mat[2][0] = 1
                mat[5][0] = 1
                mat[3][2] = 1
                mat[4][2] = 1
        elif be.upper() =="BM":
                mat[4][1] = 1
                mat[0][1] = 1
                mat[1][2] = 1
                mat[2][3] = 1
                mat[3][3] = 1
        elif be.upper() == "BBM":
                mat[4][0] = 1
                mat[0][0] = 1
                mat[3][2] = 1
                mat[2][2] = 1
                mat[1][1] = 1
        elif be.upper() == "E":
                mat[2][0] = 1
                mat[4][1] = 1
                mat[3][1] = 1
        elif be.upper() == "A":
                mat[1][1] = 1
                mat[2][1] = 1
                mat[3][1] = 1
        elif be.upper() == "D":
                mat[2][1] = 1
                mat[0][1] = 1
                mat[1][2] = 1
        elif be.upper() == "C":
                mat[1][0] = 1
                mat[3][1] = 1
                mat[4][2] = 1
        elif be.upper() == "G":
                mat[4][1] = 1
                #mat[5][2] = 1
                mat[0][2] = 1
        elif be.upper() =="F":
                mat[0][0] = 1
                mat[1][0] = 1
                mat[2][0] = 1
                mat[5][0] = 1
                mat[2][1] = 1
                mat[3][2] = 1
                mat[4][2] = 1
        elif be.upper() =="B":
                mat[4][1] = 1
                mat[0][1] = 1
                mat[1][3] = 1
                mat[2][3] = 1
                mat[3][3] = 1
        elif be.upper() == "BB":
                mat[4][0] = 1
                mat[0][0] = 1
                mat[3][2] = 1
                mat[2][2] = 1
                mat[1][2] = 1
        elif be.upper() == "E7":
                mat[2][0] = 1
                mat[4][1] = 1
        elif be.upper() == "EM7":
                mat[4][1] = 1
        elif be.upper() == "A7":
                mat[3][1] = 1
                mat[1][1] = 1
        elif be.upper() == "AM7":
                mat[1][0] = 1
                mat[3][1] = 1
        elif be.upper() == "D7":
                mat[1][0] = 1
                mat[2][1] = 1
                mat[0][1] = 1
        elif be.upper() == "DM7":
                mat[0][0] = 1
                mat[1][0] = 1
                mat[2][1] = 1
        elif be.upper() == "C7":
                mat[1][0] = 1
                mat[3][1] = 1
                mat[4][2] = 1
                mat[2][2] = 1
        elif be.upper() == "CM7":
                mat[4][2] = 1
                mat[3][2] = 1
                mat[2][2] = 1
                mat[1][2] = 1
                mat[0][2] = 1
                mat[1][3] = 1
                mat[3][4] = 1
        elif be.upper() == "G7":
                mat[0][0] = 1
                mat[4][1] = 1
                mat[5][2] = 1
        elif be.upper() == "C6":
                mat[1][0] = 1
                mat[2][1] = 1
                mat[3][1] = 1
                mat[4][2] = 1
        elif be.upper() == "CMAJ7":
                mat[3][1] = 1
                mat[4][2] = 1
        elif be.upper() == "CMAJ9":
                mat[3][1] = 1
                mat[4][2] = 1
                mat[1][2] = 1
                mat[2][3] = 1
        elif be.upper() == "CSUS4":
                mat[1][0] = 1
                mat[4][2] = 1
                mat[3][2] = 1
        elif be.upper() == "CADD9":
                mat[3][1] = 1
                mat[4][2] = 1
                mat[1][2] = 1
        elif be.upper() == "DMAJ7":
                mat[2][1] = 1
                mat[1][1] = 1
                mat[0][1] = 1
        elif be.upper() == "DSUS4":
                mat[2][1] = 1
                mat[1][2] = 1
                mat[0][2] = 1
        elif be.upper() == "DADD9":
                mat[3][3] = 1
                mat[4][4] = 1
                mat[1][4] = 1
                mat[0][4] = 1
        elif be.upper() == "GMAJ7":
                mat[5][2] = 1
                mat[1][2] = 1
                mat[3][3] = 1
                mat[2][3] = 1
        elif be.upper() == "GSUS4":
                mat[5][2] = 1
                mat[1][2] = 1
                mat[0][2] = 1
                mat[4][4] = 1
                mat[3][4] = 1
                mat[2][4] = 1
        elif be.upper() == "GADD9":
                mat[4][1] = 1
                mat[2][1] = 1
                mat[5][2] = 1
                mat[0][2] = 1
        elif be.upper() == "FSUS4":
                mat[5][0] = 1
                mat[0][0] = 1
                mat[2][1] = 1
                mat[3][2] = 1
                mat[1][2] = 1
        elif be.upper() == "FMAJ7":
                mat[1][0] = 1
                mat[2][1] = 1
                mat[3][2] = 1
        elif be.upper() == "FADD9":
                mat[1][0] = 1
                mat[2][1] = 1
                mat[3][2] = 1
                mat[0][2] = 1
        elif be.upper() == "BMAJ7":
                mat[4][1] = 1
                mat[0][1] = 1
                mat[2][2] = 1
                mat[3][3] = 1
                mat[1][3] = 1
        elif be.upper() == "BSUS4":
                mat[4][1] = 1
                mat[0][1] = 1
                mat[3][3] = 1
                mat[2][3] = 1
                mat[1][4] = 1
        elif be.upper() == "BADD9":
                mat[3][0] = 1
                mat[4][1] = 1
                mat[1][1] = 1
                mat[0][1] = 1
        elif be.upper() == "B7":
                mat[3][0] = 1
                mat[4][1] = 1
                mat[2][1] = 1
                mat[0][1] = 1
        elif be.upper() == "EMAJ7":
                mat[2][0] = 1
                mat[4][1] = 1
                mat[3][1] = 1
                mat[1][3] = 1
        elif be.upper() =="ESUS4":
                mat[4][1] = 1
                mat[3][1] = 1
                mat[2][1] = 1
        elif be.upper() =="EADD9":
                mat[2][0] = 1
                mat[4][1] = 1
                mat[3][1] = 1
                mat[0][1] = 1
        elif be.upper() =="AMAJ7":
                mat[3][1] = 1
                mat[2][1] = 1
                mat[1][1] = 1
                mat[0][3] = 1
        elif be.upper() =="ASUS4":
                mat[3][1] = 1
                mat[1][1] = 1
                mat[2][3] = 1
        elif be.upper() =="AADD9":
                mat[3][1] = 1
                mat[1][1] = 1
                mat[2][3] = 1
        return mat

def szita (f):
        szoveg = f.read().split("\n")

        x=[]
        i=0
        t=[]

        while i < len(szoveg):
                sor=szoveg[i]
                for j in range(len(sor)):
                        if sor[j]!=' ':
                                x.append(sor[j])
                i=i+2

        x=''.join(x)
        import re
        t = [i for i in re.findall('[A-Z][a-z]*', x)]
        return t

def dalok(x):
        ido = {
                "Egyszerű dal": 1,
                "Boulevard of Broken Dreams": 1.75,
                "Jó nekem": 2,
                "Pioneer":1.6 ,
                "Heavy": 2.5,
                "67-es út": 2,
                "Monster": 1.75,
                "Believer": 1.72,
                "Let It Be": 1.79,
                "Can't Help Falling in Love": 1.77,
                "Mad World": 2.44,
                "Here Comes the Sun": 2,
        }[x]
        dal = {
                "Egyszerű dal": "EgyszeruDal",
                "Boulevard of Broken Dreams": "BoulevardOfBrokenDreams",
                "Jó nekem": "JoNekem",
                "Pioneer": "Pioneer",
                "Heavy": "Heavy",
                "67-es út": "67esUt",
                "Monster": "Monster",
                "Believer": "Believer",
                "Let It Be": "LetItBe",
                "Can't Help Falling in Love": "CantHelpFallingInLove",
                "Mad World": "MadWorld",
                "Here Comes the Sun": "HereComesTheSun",
        }[x]
        print(ido)
        dal=dal+".txt"
        f = open(dal,'r')
        t=[]
        t=szita(f)

        for i in t:
                mat=general(i)
                for row in range(6):
                        for col in range(6):
                                if mat[row][col]==1:
                                        if(row == 4):
                                                if(col == 1):
                                                       wiringpi.digitalWrite(101, 1)
                                        wiringpi.digitalWrite(6*row+col+65, 1)
                time.sleep(ido)

                for j in range(65, 129):
                        wiringpi.digitalWrite(j, 0)

def akkordok(x):
        matrix = general(x)
        for i in matrix:
                print(i)

def gyujtAkkord(akkord):
        kikapcsolLedek()
        akkord = general(akkord)
        for row in range(6):
                for col in range(6):
                        if akkord[row][col] == 1:
                                if(row == 4):
                                        if(col == 1):
                                                wiringpi.digitalWrite(101, 1)
                                wiringpi.digitalWrite(6*row+col+65, 1)

def kikapcsolLedek():
        for i in range(6):
                for j in range(6):
                        wiringpi.digitalWrite(6 * i + j + 65, 0)
                        print(6*i+j+65)
        wiringpi.digitalWrite(101, 0)

def gyujtAkPengetes(akkord):
        print(akkord)
        def kezdoertek(akkord):
                if akkord == 'em' or akkord == "e" or akkord == "a" or akkord == "c":
                        return 104
                elif akkord == "am" or akkord == "d" or akkord == "dm":
                        return 105
                else:
                        return 103

        def penget():
                k=kezdoertek(akkord)
                for i in range(k,109):
                        print(i)
                        wiringpi.digitalWrite(i, 1)
                        sleep(0.5)
                        wiringpi.digitalWrite(i,0)
        penget()

def gyujtPengFajta(x):
        def le():
                for i in range(103,109):
                        wiringpi.digitalWrite(i,1)
                        sleep(0.2)
                        wiringpi.digitalWrite(i,0)
                        print(i)
        def le_fele():
                for i in range(103,106):
                        wiringpi.digitalWrite(i,1)
                        sleep(0.2)
                        wiringpi.digitalWrite(i,0)
                        print(i)
        def fel():
                for i in range(109,103,-1):
                        wiringpi.digitalWrite(i,1)
                        sleep(0.2)
                        wiringpi.digitalWrite(i,0)
                        print(i)
        def peng(x):
                if x == "1":
                        for i in  range(1,3):
                                le()
                                le()
                                fel()
                                fel()
                                sleep(1)
                elif x == "2":
                        for i in range(1,3):
                                le()
                                sleep(1)
                                le()
                                le()
                                fel()
                                sleep(1)
                elif x == "3":
                        for i in range(1,3):
                                le()
                                le_fele()
                                le()
                                fel()
                                le()
                                sleep(1)
                elif x == "4":
                        for i in range(1,3):
                                le()
                                le_fele()
                                le()
                                fel()
                                le()
                                fel()
                                le()
                                sleep(1)
                elif x == "5":
                        for i in range(1,3):
                                le()
                                fel()
                                le()
                                fel()
                                sleep(1)
                else:
                        for i in range(1,3):
                                le()
                                le()
                                fel()
                                fel()
                                sleep(1)

        peng(x)
        
def gyujtAkkordFelbont1(akkord):
        def felbontas1():
                for i in range(109,105,-1):
                        wiringpi.digitalWrite(i,1)
                        print(i)
                        sleep(0.5)
                        wiringpi.digitalWrite(i,0)
        def elso(x):
                if x == "em" or x == "e" or x == "a" or x == "am" or x == "c":
                        for i in range(0,3):
                                wiringpi.digitalWrite(104,1)
                                wiringpi.digitalWrite(108,1)
                                sleep(0.5)
                                wiringpi.digitalWrite(104,0)
                                wiringpi.digitalWrite(108,0)
                                felbontas1()
                                sleep(0.5)
                elif x == "d" or x == "dm":
                        for i in range(0,3):
                                wiringpi.digitalWrite(105,1)
                                wiringpi.digitalWrite(108,1)
                                sleep(0.5)
                                wiringpi.digitalWrite(105,0)
                                wiringpi.digitalWrite(108,0)
                                felbontas1()
                                sleep(0.5)
                else:
                        for i in range(0,3):
                                wiringpi.digitalWrite(103,1)
                                wiringpi.digitalWrite(108,1)
                                sleep(0.5)
                                wiringpi.digitalWrite(103,0)
                                wiringpi.digitalWrite(108,0)
                                felbontas1()
                                sleep(0.5)
        elso(akkord)

def gyujtAkkordFelbont2(akkord):
        def felbontas2():
                for i in range(105,109):
                        wiringpi.digitalWrite(i,1)
                        print(i)
                        sleep(0.5)
                        wiringpi.digitalWrite(i,0)
                for i in range(109,105,-1):
                        wiringpi.digitalWrite(i,1)
                        print(i)
                        sleep(0.5)
                        wiringpi.digitalWrite(i,0)
        def masodik(x):
                if x == "em" or x == "e" or x == "a" or x == "am" or x == "c":
                        for i in range(0,3):
                                wiringpi.digitalWrite(104,1)
                                wiringpi.digitalWrite(104,0)
                                felbontas2()
                                sleep(0.5)
                elif x == "d" or x == "dm":
                        for i in range(0,3):
                                wiringpi.digitalWrite(105,1)
                                wiringpi.digitalWrite(105,0)
                                felbontas2()
                                sleep(0.5)
                else:
                        for i in range(0,3):
                                wiringpi.digitalWrite(103,1)
                                wiringpi.digitalWrite(103,0)
                                felbontas2()
                                sleep(0.5)
        masodik(akkord)

def gyujtAkkordFelbont3(akkord):
        def felbontas3():
                    wiringpi.digitalWrite(105,1)
                    print(105)
                    sleep(0.5)
                    wiringpi.digitalWrite(105,0)
                    wiringpi.digitalWrite(108,1)
                    print(108)
                    sleep(0.5)
                    wiringpi.digitalWrite(108,0)
                    wiringpi.digitalWrite(107,1)
                    print(107)
                    sleep(0.5)
                    wiringpi.digitalWrite(107,0)

        def harmadik(x):
            if x == "em" or x == "e" or x == "a" or x == "am" or x == "c":
                    for i in range(0,3):
                            wiringpi.digitalWrite(104,1)
                            wiringpi.digitalWrite(104,0)
                            felbontas3()
                            sleep(0.5)

            elif x == "d" or x == "dm":
                    for i in range(0,3):
                            wiringpi.digitalWrite(105,1)
                            wiringpi.digitalWrite(105,0)
                            felbontas3()
                            sleep(0.5)
            else:
                    for i in range(0,3):
                            wiringpi.digitalWrite(103,1)
                            wiringpi.digitalWrite(103,0)
                            felbontas3()
                            sleep(0.5)
        harmadik(akkord)

