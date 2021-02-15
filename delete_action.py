#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Gabriel Garcia Da Silva
Email: gsilva.gabriel@outlook.com
exclui os dados antigos
"""
import pymysql
import pymysql.cursors
import requests
from datetime import datetime

# conexao com o banco de dados MySQL
con = pymysql.connect(host='localhost', db='developer', user='root', passwd='password',cursorclass=pymysql.cursors.DictCursor)

# abre um cursor para realizar a query
cur = con.cursor()
cur.execute("DELETE FROM developer.ACTION_MONITORING WHERE DATE_ACTION < (NOW() - INTERVAL 4 HOUR);")

print('Termino do script !')