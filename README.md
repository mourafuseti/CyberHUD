# 👋🏻 Leonardo de Moura Fuseti

Estudante de Defesa Cibernetica no Polo Estacio Piumhi MG . Formação tecnica em Tecnico em Redes de Computadores no IFMG Bambui MG , intusiasta na programação gostando muito de Python e evoluindo dia a dia .

### Conecte-se comigo

[![Perfil DIO](https://img.shields.io/badge/-Meu%20Perfil%20na%20DIO-30A3DC?style=for-the-badge)](https://www.dio.me/users/mourafuseti)
[![E-mail](https://img.shields.io/badge/-Email-000?style=for-the-badge&logo=microsoft-outlook&logoColor=E94D5F)](mailto:mourafuseti@gmail.com)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=30A3DC)](https://www.linkedin.com/in/leonardo-moura-fuseti-4052b0359/)

### Habilidades

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kali-linux&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-000?style=for-the-badge&logo=html5&logoColor=30A3DC)
![CSS3](https://img.shields.io/badge/CSS3-000?style=for-the-badge&logo=css3&logoColor=E94D5F)
![JavaScript](https://img.shields.io/badge/JavaScript-000?style=for-the-badge&logo=javascript&logoColor=F0DB4F)
![Sass](https://img.shields.io/badge/SASS-000?style=for-the-badge&logo=sass&logoColor=CD6799)
![Bootstrap](https://img.shields.io/badge/bootstrap-000?style=for-the-badge&logo=bootstrap&logoColor=553C7B)
[![Git](https://img.shields.io/badge/Git-000?style=for-the-badge&logo=git&logoColor=E94D5F)](https://git-scm.com/doc)
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=30A3DC)](https://docs.github.com/)

### 📊 GitHub Stats

<a href="https://github.com/mourafuseti">
  <img align="left" src="https://github-readme-stats.vercel.app/api?username=mourafuseti&show_icons=true&theme=transparent&bg_color=000&border_color=30A3DC&icon_color=30A3DC&title_color=E94D5F&text_color=FFF" alt="Estatísticas do GitHub de Leonardo" />
</a>
<br><br><br><br><br><br><br><br><br>


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


