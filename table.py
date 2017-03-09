#table
#coding=utf-8

import MySQLdb
import json

class Table(object):
    #classmembervariables

    Name = "table"
    #classmembermethods
    def __init__(self,conn,tablename,dbname = 'testdb'):
        
        self.Conn = conn
        self.TableName = tablename
        self.Name = tablename
        self.Cur = conn.cursor()
        
        #init colmuns
        sql = "select column_name from information_schema.columns where table_schema = '"
        sql = sql + dbname
        sql = sql + "' and table_name = '"
        sql = sql + tablename
        sql = sql + "'"
        self.Cur.execute(sql)
        self.Columns = []
        resultsrows = self.Cur.fetchall()
        for eachrow in resultsrows:
            self.Columns.append(eachrow[0])
            
        self.HaveInsertSql = False
        self.InsertSql = ""
        
        self.HaveJsonData = False
        
        
    
    def GenerateInsertSql(self,jsondata):
        print 1
        pass
        
    
    def LoadJsonData(self,jsondata):
        self.JsonData = jsondata
        self.HaveJsonData = True
        return True
    
    def GetInsertSql(self):
        if self.HaveInsertSql == True:
            return self.InsertSql
        
        
        return self.GenerateInsertSql(self.JsonData)
    
    def Insert(self,jsondata):
        
        
        self.GenerateInsertSql(jsondata)
        #print self.InsertSql
        
        try :
            self.Cur.execute(self.InsertSql)
            
            self.Conn.commit()
                  
        except :
            
            #print e.args[1]
            self.Conn.rollback()
            
            return False
        
        return True
            
            
    
    
        
        
        
        