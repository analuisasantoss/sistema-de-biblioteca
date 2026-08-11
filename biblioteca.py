livros = []
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
        # Cadastro de livros
        print("CADASTRAR LIVRO")
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
        arquivo = open("livros.csv", "a", encoding="utf-8")
        arquivo.write(titulo + "," + autor + "," + ano + "," + isbn + "," + status + "\n")
        arquivo.close()
        print("Livro cadastrado com sucesso!")
        print("Arquivo salvo!")
    elif opcao == "2":
        print("REGISTRAR EMPRÉSTIMO")
    elif opcao == "3":
        print("REGISTRAR DEVOLUÇÃO")
    elif opcao == "4":
        print("LISTAR LIVROS")
    elif opcao == "5":
        print("BUSCAR LIVRO")
    elif opcao == "6":
        print("ORDENAR LIVROS")
    elif opcao == "7":
        print("Sistema encerrado")
        break
    else:
        print("Opção inválida")