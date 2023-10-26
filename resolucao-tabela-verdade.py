def gerar_lista_binarios(num_digitos):
    n_linhas = 2**num_digitos
    binario = [False] * num_digitos
    lista_binarios = []
    for _ in range(n_linhas):
        binario_temporario = binario.copy()
        lista_binarios.append(binario_temporario)
        for i in range(num_digitos - 1, -1, -1):
            if binario[i] == False:
                binario[i] = True
                for j in range(i + 1, num_digitos):
                    binario[j] = False
                break
    return lista_binarios


def trocar_caracteres(string, substituicao_caracteres):
    for c in range(len(substituicao_caracteres[0])):
        string = string.replace(
            substituicao_caracteres[0][c], substituicao_caracteres[1][c]
        )
    return string


substituicao_caracteres = ["_!$", "V→↔"]
lista_expressoes = [
    "¬(p^¬q)",
    "(¬p_¬q)_(¬(q$p))",
    "¬(p_q)^(p^q)",
    "¬p_(q^¬r)",
    "¬(p_¬q)^(¬p_r)",
    "p_q$¬(¬p^¬q)",
    "¬(¬p_¬q)",
    "¬(p^q)",
    "p_(p^q)",
    "(p^q)_(p^q)",
    "(p_q)^(p_q)",
    "p^q_r",
    "¬q!(p_¬r)",
    "(p_q)!(p_r)",
    "(p_q)$(p_r)",
]


# Resolvendo expressões
for e in range(len(lista_expressoes)):
    expressao = lista_expressoes[e].replace(" ", "")
    print(
        f"● Exercício {e + 1} : {trocar_caracteres(expressao, substituicao_caracteres)}"
    )
    print()

    # Determinando variáveis da expressão
    string_variaveis = ""

    for c in expressao:
        if c not in string_variaveis and c not in "^_¬!$()":
            string_variaveis += c

    # Determinando número de variáveis da expressão
    n_variaveis_inicial = len(string_variaveis)

    # Substituindo variáveis por números
    lista_variaveis = []
    for i in range(n_variaveis_inicial):
        expressao = expressao.replace(string_variaveis[i], str(i))
        lista_variaveis.append(str(i))

    # Definindo colunas da tabela
    n_variaveis = len(lista_variaveis)
    loop = True
    while loop:
        n_variaveis = len(lista_variaveis)
        loop = False
        for c in range(len(expressao) - 1):
            if expressao[c] == "¬" and expressao[c + 1].isnumeric():
                lista_variaveis.append(expressao[c : c + 2])
                expressao = expressao[:c] + str(n_variaveis) + expressao[c + 2 :]
                loop = True
                break

            elif (
                expressao[c].isnumeric()
                and expressao[c + 1] in "^_!$"
                and expressao[c + 2].isnumeric()
            ):
                lista_variaveis.append(expressao[c : c + 3])
                expressao = expressao[:c] + str(n_variaveis) + expressao[c + 3 :]
                loop = True
                break

            elif expressao[c] == "(" and expressao[c + 2] == ")":
                expressao = expressao[:c] + expressao[c + 1] + expressao[c + 3 :]
                loop = True
                break

    # Gerando lista de variáveis finais
    lista_variaveis_final = []
    for v in range(n_variaveis_inicial):
        lista_variaveis_final.append(string_variaveis[v])
    for v in range(n_variaveis_inicial, n_variaveis):
        variavel = lista_variaveis[v]
        for v2 in range(v):
            variavel_troca = lista_variaveis_final[v2]
            if variavel_troca[0:2] != "¬(" and len(variavel_troca) >= 3:
                variavel_troca = f"({variavel_troca})"
            variavel = variavel.replace(str(v2), variavel_troca)
        variavel = trocar_caracteres(variavel, substituicao_caracteres)
        lista_variaveis_final.append(variavel)

    # Resolvendo linhas da tabela
    tabela = [lista_variaveis_final]

    lista_binarios = gerar_lista_binarios(n_variaveis_inicial)

    n_linhas = 2**n_variaveis_inicial
    for l in range(n_linhas):
        linha = lista_binarios[l]

        for v in range(n_variaveis_inicial, n_variaveis):
            variavel = lista_variaveis[v]
            operador = variavel[1]
            resultado = False
            if variavel[0] == "¬":
                resultado = not linha[int(variavel[1])]
            elif operador == "^":
                resultado = linha[int(variavel[0])] and linha[int(variavel[2])]
            elif operador == "_":
                resultado = linha[int(variavel[0])] or linha[int(variavel[2])]
            elif operador == "!":
                resultado = linha[int(variavel[0])] == 0 or linha[int(variavel[2])] == 1
            elif operador == "$":
                resultado = linha[int(variavel[0])] == linha[int(variavel[2])]
            linha.append(resultado)
        tabela.append(linha)

    # Definindo tamanho das colunas
    len_colunas = []
    for c in range(n_variaveis):
        len_coluna = len(lista_variaveis_final[c]) + 2
        if len_coluna < 5:
            len_coluna = 5
        len_colunas.append(len_coluna)

    # Printando tabela formatada
    for l in range(n_linhas + 1):
        for c in range(n_variaveis):
            item = tabela[l][c]
            if l != 0:
                if item:
                    item = "V"
                else:
                    item = "F"
            print(f"{item:^{len_colunas[c]}}", end="")
            if c != n_variaveis - 1:
                print("|", end="")
        if l == 0:
            print()
            for c in range(n_variaveis):
                print("-" * len_colunas[c], end="")
                if c != n_variaveis - 1:
                    print("+", end="")
        print()
    print("\n\n")
