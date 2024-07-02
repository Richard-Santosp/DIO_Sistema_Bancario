
class Cliente:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
        self.qtd_saque = 0
        self.extrato = []

    def saque(self, valor):
        try:
            if valor < 0:
                return 'Não é aceito valores menos que R$0'
            elif valor > self.saldo:
                return 'O valor de saque não pode ser superior ao valor do saldo!'
            else:

                self.saldo -= valor
                extrato = {
                    "nome": self.nome,
                    "operação":"Saque",
                    "valor": valor,
                    "saldo": self.saldo
                }
                self.extrato.append(extrato)
                print(f'\nSaldo atual: R${self.saldo}.00\n')
                self.qtd_saque += 1
                return True
        except ValueError as e:
            print(f'Valor Incorreto')

    def emitir_extrato(self):
        if self.extrato:
            print(f'\n{"Nome":<15} {"Operação":<15} {"Valor":<15} {"Saldo":<15}')
            for item in self.extrato:
                print(f'{item["nome"]:<15} {item["operação"]:<15} R${item["valor"]:<15.2f} R${item["saldo"]:<15.2f}')
            return True
        else:
            print('\nNão há extratos registrados\n')
            return None
    def deposito(self, valor):
        if valor < 0:
            print('\nImposivel depositar um valor abaixo de R$0\n')
            return False
        else:
            self.saldo += valor
            extrato = {
                    "nome": self.nome,
                    "operação":"Deposito",
                    "valor": valor,
                    "saldo": self.saldo
                }
            self.extrato.append(extrato)
            print(f'\nSaldo atual: {self.saldo}\n')
            return True


richard = Cliente('Richard',10000000)

while True:
    opcao = input("\nOperação: [S]acar --  [E]xtrato -- [D]epositar -- [C]ancelar:   \n").upper()

    if opcao == 'S':
        if richard.qtd_saque == 3:
            print('Limite de saque diario excedido!')
            continue
        try:
            valor = eval(input('\nValor de saque: \n'))
            richard.saque(valor)
        except ValueError:
            print(f'\nValor não é um número!\n')
        except NameError:
            print(f'\nValor não é um número!\n')
        except SyntaxError:
            print('Valor incorreto')

    elif opcao == 'D':
        try:
            valor = eval(input('\nValor do deposito: \n'))
            richard.deposito(valor)
        except ValueError:
            print(f'\nValor não é um número!\n')
        except NameError:
            print(f'\nValor não é um número!\n')
        except SyntaxError:
            print('Valor incorreto')

    elif opcao == "E":
        richard.emitir_extrato()

    elif opcao == "C":
        print('\nAdeus!!\n')
        break
    else:
        print('\nComando incorreto. Tente novamente\n')