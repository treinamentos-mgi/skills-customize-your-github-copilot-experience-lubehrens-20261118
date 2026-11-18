
# 📘 Atividade: Jogos em Python

## 🎯 Objetivo

Pratique manipulação de strings, listas, seleção aleatória, condicionais, loops e entrada de dados criando uma versão jogável do clássico jogo da Forca.

## 📝 Tarefas

### 🛠️ Preparação da palavra e do jogo

#### Descrição
Complete o código inicial para selecionar uma palavra secreta da lista disponível e preparar as variáveis que acompanham o andamento da partida.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra da lista predefinida.
- Inicializar o registro de letras corretas e o número de palpites incorretos.
- Definir um limite para os palpites incorretos.

### 🛠️ Rodada de palpites e encerramento

#### Descrição
Implemente o loop principal para receber palpites, atualizar o progresso e encerrar a partida quando o jogador vencer ou atingir o limite de erros.

#### Requisitos
O programa concluído deve:

- Solicitar uma letra ao jogador e verificar se ela aparece na palavra secreta.
- Exibir as letras descobertas e indicar as posições ainda ocultas, usando `_` para cada letra não descoberta.
- Atualizar e informar quantos palpites incorretos ainda restam.
- Encerrar quando todas as letras forem descobertas ou quando o limite de palpites incorretos for atingido.
- Exibir uma mensagem indicando vitória ou derrota; em caso de derrota, revelar a palavra secreta.