#importar bliblioteca Faker
from faker import Faker

#crie uma instancia do faker

fake = Faker()

#Gere um nome ficiticio

nome = fake.name()

#gere um endereço ficiticio

endereco = fake.address()


#Gere um numero de telefone ficticio

telefone = fake.phone_number()

#gere uma data de nascimento ficticia( indade entre 18 e 65 anos)

data_de_nascimento = fake.date_of_birth(minimum_age = 18, maximum_age = 65)


#imprima os dados ficticios

print('Nome: ', nome)
print('Endereço: ', endereco)
print('Telefone: ', telefone)
print('Data de nascimento: ', data_de_nascimento)