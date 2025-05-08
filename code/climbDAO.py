# -*- coding: utf-8 -*-
# 

import mysql.connector
import dbconfig as cfg

class ClimbDAO:
    connection = ""
    cursor = ''
    host = ''
    user = ''
    password = ''
    database = ''

    def __init__(self):
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.cursor.close()
        self.connection.close()

    def getAll_climbs(self):
        cursor = self.getcursor()
        sql = "SELECT * FROM climbs"
        cursor.execute(sql)
        results = cursor.fetchall()
        climbs = []
        for result in results:
            climbs.append(self.convertToDictionary(result))
        self.closeAll()
        return climbs

    def convertToDictionary(self, resultLine):
        keys = ['id', 'name', 'grade', 'crag_id', 'style_id']
        return dict(zip(keys, resultLine))

climbDAO = ClimbDAO()
