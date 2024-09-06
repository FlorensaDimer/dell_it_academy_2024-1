from team import Team

class Match:
    """A classe Match é responsável por armazenar as informações de uma partida.    

        @autor: Florensa Dimer
        Created: 06/08/2024
    """
    team1: Team
    team2: Team
    pts_team1: int
    pts_team2: int
    status: bool
    winner: Team
    loser: Team
    
    def __init__(self, team1, team2, pts_team1=50, pts_team2=50, status=False, winner=None, loser=None):
        self.team1 = team1
        self.team2 = team2
        self.pts_team1 = pts_team1
        self.pts_team2 = pts_team2
        self.status = status
        self.winner = winner
        self.loser = loser

    @property
    def team1(self):
        return self._team1
    
    @property
    def team2(self):
        return self._team2
    
    @property
    def pts_team1(self):
        return self._pts_team1
    
    @property
    def pts_team2(self):
        return self._pts_team2
    
    @property
    def status(self):
        return self._status
    
    @property
    def winner(self):
        return self._winner
    
    @property
    def loser(self):
        return self._loser
    
    @team1.setter
    def team1(self, team1):
        self._team1 = team1

    @team2.setter 
    def team2(self, team2):
        self._team2 = team2

    @pts_team1.setter
    def pts_team1(self, pts_team1):
        self._pts_team1 = pts_team1

    @pts_team2.setter
    def pts_team2(self, pts_team2):
        self._pts_team2 = pts_team2
    
    @status.setter
    def status(self, status):
        self._status = status
    
    @winner.setter
    def winner(self, winner):
        self._winner = winner

    @loser.setter
    def loser(self, loser):
        self._loser = loser

    """Método que registra soma de 5 pontos para o time 1."""
    def registrar_blot_team1(self):
        self.pts_team1 += 5
        self.team1.count_blots += 1

    """Método que registra soma de 5 pontos para o time 2."""
    def registrar_blot_team2(self):
        self.pts_team2 += 5
        self.team2.count_blots += 1

    """Método que registra soma de 1 ponto para o time 1."""
    def registrar_plif_team1(self):
        self.pts_team1 += 1
        self.team1.count_plifs += 1

    """Método que registra soma de 1 pontos para o time 2."""
    def registrar_plif_team2(self):
        self.pts_team2 += 1
        self.team2.count_plifs += 1
    
    """Método que registra soma de 3 pontos para o time que ganhou o desempate."""
    def registrar_grusht(self, vencedor):
        if vencedor == "1":
            self.pts_team1 += 3
            self.team1.score += 3
            self.team1.count_grusht += 1
            self.winner = self.team1
            self.loser = self.team2
        elif vencedor == "2":
            self.pts_team2 += 3
            self.team2.score += 3
            self.team2.count_grusht += 1
            self.winner = self.team2
            self.loser = self.team1
        
    
    """Método que registra o resultado da partida em score dos times.
    Se o time 1 tiver mais ponyos, o time 1 é o vencedor e o time 2 é perdedor e retorna time 1.
    Se o time 2 tiver mais ponyos, o time 2 é o vencedor e o time 1 é perdedor e retorna o time 2.
    Se os dois times tiverem a mesma quantidade de pontos, não tem vencedor e nem perdedor e retorna None.
    Muda o status da partida para True."""
    def registrar_resultado(self):

        self.team1.score += self.pts_team1
        self.team2.score += self.pts_team2
        
        """Verifica se o time 1 é o vencedor."""
        if  self.pts_team1 > self.pts_team2:
            self.winner = self.team1
            self.loser = self.team2
            self.status = True
            return self.winner
                        
        elif self.pts_team2 > self.pts_team1:
            self.winner = self.team2
            self.loser = self.team1
            self.status = True
            return self.winner
        else:
            self.status = True
            return None
        
    """Método que salva a partida em um arquivo CSV."""
    def salvar_partida_csv(self, vencedor, fase):
        with open ("partidas.csv", "a") as u:
                u.write(
                    str(fase) + ", " + \
                    self.team1.nome + ", " + \
                    self.team2.nome + ", " + \
                    str(self.pts_team1) + ", " + \
                    str(self.pts_team2) + ", " + \
                    vencedor + ", " + \
                    str(self.team1.score) + ", " + \
                    str(self.team2.score) + "\n"               
                )

    def __str__(self):
        return f"\nTime 1: {self.team1.nome} Placar: {self.team1.score}\n Time 2: {self.team2.nome} Placar: {self.team2.score}\n"
    
