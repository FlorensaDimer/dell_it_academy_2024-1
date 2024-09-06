from team import Team

class TeamManager:
    """Classe teamManager é um Gerenciador de times.
    
        @autor: Florensa Dimer
        Created: 06/08/2024
    """
    times: list

    def __init__(self):
        self._times = []

    @property
    def times(self):
        return self._times
    
    @times.setter
    def times(self, times):
        self._times = times

    def cadastrar_time(self, nome, grito, ano_fundacao):
        novo_time = Team(nome, grito, ano_fundacao)
        self._times.append(novo_time)
        print("\nTime adicionado com sucesso.\n")

    
    def contar_times(self):
        return len(self._times)

    def listar_times(self):
        for time in self._times:
            print(time)

    def buscar_time(self, nome):
        for time in self._times:
            if time.nome == nome:
                return time
        return None
    
    def remover_time(self, time):
        self._times.remove(time)

    """Método que registra subtração de pontos para o time que cometeu penalidade."""
    def registrar_advrungh(self, time):
        time.score -= 10
        time.count_advrunghs += 1
        return time.score