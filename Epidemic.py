from random import randint
import time 
import pygame

N = 100
B = 2
BETA = B / (N-1)
PACKETLOSS = 0
MODIFICA = True
NEW_NODI_PER_EPOCA=1000
blue = (0, 0, 255)
red = (255, 0, 0)
green=(0,255,0)

pygame.init()

# Crea la finestra di gioco
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Imposta il font per il testo
font = pygame.font.SysFont(None, 30)

cordinate={}
def generate_unique_pairs():
    while True:
        x = randint(0, width)
        y = randint(0, height)
        new_pair = (x, y)
        if new_pair in cordinate:
            continue
        
        
        for item in cordinate.items():

            if (abs(x - item[0][0]) > 15 and abs(y - item[0][1])>15):
                cordinate[new_pair] = (x,y)
                return new_pair
        if len(cordinate.items())==0:
                cordinate[new_pair] = (x,y)
                return new_pair
class Node:
    def __init__(self, x,y, infected=False,color=blue):
        if infected:
            color=red
        self.x = x
        self.y = y
        self.color = color
        self.infected = infected
        self.children = []

    def __repr__(self):
        string = str(self.x," ",self.y)
        return string
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 8)




def aggiungi_a_gli_infetti(nodo):
    infected.append(nodo)
    not_infected.remove(nodo)
    nodo.color= red
            




def add_node():
    print("ciao")
    if MODIFICA:
        for j in range(NEW_NODI_PER_EPOCA):
            x, y = generate_unique_pairs()
            nodo=Node(x,y)
            nodo.color=green
            nodes.append(nodo)
            not_infected.append(nodo)


def check_all_infected():
    for node in not_infected:
        
        if not node.infected:
            return False
    return True


# infettazzione
def infetta(nodo):
    for i in range(int((1 - PACKETLOSS) * B)):
        r = randint(0, len(nodes) - 1)
        new_nodo = nodes[r]
        if new_nodo not in infected:
            new_nodo.infected = True
            nodo.children.append(new_nodo)
            aggiungi_a_gli_infetti(new_nodo)

    
            



def simulazione():








    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
    

    
        # infettare il primo nodo
        
        infected.append(nodo_cattivo)
        epoca = 1

        while not check_all_infected():
            for node in nodes:
                node.draw()

            
            print(f"Epoca {epoca}")
            print(f"N: {len(nodes)}")

            add_node()
            for i in range(0,len(infected)): #ogni nodo degli infetti ad ogni epoca infetta due nodi appartenenti a nodi, a meno che non siano già infetti
                for j in range(B):  #numero di chiamate random
                    r = randint(0, len(infected) - 1)
                    infetta(infected[r])
            time.sleep(2)
            pygame.display.flip()
            print(f"ni: {len(not_infected)}")
            print(f"i: {len(infected)}")
            epoca += 1
        for node in nodes:
            node.draw()
        pygame.display.flip()
        
# creazione nodi

nodes = []
not_infected = []
infected = []
x, y = generate_unique_pairs()
nodo_cattivo = Node(x,y, True)
print("ciao mondo")
print(cordinate)
nodes.append(nodo_cattivo)

for i in range(N):
    x, y = generate_unique_pairs()
    node = Node(x,y)
    nodes.append(node)
    not_infected.append(node)

simulazione()







