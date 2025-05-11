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
        sql = """
        SELECT c.name,c.grade,cr.name as Crag_Name,s.style_name as Style,cl.date_climbed
              FROM climbs as c  
              JOIN crags as cr  
              ON c.crag_id = cr.id  
              JOIN styles as s 
              ON c.style_id = s.id
              JOIN climb_log as cl
                ON c.id = cl.climb_id
        """
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

    def create_climb_with_log(self, data):
        cursor = self.getcursor()
    
        # Insert into climbs
        sql_climb = "INSERT INTO climbs (name, grade, crag_id, style_id) VALUES (%s, %s, %s, %s)"
        climb_values = (
            data.get("name"),
            data.get("grade"),
            data.get("crag_id"),
            data.get("style_id")
            )
        cursor.execute(sql_climb, climb_values)
        climb_id = cursor.lastrowid

        # Insert into climb_log
        sql_log = """
            INSERT INTO climb_log (climb_id, completed, attempts, personal_grade_feeling, date_climbed)
            VALUES (%s, %s, %s, %s, %s)
            """
        log_values = (
            climb_id,
            data.get("completed", False),
            data.get("attempts", 0),
            data.get("personal_grade_feeling", None),
            data.get("date_climbed", None)
        )
        cursor.execute(sql_log, log_values)
        self.connection.commit()
        self.closeAll()

        return {
            "id": climb_id,
         "name": data.get("name"),
         "grade": data.get("grade"),
         "crag_id": data.get("crag_id"),
         "style_id": data.get("style_id"),
         "log": {
               "completed": log_values[1],
                "attempts": log_values[2],
                "personal_grade_feeling": log_values[3],
                "date_climbed": log_values[4]
            }
        }


climbDAO = ClimbDAO()
