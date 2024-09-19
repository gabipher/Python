class Empregado:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

    def __str__(self):
        return f"{self.nome}, Salário: R${self.calcular_salario():.2f}"


class Gerente(Empregado):
    def __init__(self, nome, salario_base, bonus_fixo):
        super().__init__(nome, salario_base)
        self.bonus_fixo = bonus_fixo

    def calcular_salario(self):
        return self.salario_base + self.bonus_fixo


class Vendedor(Empregado):
    def __init__(self, nome, salario_base, comissao):
        super().__init__(nome, salario_base)
        self.comissao = comissao

    def calcular_salario(self, vendas):
        return self.salario_base + (vendas * self.comissao)


gerente = Gerente("Alice", 5000, 1000)
print(gerente)

vendedor = Vendedor("Bob", 3000, 0.1)
print(vendedor.calcular_salario(15000))