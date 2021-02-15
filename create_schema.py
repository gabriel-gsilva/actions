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
cur.execute("SELECT NAME_URL FROM developer.abc;")

try:
    for result in cur.fetchall():
        print(result)
except pymysql.err.ProgrammingError as except_detail:
    print("Deu RUIM pymysql.err.ProgrammingError: «{}»".format(except_detail))