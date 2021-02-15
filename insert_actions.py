#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Gabriel Garcia Da Silva
Email: gsilva.gabriel@outlook.com
Script para automação da tarefa de verificar preço de ações
"""
import pymysql
import pymysql.cursors
import requests
from datetime import datetime

# informacoes mutaveis
hostname = 'localhost'
dbname = 'developer'
username = 'root'
key = 'password'

# conexao com o banco de dados MySQL
con = pymysql.connect(host=hostname, db=dbname, user=username, passwd=key,cursorclass=pymysql.cursors.DictCursor)

# abre um cursor para realizar a query
cur = con.cursor()
cur.execute("SELECT NAME_URL FROM developer.ACTION_URL;")

for row in cur.fetchall():
    # lendo pagina html
    url = row['NAME_URL']
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

    # abrindo conexao
    conexao = pymysql.connect(db=dbname, user=username, passwd=key)

    # cria cursor
    cursor = conexao.cursor()

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

    # executa comando no MySQL
    cursor.execute(text_insert)

    # commit no MySQL
    conexao.commit()

    # finaliza a conexao
    conexao.close()

# fecha a conexao aberta nas primeiras linhas
con.close()

# finalizando script
print('O script foi executado com sucesso !')