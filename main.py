produtos = []

def cadastrar_produtos():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade de produtos: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    produtos.append(produto)

    print("Produto cadastrado!")


def listar_produtos():
    if len(produtos) == 0:
        print("Não existe nenhum produto cadastrado!")
        return

    for produto in produtos:
        print("---------------")
        print(f"Nome: {produto['nome']}")
        print(f"Preço: {produto['preco']: .2f}")
        print(f"Quantidade: {produto['quantidade']}")

while True:
    print("\n SISTEMA DE ESTOQUE ")
    print("1- Cadastrar produto")
    print("2- Listar produtos ")
    print("3- Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produtos()

    elif opcao == "2":
        listar_produtos()

    elif opcao == "3":
        print("Programa encerrado.")
        break
    
    else:
        print("Opção inválida...")
    
