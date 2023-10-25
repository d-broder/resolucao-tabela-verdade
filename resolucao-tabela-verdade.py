def gerar_lista_binarios(num_digitos):
    n_linhas = 2**num_digitos
    binario = [0] * num_digitos
    lista_binarios = []
    for _ in range(n_linhas):
        binario_temporario = binario.copy()
        lista_binarios.append(binario_temporario)
        for i in range(num_digitos - 1, -1, -1):
            if binario[i] == 0:
                binario[i] = 1
                for j in range(i + 1, num_digitos):
                    binario[j] = 0
                break
    return lista_binarios


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

for e in range(len(lista_expressoes)):
    expressao = lista_expressoes[e].replace(" ", "")
    print("Exercício ", e + 1, ": ", expressao)

    string_variaveis = ""

    for c in expressao:
        if c not in string_variaveis and c not in "^_¬!$()":
            string_variaveis += c

    n_variaveis_inicial = len(string_variaveis)

    lista_variaveis = []
    for i in range(n_variaveis_inicial):
        expressao = expressao.replace(string_variaveis[i], str(i))
        lista_variaveis.append(str(i))

    cont_variaveis = n_variaveis_inicial
    cont_mudancas = 1
    while cont_mudancas > 0:
        cont_mudancas = 0
        for c in range(len(expressao) - 1):
            if expressao[c] == "¬" and expressao[c + 1].isnumeric():
                lista_variaveis.append(expressao[c : c + 2])
                expressao = expressao[:c] + str(cont_variaveis) + expressao[c + 2 :]
                cont_variaveis += 1
                cont_mudancas += 1
                break

            if (
                expressao[c].isnumeric()
                and expressao[c + 1] in "^_!$"
                and expressao[c + 2].isnumeric()
            ):
                lista_variaveis.append(expressao[c : c + 3])
                expressao = expressao[:c] + str(cont_variaveis) + expressao[c + 3 :]
                cont_variaveis += 1
                cont_mudancas += 1
                break

            if expressao[c] == "(" and expressao[c + 2] == ")":
                expressao = expressao[:c] + expressao[c + 1] + expressao[c + 3 :]
                cont_mudancas += 1
                break

    n_variaveis = len(lista_variaveis)
    n_linhas = 2**n_variaveis_inicial

    print(lista_variaveis)

    lista_binarios = gerar_lista_binarios(n_variaveis_inicial)

    for l in range(n_linhas):
        resultados_linha = lista_binarios[l].copy()

        for v in range(n_variaveis_inicial, n_variaveis):
            if lista_variaveis[v][0] == "¬":
                resultados_linha.append(
                    int(not resultados_linha[int(lista_variaveis[v][1])])
                )
            elif lista_variaveis[v][1] == "^":
                resultados_linha.append(
                    int(
                        resultados_linha[int(lista_variaveis[v][0])]
                        and resultados_linha[int(lista_variaveis[v][2])]
                    )
                )
            elif lista_variaveis[v][1] == "_":
                resultados_linha.append(
                    int(
                        resultados_linha[int(lista_variaveis[v][0])]
                        or resultados_linha[int(lista_variaveis[v][2])]
                    )
                )
            elif lista_variaveis[v][1] == "!":
                if (
                    resultados_linha[int(lista_variaveis[v][0])] == 0
                    or resultados_linha[int(lista_variaveis[v][2])] == 1
                ):
                    resultados_linha.append(1)
                else:
                    resultados_linha.append(0)
            elif lista_variaveis[v][1] == "$":
                if (
                    resultados_linha[int(lista_variaveis[v][0])]
                    == resultados_linha[int(lista_variaveis[v][2])]
                ):
                    resultados_linha.append(1)
                else:
                    resultados_linha.append(0)
        print(resultados_linha)
    print()
