from match import Match

class MatchManager:
    """Classe MatchManager é um Gerenciador de partidas.
        
        @autor: Florensa Dimer
        Created: 06/08/2024
    """
    partidas: list

    def __init__(self):
        self._partidas = []

    @property
    def partidas(self):
        return self._partidas
    
    @partidas.setter
    def partidas(self, partida):
        self._partidas = partida

    """Método que cadastra uma partida em uma lista partidas."""
    def cadastrar_partida(self, time1, time2):
        nova_partida = Match(time1, time2)
        self._partidas.append(nova_partida)
    
    def listar_partidas(self):
        for partida in self._partidas:
            print(f"{partida.team1.nome} vs {partida.team2.nome} status:{partida.status}\n")
    
    def buscar_partida(self, nometime1, nometime2):
        for partida in self.partidas:
            if partida.team1.nome == nometime1 and partida.team2.nome == nometime2:
                return partida
        return None
    
    def verificar_fim_fase(self):
        for partida in self._partidas:
            if partida.status == False:
                return False
        return True
    
    def remover_partida(self, partida):
        self._partidas.remove(partida)

    def contar_partidas(self):
        return len(self._partidas)
