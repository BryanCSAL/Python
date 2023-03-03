import random

nvl_desenvolvimento = int(input("Escreva o nivel de desenvolvimento da cidade: "))

if nvl_desenvolvimento < 5:
    armas_armaduras = random.randint(0, 2)
    joias = random.randint(0, 2)
    livros = random.randint(0, 2)
    artigos_magicos = random.randint(0, 2)
    ferramentas = random.randint(0, 2)
    comida = random.randint(1, 2)
    lojas = armas_armaduras + joias + livros + artigos_magicos + ferramentas + comida

    igrejas = random.randint(0, 3)

    guildas = random.randint(0, 2)

    mercenarismo = random.randint(0, 1)

    taverna_e_pousada = random.randint(1, 3)
    pousada = random.randint(0, 3)
    tavernas_pousadas = pousada + taverna_e_pousada

    feiras = random.randint(1, 2)

    racas = ["ELFO", "ANAO", "AARAKOCRA", "AASIMAR", "AVIANO", "BUGBEAR", "DRACONATO", "ETERGENITO", "FERAL", "FIRBOLG",
             "FORJADO BELICO", "GENASI", "GNOMO", "GOBLIN", "GOLIAS", "HALFLING", "HOBGOBLIN", "HOMEM-LAGARTO", "KENKU",
             "KHENRA", "KOBOLD", "KOR", "MEIO-ELFO", "MEIO-ORC", "MINOTAURO", "NAGA", "ORC", "TABAXI", "DOPPELGANGER",
             "TIEFLING", "TRITAO", "VAMPIRO", "VELDAKEN", "YUAN-TI"]

    nvl_preconceito = random.randint(0, 8)
    quantia_escolhas = (int(nvl_preconceito)) / 3
    preconceito_contra = random.choices(racas, k=int(quantia_escolhas))
    nvl_criminalidade = random.randint(3, 8)
    nvl_mercado_negro = 10 - nvl_criminalidade
    nvl_tlc_monstros = random.randint(0, 10)
    nvl_tlc_pet = random.randint(nvl_tlc_monstros, 10)
    nvl_protecao = 10 - nvl_criminalidade
    nvl_med_guardas = random.randint(2, 8)
    nvl_desigualdade = random.randint(2, 8)
    nvl_med_populacao = random.randint(1, nvl_med_guardas)
    nvl_urbano = random.randint(1, 10)
    capital_estimado = (random.randint(1, 7))
    if capital_estimado == 0:
        classe_mais_comum = "Miseravel"
    elif capital_estimado == 1:
        classe_mais_comum = "Muito pobre"
    elif capital_estimado < 5 and capital_estimado > 1:
        classe_mais_comum = "Pobre"
    elif capital_estimado < 15 and capital_estimado > 6:
        classe_mais_comum = "Modesto"
    elif capital_estimado < 30 and capital_estimado > 16:
        classe_mais_comum = "Confortavel"
    elif capital_estimado < 99 and capital_estimado > 31:
        classe_mais_comum = "Abundante"
    else:
        classe_mais_comum = "Aristocratico"
    habitantes = (random.randint(1, 3)) * 1.5
    formas_renda = ["pesca", "caca", "agricultura", "comercio", "mineracao", "coleta", "arte", "material intelectual", "turismo"]
    renda = random.choices(formas_renda, weights=[5, 10, 10, 1, 5, 5, 1, 1, 1], k=1)
    if renda == "coleta":
        renda = "Coleta e comercio"


    print(" ")
    print("--------------------------------------------------------------------")
    print(" ")
    print("Cidade subdesenvolvida de nivel " + str(nvl_desenvolvimento))
    print(" ")
    print("--------------------------------------------------------------------")
    print(" ")
    print("Quantidade de Lojas: " + str(lojas))
    print("Quantidade de Lojas de armas/armaduras: " + str(armas_armaduras))
    print("Quantidade de Joalherias: " + str(joias))
    print("Quantidade de Livrarias: " + str(livros))
    print("Quantidade de Lojas de artigos magicos: " + str(artigos_magicos))
    print("Quantidade de Lojas de ferramentas: " + str(ferramentas))
    print("Quantidade de Lojas de comida: " + str(comida))
    print(" ")
    print("--------------------------------------------------------------------")
    print(" ")
    print("Quantidade de Igrejas: " + str(igrejas))
    print("Nomes das Igrejas: NONE")
    print(" ")
    print("--------------------------------------------------------------------")
    print(" ")
    print("Quantidade de Guildas: " + str(guildas))
    print("Nomes das Guildas: NONE")
    print(" ")
    print("--------------------------------------------------------------------")
    print(" ")
    print("Quantidade de Grupos mercenarios: " + str(mercenarismo))
    print("Nomes das Grupos: NONE")
    print(" ")
    print("--------------------------------------------------------------------")
    print(" ")
    print("Quantidade de tavernas e pousadas: " + str(tavernas_pousadas))
    print("Quantidade de tavernas que sao pousadas: " + str(taverna_e_pousada))
    print("Quantidade de pousadas: " + str(pousada))
    print("Nomes das tavernas que sao pousadas: NONE")
    print("Nomes das pousadas: NONE")
    print(" ")
    print("--------------------------------------------------------------------")
    print(" ")
    print("Quantidade de Feiras: " + str(feiras))
    print("Nomes das Grupos: NONE")
    print(" ")
    print("--------------------------------------------------------------------")
    print(" ")
    print("Nivel de preconceito: " + str(nvl_preconceito))
    print("Preconceito contra: " + str(preconceito_contra))
    print("Nivel de criminalidade: " + str(nvl_criminalidade))
    print("Nivel de Mercado-negro: " + str(nvl_mercado_negro))
    print("Nivel de tolerancia a monstros nÃ£o controlados: " + str(nvl_tlc_monstros))
    print("Nivel de tolerancia Pets monstruosos: " + str(nvl_tlc_pet))
    print("Nivel de protecao: " + str(nvl_protecao))
    print("Nivel de medio dos guardas: " + str(nvl_med_guardas))
    print("Nivel de desenvolvimento: " + str(nvl_desenvolvimento))
    print("Nivel de desigualdade: " + str(nvl_desigualdade))
    print("Nivel de medio da populacao: " + str(nvl_med_populacao))
    print("Nivel de urbanizacao: " + str(nvl_urbano))
    print("Principal forma de renda: " + str(renda))
    print("Gasto estimado por individuo: " + str(capital_estimado) + " pratas")
    print("Habitantes: " + str(habitantes) + " mil")
    print("Estilo de vida da populacao em media: " + str(classe_mais_comum))

elif 5 < nvl_desenvolvimento < 8:
    armas_armaduras = random.randint(1, 4)
    joias = random.randint(1, 4)
    livros = random.randint(1, 4)
    artigos_magicos = random.randint(1, 4)
    ferramentas = random.randint(1, 4)
    comida = random.randint(1, 4)
    lojas = armas_armaduras + joias + livros + artigos_magicos + ferramentas + comida

    igrejas = random.randint(1, 4)

    guildas = random.randint(1, 4)

    mercenarismo = random.randint(1, 3)

    taverna_e_pousada = random.randint(1, 4)
    pousada = random.randint(0, 4)
    tavernas_pousadas = pousada + taverna_e_pousada

    feiras = random.randint(1, 3)

    racas = ["ELFO", "ANAO", "AARAKOCRA", "AASIMAR", "AVIANO", "BUGBEAR", "DRACONATO", "ETERGENITO", "FERAL", "FIRBOLG",
             "FORJADO BELICO", "GENASI", "GNOMO", "GOBLIN", "GOLIAS", "HALFLING", "HOBGOBLIN", "HOMEM-LAGARTO", "KENKU",
             "KHENRA", "KOBOLD", "KOR", "MEIO-ELFO", "MEIO-ORC", "MINOTAURO", "NAGA", "ORC", "TABAXI", "DOPPELGANGER",
             "TIEFLING", "TRITAO", "VAMPIRO", "VELDAKEN", "YUAN-TI"]

    nvl_preconceito = random.randint(0, 6)
    quantia_escolhas = (int(nvl_preconceito)) / 3
    preconceito_contra = random.choices(racas, k=int(quantia_escolhas))
    nvl_criminalidade = random.randint(0, 7)
    nvl_mercado_negro = 10 - nvl_criminalidade
    nvl_tlc_monstros = random.randint(0, 10)
    nvl_tlc_pet = random.randint(nvl_tlc_monstros, 10)
    if nvl_tlc_pet < 10:
        nvl_tlc_pet = nvl_tlc_pet + 1
    nvl_protecao = 10 - nvl_criminalidade
    nvl_med_guardas = random.randint(4, 12)
    nvl_desigualdade = random.randint(1, 7)
    nvl_med_populacao = random.randint(1, nvl_med_guardas)
    nvl_urbano = random.randint(3, 10)
    capital_estimado = (random.randint(4, 15))
    if capital_estimado == 0:
        classe_mais_comum = "Miseravel"
    elif capital_estimado == 1:
        classe_mais_comum = "Muito pobre"
    elif 5 > capital_estimado > 1:
        classe_mais_comum = "Pobre"
    elif 15 > capital_estimado > 6:
        classe_mais_comum = "Modesto"
    elif 30 > capital_estimado > 16:
        classe_mais_comum = "Confortavel"
    elif 99 > capital_estimado > 31:
        classe_mais_comum = "Abundante"
    else:
        classe_mais_comum = "Aristocratico"
    habitantes = (random.randint(3, 7)) * 1.5
    formas_renda = ["pesca", "caca", "agricultura", "comercio", "mineracao", "coleta", "arte", "material intelectual", "turismo", "duplo"]
    formas_renda_dupla = ["pesca", "caca", "agricultura", "comercio", "mineracao", "coleta", "arte", "material intelectual", "turismo"]
    renda = random.choices(formas_renda, weights=[5, 10, 10, 10, 5, 1, 5, 5, 5, 3], k=1)
    if renda == "coleta":
        renda = "Coleta e comercio"
    elif renda == "duplo":
        renda = random.choices(formas_renda_dupla, weights=[5, 10, 10, 10, 5, 1, 5, 5, 5], k=2)

    print(" ")
    print("--------------------------------------------------------------------")
    print(" ")
    print("Cidade Emergente de nivel " + str(nvl_desenvolvimento))
    print(" ")
    print("--------------------------------------------------------------------")
    print(" ")
    print("Quantidade de Lojas: " + str(lojas))
    print("Quantidade de Lojas de armas/armaduras: " + str(armas_armaduras))
    print("Quantidade de Joalherias: " + str(joias))
    print("Quantidade de Livrarias: " + str(livros))
    print("Quantidade de Lojas de artigos magicos: " + str(artigos_magicos))
    print("Quantidade de Lojas de ferramentas: " + str(ferramentas))
    print("Quantidade de Lojas de comida: " + str(comida))
    print(" ")
    print("--------------------------------------------------------------------")
    print(" ")
    print("Quantidade de Igrejas: " + str(igrejas))
    print("Nomes das Igrejas: NONE")
    print(" ")
    print("--------------------------------------------------------------------")
    print(" ")
    print("Quantidade de Guildas: " + str(guildas))
    print("Nomes das Guildas: NONE")
    print(" ")
    print("--------------------------------------------------------------------")
    print(" ")
    print("Quantidade de Grupos mercenarios: " + str(mercenarismo))
    print("Nomes das Grupos: NONE")
    print(" ")
    print("--------------------------------------------------------------------")
    print(" ")
    print("Quantidade de tavernas e pousadas: " + str(tavernas_pousadas))
    print("Quantidade de tavernas que sao pousadas: " + str(taverna_e_pousada))
    print("Quantidade de pousadas: " + str(pousada))
    print("Nomes das tavernas que sao pousadas: NONE")
    print("Nomes das pousadas: NONE")
    print(" ")
    print("--------------------------------------------------------------------")
    print(" ")
    print("Quantidade de Feiras: " + str(feiras))
    print("Nomes das Grupos: NONE")
    print(" ")
    print("--------------------------------------------------------------------")
    print(" ")
    print("Nivel de preconceito: " + str(nvl_preconceito))
    print("Preconceito contra: " + str(preconceito_contra))
    print("Nivel de criminalidade: " + str(nvl_criminalidade))
    print("Nivel de Mercado-negro: " + str(nvl_mercado_negro))
    print("Nivel de tolerancia a monstros nÃ£o controlados: " + str(nvl_tlc_monstros))
    print("Nivel de tolerancia Pets monstruosos: " + str(nvl_tlc_pet))
    print("Nivel de protecao: " + str(nvl_protecao))
    print("Nivel de medio dos guardas: " + str(nvl_med_guardas))
    print("Nivel de desenvolvimento: " + str(nvl_desenvolvimento))
    print("Nivel de desigualdade: " + str(nvl_desigualdade))
    print("Nivel de medio da populacao: " + str(nvl_med_populacao))
    print("Nivel de urbanizacao: " + str(nvl_urbano))
    print("Principal forma de renda: " + str(renda))
    print("Gasto estimado por individuo: " + str(capital_estimado) + " pratas")
    print("Habitantes: " + str(habitantes) + " mil")
    print("Estilo de vida da populacao em media: " + str(classe_mais_comum))

else:
    armas_armaduras = random.randint(2, 6)
    joias = random.randint(2, 6)
    livros = random.randint(2, 6)
    artigos_magicos = random.randint(2, 6)
    ferramentas = random.randint(2, 6)
    comida = random.randint(2, 6)
    lojas = armas_armaduras + joias + livros + artigos_magicos + ferramentas + comida

    igrejas = random.randint(2, 5)

    guildas = random.randint(3, 7)

    mercenarismo = random.randint(2, 4)

    taverna_e_pousada = random.randint(3, 7)
    pousada = random.randint(0, 4)
    tavernas_pousadas = pousada + taverna_e_pousada

    feiras = random.randint(2, 4)

    racas = ["ELFO", "ANAO", "AARAKOCRA", "AASIMAR", "AVIANO", "BUGBEAR", "DRACONATO", "ETERGENITO", "FERAL", "FIRBOLG",
             "FORJADO BELICO", "GENASI", "GNOMO", "GOBLIN", "GOLIAS", "HALFLING", "HOBGOBLIN", "HOMEM-LAGARTO", "KENKU",
             "KHENRA", "KOBOLD", "KOR", "MEIO-ELFO", "MEIO-ORC", "MINOTAURO", "NAGA", "ORC", "TABAXI", "DOPPELGANGER",
             "TIEFLING", "TRITAO", "VAMPIRO", "VELDAKEN", "YUAN-TI"]

    nvl_preconceito = random.randint(0, 5)
    quantia_escolhas = (int(nvl_preconceito)) / 3
    preconceito_contra = random.choices(racas, k=int(quantia_escolhas))
    nvl_criminalidade = random.randint(0, 5)
    nvl_mercado_negro = 10 - nvl_criminalidade
    nvl_tlc_monstros = random.randint(0, 10)
    nvl_tlc_pet = random.randint(nvl_tlc_monstros, 10)
    if nvl_tlc_pet == 9 and nvl_tlc_pet < 10:
        nvl_tlc_pet = nvl_tlc_pet + 1
    elif nvl_tlc_pet < 9:
        nvl_tlc_pet = nvl_tlc_pet + 2
    nvl_protecao = 10 - nvl_criminalidade
    nvl_med_guardas = random.randint(6, 12)
    nvl_desigualdade = random.randint(1, 5)
    nvl_med_populacao = random.randint(1, nvl_med_guardas)
    nvl_urbano = random.randint(5, 10)
    capital_estimado = (random.randint(10, 31))
    if capital_estimado == 0:
        classe_mais_comum = "Miseravel"
    elif capital_estimado == 1:
        classe_mais_comum = "Muito pobre"
    elif 5 > capital_estimado > 1:
        classe_mais_comum = "Pobre"
    elif 15 > capital_estimado >= 5:
        classe_mais_comum = "Modesto"
    elif 30 > capital_estimado >= 15:
        classe_mais_comum = "Confortavel"
    elif 99 > capital_estimado >= 30:
        classe_mais_comum = "Abundante"
    else:
        classe_mais_comum = "Aristocratico"
    habitantes = (random.randint(3, 7)) * 1.5
    formas_renda = ["pesca", "caca", "agricultura", "comercio", "mineracao", "coleta", "arte", "material intelectual", "turismo", "duplo"]
    formas_renda_dupla = ["pesca", "caca", "agricultura", "comercio", "mineracao", "coleta", "arte", "material intelectual", "turismo"]
    renda = random.choices(formas_renda, weights=[1, 1, 10, 10, 1, 1, 5, 10, 10, 5], k=1)
    if renda == "coleta":
        renda = "Coleta e comercio"
    elif renda == "duplo":
        renda = random.choices(formas_renda, weights=[1, 1, 10, 10, 1, 1, 5, 10, 10], k=2)


    print(" ")
    print("--------------------------------------------------------------------")
    print(" ")
    print("Cidade Desenvolvida de nivel " + str(nvl_desenvolvimento))
    print(" ")
    print("--------------------------------------------------------------------")
    print(" ")
    print("Quantidade de Lojas: " + str(lojas))
    print("Quantidade de Lojas de armas/armaduras: " + str(armas_armaduras))
    print("Quantidade de Joalherias: " + str(joias))
    print("Quantidade de Livrarias: " + str(livros))
    print("Quantidade de Lojas de artigos magicos: " + str(artigos_magicos))
    print("Quantidade de Lojas de ferramentas: " + str(ferramentas))
    print("Quantidade de Lojas de comida: " + str(comida))
    print(" ")
    print("--------------------------------------------------------------------")
    print(" ")
    print("Quantidade de Igrejas: " + str(igrejas))
    print("Nomes das Igrejas: NONE")
    print(" ")
    print("--------------------------------------------------------------------")
    print(" ")
    print("Quantidade de Guildas: " + str(guildas))
    print("Nomes das Guildas: NONE")
    print(" ")
    print("--------------------------------------------------------------------")
    print(" ")
    print("Quantidade de Grupos mercenarios: " + str(mercenarismo))
    print("Nomes das Grupos: NONE")
    print(" ")
    print("--------------------------------------------------------------------")
    print(" ")
    print("Quantidade de tavernas e pousadas: " + str(tavernas_pousadas))
    print("Quantidade de tavernas que sao pousadas: " + str(taverna_e_pousada))
    print("Quantidade de pousadas: " + str(pousada))
    print("Nomes das tavernas que sao pousadas: NONE")
    print("Nomes das pousadas: NONE")
    print(" ")
    print("--------------------------------------------------------------------")
    print(" ")
    print("Quantidade de Feiras: " + str(feiras))
    print("Nomes das Grupos: NONE")
    print(" ")
    print("--------------------------------------------------------------------")
    print(" ")
    print("Nivel de preconceito: " + str(nvl_preconceito))
    print("Preconceito contra: " + str(preconceito_contra))
    print("Nivel de criminalidade: " + str(nvl_criminalidade))
    print("Nivel de Mercado-negro: " + str(nvl_mercado_negro))
    print("Nivel de tolerancia a monstros nÃ£o controlados: " + str(nvl_tlc_monstros))
    print("Nivel de tolerancia Pets monstruosos: " + str(nvl_tlc_pet))
    print("Nivel de protecao: " + str(nvl_protecao))
    print("Nivel de medio dos guardas: " + str(nvl_med_guardas))
    print("Nivel de desenvolvimento: " + str(nvl_desenvolvimento))
    print("Nivel de desigualdade: " + str(nvl_desigualdade))
    print("Nivel de medio da populacao: " + str(nvl_med_populacao))
    print("Nivel de urbanizacao: " + str(nvl_urbano))
    print("Principal forma de renda: " + str(renda))
    print("Gasto estimado por individuo: " + str(capital_estimado) + " pratas")
    print("Habitantes: " + str(habitantes) + " mil")
    print("Estilo de vida da populacao em media: " + str(classe_mais_comum))
