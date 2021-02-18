#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Gabriel Garcia Da Silva
Email: gsilva.gabriel@outlook.com
Script para automação da tarefa de verificar preço de ações
"""
import sqlite3
import requests
from datetime import datetime

# criacao do database e conexao
try:
    conn = sqlite3.connect('developer.db')
    connection = conn.cursor()
except Error as e:
    print(e)

# criacao de tabela para url de acoes
connection.execute('''
    CREATE TABLE IF NOT EXISTS ACTION_URL (
	    ID_URL INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME_URL TEXT NOT NULL
    )
''')

# query para consultar dados
connection.execute("SELECT NAME_URL FROM ACTION_URL;")

r = connection.fetchall()
if len(r) == 0:
    connection.execute("INSERT INTO ACTION_URL(NAME_URL) VALUES('https://www.infomoney.com.br/cotacoes/banco-inter-bidi4/')")
    connection.execute("INSERT INTO ACTION_URL(NAME_URL) VALUES('https://www.infomoney.com.br/cotacoes/itau-unibanco-itub3f/')")

connection.execute('''
    CREATE TABLE IF NOT EXISTS ACTION_MONITORING(
        ID_ACTION INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME_ACTION VARCHAR(30) NOT NULL,
        CODE_ACTION VARCHAR(10) NOT NULL,
        VALUE_ACTION NUMERIC(4,2) NOT NULL,
        DATE_ACTION TIMESTAMP NOT NULL
    )
''')

# consultando informacoes e 
connection.execute("SELECT NAME_URL FROM ACTION_URL")

for row in connection.fetchall():
    # lendo pagina html
    url = row[0]
    html = requests.get(url)

    # tags html para consulta
    tag_title = '<title>'
    tag_value = '<p>'

    contador = 0
    for content in html:
        content = str(content)

        # procura o titulo da aplicacao e aplica tratamento de string
        if content.find(tag_title) != -1:
            title_raw = content.split(tag_title)
            title_raw2 = title_raw[1]
            title = title_raw2.split(' | ')
        
        # procura o valor e aplica o tratamento de string
        elif content.find(tag_value) != -1:
            value_raw = content.split(tag_value)
            for n in value_raw:
                if contador == 21:
                    value = n.split('<')
                contador += 1

    # data e hora que o script esta rodando
    now = datetime.now()
    date_now = str(now.strftime("%Y/%m/%d %H:%M:%S")).replace('/', '-')

    # monta a variavel em string para posterior insert
    value = value[0]
    value = value.replace(',','.')
    
    # criando o codigo da aplicacao
    code_temp = title[0]
    code = code_temp.split()

    # criando o nome da empresa
    title_temp = title[0]
    title_temp = title_temp.split('(')
    title = title_temp[1]
    title = title[:-1]

    text_insert = ("INSERT INTO ACTION_MONITORING(NAME_ACTION, CODE_ACTION, VALUE_ACTION, DATE_ACTION) VALUES ('%s', '%s', '%s', '%s')"%(title, code[0], value, date_now))

    # executa comando
    connection.execute(text_insert)

# fecha a conexao aberta nas primeiras linhas
connection.close()

# finalizando script
print('O script foi executado com sucesso !')