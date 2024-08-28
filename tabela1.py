import sqlite3

# Conectar (ou criar) um banco de dados
conexao = sqlite3.connect('pokemon.db')

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()
cursor.execute('''  CREATE TABLE IF NOT EXISTS pokemons (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Chave primária e autoincremento
                    name text,
                    level int,
                    forca int);
''')
cursor.execute('''
    INSERT INTO pokemons (name, level, forca)
    VALUES ('charizard', 50, 25)
''')

# Consultar todos os dados da tabela
cursor.execute('SELECT * FROM pokemons')

# Obter todos os registros da tabela
usuarios = cursor.fetchall()

# Printar (exibir) os dados da tabela
print("id | cpf            | nascimento | matricula")
print("----------------------------------------------")
for usuario in usuarios:
    print(f"{usuario[0]} | {usuario[1]} | {usuario[2]} | {usuario[3]}")

# Fechar a conexão
conexao.commit()
conexao.close()