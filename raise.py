def dividi(a,b):
    if b==0:
        raise ZeroDivisionError("Il divisore non può essere 0!")
    return a/b

try:
    print(dividi(a=1, b=0))
except (ZeroDivisionError, ValueError) as e: #chiamiamo l'errore e
    print(e)


#%%

def dividi(a,b):
    if b==7:
        raise ErroreCustom("Non mi piace il 7.")
    return a/b

try:
    print(dividi(a=1, b=7))
except ErroreCustom as e: #chiamiamo l'errore e
    print("Non mi piace il 7!")