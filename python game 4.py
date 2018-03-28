c=5
def main():
   

    print ("cover two box beside other and not as diametr")
    list1=[1 , 2, 3, 4]
    list2=[5 , 6, 7, 8]
    list3=[9, 10, 11,12]
    list4=[13,14,15,16]
    x=0
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    for i in range (17):
        a=int(input("player 1 choose any numper :"))
        if a in list1 :
            c=list1.index(a)       
            list1.remove(a)
            list1.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        elif a in list2 :
            c=list2.index(a)
            list2.remove(a)
            list2.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        elif a in list3 :
            c=list3.index(a)       
            list3.remove(a)
            list3.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        elif a in list4 :
            c=list4.index(a)       
            list4.remove(a)
            list4.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        else:
            continue
            
        while a==1 :
            j=int(input("player 1 choose any numper from 2,5 :"))
            if j==2 and j in list1 or j==5 and j in list2:
                print("complete")
            else :
                continue    
                
           
            while j==2 and j in list1 or j==5 and j in list2 :
            
           
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break 
                    
                
                 
                
                
                    
               
           
            
        while a==2 :
            
            j=int(input("player 1 choose any numper from 1,3,6 :"))
            if j==1 and j in list1 or j==3 and j in list1 or j==6 and j in list2:
                print("complete")
            else :
                continue    

            while j==1 or j==3 or j==6 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
        while a==3 :
            
            j=int(input("player 1 choose any numper from 2,4,7 :"))
          
            if j==2 and j in list1 or j==4 and j in list1 or j==7 and j in list2:
                print("complete")
            else :
                continue 
            while j==2 or j==4 or j==7 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
            
                    
        while a==4 :
            
            j=int(input("player 1 choose any numper from 3,8 :"))
            if j==3 and j in list1 or j==8 and j in list2 :
                print("complete")
            else :
                continue 
            while j==3 or j==8 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
            
        while a==5 :
            
            j=int(input("player 1 choose any numper from 1,6,9 :"))
            if j==1 and j in list1 or j==6 and j in list2 or j==9 and j in list3:
                print("complete")
            else :
                continue 
            while j==1 or j==6 or j==9 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
          
                    
        while a==6 :
            
            j=int(input("player 1 choose any numper from 2,5,7,10 :"))
            if j==2 and j in list1 or j==5 and j in list2 or j==7 and j in list2 or j==10 and j in list3:
                print("complete")
            else :
                continue 
            while j==2 or j==5 or j==7 or j==10 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    
                    break
                break
            break
            
        while a==7 :
            
            
            j=int(input("player 1 choose any numper from 3,6,8,11 :"))
            if j==3 and j in list1 or j==6 and j in list2 or j==8 and j in list2 or j==11 and j in list3:
                print("complete")
            else :
                continue 
            while j==3 or j==6 or j==8 or j==11 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break

           
        while a==8 :
            
            
            j=int(input("player 1 choose any numper from 4,7,12 :"))
            if j==4 and j in list1 or j==7 and j in list2 or j==12 and j in list3 :
                print("complete")
            else :
                continue           
            while j==4 or j==7  or j==12 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
          
        while a==9 :
            
            j=int(input("player 1 choose any numper from 5,10,13 :"))
            
            if j==5 and j in list2 or j==10 and j in list3 or j==13 and j in list4 :
                print("complete")
            else :
                continue 
            while j==5 or j==10  or j==13 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
         
        while a==10 :
            
            j=int(input("player 1 choose any numper from 6,9,11,14 :"))
            if j==6 and j in list2 or j==9 and j in list3 or j==11 and j in list3 or j==14 and j in list4 :
                print("complete")
            else :
                continue 
            while j==6 or j==9 or j==11 or j==14 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
                    
        while a==11 :
            
            j=int(input("player 1 choose any numper from 7,10,12,15 :"))
            if j==7 and j in list2 or j==10 and j in list3 or j==12 and j in list3 or j==15 and j in list4 :
                print("complete")
            else :
                continue 

            while j==7 or j==10 or j==12 or j==15 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
            
                    
        
        while a==12 :
            
            j=int(input("player 1 choose any numper from 8,11,16 :"))
            if j==8 and j in list2 or j==11 and j in list3 or j==16 and j in list4 :
                print("complete")
            else :
                continue 
            while j==8 or j==11 or j==16 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :  
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
           
                    
        while a==13 :
            
            j=int(input("player 1 choose any numper from 9,14 :"))
            if j==9 and j in list3 or j==14 and j in list4  :
                print("complete")
            else :
                continue 
            while j==9 or j==14  :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
           
        while a==14 :
            
            j=int(input("player 1 choose any numper from 10,13,15 :"))
            if j==10 and j in list3 or j==13 and j in list4 or j==15 and j in list4 :
                print("complete")
            else :
                continue 
            while j==10 or j==13 or j==15  :    
        


                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
           
        while a==15 :
            
            j=int(input("player 1 choose any numper from 11,14,16:"))
            if j==11 and j in list3 or j==14 and j in list4 or j==16 and j in list4 :
                print("complete")
            else :
                continue 
            while  j==11 or j==14 or j==16 :

                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                 
                    break
                break
            break
            
            
        while a==16 :
            
            j=int(input("player 1 choose any numper from 12,15:"))
            if j==12 and j in list3 or j==15 and j in list4  :
                print("complete")
            else :
                continue 
            while  j==12 or j==15 :

                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
        break
            
       

    
    for i in range (17):
        f=int(input("player 2 choose any numper :"))
        if f in list1 :
            c=list1.index(f)       
            list1.remove(f)
            list1.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        elif f in list2 :
            c=list2.index(f)
            list2.remove(f)
            list2.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        elif f in list3 :
            c=list3.index(f)       
            list3.remove(f)
            list3.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        elif f in list4 :
            c=list4.index(f)       
            list4.remove(f)
            list4.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        else :
             continue

            
        
        while f==1 :
            j=int(input("player 2 choose any numper from 2,5 :"))
            if j==2 and j in list1 or j==5 and j in list2:
                print("complete")
            else :
                continue    
                
           
            while j==2 and j in list1 or j==5 and j in list2 :
            
           
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break 
                    
                
                 
                
                
                    
               
           
            
        while f==2 :
            
            j=int(input("player 2 choose any numper from 1,3,6 :"))
            if j==1 and j in list1 or j==3 and j in list1 or j==6 and j in list2:
                print("complete")
            else :
                continue    

            while j==1 or j==3 or j==6 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
        while f==3 :
            
            j=int(input("player 2 choose any numper from 2,4,7 :"))
          
            if j==2 and j in list1 or j==4 and j in list1 or j==7 and j in list2:
                print("complete")
            else :
                continue 
            while j==2 or j==4 or j==7 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
            
                    
        while f==4 :
            
            j=int(input("player 2 choose any numper from 3,8 :"))
            if j==3 and j in list1 or j==8 and j in list2 :
                print("complete")
            else :
                continue 
            while j==3 or j==8 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
            
        while f==5 :
            
            j=int(input("player 2 choose any numper from 1,6,9 :"))
            if j==1 and j in list1 or j==6 and j in list2 or j==9 and j in list3:
                print("complete")
            else :
                continue 
            while j==1 or j==6 or j==9 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
          
                    
        while f==6 :
            
            j=int(input("player 2 choose any numper from 2,5,7,10 :"))
            if j==2 and j in list1 or j==5 and j in list2 or j==7 and j in list2 or j==10 and j in list3:
                print("complete")
            else :
                continue 
            while j==2 or j==5 or j==7 or j==10 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    
                    break
                break
            break
            
        while f==7 :
            
            
            j=int(input("player 2 choose any numper from 3,6,8,11 :"))
            if j==3 and j in list1 or j==6 and j in list2 or j==8 and j in list2 or j==11 and j in list3:
                print("complete")
            else :
                continue 
            while j==3 or j==6 or j==8 or j==11 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break

           
        while f==8 :
            
            
            j=int(input("player 2 choose any numper from 4,7,12 :"))
            if j==4 and j in list1 or j==7 and j in list2 or j==12 and j in list3 :
                print("complete")
            else :
                continue           
            while j==4 or j==7  or j==12 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
          
        while f==9 :
            
            j=int(input("player 2 choose any numper from 5,10,13 :"))
            
            if j==5 and j in list2 or j==10 and j in list3 or j==13 and j in list4 :
                print("complete")
            else :
                continue 
            while j==5 or j==10  or j==13 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
         
        while f==10 :
            
            j=int(input("player 2 choose any numper from 6,9,11,14 :"))
            if j==6 and j in list2 or j==9 and j in list3 or j==11 and j in list3 or j==14 and j in list4 :
                print("complete")
            else :
                continue 
            while j==6 or j==9 or j==11 or j==14 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
                    
        while f==11 :
            
            j=int(input("player 2 choose any numper from 7,10,12,15 :"))
            if j==7 and j in list2 or j==10 and j in list3 or j==12 and j in list3 or j==15 and j in list4 :
                print("complete")
            else :
                continue 

            while j==7 or j==10 or j==12 or j==15 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
            
                    
        
        while f==12 :
            
            j=int(input("player 2 choose any numper from 8,11,16 :"))
            if j==8 and j in list2 or j==11 and j in list3 or j==16 and j in list4 :
                print("complete")
            else :
                continue 
            while j==8 or j==11 or j==16 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :  
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
           
                    
        while f==13 :
            
            j=int(input("player 2 choose any numper from 9,14 :"))
            if j==9 and j in list3 or j==14 and j in list4  :
                print("complete")
            else :
                continue 
            while j==9 or j==14  :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
           
        while f==14 :
            
            j=int(input("player 2 choose any numper from 10,13,15 :"))
            if j==10 and j in list3 or j==13 and j in list4 or j==15 and j in list4 :
                print("complete")
            else :
                continue 
            while j==10 or j==13 or j==15  :    
        


                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
           
        while f==15 :
            
            j=int(input("player 2 choose any numper from 11,14,16:"))
            if j==11 and j in list3 or j==14 and j in list4 or j==16 and j in list4 :
                print("complete")
            else :
                continue 
            while  j==11 or j==14 or j==16 :

                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                 
                    break
                break
            break
            
            
        while f==16 :
            
            j=int(input("player 2 choose any numper from 12,15:"))
            if j==12 and j in list3 or j==15 and j in list4  :
                print("complete")
            
            else :
                continue 
            while  j==12 or j==15 :

                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
        break    
            
    #player 1 secend term   
    for i in range (17):
        a=int(input("player 1 choose any numper :"))
        if a in list1 :
            c=list1.index(a)       
            list1.remove(a)
            list1.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        elif a in list2 :
            c=list2.index(a)
            list2.remove(a)
            list2.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        elif a in list3 :
            c=list3.index(a)       
            list3.remove(a)
            list3.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        elif a in list4 :
            c=list4.index(a)       
            list4.remove(a)
            list4.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        else :
            continue
            
        
        while a==1 :
            j=int(input("player 1 choose any numper from 2,5 :"))
            if j==2 and j in list1 or j==5 and j in list2:
                print("complete")
            elif 2 not in list1 and 5 not in list2:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6   
            else :
                continue    
                
           
            while j==2 and j in list1 or j==5 and j in list2 :
            
           
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break 
                    
                
                 
                
                
                    
               
           
            
        while a==2 :
            
            j=int(input("player 1 choose any numper from 1,3,6 :"))
            if j==1 and j in list1 or j==3 and j in list1 or j==6 and j in list2:
                print("complete")
            elif  1  not in list1 and 3  not in list1 and 6  not in list2:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6
                
            else :
                continue    

            while j==1 or j==3 or j==6 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
        while a==3 :
            
            j=int(input("player 1 choose any numper from 2,4,7 :"))
          
            if j==2 and j in list1 or j==4 and j in list1 or j==7 and j in list2:
                print("complete")
            elif 2 not in list1 and 4 not in list1 and 7 not in list2:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6
            else :
                continue 
            while j==2 or j==4 or j==7 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
            
                    
        while a==4 :
            
            j=int(input("player 1 choose any numper from 3,8 :"))
            if j==3 and j in list1 or j==8 and j in list2 :
                print("complete")
            elif  3  not in list1 and 8  not in list2 :
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6        
            else :
                continue 
            while j==3 or j==8 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
            
        while a==5 :
            
            j=int(input("player 1 choose any numper from 1,6,9 :"))
            if j==1 and j in list1 or j==6 and j in list2 or j==9 and j in list3:
                print("complete")
            elif  1  not in list1 and 6  not in list2 and 9  not in list3:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6      
            else :
                continue 
            while j==1 or j==6 or j==9 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
          
                    
        while a==6 :
            
            j=int(input("player 1 choose any numper from 2,5,7,10 :"))
            if j==2 and j in list1 or j==5 and j in list2 or j==7 and j in list2 or j==10 and j in list3:
                print("complete")
            elif  2  not in list1 and 5 not in list2 and 7  not in list2:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6       
            else :
                continue 
            while j==2 or j==5 or j==7 or j==10 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    
                    break
                break
            break
            
        while a==7 :
            
            
            j=int(input("player 1 choose any numper from 3,6,8,11 :"))
            if j==3 and j in list1 or j==6 and j in list2 or j==8 and j in list2 or j==11 and j in list3:
                print("complete")

            elif  3  not in list1 and 6  not in list2 and 8  not in list2 and 11 not in list3:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6      
            else :
                continue 
            while j==3 or j==6 or j==8 or j==11 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break

           
        while a==8 :
            
            
            j=int(input("player 1 choose any numper from 4,7,12 :"))
            if j==4 and j in list1 or j==7 and j in list2 or j==12 and j in list3 :
                print("complete")
            elif  4  not in list1 and 7  not in list2 and 12  not in list3:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                x=6        
            else :
                continue           
            while j==4 or j==7  or j==12 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
          
        while a==9 :
            
            j=int(input("player 1 choose any numper from 5,10,13 :"))
            
            if j==5 and j in list2 or j==10 and j in list3 or j==13 and j in list4 :
                print("complete")
            elif  5  not in list2 and 10  not in list3 and 13  not in list4:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6      
            else :
                continue 
            while j==5 or j==10  or j==13 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
         
        while a==10 :
            
            j=int(input("player 1 choose any numper from 6,9,11,14 :"))
            if j==6 and j in list2 or j==9 and j in list3 or j==11 and j in list3 or j==14 and j in list4 :
                print("complete")
            elif  6  not in list2 and 9  not in list3 and 11  not in list3:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6    
            else :
                continue 
            while j==6 or j==9 or j==11 or j==14 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
                    
        while a==11 :
            
            j=int(input("player 1 choose any numper from 7,10,12,15 :"))
            if j==7 and j in list2 or j==10 and j in list3 or j==12 and j in list3 or j==15 and j in list4 :
                print("complete")
            elif  7  not in list2 and 10  not in list3 and 12  not in list4:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6    
            else :
                continue 

            while j==7 or j==10 or j==12 or j==15 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
            
                    
        
        while a==12 :
            
            j=int(input("player 1 choose any numper from 8,11,16 :"))
            if j==8 and j in list2 or j==11 and j in list3 or j==16 and j in list4 :
                print("complete")
            elif  8  not in list2 and 11  not in list3 and 16  not in list4:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6         
            else :
                continue 
            while j==8 or j==11 or j==16 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :  
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
           
                    
        while a==13 :
            
            j=int(input("player 1 choose any numper from 9,14 :"))
            if j==9 and j in list3 or j==14 and j in list4  :
                print("complete")
            elif  9  not in list3 and 14  not in list4 :
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6        
            else :
                continue 
            while j==9 or j==14  :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
           
        while a==14 :
            
            j=int(input("player 1 choose any numper from 10,13,15 :"))
            if j==10 and j in list3 or j==13 and j in list4 or j==15 and j in list4 :
                print("complete")
            elif  10  not in list3 and 13  not in list4 and 15  not in list4:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6      
            else :
                continue 
            while j==10 or j==13 or j==15  :    
        


                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
           
        while a==15 :
            
            j=int(input("player 1 choose any numper from 11,14,16:"))
            if j==11 and j in list3 or j==14 and j in list4 or j==16 and j in list4 :
                print("complete")
            elif  11  not in list3 and 14  not in list4 and 16  not in list4:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6       
            else :
                continue 
            while  j==11 or j==14 or j==16 :

                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                 
                    break
                break
            break
            
            
        while a==16 :
            
            j=int(input("player 1 choose any numper from 12,15:"))
            if j==12 and j in list3 or j==15 and j in list4  :
                print("complete")
            elif  12  not in list3 and 15  not in list4 :
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                
                x=6       
            else :
                continue 
            while  j==12 or j==15 :

                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
        break

    if x==6  :
        print("end")
        print("the game is end")
        print("restart game to play again")
        
    for i in range (17):
        f=int(input("player 2 choose any numper :"))
        if f in list1 :
            c=list1.index(f)       
            list1.remove(f)
            list1.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        elif f in list2 :
            c=list2.index(f)
            list2.remove(f)
            list2.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        elif f in list3 :
            c=list3.index(f)       
            list3.remove(f)
            list3.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        elif f in list4 :
            c=list4.index(f)       
            list4.remove(f)
            list4.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        else :
             continue

            
        
        while f==1 :
            j=int(input("player 2 choose any numper from 2,5 :"))
            if j==2 and j in list1 or j==5 and j in list2:
                print("complete")
            elif 2 not in list1 and 5 not in list2:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6
                
        
            else :
                continue    
                
           
            while j==2 and j in list1 or j==5 and j in list2 :
            
           
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break 
                    
                
                 
                
                
                    
               
           
            
        while f==2 :
            
            j=int(input("player 2 choose any numper from 1,3,6 :"))
            if j==1 and j in list1 or j==3 and j in list1 or j==6 and j in list2:
                print("complete")
            
            elif  1  not in list1 and 3  not in list1 and 6  not in list2:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6
               
            else :
                continue    

            while j==1 or j==3 or j==6 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
        while f==3 :
            
            j=int(input("player 2 choose any numper from 2,4,7 :"))
          
            if j==2 and j in list1 or j==4 and j in list1 or j==7 and j in list2:
                print("complete")
            elif 2 not in list1 and 4 not in list1 and 7 not in list2:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6
            else :
                continue 
            while j==2 or j==4 or j==7 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
            
                    
        while f==4 :
            
            j=int(input("player 2 choose any numper from 3,8 :"))
            if j==3 and j in list1 or j==8 and j in list2 :
                print("complete")
            elif  3  not in list1 and 8  not in list2 :
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6    
            else :
                continue 
            while j==3 or j==8 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
            
        while f==5 :
            
            j=int(input("player 2 choose any numper from 1,6,9 :"))
            if j==1 and j in list1 or j==6 and j in list2 or j==9 and j in list3:
                print("complete")
            elif  1  not in list1 and 6  not in list2 and 9  not in list3:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6  
            else :
                continue 
            while j==1 or j==6 or j==9 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
          
                    
        while f==6 :
            
            j=int(input("player 2 choose any numper from 2,5,7,10 :"))
            if j==2 and j in list1 or j==5 and j in list2 or j==7 and j in list2 or j==10 and j in list3:
                print("complete")
            elif  2  not in list1 and 5 not in list2 and 7  not in list2:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6   
            else :
                continue 
            while j==2 or j==5 or j==7 or j==10 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    
                    break
                break
            break
            
        while f==7 :
            
            
            j=int(input("player 2 choose any numper from 3,6,8,11 :"))
            if j==3 and j in list1 or j==6 and j in list2 or j==8 and j in list2 or j==11 and j in list3:
                print("complete")
            elif  3  not in list1 and 6  not in list2 and 8  not in list2 and 11 not in list3:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6    
            else :
                continue 
            while j==3 or j==6 or j==8 or j==11 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break

           
        while f==8 :
            
            
            j=int(input("player 2 choose any numper from 4,7,12 :"))
            if j==4 and j in list1 or j==7 and j in list2 or j==12 and j in list3 :
                print("complete")
            elif  4  not in list1 and 7  not in list2 and 12  not in list3:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6    
            else :
                continue           
            while j==4 or j==7  or j==12 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
          
        while f==9 :
            
            j=int(input("player 2 choose any numper from 5,10,13 :"))
            
            if j==5 and j in list2 or j==10 and j in list3 or j==13 and j in list4 :
                print("complete")
            elif  5  not in list2 and 10  not in list3 and 13  not in list4:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6    
            else :
                continue 
            while j==5 or j==10  or j==13 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
         
        while f==10 :
            
            j=int(input("player 2 choose any numper from 6,9,11,14 :"))
            if j==6 and j in list2 or j==9 and j in list3 or j==11 and j in list3 or j==14 and j in list4 :
                print("complete")
            elif  6  not in list2 and 9  not in list3 and 11  not in list3:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6
            else :
                continue 
            while j==6 or j==9 or j==11 or j==14 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
                    
        while f==11 :
            
            j=int(input("player 2 choose any numper from 7,10,12,15 :"))
            if j==7 and j in list2 or j==10 and j in list3 or j==12 and j in list3 or j==15 and j in list4 :
                print("complete")
            elif  7  not in list2 and 10  not in list3 and 12  not in list4:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6
            else :
                continue 

            while j==7 or j==10 or j==12 or j==15 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
            
                    
        
        while f==12 :
            
            j=int(input("player 2 choose any numper from 8,11,16 :"))
            if j==8 and j in list2 or j==11 and j in list3 or j==16 and j in list4 :
                print("complete")
            elif  8  not in list2 and 11  not in list3 and 16  not in list4:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6       
            else :
                continue 
            while j==8 or j==11 or j==16 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :  
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
           
                    
        while f==13 :
            
            j=int(input("player 2 choose any numper from 9,14 :"))
            if j==9 and j in list3 or j==14 and j in list4  :
                print("complete")
            elif  9  not in list3 and 14  not in list4 :
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6       
            else :
                continue 
            while j==9 or j==14  :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
           
        while f==14 :
            
            j=int(input("player 2 choose any numper from 10,13,15 :"))
            if j==10 and j in list3 or j==13 and j in list4 or j==15 and j in list4 :
                print("complete")
            elif  10  not in list3 and 13  not in list4 and 15  not in list4:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6       
            else :
                continue 
            while j==10 or j==13 or j==15  :    
        


                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
           
        while f==15 :
            
            j=int(input("player 2 choose any numper from 11,14,16:"))
            if j==11 and j in list3 or j==14 and j in list4 or j==16 and j in list4 :
                print("complete")
            elif  11  not in list3 and 14  not in list4 and 16  not in list4:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6        
            else :
                continue 
            while  j==11 or j==14 or j==16 :

                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                 
                    break
                break
            break
            
            
        while f==16 :
            
            j=int(input("player 2 choose any numper from 12,15:"))
            if j==12 and j in list3 or j==15 and j in list4  :
                print("complete")
            elif  12  not in list3 and 15  not in list4 :
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6        
            
            else :
                continue 
            while  j==12 or j==15 :

                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
        break
    if x==6  :
        print("end")
        print("the game is end")
        print("restart game to play again")
    for i in range (17):
        a=int(input("player 1 choose any numper :"))
        if a in list1 :
            c=list1.index(a)       
            list1.remove(a)
            list1.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        elif a in list2 :
            c=list2.index(a)
            list2.remove(a)
            list2.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        elif a in list3 :
            c=list3.index(a)       
            list3.remove(a)
            list3.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        elif a in list4 :
            c=list4.index(a)       
            list4.remove(a)
            list4.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        else :
            continue
            
        
        while a==1 :
            j=int(input("player 1 choose any numper from 2,5 :"))
            if j==2 and j in list1 or j==5 and j in list2:
                print("complete")
            elif 2 not in list1 and 5 not in list2:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6   
            else :
                continue    
                
           
            while j==2 and j in list1 or j==5 and j in list2 :
            
           
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break 
                    
                
                 
                
                
                    
               
           
            
        while a==2 :
            
            j=int(input("player 1 choose any numper from 1,3,6 :"))
            if j==1 and j in list1 or j==3 and j in list1 or j==6 and j in list2:
                print("complete")
            elif  1  not in list1 and 3  not in list1 and 6  not in list2:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6
                
            else :
                continue    

            while j==1 or j==3 or j==6 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
        while a==3 :
            
            j=int(input("player 1 choose any numper from 2,4,7 :"))
          
            if j==2 and j in list1 or j==4 and j in list1 or j==7 and j in list2:
                print("complete")
            elif 2 not in list1 and 4 not in list1 and 7 not in list2:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6
            else :
                continue 
            while j==2 or j==4 or j==7 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
            
                    
        while a==4 :
            
            j=int(input("player 1 choose any numper from 3,8 :"))
            if j==3 and j in list1 or j==8 and j in list2 :
                print("complete")
            elif  3  not in list1 and 8  not in list2 :
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6        
            else :
                continue 
            while j==3 or j==8 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
            
        while a==5 :
            
            j=int(input("player 1 choose any numper from 1,6,9 :"))
            if j==1 and j in list1 or j==6 and j in list2 or j==9 and j in list3:
                print("complete")
            elif  1  not in list1 and 6  not in list2 and 9  not in list3:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6      
            else :
                continue 
            while j==1 or j==6 or j==9 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
          
                    
        while a==6 :
            
            j=int(input("player 1 choose any numper from 2,5,7,10 :"))
            if j==2 and j in list1 or j==5 and j in list2 or j==7 and j in list2 or j==10 and j in list3:
                print("complete")
            elif  2  not in list1 and 5 not in list2 and 7  not in list2:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6       
            else :
                continue 
            while j==2 or j==5 or j==7 or j==10 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    
                    break
                break
            break
            
        while a==7 :
            
            
            j=int(input("player 1 choose any numper from 3,6,8,11 :"))
            if j==3 and j in list1 or j==6 and j in list2 or j==8 and j in list2 or j==11 and j in list3:
                print("complete")

            elif  3  not in list1 and 6  not in list2 and 8  not in list2 and 11 not in list3:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6      
            else :
                continue 
            while j==3 or j==6 or j==8 or j==11 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break

           
        while a==8 :
            
            
            j=int(input("player 1 choose any numper from 4,7,12 :"))
            if j==4 and j in list1 or j==7 and j in list2 or j==12 and j in list3 :
                print("complete")
            elif  4  not in list1 and 7  not in list2 and 12  not in list3:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                x=6        
            else :
                continue           
            while j==4 or j==7  or j==12 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
          
        while a==9 :
            
            j=int(input("player 1 choose any numper from 5,10,13 :"))
            
            if j==5 and j in list2 or j==10 and j in list3 or j==13 and j in list4 :
                print("complete")
            elif  5  not in list2 and 10  not in list3 and 13  not in list4:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6      
            else :
                continue 
            while j==5 or j==10  or j==13 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
         
        while a==10 :
            
            j=int(input("player 1 choose any numper from 6,9,11,14 :"))
            if j==6 and j in list2 or j==9 and j in list3 or j==11 and j in list3 or j==14 and j in list4 :
                print("complete")
            elif  6  not in list2 and 9  not in list3 and 11  not in list3:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6    
            else :
                continue 
            while j==6 or j==9 or j==11 or j==14 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
                    
        while a==11 :
            
            j=int(input("player 1 choose any numper from 7,10,12,15 :"))
            if j==7 and j in list2 or j==10 and j in list3 or j==12 and j in list3 or j==15 and j in list4 :
                print("complete")
            elif  7  not in list2 and 10  not in list3 and 12  not in list4:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6    
            else :
                continue 

            while j==7 or j==10 or j==12 or j==15 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
            
                    
        
        while a==12 :
            
            j=int(input("player 1 choose any numper from 8,11,16 :"))
            if j==8 and j in list2 or j==11 and j in list3 or j==16 and j in list4 :
                print("complete")
            elif  8  not in list2 and 11  not in list3 and 16  not in list4:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6         
            else :
                continue 
            while j==8 or j==11 or j==16 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :  
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
           
                    
        while a==13 :
            
            j=int(input("player 1 choose any numper from 9,14 :"))
            if j==9 and j in list3 or j==14 and j in list4  :
                print("complete")
            elif  9  not in list3 and 14  not in list4 :
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6        
            else :
                continue 
            while j==9 or j==14  :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
           
        while a==14 :
            
            j=int(input("player 1 choose any numper from 10,13,15 :"))
            if j==10 and j in list3 or j==13 and j in list4 or j==15 and j in list4 :
                print("complete")
            elif  10  not in list3 and 13  not in list4 and 15  not in list4:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6      
            else :
                continue 
            while j==10 or j==13 or j==15  :    
        


                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
           
        while a==15 :
            
            j=int(input("player 1 choose any numper from 11,14,16:"))
            if j==11 and j in list3 or j==14 and j in list4 or j==16 and j in list4 :
                print("complete")
            elif  11  not in list3 and 14  not in list4 and 16  not in list4:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6       
            else :
                continue 
            while  j==11 or j==14 or j==16 :

                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                 
                    break
                break
            break
            
            
        while a==16 :
            
            j=int(input("player 1 choose any numper from 12,15:"))
            if j==12 and j in list3 or j==15 and j in list4  :
                print("complete")
            elif  12  not in list3 and 15  not in list4 :
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                
                x=6       
            else :
                continue 
            while  j==12 or j==15 :

                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
        break

    if x==6  :
        print("end")
        print("the game is end")
        print("restart game to play again")
        
    for i in range (17):
        f=int(input("player 2 choose any numper :"))
        if f in list1 :
            c=list1.index(f)       
            list1.remove(f)
            list1.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        elif f in list2 :
            c=list2.index(f)
            list2.remove(f)
            list2.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        elif f in list3 :
            c=list3.index(f)       
            list3.remove(f)
            list3.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        elif f in list4 :
            c=list4.index(f)       
            list4.remove(f)
            list4.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        else :
             continue

            
        
        while f==1 :
            j=int(input("player 2 choose any numper from 2,5 :"))
            if j==2 and j in list1 or j==5 and j in list2:
                print("complete")
            elif 2 not in list1 and 5 not in list2:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6
                
        
            else :
                continue    
                
           
            while j==2 and j in list1 or j==5 and j in list2 :
            
           
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break 
                    
                
                 
                
                
                    
               
           
            
        while f==2 :
            
            j=int(input("player 2 choose any numper from 1,3,6 :"))
            if j==1 and j in list1 or j==3 and j in list1 or j==6 and j in list2:
                print("complete")
            
            elif  1  not in list1 and 3  not in list1 and 6  not in list2:
                x="player 1 win "
                print(x)
                print (main())
                print("the game is end")
                print("game is restart")
                x=6
               
            else :
                continue    

            while j==1 or j==3 or j==6 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
        while f==3 :
            
            j=int(input("player 2 choose any numper from 2,4,7 :"))
          
            if j==2 and j in list1 or j==4 and j in list1 or j==7 and j in list2:
                print("complete")
            elif 2 not in list1 and 4 not in list1 and 7 not in list2:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6
            else :
                continue 
            while j==2 or j==4 or j==7 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
            
                    
        while f==4 :
            
            j=int(input("player 2 choose any numper from 3,8 :"))
            if j==3 and j in list1 or j==8 and j in list2 :
                print("complete")
            elif  3  not in list1 and 8  not in list2 :
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6    
            else :
                continue 
            while j==3 or j==8 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
            
        while f==5 :
            
            j=int(input("player 2 choose any numper from 1,6,9 :"))
            if j==1 and j in list1 or j==6 and j in list2 or j==9 and j in list3:
                print("complete")
            elif  1  not in list1 and 6  not in list2 and 9  not in list3:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6  
            else :
                continue 
            while j==1 or j==6 or j==9 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
          
                    
        while f==6 :
            
            j=int(input("player 2 choose any numper from 2,5,7,10 :"))
            if j==2 and j in list1 or j==5 and j in list2 or j==7 and j in list2 or j==10 and j in list3:
                print("complete")
            elif  2  not in list1 and 5 not in list2 and 7  not in list2:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6   
            else :
                continue 
            while j==2 or j==5 or j==7 or j==10 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    
                    break
                break
            break
            
        while f==7 :
            
            
            j=int(input("player 2 choose any numper from 3,6,8,11 :"))
            if j==3 and j in list1 or j==6 and j in list2 or j==8 and j in list2 or j==11 and j in list3:
                print("complete")
            elif  3  not in list1 and 6  not in list2 and 8  not in list2 and 11 not in list3:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6    
            else :
                continue 
            while j==3 or j==6 or j==8 or j==11 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break

           
        while f==8 :
            
            
            j=int(input("player 2 choose any numper from 4,7,12 :"))
            if j==4 and j in list1 or j==7 and j in list2 or j==12 and j in list3 :
                print("complete")
            elif  4  not in list1 and 7  not in list2 and 12  not in list3:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6    
            else :
                continue           
            while j==4 or j==7  or j==12 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
          
        while f==9 :
            
            j=int(input("player 2 choose any numper from 5,10,13 :"))
            
            if j==5 and j in list2 or j==10 and j in list3 or j==13 and j in list4 :
                print("complete")
            elif  5  not in list2 and 10  not in list3 and 13  not in list4:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6    
            else :
                continue 
            while j==5 or j==10  or j==13 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
         
        while f==10 :
            
            j=int(input("player 2 choose any numper from 6,9,11,14 :"))
            if j==6 and j in list2 or j==9 and j in list3 or j==11 and j in list3 or j==14 and j in list4 :
                print("complete")
            elif  6  not in list2 and 9  not in list3 and 11  not in list3:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6
            else :
                continue 
            while j==6 or j==9 or j==11 or j==14 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
                    
        while f==11 :
            
            j=int(input("player 2 choose any numper from 7,10,12,15 :"))
            if j==7 and j in list2 or j==10 and j in list3 or j==12 and j in list3 or j==15 and j in list4 :
                print("complete")
            elif  7  not in list2 and 10  not in list3 and 12  not in list4:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6
            else :
                continue 

            while j==7 or j==10 or j==12 or j==15 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
            
                    
        
        while f==12 :
            
            j=int(input("player 2 choose any numper from 8,11,16 :"))
            if j==8 and j in list2 or j==11 and j in list3 or j==16 and j in list4 :
                print("complete")
            elif  8  not in list2 and 11  not in list3 and 16  not in list4:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6       
            else :
                continue 
            while j==8 or j==11 or j==16 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :  
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
           
                    
        while f==13 :
            
            j=int(input("player 2 choose any numper from 9,14 :"))
            if j==9 and j in list3 or j==14 and j in list4  :
                print("complete")
            elif  9  not in list3 and 14  not in list4 :
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6       
            else :
                continue 
            while j==9 or j==14  :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
           
        while f==14 :
            
            j=int(input("player 2 choose any numper from 10,13,15 :"))
            if j==10 and j in list3 or j==13 and j in list4 or j==15 and j in list4 :
                print("complete")
            elif  10  not in list3 and 13  not in list4 and 15  not in list4:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6       
            else :
                continue 
            while j==10 or j==13 or j==15  :    
        


                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
           
        while f==15 :
            
            j=int(input("player 2 choose any numper from 11,14,16:"))
            if j==11 and j in list3 or j==14 and j in list4 or j==16 and j in list4 :
                print("complete")
            elif  11  not in list3 and 14  not in list4 and 16  not in list4:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6        
            else :
                continue 
            while  j==11 or j==14 or j==16 :

                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                 
                    break
                break
            break
            
            
        while f==16 :
            
            j=int(input("player 2 choose any numper from 12,15:"))
            if j==12 and j in list3 or j==15 and j in list4  :
                print("complete")
            elif  12  not in list3 and 15  not in list4 :
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6        
            
            else :
                continue 
            while  j==12 or j==15 :

                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
        break
    if x==6  :
        print("end")
        print("the game is end")
        print("restart game to play again")
    for i in range (17):
        a=int(input("player 1 choose any numper :"))
        if a in list1 :
            c=list1.index(a)       
            list1.remove(a)
            list1.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        elif a in list2 :
            c=list2.index(a)
            list2.remove(a)
            list2.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        elif a in list3 :
            c=list3.index(a)       
            list3.remove(a)
            list3.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        elif a in list4 :
            c=list4.index(a)       
            list4.remove(a)
            list4.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        else :
            continue
            
        
        while a==1 :
            j=int(input("player 1 choose any numper from 2,5 :"))
            if j==2 and j in list1 or j==5 and j in list2:
                print("complete")
            elif 2 not in list1 and 5 not in list2:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6   
            else :
                continue    
                
           
            while j==2 and j in list1 or j==5 and j in list2 :
            
           
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break 
                    
                
                 
                
                
                    
               
           
            
        while a==2 :
            
            j=int(input("player 1 choose any numper from 1,3,6 :"))
            if j==1 and j in list1 or j==3 and j in list1 or j==6 and j in list2:
                print("complete")
            elif  1  not in list1 and 3  not in list1 and 6  not in list2:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6
                
            else :
                continue    

            while j==1 or j==3 or j==6 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
        while a==3 :
            
            j=int(input("player 1 choose any numper from 2,4,7 :"))
          
            if j==2 and j in list1 or j==4 and j in list1 or j==7 and j in list2:
                print("complete")
            elif 2 not in list1 and 4 not in list1 and 7 not in list2:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6
            else :
                continue 
            while j==2 or j==4 or j==7 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
            
                    
        while a==4 :
            
            j=int(input("player 1 choose any numper from 3,8 :"))
            if j==3 and j in list1 or j==8 and j in list2 :
                print("complete")
            elif  3  not in list1 and 8  not in list2 :
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6        
            else :
                continue 
            while j==3 or j==8 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
            
        while a==5 :
            
            j=int(input("player 1 choose any numper from 1,6,9 :"))
            if j==1 and j in list1 or j==6 and j in list2 or j==9 and j in list3:
                print("complete")
            elif  1  not in list1 and 6  not in list2 and 9  not in list3:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6      
            else :
                continue 
            while j==1 or j==6 or j==9 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
          
                    
        while a==6 :
            
            j=int(input("player 1 choose any numper from 2,5,7,10 :"))
            if j==2 and j in list1 or j==5 and j in list2 or j==7 and j in list2 or j==10 and j in list3:
                print("complete")
            elif  2  not in list1 and 5 not in list2 and 7  not in list2:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6       
            else :
                continue 
            while j==2 or j==5 or j==7 or j==10 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    
                    break
                break
            break
            
        while a==7 :
            
            
            j=int(input("player 1 choose any numper from 3,6,8,11 :"))
            if j==3 and j in list1 or j==6 and j in list2 or j==8 and j in list2 or j==11 and j in list3:
                print("complete")

            elif  3  not in list1 and 6  not in list2 and 8  not in list2 and 11 not in list3:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6      
            else :
                continue 
            while j==3 or j==6 or j==8 or j==11 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break

           
        while a==8 :
            
            
            j=int(input("player 1 choose any numper from 4,7,12 :"))
            if j==4 and j in list1 or j==7 and j in list2 or j==12 and j in list3 :
                print("complete")
            elif  4  not in list1 and 7  not in list2 and 12  not in list3:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                x=6        
            else :
                continue           
            while j==4 or j==7  or j==12 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
          
        while a==9 :
            
            j=int(input("player 1 choose any numper from 5,10,13 :"))
            
            if j==5 and j in list2 or j==10 and j in list3 or j==13 and j in list4 :
                print("complete")
            elif  5  not in list2 and 10  not in list3 and 13  not in list4:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6      
            else :
                continue 
            while j==5 or j==10  or j==13 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
         
        while a==10 :
            
            j=int(input("player 1 choose any numper from 6,9,11,14 :"))
            if j==6 and j in list2 or j==9 and j in list3 or j==11 and j in list3 or j==14 and j in list4 :
                print("complete")
            elif  6  not in list2 and 9  not in list3 and 11  not in list3:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6    
            else :
                continue 
            while j==6 or j==9 or j==11 or j==14 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
                    
        while a==11 :
            
            j=int(input("player 1 choose any numper from 7,10,12,15 :"))
            if j==7 and j in list2 or j==10 and j in list3 or j==12 and j in list3 or j==15 and j in list4 :
                print("complete")
            elif  7  not in list2 and 10  not in list3 and 12  not in list4:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6    
            else :
                continue 

            while j==7 or j==10 or j==12 or j==15 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
            
                    
        
        while a==12 :
            
            j=int(input("player 1 choose any numper from 8,11,16 :"))
            if j==8 and j in list2 or j==11 and j in list3 or j==16 and j in list4 :
                print("complete")
            elif  8  not in list2 and 11  not in list3 and 16  not in list4:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6         
            else :
                continue 
            while j==8 or j==11 or j==16 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :  
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
           
                    
        while a==13 :
            
            j=int(input("player 1 choose any numper from 9,14 :"))
            if j==9 and j in list3 or j==14 and j in list4  :
                print("complete")
            elif  9  not in list3 and 14  not in list4 :
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6        
            else :
                continue 
            while j==9 or j==14  :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
           
        while a==14 :
            
            j=int(input("player 1 choose any numper from 10,13,15 :"))
            if j==10 and j in list3 or j==13 and j in list4 or j==15 and j in list4 :
                print("complete")
            elif  10  not in list3 and 13  not in list4 and 15  not in list4:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6      
            else :
                continue 
            while j==10 or j==13 or j==15  :    
        


                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
           
        while a==15 :
            
            j=int(input("player 1 choose any numper from 11,14,16:"))
            if j==11 and j in list3 or j==14 and j in list4 or j==16 and j in list4 :
                print("complete")
            elif  11  not in list3 and 14  not in list4 and 16  not in list4:
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6       
            else :
                continue 
            while  j==11 or j==14 or j==16 :

                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                 
                    break
                break
            break
            
            
        while a==16 :
            
            j=int(input("player 1 choose any numper from 12,15:"))
            if j==12 and j in list3 or j==15 and j in list4  :
                print("complete")
            elif  12  not in list3 and 15  not in list4 :
                x="player 2 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                
                x=6       
            else :
                continue 
            while  j==12 or j==15 :

                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
        break

    if x==6  :
        print("end")
        print("the game is end")
        print("restart game to play again")
        
    for i in range (17):
        f=int(input("player 2 choose any numper :"))
        if f in list1 :
            c=list1.index(f)       
            list1.remove(f)
            list1.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        elif f in list2 :
            c=list2.index(f)
            list2.remove(f)
            list2.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        elif f in list3 :
            c=list3.index(f)       
            list3.remove(f)
            list3.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        elif f in list4 :
            c=list4.index(f)       
            list4.remove(f)
            list4.insert((c),"X")
            print(list1)
            print(list2)
            print(list3)
            print(list4)
        else :
             continue

            
        
        while f==1 :
            j=int(input("player 2 choose any numper from 2,5 :"))
            if j==2 and j in list1 or j==5 and j in list2:
                print("complete")
            elif 2 not in list1 and 5 not in list2:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6
                
        
            else :
                continue    
                
           
            while j==2 and j in list1 or j==5 and j in list2 :
            
           
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break 
                    
                
                 
                
                
                    
               
           
            
        while f==2 :
            
            j=int(input("player 2 choose any numper from 1,3,6 :"))
            if j==1 and j in list1 or j==3 and j in list1 or j==6 and j in list2:
                print("complete")
            
            elif  1  not in list1 and 3  not in list1 and 6  not in list2:
                x="player 1 win "
                print(x)
                print (main())
                print("the game is end")
                print("game is restart")
                x=6
               
            else :
                continue    

            while j==1 or j==3 or j==6 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
        while f==3 :
            
            j=int(input("player 2 choose any numper from 2,4,7 :"))
          
            if j==2 and j in list1 or j==4 and j in list1 or j==7 and j in list2:
                print("complete")
            elif 2 not in list1 and 4 not in list1 and 7 not in list2:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6
            else :
                continue 
            while j==2 or j==4 or j==7 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
            
                    
        while f==4 :
            
            j=int(input("player 2 choose any numper from 3,8 :"))
            if j==3 and j in list1 or j==8 and j in list2 :
                print("complete")
            elif  3  not in list1 and 8  not in list2 :
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6    
            else :
                continue 
            while j==3 or j==8 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
            
        while f==5 :
            
            j=int(input("player 2 choose any numper from 1,6,9 :"))
            if j==1 and j in list1 or j==6 and j in list2 or j==9 and j in list3:
                print("complete")
            elif  1  not in list1 and 6  not in list2 and 9  not in list3:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6  
            else :
                continue 
            while j==1 or j==6 or j==9 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
          
                    
        while f==6 :
            
            j=int(input("player 2 choose any numper from 2,5,7,10 :"))
            if j==2 and j in list1 or j==5 and j in list2 or j==7 and j in list2 or j==10 and j in list3:
                print("complete")
            elif  2  not in list1 and 5 not in list2 and 7  not in list2:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6   
            else :
                continue 
            while j==2 or j==5 or j==7 or j==10 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    
                    break
                break
            break
            
        while f==7 :
            
            
            j=int(input("player 2 choose any numper from 3,6,8,11 :"))
            if j==3 and j in list1 or j==6 and j in list2 or j==8 and j in list2 or j==11 and j in list3:
                print("complete")
            elif  3  not in list1 and 6  not in list2 and 8  not in list2 and 11 not in list3:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6    
            else :
                continue 
            while j==3 or j==6 or j==8 or j==11 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break

           
        while f==8 :
            
            
            j=int(input("player 2 choose any numper from 4,7,12 :"))
            if j==4 and j in list1 or j==7 and j in list2 or j==12 and j in list3 :
                print("complete")
            elif  4  not in list1 and 7  not in list2 and 12  not in list3:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6    
            else :
                continue           
            while j==4 or j==7  or j==12 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
          
        while f==9 :
            
            j=int(input("player 2 choose any numper from 5,10,13 :"))
            
            if j==5 and j in list2 or j==10 and j in list3 or j==13 and j in list4 :
                print("complete")
            elif  5  not in list2 and 10  not in list3 and 13  not in list4:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6    
            else :
                continue 
            while j==5 or j==10  or j==13 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
         
        while f==10 :
            
            j=int(input("player 2 choose any numper from 6,9,11,14 :"))
            if j==6 and j in list2 or j==9 and j in list3 or j==11 and j in list3 or j==14 and j in list4 :
                print("complete")
            elif  6  not in list2 and 9  not in list3 and 11  not in list3:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6
            else :
                continue 
            while j==6 or j==9 or j==11 or j==14 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
                    
        while f==11 :
            
            j=int(input("player 2 choose any numper from 7,10,12,15 :"))
            if j==7 and j in list2 or j==10 and j in list3 or j==12 and j in list3 or j==15 and j in list4 :
                print("complete")
            elif  7  not in list2 and 10  not in list3 and 12  not in list4:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6
            else :
                continue 

            while j==7 or j==10 or j==12 or j==15 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
            
                    
        
        while f==12 :
            
            j=int(input("player 2 choose any numper from 8,11,16 :"))
            if j==8 and j in list2 or j==11 and j in list3 or j==16 and j in list4 :
                print("complete")
            elif  8  not in list2 and 11  not in list3 and 16  not in list4:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6       
            else :
                continue 
            while j==8 or j==11 or j==16 :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :  
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
           
                    
        while f==13 :
            
            j=int(input("player 2 choose any numper from 9,14 :"))
            if j==9 and j in list3 or j==14 and j in list4  :
                print("complete")
            elif  9  not in list3 and 14  not in list4 :
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6       
            else :
                continue 
            while j==9 or j==14  :
            
                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
           
        while f==14 :
            
            j=int(input("player 2 choose any numper from 10,13,15 :"))
            if j==10 and j in list3 or j==13 and j in list4 or j==15 and j in list4 :
                print("complete")
            elif  10  not in list3 and 13  not in list4 and 15  not in list4:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6       
            else :
                continue 
            while j==10 or j==13 or j==15  :    
        


                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
           
        while f==15 :
            
            j=int(input("player 2 choose any numper from 11,14,16:"))
            if j==11 and j in list3 or j==14 and j in list4 or j==16 and j in list4 :
                print("complete")
            elif  11  not in list3 and 14  not in list4 and 16  not in list4:
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6        
            else :
                continue 
            while  j==11 or j==14 or j==16 :

                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                 
                    break
                break
            break
            
            
        while f==16 :
            
            j=int(input("player 2 choose any numper from 12,15:"))
            if j==12 and j in list3 or j==15 and j in list4  :
                print("complete")
            elif  12  not in list3 and 15  not in list4 :
                x="player 1 win "
                print(x)
                print("the game is end")
                print("game is restart")
                print (main())
                x=6        
            
            else :
                continue 
            while  j==12 or j==15 :

                if j in list1 :
                    c=list1.index(j)       
                    list1.remove(j)
                    list1.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                elif j in list2 :
                    
                    c=list2.index(j)
                    list2.remove(j)
                    list2.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                
                elif j in list3 :
                    c=list3.index(j)       
                    list3.remove(j)
                    list3.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)               
                elif j in list4 :
                    c=list4.index(j)       
                    list4.remove(j)
                    list4.insert((c),"X")
                    print(list1)
                    print(list2)
                    print(list3)
                    print(list4)
                    break
                break
            break
        break
    if x==6  :
        print("end")
        print("the game is end")
        print("restart game to play again")
    

    
if c==5 :main()       





    
              
