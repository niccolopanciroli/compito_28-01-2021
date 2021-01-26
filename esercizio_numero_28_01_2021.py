print("Organizza con un dizionario i dati sui conti correnti bancari con un numero del conto e saldo. Fornito poi il numero di conto, il programma visualizza il saldo oppure un messaggio nel caso in cui il conto non sia presente nella mappa")

conti_correnti_bancari = {"1": 1000, "2": 2000, "3":3000, "4":4000}

numero_conto_corrente = input("Inserisci il numero di un conto corrente per visualizzare il saldo, ovvero quanti soldi ci sono sul conto Corrente ")

if numero_conto_corrente in conti_correnti_bancari:
    print("Il saldo associato a questo numero é", conti_correnti_bancari[numero_conto_corrente])
else:
    print("Il conto non è presente nella mappa, mi dispiace")