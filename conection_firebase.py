#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Gabriel Garcia Da Silva
Email: gsilva.gabriel@outlook.com
Script que conecta com o firebase e faz inserção
"""
# script para conexão e salvar no firebase
from pyrebase import pyrebase
import pymysql

# daodos necessarios para se conectar com o firebase
firebaseConfig = {
    "apiKey": "AIzaSyAn0Fp13RTGPd4IvfkcsIbZo8v3cyamL5o",
    "authDomain": "golden-knight-4c92c.firebaseapp.com",
    "databaseURL": "https://golden-knight-4c92c.firebaseio.com",
    "projectId": "golden-knight-4c92c",
    "storageBucket": "golden-knight-4c92c.appspot.com",
    "messagingSenderId": "699482600799",
    "appId": "1:699482600799:web:e3afe2e2cc2c320b77b2ea"
}

# iniciando a conexao com o firebase
firebase = pyrebase.initialize_app(firebaseConfig)

# criando instancia
dados = firebase.database()

# conexao com o banco de dados MySQL
con = pymysql.connect(host='localhost', db='developer', user='root', passwd='password',cursorclass=pymysql.cursors.DictCursor)

# abre um cursor para realizar a query
cur = con.cursor()
cur.execute(''' SELECT 	MAX(DATE_ACTION) DATE_ACTION,
		                NAME_ACTION,
                        CODE_ACTION,
                        VALUE_ACTION
                FROM 	developer.ACTION_MONITORING
                GROUP BY    NAME_ACTION,
			                CODE_ACTION,
                            VALUE_ACTION;
''')

for row in cur.fetchall():
    dados.child().update(
        {
            "%s"%row['CODE_ACTION']:{
                "nome_ação": "%s"%row['NAME_ACTION'],
                "data_ação": "%s"%row['DATE_ACTION'],
                "valor_ação": "%s"%row['VALUE_ACTION']
            }
        }
    )

print('Termino do script !')