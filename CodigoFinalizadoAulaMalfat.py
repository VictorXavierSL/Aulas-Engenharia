import pygame
import math
import random
import heapq
import time
class Edge:
    def __init__(self, target, weight):
        self.target = target
        self.weight = weight
        

class Vertex:
    def __init__(self, name):
        self.name = name
        self.adjacents = []
        self.x = 0 
        self.y = 0
        
    def addEdge(self, target, weight):
        self.adjacents.append(Edge(target, weight))
        

class Graph:
    
    locais = [
    'a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3', 'd1', 'd2', 'd3',
    'e1', 'e2', 'e3', 'f1', 'f2', 'f3', 'g1', 'g2', 'g3', 'h1', 'h2', 'h3',
    'i1', 'i2', 'i3', 'j1', 'j2', 'j3', 'k1', 'k2', 'k3', 'l1', 'l2', 'l3',
    'm1', 'm2', 'm3', 'n1', 'n2', 'n3']
        
    
    def __init__(self):
        self.vertices = {}
        
    def addVertex(self, name):
        if name not in self.vertices:
            self.vertices[name] = Vertex(name)
            
    def addEdge(self, source, target, weight):
        if source not in self.vertices:
            self.addVertex(source)
        if target not in self.vertices:
            self.addVertex(target)
        self.vertices[source].addEdge(target, weight) 
    
    def findPath(self, start_node, target_node):
        """ Encontra o caminho mais curto usando o Algoritmo de Dijkstra. """
        distances = {name: float('inf') for name in self.vertices}
        predecessors = {name: None for name in self.vertices}
        distances[start_node] = 0
        pq = [(0, start_node)]

        while pq:
            dist, current_node = heapq.heappop(pq)
            if current_node == target_node: break
            if dist > distances[current_node]: continue
            
            for edge in self.vertices[current_node].adjacents:
                new_dist = dist + edge.weight
                if new_dist < distances[edge.target]:
                    distances[edge.target] = new_dist
                    predecessors[edge.target] = current_node
                    heapq.heappush(pq, (new_dist, edge.target))
        
        path = []
        current = target_node
        while current is not None:
            path.append(current)
            current = predecessors.get(current)
        path.reverse()
        
        
        return path if path and path[0] == start_node else []
   
    def createGraph(self):
            
            cols, rows = 9, 6
            nodes = [chr(ord('a') + c) + str(r + 1) for c in range(cols) for r in range(rows)]
        
            for name in nodes: 
                self.addVertex(name)

            for c in range(cols):
                for r in range(rows):
                    node_name = chr(ord('a') + c) + str(r + 1)
                    self.vertices[node_name].x = 70 + c * 85
                    self.vertices[node_name].y = 70 + r * 110
                
                    if c + 1 < cols: self.addEdge(node_name, chr(ord('a') + c + 1) + str(r + 1), random.randint(1, 5))
                    if r + 1 < rows: self.addEdge(node_name, chr(ord('a') + c) + str(r + 2), random.randint(1, 5))

            for _ in range(len(nodes)):
                node1_name, node2_name = random.sample(nodes, 2)
                self.addEdge(node1_name, node2_name, random.randint(3, 8))
            
        
            num_saidas = random.randint(2, 4)
            
            potential_winners = [n for n in nodes if self.vertices[n].adjacents]
            self.winning_nodes = random.sample(potential_winners, min(num_saidas, len(potential_winners)))
            for node_name in self.winning_nodes: self.vertices[node_name].adjacents.clear()
            

    def selectRandonNode(self):
        return random.choice(list(self.vertices.keys()))
# --- Configurações do Pygame ---
pygame.init()
LARGURA, ALTURA = 1280, 800
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Fuga")
FONTE_NO, FONTE_UI, FONTE_CUSTO = pygame.font.Font(None, 24), pygame.font.Font(None, 36), pygame.font.Font(None, 22)
RELOGIO = pygame.time.Clock()

# Cores e Constantes
BRANCO, PRETO, AZUL, VERMELHO = (255, 255, 255), (0, 0, 0), (0, 100, 255), (255, 50, 50)
CINZA, VERDE, AMARELO, LARANJA_RESET = (180, 180, 180), (50, 200, 50), (255, 200, 0), (255, 140, 0)
RAIO_NO, PONTOS_DE_ACAO_MAX = 20, 10
RODADAS_MAX = 4

# --- Classe do Personagem ---
class personagen:
    def __init__(self, Node, cor, graph):
        self.no_atual = Node
        self.cor = cor
        self.custoMAX = PONTOS_DE_ACAO_MAX
        vertex = graph.vertices[Node]
        self.x, self.y = vertex.x, vertex.y

    def muve(self, destinoNode, custo, graph):
        if self.custoMAX >= custo:
            self.custoMAX -= custo
            self.no_atual = destinoNode
            new_vertex = graph.vertices[destinoNode]
            self.x, self.y = new_vertex.x, new_vertex.y
            return True
        return False

    def personagenImagen(self, tela):
        pygame.draw.circle(tela, self.cor, (self.x, self.y), RAIO_NO - 5)
    
    def resetPontosMuve(self):
        self.custoMAX = PONTOS_DE_ACAO_MAX

# --- Funções de Desenho ---
def draw_arrow(screen, color, start_pos, end_pos):
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    dist = math.hypot(dx, dy)
    if dist == 0: return

    # Normaliza o vetor de direção
    dx, dy = dx / dist, dy / dist

    # Calcula novos pontos de início e fim na borda dos círculos
    line_start = (start_pos[0] + dx * RAIO_NO, start_pos[1] + dy * RAIO_NO)
    line_end = (end_pos[0] - dx * RAIO_NO, end_pos[1] - dy * RAIO_NO)
    
    pygame.draw.line(screen, color, line_start, line_end, 2)
    
    # Desenha a cabeça da seta (um polígono preenchido)
    angle = math.atan2(dy, dx)
    arrow_size = 8
    p1 = (line_end[0] - arrow_size * math.cos(angle - 0.5), line_end[1] - arrow_size * math.sin(angle - 0.5))
    p2 = (line_end[0] - arrow_size * math.cos(angle + 0.5), line_end[1] - arrow_size * math.sin(angle + 0.5))
    pygame.draw.polygon(screen, color, (line_end, p1, p2))


def drawGraph(tela, graph):
    for vertex in graph.vertices.values():
        edge_color = VERDE if vertex.name in graph.winning_nodes else CINZA
        for edge in vertex.adjacents:
            v_start = vertex
            v_end = graph.vertices.get(edge.target)
            if v_end:
                # Passa as coordenadas como tuplos para draw_arrow
                draw_arrow(tela, edge_color, (v_start.x, v_start.y), (v_end.x, v_end.y))
                
                pos_custo = ((v_start.x + v_end.x) / 2 + 8, (v_start.y + v_end.y) / 2 - 8)
                texto_custo = FONTE_CUSTO.render(str(edge.weight), True, PRETO)
                rect_custo = texto_custo.get_rect(center=pos_custo)
                pygame.draw.rect(tela, BRANCO, rect_custo.inflate(4, 4))
                tela.blit(texto_custo, rect_custo)

    for vertex in graph.vertices.values():
        cor_no = VERDE if vertex.name in graph.winning_nodes else BRANCO
        pygame.draw.circle(tela, PRETO, (vertex.x, vertex.y), RAIO_NO)
        pygame.draw.circle(tela, cor_no, (vertex.x, vertex.y), RAIO_NO - 3)
        texto = FONTE_NO.render(vertex.name, True, PRETO)
        tela.blit(texto, texto.get_rect(center=(vertex.x, vertex.y)))


def drawUI(tela, jogador, perseguidor, turno, mensagem, rodada):
    pygame.draw.rect(tela, BRANCO, (0, ALTURA - 80, LARGURA, 80))
    pygame.draw.line(tela, PRETO, (0, ALTURA - 80), (LARGURA, ALTURA - 80), 3)
    tela.blit(FONTE_UI.render(f"Jogador PA: {jogador.custoMAX}", True, AZUL), (20, ALTURA - 60))
    tela.blit(FONTE_UI.render(f"Inimigo PA: {perseguidor.custoMAX}", True, VERMELHO), (240, ALTURA - 60))
    tela.blit(FONTE_UI.render(f"Rodada: {rodada}/{RODADAS_MAX}", True, PRETO), (480, ALTURA-60))
    texto_turno = FONTE_UI.render("Sua Vez" if turno == 'jogador' else "Vez do Inimigo", True, VERDE if turno == 'jogador' else VERMELHO)
    tela.blit(texto_turno, texto_turno.get_rect(center=(LARGURA / 2 + 100, 40)))
    if mensagem:
        cor_fundo = VERDE if "Vitória" in mensagem else PRETO
        pygame.draw.rect(tela, cor_fundo, (LARGURA/2 - 250, ALTURA/2 - 50, 500, 100), border_radius=15)
        texto_msg = FONTE_UI.render(mensagem, True, BRANCO)
        tela.blit(texto_msg, texto_msg.get_rect(center=(LARGURA/2, ALTURA/2)))

def drawBotao_passar(tela):
    rect = pygame.Rect(LARGURA - 220, ALTURA - 65, 200, 50)
    pygame.draw.rect(tela, AMARELO, rect, border_radius=10)
    pygame.draw.rect(tela, PRETO, rect, 3, border_radius=10)
    texto = FONTE_UI.render("Passar a Vez", True, PRETO)
    tela.blit(texto, texto.get_rect(center=rect.center))
    return rect

def drawBotao_reset(tela):
    rect = pygame.Rect(LARGURA - 440, ALTURA - 65, 200, 50)
    pygame.draw.rect(tela, LARANJA_RESET, rect, border_radius=10)
    pygame.draw.rect(tela, PRETO, rect, 3, border_radius=10)
    texto = FONTE_UI.render("Reiniciar Jogo", True, PRETO)
    tela.blit(texto, texto.get_rect(center=rect.center))
    return rect

def iniciar_novo_jogo():
    graph = Graph()
    graph.createGraph()
    jogador = personagen(graph.selectRandonNode(), AZUL, graph)
    perseguidor = personagen(graph.selectRandonNode(), VERMELHO, graph)
    while jogador.no_atual == perseguidor.no_atual or jogador.no_atual in graph.winning_nodes:
        jogador = personagen(graph.selectRandonNode(), AZUL, graph)
    return graph, jogador, perseguidor, 'jogador', "", 1

# --- Loop Principal ---
def main():
    graph, jogador, perseguidor, turno, mensagem_jogo, rodada_atual = iniciar_novo_jogo()
    
    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if drawBotao_reset(TELA).collidepoint(event.pos):
                    graph, jogador, perseguidor, turno, mensagem_jogo, rodada_atual = iniciar_novo_jogo()
                    continue

                if turno == 'jogador' and not mensagem_jogo:
                    if drawBotao_passar(TELA).collidepoint(event.pos):
                        turno = 'perseguidor'
                        jogador.resetPontosMuve()
                        perseguidor.resetPontosMuve()
                        continue
                    
                    for vertex in graph.vertices.values():
                        if math.hypot(event.pos[0] - vertex.x, event.pos[1] - vertex.y) <= RAIO_NO:
                            custo = next((e.weight for e in graph.vertices[jogador.no_atual].adjacents if e.target == vertex.name), -1)
                            if custo != -1: 
                                jogador.muve(vertex.name, custo, graph)
                            break
        
        if turno == 'perseguidor' and not mensagem_jogo:
            pygame.time.delay(100)
            caminho = graph.findPath(perseguidor.no_atual, jogador.no_atual)
            
            if perseguidor.custoMAX > 0 and caminho and len(caminho) > 1:
                proximo_no = caminho[1]
                custo = next((e.weight for e in graph.vertices[perseguidor.no_atual].adjacents if e.target == proximo_no), float('inf'))
                
                if perseguidor.muve(proximo_no, custo, graph):
                    pass
                else:
                    turno = 'jogador'
                    rodada_atual += 1
                    jogador.resetPontosMuve()
                    perseguidor.resetPontosMuve()
            else:
                turno = 'jogador'
                rodada_atual += 1
                jogador.resetPontosMuve()
                perseguidor.resetPontosMuve()

        if not mensagem_jogo:
            if jogador.no_atual in graph.winning_nodes: mensagem_jogo = "Você escapou! Vitória!"
            elif jogador.no_atual == perseguidor.no_atual: mensagem_jogo = "Você foi apanhado! Fim de jogo."
            elif rodada_atual > RODADAS_MAX: mensagem_jogo = "O tempo acabou! Vitória!"
            
            if turno == 'jogador' and jogador.custoMAX <= 0:
                turno = 'perseguidor'
                jogador.resetPontosMuve()
                perseguidor.resetPontosMuve()

        TELA.fill(BRANCO)
        drawGraph(TELA, graph)
        drawUI(TELA, jogador, perseguidor, turno, mensagem_jogo, rodada_atual)
        jogador.personagenImagen(TELA)
        perseguidor.personagenImagen(TELA)
        
        if not mensagem_jogo:
            drawBotao_passar(TELA)
        drawBotao_reset(TELA)
        pygame.display.flip()

        RELOGIO.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
