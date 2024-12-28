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
    # lista para armazenarf objetos do tipo Livro, Usuário e Emprestimo
    self.livros = []
    self.usuarios = []
    self.emprestimos = {} # DIcionário para registrar emprestimos: (usuario_id: lista de livros)
  
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
  
  # Função - Emprestar livros
  def emprestar_livros(self, id_usuario, titulo_livro):
    # Encontrar usuário
    usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
    if not usuario:
      print('Usuário não encontrado!')
      return
    
    # Encontrar livro
    livro = next((l for l in self.livros if l.titulo == titulo_livro), None)
    if not livro:
      print('Livro não encontrado!')
      return
    
    # Verificar disponibilidade
    if livro.num_copias_disponiveis <= 0:
      print(f"O livro '{livro.titulo}' não está disponível para empréstimo!")
      return
    
    # Registrando empréstimo
    if id_usuario not in self.emprestimos:
      self.emprestimos[id_usuario] = []
    self.emprestimos[id_usuario].append(livro)
    livro.num_copias_disponiveis -= 1
    print(f"Livro '{livro.titulo}' emprestado para {usuario.nome} com sucesso!")

  # Função para devolver livro
  def devolver_livro(self, id_usuario, titulo_livro):
    # verificando se o usuário fez empréstimos
    if id_usuario not in self.emprestimos or not self.emprestimos[id_usuario]:
      print('Nenhum empréstimo encontrado para este usuário!')
      return
    
    #encontrando livro emprestado
    livro = next((l for l in self.emprestimos[id_usuario] if l.titulo == titulo_livro), None)
    if not livro:
      print(f"O livro '{titulo_livro}' não está registrado como emprestado para esse usuário!")
      return
    
    # Atualizando devolução
    self.emprestimos[id_usuario].remove(livro)
    livro.num_copias_disponiveis += 1
    print(f"O livro '{livro.titulo}' devolvido com sucesso!")
  
  def gerar_relatorios_livros_disponiveis(self):
    print('\n---- Relatório de Livros Disponíveis ----')
    for livro in self.livros:
      if livro.num_copias_disponiveis > 0:
        livro.exibir_informacoes_autor_livro()
        print('-' * 20)
  
  def gerar_relatorios_livros_emprestados(self):
    print('\n---- Relatórios de Livros Emprestados ----')
    for usuario_id, livros in self.emprestimos.items():
      if livros:
        usuario = next((u for u in self.usuarios if u.id_usuario == usuario_id), None)
        print(f"Usuário: {usuario.nome} (ID: {usuario.id_usuario})")
        for livro in livros:
          print(f' - {livro.titulo} por {livro.autor}')
        print('-' * 20)
  
  def gerar_relatorio_usuarios(self):
    print('\n---- Relatório de Usuários Cadastrados ----')
    for usuario in self.usuarios:
      usuario.exibir_informacoes_usuario()
      print('-' * 20)

# Criando a instância da biblioteca
biblioteca = Biblioteca()

# Criando alguns livros e usuários para cadastro
livro1 = Livro('1984', 'George Orwell', 1949, 5)
livro2 = Livro('Dom Casmurro', 'Marchado de Assis', 1899, 2)
livro3 = Livro('Biografia de Isaque', 'Isaque Almeida', 2026, 100)
print('\n')

usuario1 = Usuario('Isaque Almeida', '001', 'isaque@gmail.com')
usuario2 = Usuario('Nauhanne da Silva', '002', 'nauhanne@gmail.com')
usuario3 = Usuario('Vitor Araújo', '003', 'vitor@gmail.com')
print('\n')

# cadastrando os livros e usuários na biblioteca
biblioteca.cadastrar_livros(livro1)
biblioteca.cadastrar_livros(livro2)
biblioteca.cadastrar_livros(livro3)
print('\n')

biblioteca.cadastrar_usuario(usuario1)
biblioteca.cadastrar_usuario(usuario2)
biblioteca.cadastrar_usuario(usuario3)
print('\n')

# Testando os empréstimos
print('\n---- Empréstimos ----')
biblioteca.emprestar_livros('003', 'Biografia de Isaque')
biblioteca.emprestar_livros('002', 'Dom Casmurro')
biblioteca.emprestar_livros('002', 'Biografia de Isaque')

# Testando devolução
print('\n---- Devoluções ----')
biblioteca.devolver_livro('003', 'Biografia de Isaque')
biblioteca.devolver_livro('002', 'Dom Casmurro')

# Gerando Relatórios
biblioteca.gerar_relatorios_livros_disponiveis()
biblioteca.gerar_relatorios_livros_emprestados()
biblioteca.gerar_relatorio_usuarios()
