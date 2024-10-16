from abc import ABC, abstractclassmethod,  abstractmethod, abstractproperty
import datetime

class Cliente:
	def __init__(self, endereco):
		self.endereco= endereco
		self.conta= []
	
	def realizar_transacao(self, conta, transação):
		transação.registrar(conta)

	def adicionar_conta(self, conta):
		self.conta.append(conta)
		
class Pessoa_fisica(Cliente):
	def __init__(self, endereco, cpf, nome, data_nascimento):
		super().__init__(endereco)
		self.cpf= cpf
		self.nome= nome
		self.data_nascimento= data_nascimento

class Conta:
	def __init__(self, numero, cliente):
		self._saldo= 0.0
		self._numero= numero
		self._agencia= '0001'
		self._cliente= cliente
		self._historico= Historico()
	
	@classmethod	
	def nova_conta(cls, cliente,numero):
		return cls(numero,cliente)

	@property
	def saldo(self):
		return self._saldo

	@property
	def numero(self):
		return self._numero
	
	@property
	def agencia(self):
		return self._agencia
	
	@property
	def cliente(self):
		return self._cliente
	
	@property
	def historico(self):
		return self._historico

	
	def sacar(self, valor):
		saldo = self._saldo
		excedeu_saldo= valor > saldo

		if excedeu_saldo:
			print("sem saldo.")
		
		elif valor > 0:
			self._saldo -= valor
			print("saque realizado")
			return True
		
		else:
			print("operação falhou!!!")

		return False

	def depositar(self, valor):
		if valor > 0:
			self._saldo+= valor
			print("deposito realizado com sucesso!!!")

		else:
			print("operação falhou!!!")
			return False

		return True		

class Conta_corrente(Conta):
	def __init__(self, cliente, numero, agencia, limite= 500, limite_saque= 3):
		super().__init__(cliente, numero ,agencia)
		self._limite= limite
		self._limite_saque= limite_saque	

	def sacar(self, valor):
		numero_saque = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])

		excedeu_limite = valor > self.limite
		excedeu_saques = numero_saque >= self._limite_saque

		if excedeu_limite:
			print("valor excede o limite.")

		elif excedeu_saques:
			print('saque excedido')

		else:
			return super().sacar(valor)
		
		return False
	
	def __str__(self):
		return f"""
			Agencia:\t{self.agencia}
			C/C:\t\t{self.numero}
			Titular:\t{self.cliente.nome}"""
			
class Historico:
	def __init__(self):
		self._transacoes= []

	@property
	def transacoes(self):
		return self.transacoes

	def adicionar_transacao(self, transacao):
		self.transacoes.append({
			"tipo":transacao.__class__.__name__,
			"valor":transacao.valor,
			"data":datetime.now().strftime("%d-%m-%Y %H:%M:%s")
		})
		
class Transacao(ABC):
	@property
	@abstractmethod
	def valor(self):
		pass

	@classmethod
	@abstractmethod
	def registrar(conta):
		pass

class Deposito(Transacao):
	def __inti__(self,valor):
		self._valor= valor

	@property
	def valor(self):
		return self._valor
		
	def registrar(self, conta):
		sucesso_transacao= conta.depositar(self.valor)

		if sucesso_transacao:
			conta.historico.adicionar_transacao(self)
		
class Saque(Transacao):
	def __inti__(self,valor):
		self._valor= valor

	@property
	def valor(self):
		return self._valor
		
	def registrar(self, conta):
		sucesso_transacao= conta.sacar(self.valor)

		if sucesso_transacao:
			conta.historico.adicionar_transacao(self)



def main():
	Cliente= []
	contas= []

	while True:
		opcao= menu()

		if opcao =='d':
			depo