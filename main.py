import pygame
import random
import math

# Definindo cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
GREEN = (0, 128, 0)

# Definindo as configurações do ambiente
GRID_SIZE = 10
CELL_SIZE = 50
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE
NUM_DIRTS = 20  # Número de sujeiras a serem geradas

# Classe para representar o agente aspirador de pó
class VacuumAgent:
    def __init__(self):
        self.x = random.randint(0, GRID_SIZE - 1)
        self.y = random.randint(0, GRID_SIZE - 1)

    def move_towards(self, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y

        # Algoritmo de Bresenham
        sx = 1 if dx > 0 else -1
        sy = 1 if dy > 0 else -1
        dx = abs(dx)
        dy = abs(dy)
        err = dx - dy

        while self.x != target_x or self.y != target_y:
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                self.x += sx
            if e2 < dx:
                err += dx
                self.y += sy

# Inicializando o Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ambiente do Aspirador de Pó")

# Função para desenhar a grade e as sujeiras
def draw_environment(agent, dirt_positions):
    screen.fill(WHITE)
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)
            if (x, y) in dirt_positions:
                pygame.draw.circle(screen, GREEN, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), 10)
    pygame.draw.circle(screen, ORANGE, (agent.x * CELL_SIZE + CELL_SIZE // 2, agent.y * CELL_SIZE + CELL_SIZE // 2), 20)

# Instanciando o agente aspirador de pó
vacuum_agent = VacuumAgent()

# Lista para armazenar as posições das sujeiras
dirt_positions = []

# Função para gerar sujeiras aleatoriamente
def generate_dirt():
    global dirt_positions
    dirt_positions = []
    for _ in range(NUM_DIRTS):
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        dirt_positions.append((x, y))

generate_dirt()  # Gerando sujeiras inicialmente

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Verificando a posição mais próxima de sujeira
    closest_dirt = min(dirt_positions, key=lambda dirt: math.sqrt((dirt[0] - vacuum_agent.x) ** 2 + (dirt[1] - vacuum_agent.y) ** 2))

    # Movendo o agente em direção à sujeira mais próxima
    vacuum_agent.move_towards(closest_dirt[0], closest_dirt[1])

    # Removendo a sujeira se o agente estiver na mesma posição
    if (vacuum_agent.x, vacuum_agent.y) in dirt_positions:
        dirt_positions.remove((vacuum_agent.x, vacuum_agent.y))

    draw_environment(vacuum_agent, dirt_positions)  # Desenhando o ambiente
    pygame.display.flip()
    pygame.time.delay(500)

pygame.quit()




