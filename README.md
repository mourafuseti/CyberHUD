

# 🦾 CyberHUD - Visualização Computacional para Defesa Cibernética

Este projeto implementa uma interface de **Realidade Aumentada (AR)** inspirada em interfaces ciberpéticas (HUD). Utilizando Python e a biblioteca Mediapipe, o sistema realiza o rastreamento em tempo real de pontos biométricos da face e das mãos, aplicando uma camada gráfica de segurança e monitoramento.

## 🎯 Funcionalidades

* **Identificação Facial:** Detecção automática de face com box de rastreio e ID de usuário.
* **Mapeamento Biométrico:** Rastreamento de 21 pontos de articulação das mãos com efeito Neon.
* **Ambiente Isolado:** Totalmente conteinerizado com Docker para evitar conflitos de dependências no Kali Linux (Python 3.13).
* **Visual Cyberpunk:** Interface estilizada em Ciano e Vermelho para simular sistemas de monitoramento avançado.

## 🚀 Tecnologias Utilizadas

* **Python 3.11** (Executado via Container)
* **OpenCV:** Processamento de imagem e renderização de frames.
* **Mediapipe:** Inferência de inteligência artificial para biometria.
* **Docker:** Orquestração de ambiente e compatibilidade de hardware.

## 🛠️ Instalação e Execução

### Pré-requisitos

* Docker instalado e configurado.
* Webcam conectada (física ou mapeada via VM).

### Passo a Passo

1. **Clone o repositório:**
```bash
git clone https://github.com/mourafuseti/CyberHUD.git
cd cyber-hud

```


2. **Construa a imagem Docker:**
```bash
sudo docker build -t cyber-hud .

```


3. **Libere o acesso ao servidor X11 (para abrir a janela no Linux):**
```bash
xhost +local:docker

```


4. **Execute o sistema:**
```bash
sudo docker run -it --rm \
    --env="DISPLAY=$DISPLAY" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --device=/dev/video0:/dev/video0 \
    cyber-hud

```



## 📂 Estrutura do Projeto

* `main.py`: Script principal com a lógica de Visão Computacional e HUD.
* `Dockerfile`: Configuração do ambiente isolado e dependências de sistema.
* `README.md`: Documentação do projeto.

---

## 🛡️ Contexto de Defesa Cibernética

Este projeto foi desenvolvido como prova de conceito para sistemas de autenticação biométrica e monitoramento de perímetros. A capacidade de identificar gestos e faces em tempo real permite a criação de gatilhos de segurança automatizados, como bloqueio de terminais ou alertas de intrusão.

---

**Autor:** Leonardo de Moura Fuseti

**Status:** 🟢 Operacional

**Projeto Relacionado:** GodEye Network Auditing Tool


