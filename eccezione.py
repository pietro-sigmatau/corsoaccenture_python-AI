try:
     numero = int("ciao")
     print(numero)
except:
    print("Errore, il numero non è un numero")

# ma così è bad practice, value error: qual è l'errore che si ouò intercettare? va inserita anche il codice

#%%


try:
    numero = int(input("Inserire un numero: "))
    print("Hai inserito il numero", numero)
except ValueError:
    print("Errore, il numero non è un numero")


#%%

try:
    numero_1 = int(input("Inserire un numero: "))
    numero_2 = int(input("Inserire un altro numero: "))
    print("Risultato: ", numero_1/numero_2)

except ValueError:
    print("Errore, il numero non è un numero")

except ZeroDivisionError:
    print("Non puoi didvidere per zero!")

finally:
    print("Qualsiasi cosa succeda, io vengo eseguito")

# %%


#blocchi di codice che POSSONO fallire in maniera programmata nel try
try:
    numero_1 = int(input("Inserire un numero: "))
    numero_2 = int(input("Inserire un altro numero: "))
    print("Risultato: ", numero_1 / numero_2)

#gli IF nel try, non usiamo il try per controllare l'IF

except ValueError:
    print("Errore, il numero non è un numero")

except ZeroDivisionError:
    print("Non puoi didvidere per zero!")

else:
    print("Divisione eseguita con successo")

finally:
    print("Qualsiasi cosa succeda, io vengo eseguito")