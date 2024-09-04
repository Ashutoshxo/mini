'''
class Eshop:
    prodlist=[ ]
    def __init__ (self,prod_id,prod_name,prod_type,price,quantity):
        self.prod_id=prod_id
        self.prod_name=prod_name
        self.prod_type=prod_type
        self.price=price
        self.quantity=quantity


    def __str__ (self):
        return f" {self.prod_id} {self.prod_name} {self.prod_type} {self.price} {self.quantity}"
       

       
    def add_prod(self):
       Eshop.prodlist.append(self)


    def search (prod_id_search):
        for i in Eshop.prodlist:
            if i.prod_id==prod_id_search:
                return i
        return None    


    def delete_prod(prod_id_delete):
        for i in Eshop.prodlist:
            if i.prod_id==prod_id_delete:
                Eshop.prodlist.remove (i)
                return True
        return False    

    def updateprod(prod_id,prod_name,prod_type,price,quantity ):
        for i in Eshop.prodlist:
            if i. prod_id==prod_id:
                i.prod_id=prod_id
                i.prod_name=prod_name
                i.prod_type=prod_type
                i.price=price
                i.quantity=quantity
                

e1=e_shop(101,"ruka",electroic",40000,20)

e1.show()
'''
'''
choice =1

while(choice >=1 and choice <=5):
    print(('Enter your choice: '))
    print ("please select your choice:")
    print ("1 Add product")
    print ("2 Show producta")
    print("3 Secrch product")
    print("4 delect proct")
    print("5 update product")
    
    choice =int(input("enter your choice :"))

    if choice == 1:
          prod_id = int(input("Enter id:"))
          prod_name = input ("ENTER PRODUCT CATEGORY:")
          prod_type= input ("ENTER PRODUCT NAME:")
          price = float (input ("ENTER PRICE "))
          quantity = int(input("ENTER QUANTITY"))

          p1 = Eshop(prod_id,prod_name,prod_type,price,quantity)
          p1.add_prod()
                   
    elif choice ==2:
        for i in Eshop.prodlist:
            print (i)
             
    elif choice ==3:
        prod_id_search=int(input("ENTER ID:"))
        new=Eshop.search(prod_id_search)
        if new:
            print ( "product is found ",new)
        else :
            print ("product is not fount")
            
    elif choice ==4:
        prod_id_delete=int(input("ENTER ID:"))
        new=Eshop.search(prod_id_delete)
        if new:
            print ( "product is deleted ",new)
        else :
            print ("product is not deleted casue not found")
        
    elif choice==5:
        prod_id = int(input("Enter id:"))
        prod_name = input ("ENTER PRODUCT CATEGORY:")
        prod_type= input ("ENTER PRODUCT NAME:")
        price = float (input ("ENTER PRICE "))
        quantity = int(input("ENTER QUANTITY"))

        new = Eshop.updateprod(prod_id,prod_name,prod_type,price,quantity )
        if new:
            print ("Product is successfully update")

        else :
            
            print ("product not found")
    else: 
       break
            


'''



#write a program currency in inr to dollar



def inr_to_usd(inr_amount, exchange_rate=0.012):
    usd_amount = inr_amount * exchange_rate
    return usd_amount

inr_amount = float(input("Enter amount in INR: "))
usd_amount = inr_to_usd(inr_amount)
print(f"{inr_amount} INR is equal to {usd_amount:.2f} USD")

#why  we complex number ?
#diff list and tuple??**************************** cant modify tuple is if we define onece
# what division /   and floor division //??
#diff remove and del???*** and pop
#diff shallow copy and deep copy????************
#what is list comprehensions??**********
#how to remove an element form set ??
# what tuple and packing and unpacking??
#wht is diff remove and set?????
