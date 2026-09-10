import json

produtos = []


class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def vender(self, quantidade):
        self.quantidade -= quantidade


def salvar_produtos():
    with open("produtos.json", "w") as arquivo:
        dados = []

        for produto in produtos:
            dados.append({
                "nome": produto.nome,
                "preco": produto.preco,
                "quantidade": produto.quantidade
            })

        json.dump(dados, arquivo, indent=4)


def carregar_produtos():
    global produtos

    try:
        with open("produtos.json", "r") as arquivo:
            dados = json.load(arquivo)

            produtos = []

            for produto in dados:
                novo_produto = Produto(
                    produto["nome"],
                    produto["preco"],
                    produto["quantidade"]
                )

                produtos.append(novo_produto)

    except FileNotFoundError:
        produtos = []


def cadastrar_produtos():
    nome = input("Digite o nome do produto: ")

    if not nome.replace(" ", "").isalpha():
        print("O nome deve conter apenas letras!")
        return

    try:
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade de produtos: "))

    except ValueError:
        print("Digite valores válidos!")
        return

    produto = Produto(nome, preco, quantidade)

    produtos.append(produto)
    salvar_produtos()

    print("Produto cadastrado!")


def excluir_produto():
    nome = input("Digite o nome do produto que deseja excluir: ")

    for produto in produtos:
        if produto.nome.lower() == nome.lower():
            produtos.remove(produto)
            salvar_produtos()
            print("Produto excluído!")
            return

    print("Produto não encontrado!")


def vender_produto():
    nome = input("Digite o nome do produto que deseja vender: ")

    for produto in produtos:
        if produto.nome.lower() == nome.lower():

            try:
                quantidade = int(input("Digite a quantidade que deseja vender: "))

            except ValueError:
                print("Digite um número válido!")
                return

            produto.vender(quantidade)

            salvar_produtos()

            print("Venda realizada!")
            return

    print("Produto não encontrado!")


def listar_produtos():
    if len(produtos) == 0:
        print("Não existe nenhum produto cadastrado!")
        return

    for produto in produtos:
        print("---------------")
        print(f"Nome: {produto.nome}")
        print(f"Preço: R$ {produto.preco:.2f}")
        print(f"Quantidade: {produto.quantidade}")


carregar_produtos()


while True:
    print("\nSISTEMA DE ESTOQUE")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Excluir produto")
    print("4 - Vender produto")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produtos()

    elif opcao == "2":
        listar_produtos()

    elif opcao == "3":
        excluir_produto()

    elif opcao == "4":
        vender_produto()

    elif opcao == "5":
        print("Programa Encerrado!")
        break

    else:
        print("Opção inválida...")