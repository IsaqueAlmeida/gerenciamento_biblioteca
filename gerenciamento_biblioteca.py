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
    self.livros_emprestados = []
  
  def registrar_emprestimo(self, livro):
    self.livros_emprestados.append(livro)
  
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
      raise Exception('Usuário não encontrado!')
    
    # Encontrar livro
    livro = next((l for l in self.livros if l.titulo == titulo_livro), None)
    if not livro:
      raise Exception('Livro não encontrado!')
    
    # Verificar disponibilidade
    if livro.num_copias_disponiveis <= 0:
      raise Exception(f"O livro '{livro.titulo}' não está disponível para empréstimo!")
    
    # Registrando empréstimo
    if id_usuario not in self.emprestimos:
      self.emprestimos[id_usuario] = []
    self.emprestimos[id_usuario].append(livro)
    livro.num_copias_disponiveis -= 1
    print (f"Livro '{livro.titulo}' emprestado para {usuario.nome} com sucesso!")

  # Função para devolver livro
  def devolver_livro(self, id_usuario, titulo_livro):
    # verificando se o usuário fez empréstimos
    if id_usuario not in self.emprestimos or not self.emprestimos[id_usuario]:
      raise Exception('Nenhum empréstimo encontrado para este usuário!')
    
    #encontrando livro emprestado
    livro = next((l for l in self.emprestimos[id_usuario] if l.titulo == titulo_livro), None)
    if not livro:
      raise Exception(f"O livro '{titulo_livro}' não está registrado como emprestado para esse usuário!")
    
    # Atualizando devolução
    self.emprestimos[id_usuario].remove(livro)
    livro.num_copias_disponiveis += 1
    raise Exception(f"O livro '{livro.titulo}' devolvido com sucesso!")
  
  def gerar_relatorios_livros_disponiveis(self):
    livros_disponiveis = [livro for livro in self.livros if livro.num_copias_disponiveis > 0]
    return livros_disponiveis
  
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
    if not self.usuarios:
      return ['Nenhum usuário cadastrado!']
    
    relatorio = []
    for usuario in self.usuarios:
      relatorio.append(f"Nome: {usuario.nome}, ID: {usuario.id_usuario}, contato: {usuario.contato}")
    return relatorio
