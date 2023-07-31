class ContaBancaria:
    def __init__(self, numeroConta, saldo):
        self.numeroConta = numeroConta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def detalhesConta(self):
        print("Número da conta:", self.numeroConta)
        print("Saldo:", self.saldo)

class ContaCorrente(ContaBancaria):
    def __init__(self, numeroConta, saldo, limite):
        super().__init__(numeroConta, saldo)
        self.limite = limite

    def detalhesConta(self):
        super().detalhesConta()
        print("Limite do cheque especial:", self.limite)

class ContaPoupanca(ContaBancaria):
    def __init__(self, numeroConta, saldo, taxaRendimento):
        super().__init__(numeroConta, saldo)
        self.taxaRendimento = taxaRendimento

    def detalhesConta(self):
        super().detalhesConta()
        print("Taxa de rendimento:", self.taxaRendimento)

conta_bancaria = ContaBancaria("1234", 1000)
conta_corrente = ContaCorrente("5678", 2000, 500)
conta_poupanca = ContaPoupanca("9101", 3000, 0.05)
conta_bancaria.depositar(500)
conta_bancaria.sacar(200)
conta_corrente.depositar(1000)
conta_corrente.sacar(300)
conta_poupanca.depositar(2000)
conta_poupanca.sacar(500)

conta_bancaria.detalhesConta()
print("\n")
conta_corrente.detalhesConta()
print("\n")
conta_poupanca.detalhesConta()