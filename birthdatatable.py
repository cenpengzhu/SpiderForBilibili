#birthdatatable
#coding=utf-8

import MySQLdb
import json
import table
from table import TableObject

class BirthDataTable(TableObject):
    #classmembervariables

    Name = "birthdata"
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
        insertsql = insertsql + " ( mid ,jsondata ) values ( "
        tempflag = 0
        values = list()
        values.append(jsondata['data']['mid'])
        values.append(jsondata['data'])
                    
        tempflag = 0
        for eachvalue in values:
            
            if isinstance(eachvalue, int):
                
                if tempflag == 0 :
                    
                    insertsql = insertsql + str(eachvalue)
                    tempflag = 1
                else :
                    
                    insertsql = insertsql + ' , '
                    insertsql = insertsql + str(eachvalue)
                    
            elif isinstance(eachvalue, dict):   
                
                if tempflag == 0 :
                    
                    insertsql = insertsql + "'"+json.dumps(eachvalue,encoding='utf-8',ensure_ascii=False)+"'"
                    tempflag = 1
                else :
                    print(eachvalue)
                    insertsql = insertsql + ' , '
                    insertsql = insertsql + "'"+json.dumps(eachvalue,encoding='utf-8',ensure_ascii=False)+"'"  
                      
            elif isinstance(eachvalue, str):   
                
                if tempflag == 0 :
                    
                    insertsql = insertsql + '"'+eachvalue+'"'
                    tempflag = 1
                else :
                    
                    insertsql = insertsql + ' , '
                    insertsql = insertsql + '"'+eachvalue+'"'                                                       
                
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
        print self.InsertSql
        
        try :
            self.Cur.execute(self.InsertSql)
            
            self.Conn.commit()
                  
        except :
            
            #print e.args[1]
            self.Conn.rollback()
            
            return False
        
        return True
            
            
    
    
        
        
        
        