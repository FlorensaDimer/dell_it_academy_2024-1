class Team:
    """A classe time é responsável por armazenar as informações de time.
    
        @autor: Florensa Dimer
        Created: 06/08/2024
    """
    nome: str
    grito: str
    ano_fundacao: int
    score: int
    count_blots: int
    count_plifs: int
    count_advrunghs: int
    count_grusht: int
    count_partidas: int

    def __init__(self, nome, grito, ano_fundacao, score=0, count_blots=0, count_plifs=0, count_advrunghs=0, count_grusht=0, count_partidas=0):
        self._nome = nome
        self._grito = grito
        self._ano_fundacao = ano_fundacao
        self._score = score
        self._count_blots = count_blots
        self._count_plifs = count_plifs
        self._count_advrunghs = count_advrunghs
        self._count_grusht = count_grusht
        self._count_partidas = count_partidas
        
    """Métodos de acesso aos atributos da classe"""
    @property
    def nome(self):
        return self._nome
    
    @property
    def grito(self):
        return self._grito
    
    @property
    def ano_fundacao(self):
        return self._ano_fundacao
    
    @property
    def score(self):
        return self._score
    
    @property
    def count_blots(self):
        return self._count_blots
    
    @property
    def count_plifs(self):
        return self._count_plifs
    
    @property
    def count_advrunghs(self):
        return self._count_advrunghs
    
    @property
    def count_grusht(self):
        return self._count_grusht
    
    @property
    def count_partidas(self):
        return self._count_partidas
    
    """Métodos setter que permitem a modificação dos atributos da classe"""
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @grito.setter
    def grito(self, grito):
        self._grito = grito

    @ano_fundacao.setter
    def ano_fundacao(self, ano_fundacao):
        self._ano_fundacao = ano_fundacao

    @score.setter
    def score(self, score):
        self._score = score
    
    @count_blots.setter
    def count_blots(self, count_blots):
        self._count_blots = count_blots

    @count_plifs.setter
    def count_plifs(self, count_plifs):
        self._count_plifs = count_plifs

    @count_advrunghs.setter
    def count_advrunghs(self, count_advrunghs):
        self._count_advrunghs = count_advrunghs

    @count_grusht.setter
    def count_grusht(self, count_grusht):
        self._count_grusht = count_grusht

    @count_partidas.setter
    def count_partidas(self, count_partidas):
        self._count_partidas = count_partidas
    
    """Método que calcula a média de pontos obtidos pelo time por partida.
    Somente pontuação de blots e grusht serão consideradas para o cálculo dessa média.
    Sem considerar pontos por penalidades do adversário."""
    def calcular_media_pontos(self):
        if self._count_partidas == 0:
            return 0
        return (self.count_blots + self.count_grusht) / self.count_partidas
    
    def calcular_media_penalidades(self):
        if self._count_partidas == 0:
            return 0
        return self.count_advrunghs / self.count_partidas

    """Método que retorna as informações do time"""
    def __str__(self):
        return f"Nome: {self._nome}\nGrito: {self._grito}\nAno de Fundação: {self._ano_fundacao}\nScore: {self._score}\nBlots: {self._count_blots}\nPlifs: {self._count_plifs}\nAdvrunghs: {self._count_advrunghs}\ngrushts: {self._count_grusht}\nPartidas: {self._count_partidas}\n"