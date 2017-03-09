#usertable
#coding=utf-8

import MySQLdb
import json
from table import Table

class UserTable(Table):
    #classmembervariables

    Name = "user"
    #classmembermethods
    def __init__(self,conn,tablename,dbname = 'testdb'):
        super.__init__(conn,tablename,dbname)
        
        
        
    
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

    
            
            
    
    
        
        
        
        