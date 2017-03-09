#birthdatatable

#coding=utf-8

import MySQLdb
import json
import table
from table import Table

class BirthDataTable(Table):
    #classmembervariables

    Name = "birthdata"
    #classmembermethods
    def __init__(self,conn,tablename,dbname = 'testdb'):   
        Table.__init__(self,conn,tablename,dbname)
        
        
    
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
    
    

            
            
    
    
        
        
        
        