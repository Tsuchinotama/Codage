from operator import itemgetter
from collections import defaultdict
import itertools

# fonction codant un message 

def codage(a, b, message):
    L=list(message)
    message_code=[]
    for l in L:
        message_code.append(chr(((a*(ord(l)-97)+b)%26)+97))
    return message_code
    
Correspondance_decodage={1 : 1, 3 : 9, 5 : 21,7 : 15, 9 : 3, 11 : 19, 15 : 7, 17 : 23, 19 : 11, 21 : 5, 23 : 17, 25 : 25}
    
# fonction decodant un message en partant des coeffs affines de codage
    
def decodage(a, b, message_code):
    L=list(message_code)
    message=[]
    for l in L:
        a_dec=Correspondance_decodage[a]
        message.append(chr((((a_dec*((ord(l)-97)-b))%26)+97)))
    return message

# fonction renvoyant les lettres du message codé et le nombre de fois qu'elles apparaissent,en regroupant les lettres apparaissant le même nombre de fois

def compte_lettres(message_code):
    L=list(message_code)
    freq=dict()
    for i in range(97,123):
        freq[chr(i)] = 0
    for lettre in L:
        freq[lettre] = freq[lettre]+1
    Lt=sorted(freq.items(), key=itemgetter(1), reverse=True)
    Llt=[[Lt[0]]]
    i=1
    j=0
    while i<26:
        if Lt[i][1]==Lt[i-1][1]:
            Llt[j].append(Lt[i])
        else:
            Llt.append([Lt[i]])
            j=j+1
        i=i+1
    return Llt
      
# fonction renvoyant les décalages entre la(les) lettre(s) la et la(les) lettre(s) la(les) plus fréquente(s) en francais (plusieures si certaines lettres apparaissent un même nombre de fois dans le message codé)

lettres_francais=['e','a','i','s','n','r','t','o','l','u','d','c','m','p','g','b','v','h','f','q','y','x','j','k','w','z']

def decalage_lettre(message_code):
    L=compte_lettres(message_code)
    DL=[]
    i=0
    j=0
    while i<len(L) and j<26:
        if len(L[i])==1:
            DL.append([[lettres_francais[i]],[L[i][0][0]]])
            i=i+1
            j=j+1
        else:
            La=[]
            Lc=[]
            for k in range(len(L[i])):
                La.append(lettres_francais[k+j])
                Lc.append(L[i][k][0])
            j=j+len(L[i])
            DL.append([La,Lc])
            i=i+1
    return DL

Coeffs_a=[1,3,5,7,9,11,15,17,19,21,23,25]

def permutation_lettres(L):
    return [list(elem) for elem in list(itertools.permutations(L))]
        
def Faux_codage():
    decalage_nul=[]
    for i in range(13):
        decalage_nul.append([[chr(2*i+97),chr(2*i+98)],[chr(2*i+97),chr(2*i+98)]])
    return decalage_nul

def coeffs_affine():
    Coeffs_possibles=[]
    for a in Coeffs_a:
        for b in range(26):
            for lettre_et_codage in Faux_codage():
                if len(lettre_et_codage[0])==1:
                    if ((a*(ord(lettre_et_codage[0][0])-97)+b)%26)==(ord(lettre_et_codage[1][0])-97):
                        continue
                    else:
                        break
                else:
                    for permut_lettres_arrivee in permutation_lettres(lettre_et_codage[1]):   
                        for i in range(len(lettre_et_codage[0])):
                            if ((a*(ord(lettre_et_codage[0][i])-97)+b)%26) != ((ord(permut_lettres_arrivee[i])-97)%26):
                                break
                        else:
                            break
                    else:
                        break
            else: 
                Coeffs_possibles.append((a,b))
    return Coeffs_possibles
    

                                                
                    
                    
                    
                    
                 
            
            
    
            
        
  
  
            