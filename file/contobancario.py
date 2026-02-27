#andiamo a proteggere le classi varie (private con il _)

class ContoBancario:

    def __init__(self, saldo):
        self._saldo = saldo


conto_di_ciccio = ContoBancario(10000)

conto_di_ciccio._saldo = conto_di_ciccio._saldo - 10000

print(conto_di_ciccio._saldo)

#servono metodi getter/setter, in python no però

#%%

#protezione _ (1 solo underscore convenzionale), protezione __ (2 protezione profonda)

class ContoBancario:

    def __init__(self, saldo):
        self._saldo = saldo

    def deposita(self, importo):
        if importo > 0:
            self._saldo += importo

    def preleva(self, importo):
        if 0 < importo <self._saldo:
            self._saldo -= importo

    def mostra_saldo(self):
        return self._saldo


conto_di_ciccio = ContoBancario(10000)



print(conto_di_ciccio.mostra__saldo())