import json

produtos = []


def salvar_produtos():
    with open("produtos.json", "w") as arquivo:
        json.dump(produtos, arquivo, indent=4)


def carregar_produtos():
    global produtos

    try:
        with open("produtos.json", "r") as arquivo:
            produtos = json.load(arquivo)

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

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)
    salvar_produtos()

    print("Produto cadastrado!")

def excluir_produto():
    nome = input("Digite o nome do produto que deseja excluir: ")

    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            produtos.remove(produto)
            salvar_produtos()
            print("Produto excluído!")
            return

    print("Produto não encontrado!")


def listar_produtos():
    if len(produtos) == 0:
        print("Não existe nenhum produto cadastrado!")
        return

    for produto in produtos:
        print("---------------")
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Quantidade: {produto['quantidade']}")


carregar_produtos()


while True:
    print("\nSISTEMA DE ESTOQUE")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Excluir produto")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produtos()

    elif opcao == "2":
        listar_produtos()

    elif opcao == "3":
        excluir_produto()

    elif opcap == "4":
        print("Programa Encerrado!")

    else:
        print("Opção inválida...")