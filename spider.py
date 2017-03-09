#spyder

#coding=utf-8

import urllib
import urllib2
import time
import json
import spiderjobs
import table
import MySQLdb
import birthdatatable

class SpyderObject(object) :
    #classmembervariables
      
    #classmembermethod
    
    def __init__(self,tablename):
        self.Jobs = spiderjobs.SpyderJobsObject()
        self.JsonDatas = []
        #init mysql
        
        conn = MySQLdb.connect(host='localhost',port = 3306 ,user = 'root',passwd = 'root',db = 'testdb',charset = 'utf8')
        
        if tablename == "user" :
            self.Table = table.TableObject(conn,tablename)
        
        elif tablename == "birthdata":
            self.Table = birthdatatable.BirthDataTable(conn,tablename)
            
        
        
        
        
    def RequestOne(self):
            job = self.Jobs.PopOneJob()
            if job.Type == "POST" :
                #print job.NO
                #print job.Values['mid']
                data = urllib.urlencode(job.Values)
                request = urllib2.Request(job.RequestUrl,data,job.Headers)
                try :
                    
                    print "request jos no %d"%job.NO
                    response = urllib2.urlopen(request, data)
                    re_data = re_data = response.read()
                    
                    re_data = re_data.decode('utf8')
                    
                    jsondata = json.loads(re_data)
                    
                
                    #jsondata = _decode_dict(jsondata)
                   # print jsondata
                    #print jsondata['status']
                    if jsondata['status'] == True:
                        if self.Table.TableName == 'birthdata' :
                            jsondata = _decode_dict(jsondata)
                            self.JsonDatas.append(jsondata)
                        
                        else :  
                            self.JsonDatas.append(jsondata)  
                        
                    
                except urllib2.HTTPError, e:
                    print e.code
                    print e.reason
                    print job.NO
                    self.Jobs.Done(job,0)
                    return False
                else :
                    self.Jobs.Done(job)
                
                return True
            
    
    def RequestAll(self):
        
        while self.Jobs.StillHaveJobs() :
            if self.RequestOne() == False:
                time.sleep(300)
            else :
                time.sleep(1)    
        return True
 
 
    def WriteOne(self):
        if len(self.JsonDatas) > 0 :
            
            #bilibili User special
            if self.Table.TableName == "user" :
                jsondata = self.JsonDatas.pop()['data']
                
            else :
                jsondata = self.JsonDatas.pop()
                
            self.Table.Insert(jsondata)
            
        else :
            
            return False
            
        return True
    
    def WriteAll(self):
        while self.WriteOne():
            pass
            
            
        return True
    
    

def _decode_dict(data):
    rv = {}
     
    for key,value in data.iteritems() :
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        
        if isinstance(value, unicode):
            value = value.encode('utf-8')
            
        elif isinstance(value, list):
            value = _decode_list(value)
            
        elif isinstance(value, dict):
            value = _decode_dict(value)
        
        rv[key] = value
        
    return rv

def _decode_list(data):
    rv = []
    
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
            print item
        elif isinstance(item, list):
            item = _decode_list(item)
            
        elif isinstance(item, dict):
            item = _decode_dict(item)
            
        rv.append(item)
        
    return rv
        
    
    
            
            
            
            
            
        
        
        
    
        
    
    

