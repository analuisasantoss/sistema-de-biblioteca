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
 