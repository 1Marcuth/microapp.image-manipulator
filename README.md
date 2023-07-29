# Micro aplicação de manipulação de imagem

## Breve Introdução

Essa aplicação é focada em manipular imagens, como converter formatos de arquivo, cortar, redimensionar e até girar imagens.

---

## URLs

- https://microappimage-manipulator-production.up.railway.app
- https://microapp-image-manipulator.onrender.com


## Rotas

---

### `/convert`

Converte uma imagem de um formato para outro:

#### Parâmetros

- `input`: Extensão do arquivo de entrada (sem o ponto)
- `output`: Extensão do arquivo de saída (sem o ponto)
- `file`: Arquivo de entrada em sí

---

### `/resize`

Redmensiona uma imagem de um tamanho para outro:

#### Parâmetros

- `input`: Extensão do arquivo de entrada (sem o ponto)
- `width`: Largura do arquivo de saída
- `height`: Altura do arquivo de saída
- `file`: Arquivo de entrada em sí

---

### `/crop`

Corta um pedaço de uma imagem:

#### Parâmetros

- `input`: Extensão do arquivo de entrada (sem o ponto)
- `top`: Posição X inicial
- `left`: Posição Y inicial
- `width`: Largura do corte
- `height`: Altura do corte
- `file`: Arquivo de entrada em sí

---

### `/rotate`

Corta um pedaço de uma imagem:

#### Parâmetros

- `input`: Extensão do arquivo de entrada (sem o ponto)
- `angle`: Ângulo de rotação da imagem
- `file`: Arquivo de entrada em sí