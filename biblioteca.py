livros = []
# Recupera os livros salvos no arquivo quando o programa inicia
arquivo = open("livros.csv", "r", encoding="utf-8")
for linha in arquivo:
    dados = linha.split(",")
    livro = {
        "titulo": dados[0],
        "autor": dados[1],
        "ano": dados[2],
        "isbn": dados[3],
        "status": dados[4].replace("\n", "")
    }
    livros.append(livro)
arquivo.close()
# Salva os livros no arquivo para manter os dados guardados
def salvar_arquivo():
    arquivo = open("livros.csv", "w", encoding="utf-8")
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
    print("cadastrar livro")
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano de publicação: ")
    isbn = input("Código/ISBN: ")
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
    return "Livro cadastrado!"
 # Listar todos os livros cadastrados mostrando seus dados e status
def listar_livros():
    print("listar livros")
    for livro in livros:
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Ano:", livro["ano"])
        print("ISBN:", livro["isbn"])
        print("Status:", livro["status"])
    return "Lista finalizada"
# Buscar um livro pelo título ou pelo autor
def buscar_livro():
    print("buscar livro")
    busca = input("Digite o título ou autor: ")
    for livro in livros:
        if busca == livro["titulo"] or busca == livro["autor"]:
            print("Título:", livro["titulo"])
            print("Autor:", livro["autor"])
            print("Ano:", livro["ano"])
            print("ISBN:", livro["isbn"])
            print("Status:", livro["status"])
            return "Livro encontrado"
    return "Livro não encontrado"
 # Menu principal que mantém o sistema funcionando até o usuário escolher sair
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
 
 
    
    