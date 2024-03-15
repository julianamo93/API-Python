import requests

listaDevs = []

nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))
cep = input("Digite o seu CEP: ")
login_github = input("Digite o seu login: ")

url1 = f"https://viacep.com.br/ws/{cep}/json/" 
response_cep = requests.get(url1)

if response_cep.status_code == 200:
    dados_via_cep = response_cep.json()


url2 = f"https://api.github.com/users/{login_github}"
response_git = requests.get(url2)

if response_git.status_code == 200:
    dados_github = response_git.json()

dev = {
    "nome": nome,
    "idade": idade,
    "login": login_github,
    "public_repos": dados_github['public_repos'],
    "followers": dados_github['followers'],
    "following": dados_github['following'],
    "cep": cep,
    "logradouro": dados_via_cep['logradouro'],
    "bairro": dados_via_cep['bairro'],
    "localidade": dados_via_cep['localidade'],
    "uf": dados_via_cep['uf']
}

listaDevs.append(dev)
print("Cadastro de Desenvolvedor:")
for dev in listaDevs:
            print(f"\n\n Nome: {dev['nome']} \nIdade: {dev['idade']} \nLogin GitHub: {dev['login']} \nCep: {dev['cep']} \nRua: {dev['logradouro']} \nBairro: {dev['bairro']} \nCidade: {dev['logradouro']} Estado: {dev['uf']} \n\n")


