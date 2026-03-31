# Retorno dos Aliens 👽🚀

Um jogo de nave arcade 2D estilo Retrô construído inteiramente utilizando **Python** e a biblioteca **Pygame**. Proteja o sistema atirando nas naves inimigas antes que elas cheguem ao limite inferior da tela!

## 📁 Estrutura do Projeto

```
PYGAME_YT/
├── assets/                  # Recursos do jogo
│   ├── images/             # Imagens e sprites
│   │   ├── imagem_fundo.jpg
│   │   ├── nave_player.png
│   │   ├── nave_inimiga.png
│   │   └── missil_pequeno.png
│   └── sounds/             # Efeitos sonoros
│       ├── som_explosao.wav
│       ├── som_missil.wav
│       └── som_nave_colisao.wav
├── src/                    # Código fonte
│   └── main.py            # Arquivo principal do jogo
├── docs/                  # Documentação
│   └── README.md          # Documentação detalhada
├── tests/                 # Testes (futuro)
├── .venv/                 # Ambiente virtual
├── requirements.txt       # Dependências
└── README.md             # Documentação principal
```

## 🎮 Como Jogar

O objetivo é sobreviver o máximo possível e acumular pontos ao destruir as naves alienígenas.

- **Fim de jogo (Game Over)** ocorre automaticamente se:
  1. Uma nave inimiga colidir com a sua nave principal.
  2. Uma nave inimiga escapar do seu tiro e conseguir chegar ao fundo da tela.

### 🕹️ Controles

* **Setas (Cima / Baixo / Esquerda / Direita)**: Movimenta a sua nave pelo cenário.
* **Espaço (Space)**: Atira seus mísseis.
* **Interface (Mouse)**: Interagir com os botões de Iniciar (Menu) ou Tentar Novamente (Game Over).

## 🛠️ Tecnologias e Dependências

Para rodar este projeto, você precisará ter o Python instalado com o framework Pygame.

* **Python 3.x**
* **Pygame** (`pip install pygame`)

## 🚀 Como Executar Localmente

1. Faça o clone do repositório em sua máquina.
2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   # ou
   .venv\Scripts\activate     # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o jogo:
   ```bash
   cd src
   python main.py
   ```

## 💡 Sobre o Desenvolvimento

Este projeto serviu como base para a prática dos seguintes fundamentos de desenvolvimento de jogos em Python:

- **Controle de Loop e Frames (FPS):** Aplicação de relógio `clock.tick(60)` para evitar picos de instabilidade.
- **Máquina de Estados de Interface:** Implementação e migração coesa entre as telas do jogo (`MENU`, `JOGANDO`, `GAME_OVER`).
- **Lógica e Math para Criação de Efeitos Sonoros:** Utilização da biblioteca nativa para geração autônoma de frequências de som .wav em 8-bits sem recursos externos importados.
- **Detecção Retangular (AABB):** Estrutura de cálculos baseadas no `colliderect` do Pygame.

## 📜 Licença

Projeto desenvolvido para fins educacionais e de diversão com programação. Sinta-se livre para modificar, estender funcionalidades e evoluir o código!
