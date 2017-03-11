#spiderjobs

#coding=utf-8


class SpiderJobs(object):
    
    #classmemebervariables
    
    #classmembermethods
    
    def __init__(self):
        self.ListOfJobs = []
        self.CurrentJob = 0
             
    
    def AddOneJob(self,type,requesturl,headers,values):
        no = len(self.ListOfJobs)
        job = SpiderJob(type,requesturl,headers,values,no)
        self.ListOfJobs.append(job)
        
        return True
         
    
    def PopOneJob(self):
        return self.ListOfJobs.pop(self.ListOfJobs[0])




    
    def Done(self,job,done = 1):
        if done == 0 :
            self.AddOneJob(job.Type, job.RequestUrl, job.Headers, job.Values)
            return True
        else :
            job.Done = 1
            return True
    
    def StillHaveJobs(self):
        if self.CurrentJob < len(self.ListOfJobs):
            return True
        else :
            return False
 
 
 
class SpiderJob(object):   
    
    def __init__(self,type,requesturl,headers,values,no):
        self.Type = type
        self.RequestUrl = requesturl
        self.Headers = headers
        self.Values = values
        self.NO = no
        self.Done = 0
            
       
    
        
    
        
            
        
        
    