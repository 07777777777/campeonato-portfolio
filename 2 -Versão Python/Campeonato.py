times = {
    "Iguaçu": 0,
    "Vila Sandra": 0,
    "Novo Mundo": 0,
    "Capão Raso": 0
}

while True:
    print("\n=== CAMPEONATO AMADOR ===")
    print("1 - Registrar jogo")
    print("2 - Ver classificação")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        time1 = input("Time da casa: ")
        gols1 = int(input("Gols casa: "))

        time2 = input("Time visitante: ")
        gols2 = int(input("Gols visitante: "))

        if gols1 > gols2:
            times[time1] += 3
        elif gols2 > gols1:
            times[time2] += 3
        else:
            times[time1] += 1
            times[time2] += 1

        print("Jogo registrado!")

    elif opcao == "2":
        print("\nCLASSIFICAÇÃO")
        ranking = sorted(times.items(), key=lambda x: x[1], reverse=True)

        pos = 1
        for time, pontos in ranking:
            print(f"{pos}º {time} - {pontos} pts")
            pos += 1

    elif opcao == "3":
        print("Saindo...")
        break