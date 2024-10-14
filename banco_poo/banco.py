from abc import ABC,  abstractmethod

class Cliente:
	def __init__(self, endereco):
		self.endereco= endereco
		self.conta= []
	
	def realizar_transacao(self, conta, transação):
		pass
	def adicionar_conta(self, conta):
		self.conta.append(conta)
		
class Pessoa_fisica(Cliente):
	def __init__(self, endereco, cpf, nome, data_nascimento):
		super().__init__(endereco)
		self.cpf= cpf
		self.nome= nome
		self.data_nascimento= data_nascimento

class Conta:
	def __init__(self, numero, agencia, cliente):
		self.saldo= 0.0
		self.numero= numero
		self.agencia= agencia
		self.cliente= cliente
		self.historico= Historico()
		
		cliente.adicionar_conta(self)
		
	def saldo():
		return self.saldo
	
	@classmethod	
	def nova_conta(self, cliente,numero):
		return Cliente(numero,'001',cliente)
		
	def sacar(self, valor):
		self.saldo += saldo
		return True
		
	def sacar(self, valor):
		self.saldo -= saldo
		return True

class Conta_corrente(Conta):
	def __init__(self, cliente, numero, agencia, limite, limite_saque):
		super().__init__(cliente, numero ,agencia)
		self.limite= limite
		self.limite_saque= limite_saque	
		
class Historico:
	def __init__(self):
		self.lista= ['Conta criada\n\n']
		
	def adicionar_transacao(self, transacao):
		self.lista.append(transacao)
		
class Transacao(ABC):
	@abstractmethod
	def registrar(conta):
		pass

class Deposito(Transacao):
	def __init__(self, valor):
		self.valor= valor
		
	def registrar(conta):
		pass
		
class Saque(Transacao):
	def __inti__(self,valor):
		self.valor= valor
		
	def registrar(conta):
		pass
	


