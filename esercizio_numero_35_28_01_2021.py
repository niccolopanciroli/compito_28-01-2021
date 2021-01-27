'''
es35: organizza  con un dizionario i dati sui conti bancari con numero del conto e saldo. 
Fornito poi il numero di conto, il programma visualizza il saldo oppure un messaggio nel caso in cui il conto non sia presente nella mappa.
'''
conti_bancari = {"1": 100,
                 "2": 1000,
                 "3": 10000,
                 "4": 100000}
n_chiavi = 4


risposta = int(input("Benvenuto\n1) Desideri creare un nuovo conto --> premi 1\n2) Modificare il tuo saldo bancario--> premi 2\n3) Visualizzare il tuo saldo-->premi 3\n "))
   
if risposta == 1:
    saldo = int(input("Quanto denaro vuoi inserire intanto nel tuo nuovo conto? (scrivi solo il numero) "))
    n_chiavi+=1
    conti_bancari[str(n_chiavi)]= saldo
    print(conti_bancari)

elif risposta == 2:
    add_or_subtract= input("Vorresti aggiungere dal tuo conto corrente? \nPremi 1 per aggiungere dei soldi al tuo conto corrente, qualsiasi altro tasto per togliere dei soldi ")
        
    if add_or_subtract == "1":
        conto_corrente = input("Inserisci il numero del tuo conto corrente ")
        soldi_inseriti = int(input("Quanti soldi vuoi inserire nel conto corrente? "))
        conti_bancari[conto_corrente]+= soldi_inseriti
        print("Ora il tuo conto corrente(", str(conto_corrente),") ammonta a ", conti_bancari[conto_corrente])
       
    else:
        conto_corrente = input("Inserisci il numero del tuo conto corrente ")
        soldi_inseriti = int(input("Quanti soldi vuoi togliere dal tuo conto corrente? "))
        conti_bancari[conto_corrente]-=soldi_inseriti
        print("Ora il conto corrente(", str(conto_corrente), ") ammonta a", conti_bancari[conto_corrente])
    
elif risposta == 3:
    numero_conto_corrente = input("Immettere il numero del conto corrente per visualizzare il proprio saldo: ")

    if numero_conto_corrente not in conti_bancari:
        print("Spiacenti, il conto: ", numero_conto_corrente, " non si trova nella mappa")
    else:
        print("Il saldo del ", numero_conto_corrente, " conto è di ", conti_bancari[numero_conto_corrente], " euro.")