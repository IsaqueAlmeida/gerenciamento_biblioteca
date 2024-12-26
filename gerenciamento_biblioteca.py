# Criando a classe Livro
class Livro:
  def __init__(self, titulo, autor, ano_publicacao, num_copias_disponiveis):
    self.titulo = titulo
    self.autor = autor
    self.ano_publicacao = ano_publicacao
    self.num_copias_disponiveis = num_copias_disponiveis

  def exibir_informacoes_autor_livro(self):
    print(f'Título: {self.titulo}')
    print(f'Autor: {self.autor}')
    print(f'Ano de Publicação: {self.ano_publicacao}')
    print(f'Número de Cópias Disponíveis: {self.num_copias_disponiveis}')

# Criando próxima classe: Usuário
class Usuario:
  def __init__(self, nome, id_usuario, contato):
    self.nome = nome
    self.id_usuario = id_usuario
    self.contato = contato
  
  def exibir_informacoes_usuario(self):
    print(f'Nome do Usuário: {self.nome}')
    print(f'Id do Usuário: {self.id_usuario}')
    print(f'Contato do Usuário: {self.contato}')

class Biblioteca:
  def __init__(self):
    # armazenando objetos do tipo Livro e Usuário
    self.livros = []
    self.usuarios = []
  
  # Criando uma função para cadastrar livros
  def cadastrar_livros(self, livro):
    self.livros.append(livro)
    print(f"Livro '{livro.titulo}' cadastrado com sucesso!")
  
  # Criando uma função para cadastrar o usuário
  def cadastrar_usuario(self, usuario):
    self.usuarios.append(usuario)
    print(f"Usuário '{usuario.nome}' cadastrado com sucesso!")
  
  # Buscando por livros e usuários cadastrados
  def exibir_livros(self):
    if not self.livros:
      print('Nenhum livro cadastrado!')
    else:
      print('Lista de livros cadastrados: ')
      for livro in self.livros:
        livro.exibir_informacoes_autor_livro()
        print("-" * 20)
  
  def exibir_usuario(self):
    if not self.usuarios:
      print('Nenhum usuário cadastrado!')
    else:
      print('Lista de usuário cadastrados: ')
      for usuario in self.usuarios:
        usuario.exibir_informacoes_usuario()
        print('-' * 20)

# Criando a instância da biblioteca
biblioteca = Biblioteca()

# Criando alguns livros e usuários para cadastro
livro1 = Livro('1984', 'George Orwell', 1949, 5)
livro2 = Livro('Dom Casmurro', 'Marchado de Assis', 1899, 2)

usuario1 = Usuario('Isaque Almeida', '001', 'isaque@gmail.com')
usuario2 = Usuario('Nauhanne da Silva', '002', 'nauhanne@gmail.com')

# cadastrando os livros e usuários na biblioteca
biblioteca.cadastrar_livros(livro1)
biblioteca.cadastrar_livros(livro2)

biblioteca.cadastrar_usuario(usuario1)
biblioteca.cadastrar_usuario(usuario2)

# exibindo os livros e usuários cadastrados
print('\n')
biblioteca.exibir_livros()
print('\n')
biblioteca.exibir_usuario()
