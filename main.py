import random

from teamManager import TeamManager
from matchManager import MatchManager

class Main:
    """Classe Main é a classe principal do programa.
        
        @autor: Florensa Dimer
        Created: 06/08/2024
    """
    titulo = " BALLIT CHAMPIONSHIP "
    print(titulo.center(60, '*'))
    print("_"*60)
    print("\nGERENCIADOR DE CAMPEONATO")
  
    teamManager = TeamManager()
    matchManager = MatchManager()

    """Lista de times que durante as fases do campeonato foram sendo eliminados."""
    historico_times = []

    """Cria um arquivo CSV para armazenar as partidas do campeonato."""
    with open ("partidas.csv", "a") as p:
                p.write(
                    "fase, time_1, time_2, pontos_time_1, pontos_time_2, vencedor_partida, score_time_1, score_time_2\n"      
                )

    """Menu de opções iniciais para o usuário."""
    opcao = 0

    while opcao != "9":

        print("_"*60)
        print("*"*60)
        print("\nMENU INICIAL DE OPÇÕES \n\n"
              "[1] - Cadastrar time \n" 
              "[2] - Remover time \n" 
              "[3] - Listar times \n" 
              "[4] - Quantidade de times \n" 
              "[5] - Iniciar campeonato \n" 
              "[9] - Sair \n")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            """Para cadastrar times o usuário:
            Primeiro é questionado quantos times deseja cadastrar. 
            Depois, é solicitado o nome, grito de guerra e ano de fundação de cada time."""
            
            print("_"*60)
            print("\nCADASTRAR TIME\n")

            qtd = input("Quantos times deseja cadastrar? \nDigite uma quantidade: ")

            """Se a quantidade de times for um número inteiro maior que 0, então os times poderão ser cadastrados."""
            try:
                qtd = int(qtd)
            except ValueError:
                print("\nErro: Quantidade inválida. Tente novamente.\n")
            else:
                if qtd > 0:
                                       
                    for i in range(qtd):

                        print(f"\nTIME {i+1}:")
                        nome = input(f"Nome: ")
                        grito = input(f"Grito de guerra: ")
                        ano_fundacao = input(f"Ano de fundação: ")

                        try:
                            ano_fundacao = int(ano_fundacao)
                        except ValueError:
                            print("\nErro: Ano de fundação inválido. Time não cadastrado.\n")
                                                        
                        else:
                            teamManager.cadastrar_time(nome.upper(), grito.upper(), ano_fundacao)
                else:
                    print("\nErro: Quantidade inválida. Tente novamente.\n")
                
        elif opcao == "2":

            """Para remover um time o usuário:
            Primeiro, digita o nome do time que deseja remover.
            Depois, o time é buscado na lista de times e se existir é então removido."""

            print("_"*60)
            print("\nREMOVER TIME\n")

            nome = input("Digite o nome do time que deseja remover: ").upper().strip()
            time = teamManager.buscar_time(nome)

            if time is not None:
                teamManager.remover_time(time)
                print("\nTime removido com sucesso.\n")
            else:
                print("\nTime não encontrado.\n")

        elif opcao == "3":

            """Para listar os times na tela."""

            print("_"*60)
            print("\nLISTAR TIMES\n")

            teamManager.listar_times()

        elif opcao == "4":

            """Para contar a quantidade de times cadastrados."""

            print("_"*60)
            print("\nQUANTIDADE DE TIMES\n")

            print(f"Quantidade de times: {teamManager.contar_times()} \n")

        elif opcao == "5":

            """Para iniciar partidas."""

            print("_"*60)
            print("\nINICIAR PARTIDAS\n\n"
                  "Regra: Cada campeonato necessariamente deve ter\n"
                  "no mínimo 8 times e no máximo 16 times e o \n"
                  "número total de times deve ser par.")
            
            """Se a quantidade de times for maior que 8 e menor que 16, e for par, o campeonato iniciará."""
            if teamManager.contar_times() >= 8 and teamManager.contar_times() <= 16:
                if teamManager.contar_times()%2 == 0:
                    print(f"\nCampeonato iniciado com sucesso! \nForam cadastrados o total de {teamManager.contar_times()} times.\n")

                    """Enquanto a quantidade de times for maior que 1, o usuário poderá administrar as partidas.
                    Se a quantidade de times for igual a 1, então o campeonato é finalizado e o time campeão é mostrado."""
                    
                    fase = 1
                    
                    while teamManager.contar_times() != 1:

                        print("_"*60)
                        print("*"*60)

                        print(f"\nINÍCIO DA {fase}º FASE DE PARTIDAS\n")
                        print(f"\nOrganizando partidas aleatórias ...\n")
                        
                        """Embaralhando a lista de times para que as partidas sejam aleatórias."""
                        random.shuffle(teamManager.times)

                        """Cadastrando as partidas.
                        Quando a quantidade de times é 10, 12 ou 14, sobra times sem partida nas fases.
                        Quando é 8 ou 16 times, todos os times jogam e o campeonato é perfeito.
                        Logo, para ter uma campeonato perfeito a primeira fase deve ser de 8 ou 16 times.
                        Para ter 8 times e campeonato perfeito, a primeira fase precisa eliminar a diferença.
                        Exemplo: Com 14 times cadastrados, 6 times sobram, então a primeira fase adiciona 6 partidas para elimina-los.
                                 Após isso, as fases seguintes são organizadas com 4 partidas, 2 partidas e 1 partida."""
                        qtd_times = teamManager.contar_times()
                        
                        if qtd_times == 10 or qtd_times == 12 or qtd_times == 14:
                            sobra_times = qtd_times - 8
                            
                            """Cadastrando as partidas quando acontece sobra de times."""
                            for i in range(0, sobra_times*2, 2):
                                matchManager.cadastrar_partida(teamManager.times[i], teamManager.times[i+1])
                        else:
                            """Cadastrando as partidas quando não acontece sobra de times."""
                            for i in range(0, len(teamManager.times), 2):
                                matchManager.cadastrar_partida(teamManager.times[i], teamManager.times[i+1])
                            
                        print("\nPartidas aleatórias organizadas com sucesso.\n")
                        print("_"*60)
                        print("\nINÍCIO DAS PARTIDAS\n")

                        """Enquanto tiver partidas não realizadas, o usuário poderá administrar as partidas."""
                        while matchManager.verificar_fim_fase() != True:

                            print("_"*60)
                            
                            print("\nMENU PARTIDAS\n")

                            """Menu de partidas disponiveis para o usuário administrar.                            
                            A vs B
                            C vs D
                            E vs F
                            G vs H
                            [1] - Registrar penalidade Advrungh"""

                            """Listando as partidas disponíveis que ainda não ocorreram."""
                            print("Partidas disponíveis para serem administradas: \n")

                            for partida in matchManager.partidas:
                                if partida.status == False:
                                    print(f"{partida.team1.nome} vs {partida.team2.nome}")

                            print('[1] - Registrar penalidade Advrungh')
                            
                            print("_"*60)

                            """O usuário escolhe uma partida para administrar."""
                            opcao_partida = input("Escreva uma opção (Exemplo: A-B): ").strip().upper()

                            if opcao_partida == "1":

                                """Registrar penalidade Advrungh para um time.
                                Se o time ainda não foi eliminado, então busca nos times atuais e registra a penalidade. 
                                Se o time já foi eliminado, então busca no histórico de times e e registra a penalidade.
                                Se o time não for encontrado, então é mostrado um erro."""

                                print("\nRegistrar penalidade Advrungh.\n")
                                nome = input("Digite o nome do time que cometeu a penalidade (Exemplo: A): ").upper().strip()
                                time = teamManager.buscar_time(nome)

                                if time is not None:
                                    score_atualizado = teamManager.registrar_advrungh(time)
                                    print(f"\n{time.nome} cometeu penalidade e perdeu 10 pontos no campeonato. \nScore atual: {score_atualizado}.\n")
                                else:
                                    time_encontrado = None
                                    for time in historico_times:
                                        if time.nome == nome:
                                            time_encontrado = time
                                    if time_encontrado is not None:
                                        score_atualizado = teamManager.registrar_advrungh(time_encontrado)
                                        print(f"\n{time_encontrado.nome} cometeu penalidade e perdeu 10 pontos no campeonato. \nScore atual: {score_atualizado}.\n")
                                    else:
                                        print("\nErro: Time não encontrado.\n")

                            else:
                                """Remove os espaços e separa os nomes dos times."""
                                opcao_partida = opcao_partida.replace(' ','').split("-")
                                
                                """Se entrada for válida, então segue."""
                                if len(opcao_partida) == 2:
                                    time1 = teamManager.buscar_time(opcao_partida[0])
                                    time2 = teamManager.buscar_time(opcao_partida[1])

                                    """Se os times existirem, então a partida será realizada."""
                                    if time1 is not None and time2 is not None:
                                        partida = matchManager.buscar_partida(time1.nome, time2.nome)
                                        
                                        """Se a partida existir, então a partida será iniciada."""
                                        if partida is not None:

                                            print("\nPartida iniciada.\n")
                                            print(f"                     {time1.nome} vs {time2.nome}\n")
                                            
                                            print("Placar inicial: ")
                                            print(f"{partida.team1.nome}    {partida.team2.nome}")
                                            print(f"{partida.pts_team1} x {partida.pts_team2}")
                   
                                            print("\nEstatísticas da partida:\n")

                                            
                                            print(f"                         Time:      {time1.nome}    |   {time2.nome}")

                                            print(f"Pontuação atual no campeonato:     {time1.score}    |   {time2.score}")

                                            """Comparando a média de pontos e penalidades dos times na partida.
                                            Se o time 1 tiver mais pontos, então será mostrado um sinal de + para time 1 e um sinal de - para time 2.
                                            Se o time 2 tiver mais pontos, então será mostrado um sinal de + para time 2 e um sinal de - para time 1.
                                            Se os times tiverem a mesma quantidade de pontos, então será mostrado um sinal de = para ambos os times."""
                                            if time1.calcular_media_pontos() > time2.calcular_media_pontos():
                                                print(f"Média de pontos por partida:         +   |   -   ")
                                            elif time2.calcular_media_pontos() > time1.calcular_media_pontos():
                                                print(f"Média de pontos por partida:         -   |   +   ")
                                            else:
                                                print(f"Média de pontos por partida:         =   |   =   ")

                                            """Comparando a média de penalidades dos times na partida.
                                            Se o time 1 tiver mais penalidades, então será mostrado um sinal de + para time 1 e um sinal de - para time 2.
                                            Se o time 2 tiver mais penalidades, então será mostrado um sinal de + para time 2 e um sinal de - para time 1.
                                            Se os times tiverem a mesma quantidade de penalidades, então será mostrado um sinal de = para ambos os times."""
                                            if time1.calcular_media_penalidades() > time2.calcular_media_penalidades():
                                                print("Média de penalidades por partida:    +   |   -   ")
                                            elif time2.calcular_media_penalidades() > time1.calcular_media_penalidades():
                                                print("Média de penalidades por partida:    -   |   +   ")
                                            else:
                                                print("Média de penalidades por partida:    =   |   =   ")

                                            """Menu gerenciador de partida para o usuário administrar a partida."""
                                            opcao_jogo = "0"

                                            while opcao_jogo != "9":
                                                
                                                print("_"*60)

                                                print("\nMENU GERENCIADOR DE PARTIDA\n\n"
                                                        f"[1] - Registrar Blot para o time {time1.nome}\n"
                                                        f"[2] - Registrar Blot para o time {time2.nome}\n"
                                                        f"[3] - Registrar Plif para o time {time1.nome}\n"
                                                        f"[4] - Registrar Plif para o time {time2.nome}\n"
                                                        f"[5] - Registrar penalidade Advrungh\n"
                                                        f"[9] - Encerrar Partida\n")

                                                opcao_jogo = input("Escolha uma opção: ")

                                                print("_"*60)

                                                if opcao_jogo == "1":
                                                    partida.registrar_blot_team1()
                                                    print(f"\n{time1.nome} marcou 5 pontos.\n")
                                                    print(f"Placar atual:")
                                                    print(f"{partida.team1.nome}    {partida.team2.nome}")
                                                    print(f"{partida.pts_team1} x {partida.pts_team2}")
                                                    
                                                elif opcao_jogo == "2":
                                                    partida.registrar_blot_team2()
                                                    print(f"\n{time2.nome} marcou 5 pontos.\n")
                                                    print(f"Placar atual:")
                                                    print(f"{partida.team1.nome}    {partida.team2.nome}")
                                                    print(f"{partida.pts_team1} x {partida.pts_team2}")

                                                elif opcao_jogo == "3":
                                                    partida.registrar_plif_team1()
                                                    print(f"\n{time1.nome} marcou 1 ponto.\n")
                                                    print(f"Placar atual:")
                                                    print(f"{partida.team1.nome}    {partida.team2.nome}")
                                                    print(f"{partida.pts_team1} x {partida.pts_team2}")

                                                elif opcao_jogo == "4":
                                                    partida.registrar_plif_team2()
                                                    print(f"\n{time2.nome} marcou 1 ponto.\n")
                                                    print(f"Placar atual:")
                                                    print(f"{partida.team1.nome}    {partida.team2.nome}")
                                                    print(f"{partida.pts_team1} x {partida.pts_team2}")

                                                elif opcao_jogo == "5":
                                                    print("\nRegistrar penalidade Advrungh.\n")
                                                    nome = input("Digite o nome do time que cometeu a penalidade (Exemplo: A): ").upper().strip()
                                                    time = teamManager.buscar_time(nome)

                                                    if time is not None:
                                                        score_atualizado = teamManager.registrar_advrungh(time)
                                                        print(f"\n{time.nome} cometeu penalidade e perdeu 10 pontos no campeonato. \nScore atual: {score_atualizado}.\n")
                                                    else:
                                                        time_encontrado = None
                                                        for time in historico_times:
                                                            if time.nome == nome:
                                                                time_encontrado = time
                                                        if time_encontrado is not None:
                                                            score_atualizado = teamManager.registrar_advrungh(time_encontrado)
                                                            print(f"\n{time_encontrado.nome} cometeu penalidade e perdeu 10 pontos no campeonato. \nScore atual: {score_atualizado}.\n")
                                                        else:
                                                            print("\nErro: Time não encontrado.\n")

                                                elif opcao_jogo == "9":
                                                                                                        
                                                    """Se a opção for 9, então a partida será encerrada.
                                                    Se houver um vencedor, então o time vencedor será apresentado e o time perdedor será removido dos times.
                                                    Se houve empate, então será feito o procedimento Grusht de desempate."""
                                                    
                                                    """Contando a quantidade de partidas que cada time jogou."""
                                                    partida.team1.count_partidas += 1
                                                    partida.team2.count_partidas += 1

                                                    resultado = partida.registrar_resultado()

                                                    if resultado is not None:
                                                        print(f"\nO time vencedor é: {resultado.nome}!\n")
                                                        """Adicionando o time perdedor no histórico de times antes de eliminar do campeonato."""
                                                        historico_times.append(partida.loser)
                                                        teamManager.remover_time(partida.loser)
                                                        print(f"Placar final:\n")
                                                        print(f"{partida.team1.nome}    {partida.team2.nome}")
                                                        print(f"{partida.pts_team1} x {partida.pts_team2}")
                                                        print(f"                         Time:      {time1.nome}    |   {time2.nome}")

                                                        print(f"Pontuação atual no campeonato:     {time1.score}    |   {time2.score}")
                                                        partida.salvar_partida_csv(resultado.nome, fase)

                                                    else:

                                                        """Se houver empate, então será feito o procedimento Grusht de desempate.
                                                        O usuário terá que escolher o time vencedor.
                                                        Se o time vencedor for encontrado, então o time vencedor será mostrado e o time perdedor será eliminado.
                                                        Se o time vencedor não for encontrado, então o usuário terá chances de digitar o nome correto."""
                                                        print("\nEmpate.\nOs times passarão pelo procedimento de desempate Grusht.\n")
                                                        print(f"Gripo de guerra do time {partida.team1.nome}: {partida.team1.grito}!!!\n"
                                                                f"Gripo de guerra do time {partida.team2.nome}: {partida.team2.grito}!!!\n")
                                                        print(f"O time que gritar mais alto vence no intervalo de 1 minuto.\n")
                                                        print(f"\nCRONOMÊTRO INICIADO\n")
                                                        input("Pressione Enter para parar o cronomêtro:\n")
                                                        print(f"TEMPO ENCERRADO.\n")

                                                        vencedor = ""
                                                                    
                                                        """Se o time vencedor não for encontrado, então o usuário terá que digitar o nome correto."""  
                                                        while vencedor != "1" and vencedor != "2":  
                                                        
                                                            print(f"Segundo o decibelímetro, o time vencedor é? \n[1] - {partida.team1.nome} \n[2] - {partida.team2.nome}\n")
                                                            vencedor = input(f"Escolha uma opção: ")
                                                            
                                                            
                                                            if vencedor == "1":
                                                                print(f"\nO time {partida.team1.nome} marcou 3 pontos.\n")
                                                                print(f"\nO time vencedor é: {partida.team1.nome}!\n")

                                                                partida.registrar_grusht(vencedor)
                                                                
                                                                partida.salvar_partida_csv(partida.team1.nome, fase)
                                                                
                                                                """Adicionando o time perdedor no histórico de times antes de eliminar do campeonato."""
                                                                historico_times.append(partida.loser)
                                                                teamManager.remover_time(partida.loser)
                                                                
                                                                print(f"Placar final:\n")
                                                                print(f"{partida.team1.nome}    {partida.team2.nome}")
                                                                print(f"{partida.pts_team1} x {partida.pts_team2}")

                                                                print(f"                         Time:      {time1.nome}    |   {time2.nome}")

                                                                print(f"Pontuação atual no campeonato:     {time1.score}    |   {time2.score}")

                                                            elif vencedor == "2":  
                                                                print(f"\nO time vencedor é: {partida.team2.nome}!\n")
                                                                print(f"\nO time {partida.team2.nome} marcou 3 pontos.\n")
                                                                
                                                                partida.registrar_grusht(vencedor)
                                                                                                                                
                                                                partida.salvar_partida_csv(partida.team2.nome, fase)

                                                                """Adicionando o time perdedor no histórico de times antes de eliminar do campeonato."""
                                                                historico_times.append(partida.loser)
                                                                teamManager.remover_time(partida.loser)

                                                                print(f"Placar final:\n")
                                                                print(f"{partida.team1.nome}    {partida.team2.nome}")
                                                                print(f"{partida.pts_team1} x {partida.pts_team2}")

                                                                print(f"                         Time:      {time1.nome}    |   {time2.nome}")

                                                                print(f"Pontuação atual no campeonato:     {time1.score}    |   {time2.score}")
                                                            else:
                                                                print("\nErro: Opção de time inválida.\n")


                                                    print("\nPartida encerrada com sucesso.")
                                                    print("Saindo do menu gerenciador de partida.\n")

                                                else:
                                                    print("\nErro: Opção inválida. Tente novamente.\n")
                                        else:
                                            print("\nErro: Partida não encontrada.\n")
                                    else:
                                        print("\nErro: Time não encontrado.\n")
                                else:
                                    print("\nErro: Digite uma partida válida. Tente novamente.\n")
                        fase += 1
                        print("_"*60)
                        print("*"*60)
                        print("\nFIM DE FASE\n")

     
                    print("_"*60)
                    print("*"*60)

                    """Fim campeonato."""
                    
                    """Salva o ultimo time a jogar."""
                    historico_times.append(teamManager.times[0])

                    """Ordena os times pelo score."""
                    historico_times = sorted(historico_times, key=lambda times: times.score, reverse=True)

                    print(f"\nFIM DO CAMPEONATO. \n\nO time {historico_times[0].nome} é campeão do Internacional de BALLIT CHAMPIONSHIP com total de {historico_times[0].score} pontos!!!\n"
                          f"A torcida vai a loucura cantando seu grito de guerra: {historico_times[0].grito}!!!\n")
                    
                    
                    print("_"*60)
                                    
                    print("\nTABELA FINAL\n")

                    """Mostrando a tabela final de times pelo score."""
                    print("Time | Blots | Plifs | Advrunghs |Score")
                    for i in range(len(historico_times)):
                        print(f"{historico_times[i].nome} | {historico_times[i].count_blots} | {historico_times[i].count_plifs} | {historico_times[i].count_advrunghs} | {historico_times[i].score}")
                    
                    print("_"*60)
                    print("\nFIM DO PROGRAMA.\n")
                    print("_"*60)
                    print("*"*60)

                    opcao = "9"
                else:
                    print("\nErro: Quantidade impar de times. Adicione ou remova uma equipe e tente novamente.\n")
            else:
                print("\nErro: Quantidade de times inválida. Adicione times para ter no mínimo 8 e no máximo 16 times. Tente novamente.\n")

        elif opcao == "9":
            print("_"*40)
            print("\nPrograma finalizado.\n")
        else:
            print("\nErro: Opção inválida. Tente novamente.\n")
    