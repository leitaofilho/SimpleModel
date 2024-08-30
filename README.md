# SimpleModel

## Descrição

Bem-vindo ao repositório do **SimpleModel**, um modelo de inteligência artificial, em nível de Prova de Conceito, desenvolvido pela Simple para detectar automaticamente estruturas anatômicas relacionadas à laringe (glote) e ao esôfago.

## Funcionalidades

O modelo **Simple v1.0** foi desenvolvido para realizar a seguinte tarefa:

- **Detecção Automática**: Identificação de estruturas anatômicas como glote e esôfago.

## Arquitetura

O **Simple v1.0** é baseado na arquitetura **YOLO (You Only Look Once)**, conhecida por sua eficiência em tarefas de visão computacional. O modelo foi treinado em um dataset de 4315 imagens rotuladas, obtidas a partir de vídeos de intubação feitos com o b-Safe (protótipo funcional do videolaringoscópio da Simple) em manequim humano realístico.

### Detalhes do Treinamento

- **Dataset**:
  - 4315 imagens rotuladas.
  - Divisão dos dados: 70% para treinamento, 15% para validação, e 15% para teste.
  
- **Hiperparâmetros**:
  - **Épocas**: 30
  - **Otimização**: AdamW
  - **Taxa de Aprendizagem**: 0.001667
  - **Momentum**: 0.9
  
- **Infraestrutura**:
  - Treinamento realizado em uma GPU (Graphical Processing Unit) para otimização de desempenho.

- **Desempenho**:
  - **Precisão Global**: 97%

## Como Fazer a Inferência

Para testar o modelo **Simple v1.0**, você pode utilizar o diretório `inference`, que contém vídeos no formato `*.mov` para inferência. O arquivo `main.py` do repositório inclui o código necessário para carregar o modelo e realizar a inferência em um vídeo de exemplo.

### Exemplo de Código:

```python
from ultralytics import YOLO

# Carregar modelo
model = YOLO('model/simple_ai_v1.0.pt')

# Inferencia do modelo
results = model(source='inference/video01.mov', show=True, conf=0.75, save=True)
```

## Propostas Futuras
O objetivo desta pesquisa é expandir o modelo **Simple v1.0** para guiar profissionais e estudantes de medicina durante procedimentos críticos de intubação, proporcionando feedback visual em tempo real a partir da borda do dispositivo Edge b-Safe (versão inteligente do videolaringoscópio da Simple).
