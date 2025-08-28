import pygame
import random

# Inicializa o Pygame
pygame.init()

# Define as cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)

# Configurações da tela
largura_tela = 600
altura_tela = 400
tamanho_bloco = 10
velocidade_cobra = 15

# Cria a tela e define o título
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo da Cobrinha")

# Relógio para controlar a velocidade do jogo
clock = pygame.time.Clock()

# Fonte para exibir a pontuação
fonte_pontuacao = pygame.font.SysFont("comicsansms", 25)
fonte_mensagem = pygame.font.SysFont("comicsansms", 30)

# Função para exibir a pontuação na tela
def mostrar_pontuacao(pontuacao):
    texto = fonte_pontuacao.render(f"Pontuação: {pontuacao}", True, branco)
    tela.blit(texto, [0, 0])

# Função para desenhar a cobra
def desenhar_cobra(tamanho_bloco, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, verde, [x[0], x[1], tamanho_bloco, tamanho_bloco])

# Função principal do jogo
def loop_jogo():
    fim_jogo = False
    fim_rodada = False

    # Posição inicial da cobra
    x_cobra = largura_tela / 2
    y_cobra = altura_tela / 2

    # Mudança de direção (começa parada)
    x_cobra_mudanca = 0
    y_cobra_mudanca = 0

    # Lista que armazena os segmentos do corpo da cobra
    lista_cobra = []
    tamanho_cobra = 1

    # Posição inicial da comida
    comida_x = round(random.randrange(0, largura_tela - tamanho_bloco) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura_tela - tamanho_bloco) / 10.0) * 10.0

    while not fim_jogo:
        # Loop para a tela de "Game Over"
        while fim_rodada:
            tela.fill(preto)
            mensagem = "Você perdeu! Pressione C para jogar novamente ou Q para sair."
            texto_mensagem = fonte_mensagem.render(mensagem, True, vermelho)
            # Centraliza a mensagem na tela
            texto_rect = texto_mensagem.get_rect(center=(largura_tela / 2, altura_tela / 2))
            tela.blit(texto_mensagem, texto_rect)
            mostrar_pontuacao(tamanho_cobra - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        fim_jogo = True
                        fim_rodada = False
                    if evento.key == pygame.K_c:
                        loop_jogo() # Reinicia o jogo chamando a função novamente
                        return

        # Loop principal do jogo
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and x_cobra_mudanca == 0:
                    x_cobra_mudanca = -tamanho_bloco
                    y_cobra_mudanca = 0
                elif evento.key == pygame.K_RIGHT and x_cobra_mudanca == 0:
                    x_cobra_mudanca = tamanho_bloco
                    y_cobra_mudanca = 0
                elif evento.key == pygame.K_UP and y_cobra_mudanca == 0:
                    y_cobra_mudanca = -tamanho_bloco
                    x_cobra_mudanca = 0
                elif evento.key == pygame.K_DOWN and y_cobra_mudanca == 0:
                    y_cobra_mudanca = tamanho_bloco
                    x_cobra_mudanca = 0

        # Verifica colisão com as bordas
        if x_cobra >= largura_tela or x_cobra < 0 or y_cobra >= altura_tela or y_cobra < 0:
            fim_rodada = True

        # Atualiza a posição da cobra
        x_cobra += x_cobra_mudanca
        y_cobra += y_cobra_mudanca

        tela.fill(preto)
        
        # Desenha a comida
        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
        
        # Cria a "cabeça" da cobra e a adiciona à lista de segmentos
        cabeca_cobra = [x_cobra, y_cobra]
        lista_cobra.append(cabeca_cobra)

        # Se a cobra cresceu, remove o último segmento para manter o tamanho
        if len(lista_cobra) > tamanho_cobra:
            del lista_cobra[0]

        # Verifica se a cobra colidiu consigo mesma
        for segmento in lista_cobra[:-1]:
            if segmento == cabeca_cobra:
                fim_rodada = True

        # Desenha a cobra e a pontuação
        desenhar_cobra(tamanho_bloco, lista_cobra)
        mostrar_pontuacao(tamanho_cobra - 1)

        pygame.display.update()

        # Verifica se a cobra comeu a comida
        if x_cobra == comida_x and y_cobra == comida_y:
            comida_x = round(random.randrange(0, largura_tela - tamanho_bloco) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura_tela - tamanho_bloco) / 10.0) * 10.0
            tamanho_cobra += 1

        # Controla a velocidade do jogo
        clock.tick(velocidade_cobra)

    pygame.quit()
    quit()

loop_jogo()
