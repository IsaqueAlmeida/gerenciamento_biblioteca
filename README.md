# Sistema de Gerenciamento de Biblioteca

## Descrição

O Sistema de Gerenciamento de Biblioteca é um projeto desenvolvido em Python para gerenciar livros, usuários, empréstimos e devoluções. Ele utiliza uma interface gráfica simples, baseada na biblioteca Tkinter, para facilitar o uso.

## Funcionalidades

- Cadastro de livros e usuários.
- Empréstimos de livros.
- Devoluções de livros.
- Relatórios detalhados sobre os livros e usuários.
- Interface gráfica para interagir com o sistema.

## Estrutura do Projeto

O projeto é composto pelos seguintes componentes principais:

1. **Módulo `gerenciamento_biblioteca`:** Contém as classes e a lógica de funcionamento do sistema.
2. **Módulo `interface`:** Implementa a interface gráfica do usuário (GUI).

### Algoritmo do `gerenciamento_biblioteca`

#### Estrutura Principal

```python
class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

class Usuario:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.emprestimos = []

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def registrar_emprestimo(self, isbn, matricula):
        # Implementa lógica de empréstimo

    def registrar_devolucao(self, isbn):
        # Implementa lógica de devolução

    def gerar_relatorios(self):
        # Gera relatórios de livros e usuários
```

#### Explicação
- A classe `Livro` gerencia os atributos dos livros, como título, autor e disponibilidade.
- A classe `Usuario` controla as informações dos usuários e os livros emprestados.
- A classe `Biblioteca` centraliza as operações do sistema, como cadastro, empréstimos e geração de relatórios.

### Algoritmo da Interface (`interface`)

#### Estrutura Principal

```python
import tkinter as tk
from tkinter import messagebox

class InterfaceBiblioteca:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca
        self.root = tk.Tk()
        self.root.title("Gerenciamento de Biblioteca")
        
        self._criar_widgets()

    def _criar_widgets(self):
        # Implementa campos de entrada e botões

    def iniciar(self):
        self.root.mainloop()

    def registrar_emprestimo(self):
        # Chama método da classe Biblioteca

    def registrar_devolucao(self):
        # Chama método da classe Biblioteca

    def mostrar_relatorios(self):
        # Exibe os relatórios em janelas separadas
```

#### Explicação
- A classe `InterfaceBiblioteca` utiliza Tkinter para criar a GUI.
- `_criar_widgets` monta os elementos visuais, como botões e campos de texto.
- Métodos como `registrar_emprestimo` e `registrar_devolucao` interagem diretamente com o módulo `gerenciamento_biblioteca`.

## Como Utilizar

### Pré-requisitos
Certifique-se de ter instalado:

- **Python 3.8 ou superior**
- As bibliotecas necessárias, incluindo:
  - `tkinter` (já incluída com Python)

### Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/SeuUsuario/sistema-gerenciamento-biblioteca.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd sistema-gerenciamento-biblioteca
   ```

3. Execute o arquivo principal:
   ```bash
   python main.py
   ```

## Funcionalidades Futuras

- Persistência de dados em banco de dados.
- Melhorias na interface gráfica.
- Novas funcionalidades, como reserva de livros.

## Linguagens e Bibliotecas Utilizadas

- **Linguagem:** Python
- **Bibliotecas:**
  - `tkinter` para a interface gráfica.

## Contribuição

Sinta-se à vontade para contribuir com melhorias e sugestões. Basta criar um fork do repositório, fazer as alterações e enviar um pull request.

## Contato

- **E-mail:** isaque.santos@ufpe.br
- **LinkedIn:** [LinkedIn](https://www.linkedin.com/in/isaque-f-s-almeida/)

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
