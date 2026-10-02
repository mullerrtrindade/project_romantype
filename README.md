# 🏛️ RomanType

<div align="center">

### Conversor de números inteiros para algarismos romanos

Uma aplicação desktop simples, moderna e desenvolvida em **Python**, utilizando **ttkbootstrap** para a interface gráfica.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![ttkbootstrap](https://img.shields.io/badge/ttkbootstrap-GUI-7952B3?style=for-the-badge)
![Status](https://img.shields.io/badge/status-concluído-success?style=for-the-badge)

</div>

---

## 📖 Sobre o projeto

O **RomanType** é um conversor de números inteiros para algarismos romanos desenvolvido como projeto de aprendizado em Python.

A aplicação recebe um número entre **1 e 3999**, realiza a conversão e apresenta o resultado através de uma interface gráfica simples e intuitiva.

Exemplo:

```text
Entrada: 2026

Resultado: MMXXVI
```

---

## ✨ Funcionalidades

- 🔢 Conversão de números inteiros para algarismos romanos
- ✅ Validação de entrada
- ⚠️ Tratamento de valores inválidos
- 🖥️ Interface gráfica desktop
- 🎨 Interface construída com `ttkbootstrap`
- ⌨️ Conversão através do botão da aplicação
- 📦 Possibilidade de geração de executável `.exe` com PyInstaller

---

## 🧠 Como funciona

A conversão utiliza os principais valores da numeração romana:

| Número | Romano |
|------:|:------:|
| 1000 | M |
| 900 | CM |
| 500 | D |
| 400 | CD |
| 100 | C |
| 90 | XC |
| 50 | L |
| 40 | XL |
| 10 | X |
| 9 | IX |
| 5 | V |
| 4 | IV |
| 1 | I |

O algoritmo percorre os valores do maior para o menor, verificando quantas vezes cada valor pode ser utilizado até concluir a conversão.

---

## 🛠️ Tecnologias

O projeto foi desenvolvido utilizando:

- **Python**
- **Tkinter**
- **ttkbootstrap**
- **PyInstaller**

---

## 📁 Estrutura do projeto

```text
project_romantype/
│
├── main.py
├── README.md
└── requirements.txt
```

---

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/mullerrtrindade/project_romantype.git
```

### 2. Entre na pasta

```bash
cd project_romantype
```

### 3. Crie um ambiente virtual

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

### 4. Instale as dependências

```bash
pip install ttkbootstrap
```

Ou, caso exista um `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5. Execute

```bash
python main.py
```

---

## 📦 Gerando o executável

Com o PyInstaller instalado:

```bash
pip install pyinstaller
```

Execute:

```bash
pyinstaller --onefile --windowed main.py
```

O executável será criado dentro da pasta:

```text
dist/
└── main.exe
```

---

## 🎯 Regras de conversão

O RomanType aceita números inteiros entre:

```text
1 → I

até

3999 → MMMCMXCIX
```

Entradas fora desse intervalo ou valores que não sejam números inteiros são rejeitados pela aplicação.

---

## 📚 Objetivo

Este projeto foi desenvolvido com foco no aprendizado e prática de conceitos como:

- funções em Python;
- listas;
- loops;
- operadores matemáticos;
- tratamento de exceções com `try/except`;
- validação de dados;
- interfaces gráficas;
- organização de projetos;
- criação de executáveis;
- versionamento com Git e GitHub.

---

## 👨‍💻 Autor

Desenvolvido por **Müller Trindade**.

[![GitHub](https://img.shields.io/badge/GitHub-mullerrtrindade-181717?style=for-the-badge&logo=github)](https://github.com/mullerrtrindade)

---

<div align="center">

Feito com 🐍 Python durante meus estudos de programação.

**RomanType — números modernos, representação clássica.**

</div>
