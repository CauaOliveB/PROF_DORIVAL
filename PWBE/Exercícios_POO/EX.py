"""

1. Crie uma classe chamada “Círculo” que possua um atributo para armazenar o raio e 
métodos para calcular a área e o perímetro do círculo.

"""

# class Circulo():
#     def __init__(self, raio):
#         self.raio = raio
#         self.pi = 3 

#     def calcular_area(self):
#         return self.pi * self.raio ** 2

#     def calcular_perimetro(self):
#         return 2 * self.pi * self.raio
    
#     def __str__(self):
#         return f"Círculo de raio {self.raio}"
    

# meu_circulo = Circulo() #INSIRA SEU RAIO AQUI

# print (meu_circulo)
# print(f"Raio: {meu_circulo.raio}")
# print(f"Área: {meu_circulo.calcular_area()}")
# print(f"Perimetro: {meu_circulo.calcular_perimetro()}")


"""

2. Implemente uma classe chamada “ContaBancária” que possua atributos para 
armazenar o número da conta, nome do titular e saldo. Adicione métodos para realizar 
depósitos e saques. 

"""

# class ContaBancária():
#     def __init__(self,n_conta, nome_titular, saldo):
#         self.n_conta = n_conta
#         self.nome_titular = nome_titular
#         self.saldo = saldo

#     def Depósito(self,v):
#         self.v = int(input("Insira o valor que deseja depositar:"))
#         return (f"Depósito : {v} | Saldo atual : {self.saldo + v}\n")
        

#     def Saques(self):
#         s = int(input("Insira o valor que deseja sacar:"))
#         return (f"Saque : {self.saldo} | Saldo atual :  {self.saldo - s + v}\n")
    
#     def __str__(self):
#         return (f"Conta número - ({self.n_conta}) | Títular : {self.nome_titular}  | Saldo atual :R${self.saldo} {v} \n")


# banco = ContaBancária(2,"Carlos", 300)    

# print (banco)
# print(f"{banco.Depósito()}")
# print(f"{banco.Saques()}")

"""

3. Crie uma classe chamada “Retângulo” que possua atributos para armazenar a largura e 
a altura. Implemente métodos para calcular a área e o perímetro do retângulo. 

"""

# class Retângulo():
#     def __init__(self, largura, altura):
#         self.largura = largura
#         self.altura = altura


#     def calcular_area(self):
#         return (f"Área : {self.largura * self.altura}")
    
#     def calcular_perimetro(self):
#         return (f"Perímetro : {2 * (self.largura + self.altura)}\n")
    
#     def __str__(self):
#         return (f"Forma : Retângulo | Largura : {self.largura} | Altura : {self.altura}\n")
    

# retangulo = Retângulo(8,5)

# print(retangulo)
# print(f"Área : {retangulo.calcular_area()}")
# print(f"Perímetro : {retangulo.calcular_perimetro()}")

"""
(Tive dificuldades)

4. Implemente uma classe chamada “Aluno” que possua atributos para armazenar o 
nome, a matrícula e as notas de um aluno. Adicione métodos para calcular a média das 
notas e verificar a situação do aluno (aprovado ou reprovado). 

"""        
# class Aluno:
#     def __init__(self, nome, matricula, notas):
#         self.nome = nome
#         self.matricula = matricula
#         self.notas = notas
    
#     def media(self):
#         return sum(self.notas) / len(self.notas) if self.notas else 0
    
#     def situacao(self, corte=5):
#         return "Aprovado" if self.media() >= corte else "Reprovado"
    
#     def mostrar(self):
#         print(f"Nome: {self.nome}")
#         print(f"Matrícula: {self.matricula}")
#         print(f"Notas: {self.notas}")
#         print(f"Média: {self.media():.1f}")
#         print(f"Situação: {self.situacao()}")

# aluno = Aluno("Maria", "12345", [2, 10, 6, 8])

# aluno.mostrar()

# print(f"Média: {aluno.media():.1f}")
# print(f"Situação: {aluno.situacao()}")  

"""

5. Crie uma classe chamada “Funcionário” com atributos para armazenar o nome, o 
salário e o cargo do funcionário. Implemente métodos para calcular o salário líquido, 
considerando descontos de impostos e benefícios. 

"""

# class Funcionário():
#     def __init__(self, nome, salario, cargo):
#         self.nome = nome
#         self.salario = salario
#         self.cargo = cargo

#     def desconto_de_imposto(self):
#         if self.salario <= 1302:
#             return(f"Salário  : {self.salario} | Aliquota de Desconto : 7.5% | Salário Líquido : {self.salario - (self.salario * (7.5/100))}")
#         elif self.salario >= 1302.01 and self.salario <= 2571:
#             return(f"Salário  : {self.salario} | Aliquota de Desconto : 9% | Salário Líquido : {self.salario - (self.salario * (9/100))}")
#         elif self.salario >= 2571.30 and  self.salario <= 3856:
#             return(f"Salário  : {self.salario} | Aliquota de Desconto : 12% | Salário Líquido : {self.salario - (self.salario * (12/100))}")
#         else:
#             return(f"Salário  : {self.salario} | Aliquota de Desconto : 14% | Salário Líquido : {self.salario - (self.salario * (14/100))}")
         

#     def desconto_de_beneficio(self):
#         return (f"Salário : {self.salario} | Vale-Transporte : {self.salario - (self.salario * (6/100))}")
    
#     def __str__(self):
#         return (f"Sr(A)º {self.nome} | Cargo : {self.cargo} | Salário : {self.salario}\n")
    
# f1 = Funcionário("Jeysa Castro", 1518, "Jovem Aprendiz" )

# print(f1)
# print(f1.desconto_de_imposto())
# print(f1.desconto_de_beneficio())

"""

6. Implemente uma classe chamada “Produto” que possua atributos para armazenar o 
nome, o preço e a quantidade em estoque. Adicione métodos para calcular o valor 
total em estoque e verificar se o produto está disponível. 

"""

# class Produto():
#     def __init__(self, nome, preco, quantidade_em_estoque):
#         self.nome = nome
#         self.preco = preco
#         self.quantidade_em_estoque = quantidade_em_estoque
    
#     def calcular_estoque(self):
#         return (f"Quantidade Total em Estoque : {self.nome} = {self.quantidade_em_estoque} | Valor Total do Estoque : R${self.quantidade_em_estoque * self.preco}")
    
#     def situacao(self):
#         if self.quantidade_em_estoque <= 0:
#             return (f"Quantidade em estoque está indisponível para uso\n")
#         else:
#             return (f"Quantidade em estoque está disponível para uso\n")
        
#     def __str__(self):
#         return (f"Produto : {self.nome} | Estoque : {self.quantidade_em_estoque} | Valor do Estoque : R${self.preco * self.quantidade_em_estoque}\n")

# pr1 = Produto("Peixe", 50, 5)

# print(pr1)
# print(pr1.calcular_estoque())
# print(pr1.situacao())

"""

7. Crie uma classe chamada “Triângulo” com atributos para armazenar os três lados do 
triângulo. Implemente métodos para verificar se é um triângulo válido e calcular sua 
área. 

"""

# class Triângulo():
#     def __init__(self, lado1, lado2, lado3):
#         self.a = lado1
#         self.b = lado2
#         self.c = lado3

#     def situacao(self):
#         if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
#             return (f"Esse triângulo é válido")

#     def calcular_area(self):


"""

8. Implemente uma classe chamada “Carro” com atributos para armazenar a marca, o 
modelo e a velocidade atual do carro. Adicione métodos para acelerar, frear e exibir a 
velocidade atual. 

"""
# class Carro():
#     def __init__(self, marca, modelo, velocidade_atual):
#         self.marca = marca
#         self.modelo = modelo
#         self.velocidade_atual = velocidade_atual

#     def acelerar(self):
#         ac = int(input("Velocidade Acelerada :"))
#         return (f"Acelerada :{ac} | Velocidade atual :{self.velocidade_atual}  ")

#     def frear(self):
#         fr = int(input("Velocidade Acelerada :"))
#         return (f"Freio : {fr} | Velocidade atual : {fr - self.velocidade_atual}")
    
#     def __str__(self):
#         return {f"{self.marca} | Modelo : {self.modelo} | Velocidade : {self.velocidade_atual}"}

# carro1 = Carro("Honda", "Civic", 120)
# print(carro1)    
# print(carro1.acelerar())
# print(carro1.frear())

"""

9. Crie uma classe chamada “Paciente” que possua atributos para armazenar o nome, a 
idade e o histórico de consultas de um paciente. Implemente métodos para adicionar 
uma nova consulta ao histórico e exibir as consultas realizadas. 

"""
# class Paciente():
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#         self.historico = []

#     def nova_consulta(self, data, motivo):
#         self.historico.append(f"{data} - {motivo}")

#     def mostrar_historico(self):
#         print(f"Histórico de {self.nome}:")
#         for consulta in self.historico:
#             print("-", consulta)
    
# paciente1 = Paciente("Lucas", 25)
# paciente1.nova_consulta("2025-05-18", "Dor de cabeça")
# paciente1.nova_consulta("2025-05-19", "Retorno")
# paciente1.mostrar_historico()
"""

10. Implemente uma classe chamada “Livro” com atributos para armazenar o título, o 
autor e o número de páginas do livro. Adicione métodos para emprestar o livro, 
devolvê-lo e verificar se está disponível. 

"""

class Livro():
    def __init__(self, titulo, autor, paginas,):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        

    def disponivel(self, status):
        
        print("Status do Livro" \
        "[1] - Disponível" \
        "[2] - Emprestado" )

        if status == 1:
            print("Livro disponível para emprestímo")

        else: 
            print("Livro Indisponível para emprestímo")

    def emprestar(self, usuario):
        print(f"""Serviço Nacional de Aprendizagem Industrial - SP
              501 - Escola SENAI "Roberto Mange"
              Recibo de empréstimo
              Usuário - {usuario}

            {self.titulo} - {self.autor} ({self.paginas})
              """)
    
    def devolucao(self, data, usuario):
       print(f"""Serviço Nacional de Aprendizagem Industrial - SP
             501 - Escola SENAI "Roberto Mange"
             Recibo de devolução
             Usuário - {usuario}

            {self.titulo} - {self.autor} ({self.paginas})

            Devolvido em : {data}
""")

livro = Livro("O Pequeno Princípe" , "Antoine Marie Jean-Baptiste Roger de Saint-Exupéry", 96)
livro.disponivel(1)
livro.emprestar("Dorival")
livro.devolucao("2025-05-20", "Dorival")

"""

11. Implemente uma classe chamada “Banco” que represente uma instituição financeira. 
Essa classe deve conter métodos para cadastrar clientes, abrir contas bancárias e 
realizar operações como saques, depósitos e transferências. 

"""


"""

12. Crie uma classe chamada “LojaVirtual” que represente uma plataforma de vendas 
online. Essa classe deve ter funcionalidades para cadastrar produtos, gerar carrinho de 
compras, aplicar descontos e calcular o valor total da compra. 

"""


"""

13. Implemente uma classe chamada “Agenda” que represente uma agenda telefônica. 
Essa classe deve permitir adicionar, editar e remover contatos, além de buscar por 
contatos a partir de um nome ou número de telefone. 

"""


"""

14. Crie uma classe chamada “MáquinaDeVendas” que simule uma máquina de venda de 
produtos. Essa classe deve permitir cadastrar produtos, selecionar um produto para 
compra, inserir dinheiro, retornar o troco e exibir o estoque disponível. 

"""