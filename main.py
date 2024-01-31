import pygame
import random
from unidecode import unidecode


    

# Inicializa o PyGame
pygame.init()

# Cria a janela
janela = pygame.display.set_mode((800, 600))

def is_letter(char):
    return ord(char) in range(ord('a'), ord('z') + 1)

def draw_screen(janela, pygame, word, showWord, points, misses, letters):
    janela.fill((0, 0, 0))
    draw_wrong_chars(janela,word, letters)
    draw_game(janela, pygame, word, showWord)
    draw_points(janela,points,misses)
    pygame.display.update()
    

def shuffle():
    with open ('words/br-utf8.txt', 'r', encoding='utf-8', errors='ignore') as f:
        palavras = [array.strip() for array in f.readlines()]
    return random.choice(palavras)


def draw_points(janela,win, lost):
    fontSize = 50
    x, y = (675, 35)
    fonte = pygame.font.SysFont("Arial", fontSize)
    texto0 = fonte.render("w: "+str(win), True, (0, 255, 0))
    texto1 = fonte.render("l: "+str(lost), True, (255, 0, 0))
    texto2 = fonte.render("trys: "+str(10-lost), True, (255, 0, 0))
    janela.blit(texto0, (x, y + fontSize*1))
    janela.blit(texto1, (x, y + fontSize*2))
    janela.blit(texto2, (x, y + fontSize*3))
    

def draw_font(janela, pygame, charactere, size, pos):
    # Define a fonte
    fonte = pygame.font.SysFont("Arial", size)
    # Desenha a letra
    texto = fonte.render(charactere, True, (255, 255, 255))
    janela.blit(texto, (pos['x'], pos['y']-size))


def draw_wrong_chars(janela,word, chars):
    texto = ' '.join(chars)
    for i in word:
        texto = texto.replace(i,'')
    fonte = pygame.font.SysFont("Arial", 30)
    texto = fonte.render('chars: '+texto, True, (0, 0, 255))
    janela.blit(texto, (20,50))
    print(texto, chars)

def draw_under(janela, pygame, x_i, x_e, y):
    pygame.draw.line(janela, (128, 128, 128), (x_i,y), (x_e, y), width=2)  


def draw_game(janela, pygame, word, showWord):
    #pygame.draw.rect(janela, (255, 255, 255), (150, 450, 550, 100), 3)
    ini = {'x' : 150, 'y': 550}
    end = {'x' : 700, 'y': 550}
    size = end['x']-ini['x']
    space = int(100/len(word))
    segment = int(size/len(word))
    if size//len(word)!=0:
        segment+=1
    initialShift = space/2
    charPos=0
    for i in range(ini['x'], end['x'], segment):
        if showWord[charPos]:
            draw_font(janela, pygame, word[charPos], segment, {'x':i+initialShift,'y':ini['y']})
        else:
            pygame.draw.line(janela, (128, 128, 128), (i+initialShift,ini['y']), (i+initialShift+segment-space, ini['y']), width=2)
        charPos+=1
    return


word = shuffle()
showWord = [0] * len(word)

trays = 0
letters=[]

points = 0
misses = 0
draw_screen(janela, pygame, word, showWord, points, misses,letters)
print(word)
#drawFont(janela, pygame)
# Loop principal
while True:
    # Verifica se um evento de clique ocorreu
    for evento in pygame.event.get():
        # Se o evento for um clique
        #if evento.type == pygame.MOUSEBUTTONDOWN:
            # Printa a posição do clique
            #print(evento.pos)
        if evento.type == pygame.KEYDOWN:
            key = unidecode(pygame.key.name(evento.key).lower())
            if is_letter(key):
                if key not in letters:
                    letters.append(key)
                    if key in word:
                        #aumenta pontuacao
                        points+=1
                        for nn,i in enumerate(word):
                            if unidecode(i)==key:
                                showWord[nn]=1
                    else:
                        misses+=1
                        #decrementa pontuacao
            draw_screen(janela, pygame, word, showWord, points, misses,letters)
        if 0 not in showWord:
            print(999999999999999999999)
        # Se o evento for um evento de fechamento da janela
        if evento.type == pygame.QUIT:
            pygame.quit()
            break

    if misses == 10:
        print(word)
        exit()

