livros = []
# Recupera os livros salvos no arquivo
 
arquivo = open("livros.csv", "r", encoding="utf-8")
for linha in arquivo:
# verifica e ignora linhas vazias e o cabeçalho
 dados = linha.strip().split(",")
if len(dados) >= 5 and dados[0] != "titulo":
    livro = {
        "titulo": dados[0],
        "autor": dados[1],
        "ano": dados[2],
        "isbn": dados[3],
        "status": dados[4]
    }
 
    livros.append(livro)
 
arquivo.close()
# Salva os livros no arquivo para manter os dados guardados
def salvar_arquivo():
    arquivo = open("livros.csv", "w", encoding="utf-8")

    arquivo.write("titulo,autor,ano,isbn,status\n")

    for livro in livros:
        arquivo.write(
            livro["titulo"] + "," +
            livro["autor"] + "," +
            livro["ano"] + "," +
            livro["isbn"] + "," +
            livro["status"] + "\n"
        )

    arquivo.close()

# Cadastro de livros 
def cadastrar_livro():
    print("cadastrar livros")
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano de publicação: ")
    isbn = input("Código/ISBN: ")

    for livro in livros:
        if livro["isbn"] == isbn:
            return "Já tem um livro cadastrado com esse ISBN"
    status = "disponível"
    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "isbn": isbn,
        "status": status
    }

    livros.append(livro)
    salvar_arquivo()
    return "Livro cadastrado"

# Registro de empréstimo de livros
def emprestar_livro():
    isbn = input("Digite o ISBN: ")
    for livro in livros:
        if livro["isbn"] == isbn:
            if livro["status"] == "emprestado":
                return "Livro já está emprestado"
            livro["status"] = "emprestado"
            salvar_arquivo()
            return "Empréstimo realizado"
    return "Livro não encontrado"

# Registro de devolução de livros
def devolver_livro():
    isbn = input("Digite o ISBN: ")
    for livro in livros:
        if livro["isbn"] == isbn:
            if livro["status"] == "disponível":
                return "Livro já está disponível"
            livro["status"] = "disponível"
            salvar_arquivo()
            return "Devolução realizada"
    return "Livro não encontrado"
 
# Lista todos os livros cadastrados
def listar_livros(livros):
    print("listar livros")
    for livro in livros:
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Ano:", livro["ano"])
        print("ISBN:", livro["isbn"])
        print("Status:", livro["status"])
 
    return "Lista finalizada"
 
# Busca um livro pelo título ou pelo autor 
# O lower deixa tudo em letras minúsculas para ajudar na comparação
def buscar_livro(livros):
    print("buscar livro")
    termo = input("Digite o título ou autor: ")
    encontrado = False
    for livro in livros:
        if termo.lower() in livro["titulo"].lower() or termo.lower() in livro["autor"].lower():
            print("Título:", livro["titulo"])
            print("Autor:", livro["autor"])
            print("Ano:", livro["ano"])
            print("ISBN:", livro["isbn"])
            print("Status:", livro["status"])
            encontrado = True
    if not encontrado:
        print("Nenhum livro encontrado.")

    return "Busca finalizada"
 
# Ordenação da listagem de livros por título, autor ou ano de publicação
# O sort organiza os livros de acordo com a opção 
# O key vai definir qual informação será usada para organizar
# O lambda é utilizado por ser uma opção mais rapida de pegar uma informação de cada livro
def ordenar_livros(livros):
    print("1 - Ordenar por título")
    print("2 - Ordenar por autor")
    print("3 - Ordenar por ano")
    opcao = input("Escolha: ")
    if opcao == "1":
        livros.sort(key=lambda livro: livro["titulo"])
    elif opcao == "2":
        livros.sort(key=lambda livro: livro["autor"])
    elif opcao == "3":
        livros.sort(key=lambda livro: int(livro["ano"]))
    else:
        print("Opção inválida..")
        return livros
    salvar_arquivo()
    return livros

# Menu principal que mantém o sistema funcionando
while True:
    print("\nSISTEMA DA BIBLIOTECA")
    print("1 - Cadastrar livros")
    print("2 - Registrar empréstimo")
    print("3 - Registrar devolução")
    print("4 - Listar livros")
    print("5 - Buscar livro")
    print("6 - Ordenar livros")
    print("7 - Sair")
 
    opcao = input("Escolha uma opção: ")
 
    if opcao == "1":
        print(cadastrar_livro())
 
    elif opcao == "2":
        print(emprestar_livro())
 
    elif opcao == "3":
        print(devolver_livro())
 
    elif opcao == "4":
        print(listar_livros(livros))
 
    elif opcao == "5":
        print(buscar_livro(livros))
 
    elif opcao == "6":
      ordenar_livros(livros)
      print("Livros ordenados com sucesso")
    
 
    elif opcao == "7":
        print("Sistema encerrado")
        break
 
    else:
        print("Opção inválida")