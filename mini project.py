

class Train:
    train_list=list()
    def __init__(self,train_no,train_name,arrivel_time,depature_time,platfrom_no,source,destination):
        self.train_no=train_no
        self.train_name=train_name
        self.arrivel_time=arrivel_time
        self.depature_time=depature_time
        self.platfrom_no=platfrom_no
        self.source=source
        self.destination=destination
    def add_train(self):
        Train.train_list.append(self)       #f" {self.train_no} { self.train_name } {self.arrivel_time} {self.depature_time} {self.platfrom_no} {self.source} {self.destination}

    @staticmethod
    def  gettrain_list():
        return Train.train_list
#TO  PROVIDE STRING REORESENTATION OF AN OBJECT.
    def __str__(self):
        return  f" {self.train_no} { self.train_name } {self.arrivel_time} {self.depature_time} {self.platfrom_no} {self.source} {self.destination}"

    def gettrain_number(self):
        return self.train_no
    
    def settrain_number (self ,train_number):
        self.train_number=train_number
    @staticmethod   
    def updatetrain (train_no,train_name,arrivel_time,depature_time,platfrom_no,source,destination):
        for train in Train.train_list:
            print("************",train,"*******************")
            if train. gettrain_number() == train_no:
                train.train_no = train_no
                train.arrivel_time = arrivel_time
                train.depature_time=depature_time
                train.platfrom_no=platfrom_no
                train.source=source
                train.destination=destination
          
                return True
        return False         

    @staticmethod          
    def delete_train (train_no):
          for train in Train.train_list:
              if train.gettrain_number()==train_no:
                  Train.train_list.remove(train)
                  return True
          return False

    @staticmethod
    def search_train (train_no):
         for train in Train.train_list:
             if train.gettrain_number()==train_no:
                 return train
         return None     

        
choice=1

while choice>=1 and choice <=6:
    print (" Welcome to train timetable system")
    print("Please inter your choice")

    print("1. Add New Train Details\n 2. Show Train DETAILS\n 3.UPDATE TRAIN DETAILS\n 4.DELETE \n 5.SEARCH TRAIN\n")
    choice=int(input("ENTER YOUR CHOICE  :"))
    if choice==1:
    
        train_no=int(input("ENTER TRAIN NUMBER  :"))
        train_name= input("ENTER TRAIN NAME  :")
        arrivel_time=input("ENTER ARRIVEL TIME  :")
        depature_time=input("ENTER Depature Time  :")
        platfrom_no=int (input("ENTER Platfrom No  :"))
        source=input("ENTER SOURCE:")
        destination=input("ENTER Destination   :")

        t=Train(train_no, train_name, arrivel_time, depature_time, platfrom_no, source, destination)
        t.add_train()
        print( "SUCCESSFULLY ADDED TRAIN")
        
        
    elif(choice==2):
         for train in  Train.gettrain_list():
             print(train)
             
    elif(choice==3):
         train_no=int(input("ENTER TRAIN NUMBER  :"))
         train_name= input("ENTER NEW TRAIN NAME  :")
         arrivel_time=input("ENTER NEW ARRIVEL TIME  :")
         depature_time=input("ENTER NEW Depature Time  :")
         platfrom_no=int (input("ENTER NEW  Platfrom No  :"))
         source=input("ENTER NEW  SOURCE   :")
         destination=input("ENTER NEW Destination   :")

         if Train.updatetrain (train_no, train_name, arrivel_time, depature_time, platfrom_no, source, destination):
                 print("Successfully update")
         else :
             print("  TRAIN NOT FOUND  ", train_no)
             
    elif(choice==4):
        train_no = int (input("ENTER TRAIN NUMBER TO DELETE ::"))
        if Train.delete_train (train_no):
            print ("train delete succufully")
        else:
           print ("TRAIN NOT FOUND", train_no)
        
            
    elif(choice==5):
        tarin_no= int(input("ENTER TRAIN NUMBER TO SEARCH:"))
        train = Train.search_train(train_no)
        if train:
            print("TRAIN FOUND:")
            print(train)
        else :
            print("TRAIN NOT FOUND",train_no)
        
      
    else:
      break
    
 
            

