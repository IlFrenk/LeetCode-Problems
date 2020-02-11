
def romanToInt(s: str) -> int:

    numDict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    num=0 #valore per il return
    firsttime=0
    n=0 #contatore
    sottr=0 #var temp per storare la sottrazione tra due caratteri nella stringa (nel caso in cui vada sommata la sottrerenza tra di loro anziché loro due separatamente: caso di IV, IX, CD)
    if any(char not in numDict for char in s): #controlla caratteri non validi nella stringa
        print("La stringa contiene un carattere non valido!")
        return 0
    else:
        for i in s:
            if sottr != 0 and sottr < numDict[i]: #quando effettuo una differenza tra due valori di caratteri modifico sottr. Se successivamente trovo un carattere che ha valore maggiore di una sottrazione effettuata precedentemente, il numero non è valido!
                print("numero non valido!")
                return 0
            else:
                if firsttime: #chiede se sto scorrendo il primo carattere della stringa, perché poi accedo n-1
                    if s[n] == s[n-1]: 
                        num += numDict[i] #se il carattere che sto scorrendo è uguale al precedente, sommalo
                    elif n != len(s)-1 and numDict[i]<numDict[s[n+1]]: #se il carattere che sto scorrendo (che non sia l'ultimo della stringa) ha valore minore del successivo, passa oltre. Perché poi lo sommerò nel ramo elif successivo (quando confronterò il successivo con lui)
                        n+=1
                        continue
                    elif numDict[i]>numDict[s[n-1]]:
                        sottr = numDict[i]-numDict[s[n-1]]
                        num += sottr #se il carattere che sto scorrendo ha valore maggiore del precedente (casi tipo: IV, IX, CD, ecc), somma la loro sottrazione (IV somma 4, IX somma 9, CD somma 400)
                    elif numDict[i]<numDict[s[n-1]]:
                        num += numDict[i] #caso base: se il carattere che sto scorrendo ha valore minore del precedente, sommalo
                else: #nel caso quindi stia scorrendo il primo carattere
                    firsttime=1
                    if n != len(s)-1 and numDict[i]<numDict[s[n+1]]: #se il primo carattere è da considerare in coppia con il successivo (tipo IV, IX, CD), passa oltre, dato che poi sommerò la loro sottrerenza nel secondo elif soprastante
                        n+=1
                        continue
                    else:
                        num += numDict[i] #altrimenti sommalo directly
                n+=1
        return num

s="MCMXC"

#numeri invalidi che attualmente exploitano l'algoritmo:
    #CMXXC: il ripetersi di un carattere prima in sottrazione e poi accanto a caratteri con valore minore.
    #IIII: massimo 3 caratteri uguali in fila.
    #MXM è peso. MCMXC è 1990, ma MXM lo legge come se fosse lui. XM, la differenza si può fare solo con numeri di livelli adiacenti (XC, CM, non XM). MIM invece?

print(romanToInt(s))