# dell_it_academy_2024-1
Código desenvolvido para a solução do exercício técnico chamado "BALLIT CHAMPIONSHIP Campeonato de um jogo esquisito". Este desafio fez parte do processo seletivo de novos estagiários para o programa IT Academy de 2024/1, da empresa Dell em parceria com a PUCRS.

### Programa BALLIT CHAMPIONSHIP

Um sistema para gerenciar pontuações de um campeonato. Programado em Python 3.12.2 64-bit. Orientado a objetos. Com o programa é possível administrar uma competição com 8 a 16 times. Onde cada partida é iniciada com 50 pontos, entre dois times aleatórios. O cadastramento dos times permite adicionar e deletar quantos times quiser. Entretanto, o campeonato só iniciará com 8, 10, 12, 14 ou 16 times cadastrados. É possível administrar a partida com as funções de pontuação.  Ao final do campeonato o programa apresenta o vencedor, a tabela de pontos ordenada pelo total de pontuação e um CSV é salvo com os registros das partidas realizadas.

Instalação

    Passos para instalar o programa:

    1. Instale as dependências:

        Instale a versão do python 3.12.2 64-bit.

Uso

    Instruções de como utilizar o programa:

        1. Execute a classe main.py para iniciar.

        2. Navegue nos menus preenchendo conforme solicitado a cada passo:

            Primeiro menu: Menu de opções para o usuário. Responda com um número inteiro listado.

                """Menu de opções para o usuário."""
                opcao = 0

                while opcao != "9":

                    print("_"*60)
                    print("\nMENU INICIAL DE OPÇÕES \n\n"
                        "[1] - Cadastrar time \n" 
                        "[2] - Remover time \n" 
                        "[3] - Listar times \n" 
                        "[4] - Quantidade de times \n" 
                        "[5] - Iniciar campeonato \n" 
                        "[9] - Sair \n")
                    
                    opcao = input("Escolha uma opção: ")
            
            Segundo menu: Menu de partidas disponiveis para o usuário administrar. Responda com uma opção de partida com formato nome de time cadastrado + hífen + outro nome de time cadastrado, exemplo a-b.

                """Menu de partidas disponiveis para o usuário administrar.

                print("\nMENU PARTIDAS\n")
                Exemplo: 
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

                """O usuário escolhe uma partida para administrar."""
                opcao_partida = input("Escreva uma opção (Exemplo: A-B): ").strip().upper()

            Terceiro menu: Menu gerenciador de partida para o usuário administrar a partida. Responda com um número inteiro listado.

            """Menu gerenciador de partida para o usuário administrar a partida."""
            print("\nMENU GERENCIADOR DE PARTIDA\n\n"
                    f"[1] - Registrar Blot para o time {time1.nome}\n"
                    f"[2] - Registrar Blot para o time {time2.nome}\n"
                    f"[3] - Registrar Plif para o time {time1.nome}\n"
                    f"[4] - Registrar Plif para o time {time2.nome}\n"
                    f"[5] - Registrar penalidade Advrungh\n"
                    f"[9] - Encerrar Partida\n")

            opcao_jogo = input("Escolha uma opção: ")


