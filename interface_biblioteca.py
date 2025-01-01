import tkinter as tk
from tkinter import messagebox
from gerenciamento_biblioteca import Biblioteca, Livro, Usuario
from tkinter import ttk

class BibliotecaApp:
  def __init__(self, root):
    self.root = root
    self.root.title('Sistema de Gerenciamento de Biblioteca')
    self.biblioteca = Biblioteca()

    # Adicionando título principal
    titulo = tk.Label(root, text='Sistema de Gerenciamento de Biblioteca', font=('Arial', 16, 'bold'))
    titulo.pack(pady=10)

    # Adicionando botões principais: Cadastro, Emprestimos, Relatório e Sair
    btn_cadastrar_usuario = tk.Button(root, text='Cadastrar Usuário', command=self.abrir_cadastro_usuario, width=30)
    btn_cadastrar_usuario.pack(pady=5)

    btn_cadastrar_livro = tk.Button(root, text='Cadastrar Livros', command=self.abrir_cadastro_livro, width=30)
    btn_cadastrar_livro.pack(pady=5)

    btn_emprestimos = tk.Button(root, text='Gerenciar Empréstimos e Devoluções', command=self.abrir_emprestimos, width=30)
    btn_emprestimos.pack(pady=5)

    btn_relatorios_usuarios = tk.Button(root, text='Gerar Relatórios Usuários', command=self.abrir_relatorios_usuarios, width=30)
    btn_relatorios_usuarios.pack(pady=5)

    btn_relatorios_livros = tk.Button(root, text='Gerar Relatórios', command=self.abrir_relatorios_livros, width=30)
    btn_relatorios_livros.pack(pady=5)

    btn_sair = tk.Button(root, text='Sair', command=root.quit, width=30, bg='red', fg='white')
    btn_sair.pack(pady=5)
  
  def abrir_cadastro_livro(self):
    # Adicionando a lógica para abrir a janela de cadastro
    def cadastrar_livros():
      titulo = entry_titulo.get()
      autor = entry_autor.get()
      ano = int(entry_ano.get())
      copias = int(entry_copias.get())
      livro = Livro(titulo, autor, ano, copias)
      self.biblioteca.cadastrar_livros(livro)
      messagebox.showinfo("Cadastro", f"Livro '{titulo}' cadastrado com sucesso!")
      janela_livro.destroy()
    
    janela_livro = tk.Toplevel(self.root)
    janela_livro.title('Cadastrar Livro')

    tk.Label(janela_livro, text='Título').pack()
    entry_titulo = tk.Entry(janela_livro)
    entry_titulo.pack()

    tk.Label(janela_livro, text='Autor').pack()
    entry_autor = tk.Entry(janela_livro)
    entry_autor.pack()

    tk.Label(janela_livro, text='Ano').pack()
    entry_ano = tk.Entry(janela_livro)
    entry_ano.pack()

    tk.Label(janela_livro, text='Cópias').pack()
    entry_copias = tk.Entry(janela_livro)
    entry_copias.pack()

    btn_salvar = tk.Button(janela_livro, text='Salvar', command=cadastrar_livros)
    btn_salvar.pack(pady=10)
  
  def abrir_cadastro_usuario(self):
    def cadastrar_usuario():
      nome = entry_nome.get()
      id_usuario = entry_id_usuario.get()
      contato = entry_contato.get()

      usuario = Usuario(nome, id_usuario, contato)
      self.biblioteca.cadastrar_usuario(usuario)
      messagebox.showinfo("Cadastro de Usuário", f"Usuário '{nome}', '{id_usuario}' cadastrado com sucesso!")
      janela_usuario.destroy()

    janela_usuario = tk.Toplevel(self.root)
    janela_usuario.title("Cadastrar Usuário")

    tk.Label(janela_usuario, text='Nome').pack()
    entry_nome = tk.Entry(janela_usuario)
    entry_nome.pack()

    tk.Label(janela_usuario, text='Id do Usuário').pack()
    entry_id_usuario = tk.Entry(janela_usuario)
    entry_id_usuario.pack()

    tk.Label(janela_usuario, text='Contato do Usuário').pack()
    entry_contato = tk.Entry(janela_usuario)
    entry_contato.pack()

    btn_salvar_usuario = tk.Button(janela_usuario, text='Salvar', command=cadastrar_usuario)
    btn_salvar_usuario.pack(pady=10)
  
  def abrir_janela_emprestimos():
      janela_emprestimos = tk.Toplevel(self.root)
      janela_emprestimos.title("Gerenciar Empréstimos")

      # Seção de usuários
      tk.Label(janela_emprestimos, text='Usuário').pack()
      usuarios = [f"{u.nome} ({u.id_usuario})" for u in self.biblioteca.usuarios]
      combo_usuarios = ttk.Combobox(janela_emprestimos, values=usuarios)
      combo_usuarios.pack()

      # Seção de livros
      tk.Label(janela_emprestimos, text="Livro").pack()
      livros = [l.titulo for l in self.biblioteca.livros]
      combo_livros = ttk.Combobox(janela_emprestimos, values=livros)
      combo_livros.pack()
    
  def exibir_emprestimos(self):
    emprestimos = self.biblioteca.emprestimos

    if not emprestimos:
      messagebox.showinfo("Empréstimos Ativos", "Nenhum empréstimo ativo")
      return
  
  def abrir_emprestimos(self):
    # Janela para gerenciar empréstimos
    def emprestar_livros():
      id_usuario = entry_id_usuario.get().strip() # Extrai ID do usuário
      titulo_livro = entry_titulo_livro.get().strip()

      # Verifica se o usuário e o livro foram selecionados
      if not id_usuario or not titulo_livro:
        messagebox.showwarning("Entrada Inválida", "Por favor, selecione um usuário e um livro!")
        return

      # Busca o usuário e o livro na Biblioteca
      usuario = next((u for u in self.biblioteca.usuarios if u.id_usuario == id_usuario), None)
      livro = next((l for l in self.biblioteca.livros if l.titulo == titulo_livro), None)

      if not usuario:
        messagebox.showerror("Error", f"Usuário com ID {id_usuario} não encontrado!")
        return
      
      if not livro:
        messagebox.showerror("Error", f"Livro '{titulo_livro}' não encontrado!")
      
      # Verifica se o livro está disponível para empréstimo
      if livro.num_copias_disponiveis > 0:
        livro.num_copias_disponiveis -= 1
        usuario.registrar_emprestimo(livro)
        messagebox.showinfo("Sucesso", f"Empréstimo do livro '{titulo_livro}' realizado com sucesso!")
      else:
        messagebox.showerror("Error", f"Não há cópias disponíveis do livro '{titulo_livro}'!")
      
    def exibir_emprestimos():
      emprestimos = self.biblioteca.emprestimos  # Corrigido para acessar o atributo correto
      if not emprestimos:
          messagebox.showinfo("Empréstimos Ativos", "Nenhum empréstimo ativo.")
          return

        # Cria janela para exibir empréstimos
      janela_exibir = tk.Toplevel(self.root)
      janela_exibir.title("Empréstimos Ativos")

      for usuario_id, livros in emprestimos.items():
          usuario = next((u for u in self.biblioteca.usuarios if u.id_usuario == usuario_id), None)
          if usuario:
              tk.Label(janela_exibir, text=f"Usuário: {usuario.nome}").pack()
              for livro in livros:
                  tk.Label(janela_exibir, text=f"  - {livro.titulo}").pack()
    
    def devolver_livro():
      id_usuario = entry_id_usuario.get().strip()
      titulo_livro = entry_titulo_livro.get().strip()

      try:
        self.biblioteca.devolver_livro(id_usuario, titulo_livro)
        messagebox.showinfo("Devolução", f"Livro '{titulo_livro}' devolvido com sucesso!")
        janela_emprestimos.destroy()
      except Exception as e:
        messagebox.showerror('Error', str(e))
    
    # Cria a janela de empréstimos
    janela_emprestimos = tk.Toplevel(self.root)
    janela_emprestimos.title('Gerenciar Empréstimos e Devoluções')

    tk.Label(janela_emprestimos, text='Id do Usuário').pack()
    entry_id_usuario = tk.Entry(janela_emprestimos)
    entry_id_usuario.pack()

    tk.Label(janela_emprestimos, text='Título do Livro').pack()
    entry_titulo_livro = tk.Entry(janela_emprestimos)
    entry_titulo_livro.pack()

    btn_emprestar = tk.Button(janela_emprestimos, text="Emprestar Livro", command=emprestar_livros)
    btn_emprestar.pack(pady=5)

    btn_devolver = tk.Button(janela_emprestimos, text='Devolver Livro', command=devolver_livro)
    btn_devolver.pack(pady=5)

    btn_exibir_emprestimos = tk.Button(janela_emprestimos, text="Exibir Empréstimos Ativos", command=exibir_emprestimos)
    btn_exibir_emprestimos.pack(pady=5)

    btn_fechar = tk.Button(janela_emprestimos, text="Fechar", command=janela_emprestimos.destroy)
    btn_fechar.pack(pady=5)
  
  def abrir_relatorios_livros(self):
    # Relatório de livros disponíveis
    livros = self.biblioteca.gerar_relatorios_livros_disponiveis()
    if livros:
        relatorio = '\n'.join([f"{livro.titulo} - {livro.num_copias_disponiveis} cópias" for livro in livros])
    else:
        relatorio = 'Nenhum livro disponíveis!'
    
    messagebox.showinfo('Relatórios de Livros Disponíveis', relatorio)
  
  def abrir_relatorios_usuarios(self):
    usuarios = self.biblioteca.gerar_relatorio_usuarios()
    if usuarios:
        relatorio = '\n'.join(usuarios)
    else:
        relatorio = 'Nenhum usuário encontrado!'
  
    messagebox.showinfo('Relatório de Usuários', relatorio)

# Criando aplicação
if __name__ == "__main__":
  root = tk.Tk()
  app = BibliotecaApp(root)
  root.mainloop()

