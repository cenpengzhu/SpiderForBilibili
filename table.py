#table
#coding=utf-8

import MySQLdb
import json

class TableObject(object):
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
        insertsql = "insert into "
        insertsql = insertsql + self.TableName
        insertsql = insertsql + " ( "
        tempflag = 0
        values = list()
        for eachcolumn in self.Columns:
            if jsondata.get(eachcolumn) != None :

                if tempflag == 0 :
                    insertsql = insertsql + eachcolumn
                    tempflag = 1
                else :
                    insertsql = insertsql + " , "
                    insertsql = insertsql + eachcolumn
                
                if isinstance(jsondata.get(eachcolumn), bool):
                    if jsondata.get(eachcolumn) == True :
                        values.append("1")
                    else :
                        values.append("0")
                elif isinstance(jsondata.get(eachcolumn), int):
                    values.append(str(jsondata.get(eachcolumn)))                    
                
                elif isinstance(jsondata.get(eachcolumn), unicode):  
                    tempstr =  jsondata.get(eachcolumn)
                    tempstr = "'"+tempstr+"'"
                    tempstr = tempstr.encode("utf-8")
                    values.append(tempstr)
                else :
                    #print type(jsondata.get(eachcolumn))
                    values.append(jsondata.get(eachcolumn))
                
            
        insertsql = insertsql + " ) values ( "
        tempflag = 0
        for eachvalue in values:
            if tempflag == 0 :
                insertsql = insertsql + eachvalue
                tempflag = 1
            else :
                insertsql = insertsql + ' , '
                insertsql = insertsql + eachvalue
                
                
        insertsql = insertsql + " ) "
        
        self.InsertSql = insertsql
        
        self.HaveInsertSql = True
                
        return insertsql
    
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
            
            
    
    
        
        
        
        