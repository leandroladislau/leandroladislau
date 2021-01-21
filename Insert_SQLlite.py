import sqlite3
import random
import time
import datetime
import os

# os.remove("teste.db") if os.path.exists("teste.db") else None
 
# Criando uma conexão
conn = sqlite3.connect("D:\Git\PyCharm_Git\teste.db")

# Criando um cursor
c = conn.cursor()

prod = ["Keyboard", "Monitor", "Notebook", "Mouse"]
 
# Função para criar uma tabela
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, '\
              'prod_name TEXT, valor REAL)')

def new_valor():
    for i in prod:
        if (prod == "Keyboard"):
            random.randrange(50,100)
        elif (prod == 'Monitor'):
            random.randrange(500,1000)
        elif (prod == 'Notebook'):
            random.randrange(3500,10000)
        elif (prod == 'Mouse'):
            random.randrange(50,100)

def random_date():
    start_date = datetime.date(2010, 1, 1)
    end_date = datetime.date(2021, 12, 31)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    
# Função para inserir uma linha
def data_insert():
    c.execute("INSERT INTO products VALUES(002, '02-05-2020', 'teclado', 130 )")
    conn.commit()
 
create_table()

# Leitura de dados
def leitura_todos_dados():
    c.execute("SELECT * FROM products")
    for row in c.fetchall():
        print(row)
        
# Leitura de registros específicos
def leitura_registros():
    c.execute("SELECT * FROM products WHERE valor > 500.0")
    for row in c.fetchall():
        print(row)      
        
# Leitura de colunas específicos
def leitura_colunas():
    c.execute("SELECT * FROM products")
    for row in c.fetchall():
        print(row[3])

leitura_todos_dados()

# Definindo linhas na tabela
def contagem_linhas():
    c.execute("select * from products")
    results = c.fetchall()
    n_linhas = len(results)
    print (len(results))

contagem_linhas()

# Usando variáveis para inserir dados    
def data_insert_var():
    new_date = random_date
    new_prod_name = random.choice('prod')
    set_valor = new_valor()
    c.execute("INSERT INTO products (date, prod_name, valor) VALUES (?, ?, ?, ?)",
              (new_date, new_prod_name, new_valor))

# Gerando valores e inserindo na tabela
while 'n_linhas' < 50:
    data_insert_var()
    time.sleep(1)

leitura_todos_dados()

# Update
def atualiza_dados():
    c.execute("UPDATE products SET valor = 70.00 WHERE valor = 98.0")
    conn.commit()

# Delete
def remove_dados():
    c.execute("DELETE FROM products WHERE valor = 62.0")
    conn.commit()
    
# Encerrando a conexão
c.close()
conn.close()