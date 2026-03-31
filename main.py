import pygame 
from pygame import mixer
from time import sleep
from random import randint 

x, y = (960, 540)
pygame.init()
pygame.mixer.init()
janela = pygame.display.set_mode([x, y])
pygame.display.set_caption('Retorno dos Aliens')

# Carrega sons do jogo
try:
    som_nave_colisao = pygame.mixer.Sound('./som_nave_colisao.wav')
except Exception as e:
    som_nave_colisao = None
try:
    som_missil = pygame.mixer.Sound('./som_missil.wav')
except Exception as e:
    som_missil = None
try:
    som_explosao = pygame.mixer.Sound('./som_explosao.wav')
except Exception as e:
    som_explosao = None

# Carregamento e inserção de Imagens na Janela.
try:
    bg = pygame.image.load('./imagem_fundo.jpg')
    bg = pygame.transform.scale(bg, (x, y)) # Garante que o fundo ocupe toda a tela
    nave_principal = pygame.image.load('./nave_player.png')
    nave_inimiga = pygame.image.load('./nave_inimiga.png')
    tiro = pygame.image.load('./missil_pequeno.png')
    tiro = pygame.transform.scale(tiro, (30, 30)) #Transforma o tamanho do objeto
except Exception as e:
    print('Aviso: Erro ao carregar imagens:', e)
    bg = pygame.Surface((x, y))
    bg.fill((0, 0, 0))
    nave_principal = pygame.Surface((50, 50))
    nave_principal.fill((0, 255, 0))
    nave_inimiga = pygame.Surface((50, 50))
    nave_inimiga.fill((255, 0, 0))
    tiro = pygame.Surface((30, 30))
    tiro.fill((255, 255, 0))

tiro_alvo = False 

pos_player_x = 430
pos_player_y = 400
velocidade_nave = 10

pos_inimigo_x = 430
pos_inimigo_y = 50
velocidade_inimigo = 5 # Ajustado para não ser tão rápido com 60 FPS

vel_missil = 15
pos_x_missil = 430
pos_y_missil = 450

pontuação = 0
estado_jogo = 'MENU' # 'MENU', 'JOGANDO' ou 'GAME_OVER'

botao_start_rect = pygame.Rect(x//2 - 150, y//2, 300, 80)
botao_restart_rect = pygame.Rect(x//2 - 175, y//2 + 50, 350, 80)

clock = pygame.time.Clock()

def colisoes():
    global pontuação 
    global pos_inimigo_y 
    global pos_inimigo_x
    global tiro_alvo
    global estado_jogo

    # Se o player principal colidir com a nave inimiga.
    if player_rect.colliderect(inimigo_rect):
        if som_nave_colisao:
            som_nave_colisao.play()
        estado_jogo = 'GAME_OVER' # Jogador perdeu!
        return True 
        
    elif tiro_rect.colliderect(inimigo_rect) and tiro_alvo:
        pontuação += 1 
        pos_inimigo_y = randint(-440, -50)
        pos_inimigo_x = randint(1, 870)
        if som_explosao:
            som_explosao.play()
        tiro_alvo = False # Reseta o míssil para atirar outro
        return True 

    return False 

rodando = True 

while rodando:
    clock.tick(60) # Limita a 60 FPS
    
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            rodando = False
            
        if estado_jogo == 'MENU':
            if events.type == pygame.MOUSEBUTTONDOWN:
                if botao_start_rect.collidepoint(events.pos):
                    # Inicia o jogo
                    estado_jogo = 'JOGANDO'
                    pontuação = 0
                    pos_inimigo_y = randint(-440, -50)
                    pos_player_x = 430
                    pos_player_y = 400
                    tiro_alvo = False

        elif estado_jogo == 'GAME_OVER':
            # Permite clicar em reiniciar
            if events.type == pygame.MOUSEBUTTONDOWN:
                if botao_restart_rect.collidepoint(events.pos):
                    # Reinicia o jogo inteiro
                    estado_jogo = 'JOGANDO'
                    pontuação = 0
                    pos_inimigo_y = randint(-440, -50)
                    pos_player_x = 430
                    pos_player_y = 400
                    tiro_alvo = False

    if estado_jogo == 'MENU':
        janela.blit(bg, (0, 0))
        
        # Título do jogo na tela de menu
        fonte_titulo = pygame.font.SysFont(None, 80)
        texto_titulo = fonte_titulo.render('Retorno dos Aliens', True, (255, 255, 0))
        texto_rect = texto_titulo.get_rect(center=(x//2, y//2 - 100))
        janela.blit(texto_titulo, texto_rect)
        
        # Cor do botão de iniciar
        cor_botao = (50, 200, 50)
        pos_mouse = pygame.mouse.get_pos()
        if botao_start_rect.collidepoint(pos_mouse):
            cor_botao = (100, 255, 100)
            
        pygame.draw.rect(janela, cor_botao, botao_start_rect, border_radius=15)
        
        fonte_btn = pygame.font.SysFont(None, 50)
        texto_btn = fonte_btn.render('INICIAR JOGO', True, (0, 0, 0))
        texto_btn_rect = texto_btn.get_rect(center=botao_start_rect.center)
        janela.blit(texto_btn, texto_btn_rect)
        
        pygame.display.update()
        continue
        
    elif estado_jogo == 'GAME_OVER':
        janela.blit(bg, (0, 0))
        
        # Texto 'GAME OVER'
        fonte_gameover = pygame.font.SysFont(None, 100)
        texto_gameover = fonte_gameover.render('GAME OVER', True, (255, 0, 0))
        texto_rect = texto_gameover.get_rect(center=(x//2, y//2 - 100))
        janela.blit(texto_gameover, texto_rect)
        
        # Mostrar a pontuação da partida
        fonte_pontos = pygame.font.SysFont(None, 50)
        texto_pontos = fonte_pontos.render(f'Sua Pontuação Final: {pontuação}', True, (255, 255, 255))
        texto_pontos_rect = texto_pontos.get_rect(center=(x//2, y//2))
        janela.blit(texto_pontos, texto_pontos_rect)
        
        # Botão de reiniciar
        cor_botao = (200, 50, 50)
        pos_mouse = pygame.mouse.get_pos()
        if botao_restart_rect.collidepoint(pos_mouse):
            cor_botao = (255, 100, 100) # Hover clareia o vermelho
            
        pygame.draw.rect(janela, cor_botao, botao_restart_rect, border_radius=15)
        
        fonte_btn = pygame.font.SysFont(None, 50)
        texto_btn = fonte_btn.render('TENTAR NOVAMENTE', True, (0, 0, 0))
        texto_btn_rect = texto_btn.get_rect(center=botao_restart_rect.center)
        janela.blit(texto_btn, texto_btn_rect)
        
        pygame.display.update()
        continue

    # ==========================
    # LÓGICA DO JOGO (JOGANDO)
    # ==========================
    
    # Verifica qual comando pressionado e lhe retorna uma ação.
    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_UP] and pos_player_y > 1:   
        pos_player_y -= velocidade_nave
    if comandos[pygame.K_DOWN] and pos_player_y < 440:
        pos_player_y += velocidade_nave
    if comandos[pygame.K_LEFT] and pos_player_x > 1:
        pos_player_x -= velocidade_nave
    if comandos[pygame.K_RIGHT] and pos_player_x < 870:
        pos_player_x += velocidade_nave
        
    if comandos[pygame.K_SPACE] and not tiro_alvo:
        tiro_alvo = True
        if som_missil:
            som_missil.play()

    # Movimento do Inimigo
    pos_inimigo_y += velocidade_inimigo
    if pos_inimigo_y > 540: # Inimigo passou do limite de baixo da tela
        estado_jogo = 'GAME_OVER' 

    # Movimento do míssil
    if not tiro_alvo:
        # Acompanha a nave centralizado
        pos_x_missil = pos_player_x + nave_principal.get_width() // 2 - tiro.get_width() // 2 
        pos_y_missil = pos_player_y
    else:
        pos_y_missil -= vel_missil
        if pos_y_missil < -50:
            tiro_alvo = False

    player_rect = nave_principal.get_rect(topleft=(pos_player_x, pos_player_y))
    inimigo_rect = nave_inimiga.get_rect(topleft=(pos_inimigo_x, pos_inimigo_y))
    tiro_rect = tiro.get_rect(topleft=(pos_x_missil, pos_y_missil))

    colisoes() # Função que também pode alterar para GAME OVER

    janela.blit(bg, (0, 0))
    if tiro_alvo:
        janela.blit(tiro, (pos_x_missil, pos_y_missil))
    janela.blit(nave_inimiga, (pos_inimigo_x, pos_inimigo_y))
    janela.blit(nave_principal, (pos_player_x, pos_player_y))
    
    # Renderizar pontuação na tela
    fonte = pygame.font.SysFont(None, 40)
    texto_pontos = fonte.render(f'Pontuação: {pontuação}', True, (255, 255, 255))
    janela.blit(texto_pontos, (10, 10))

    pygame.display.update()

pygame.quit()
