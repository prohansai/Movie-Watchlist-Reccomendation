import pickle
import random
m={}
print("WELCOME TO MOVIE WATCHLIST")
u=input("enter user:")
b=0
    #f=u+'.txt'
while b==0:
        choice=input("enter your choice (1:add,2:view,3:cutoff,4:suggest a movie from list,5:change user,6:exit)")
        if choice=='1':
            n=int(input("enter no. of movies you want to add in watchlist:"))
            for i in range(1,n+1):
                x=input("enter name of movie %d"%(i))
                m[x]=input("enter its genre")
            try:
                with open(u,'wb') as f:
                        pickle.dump(m,f)
            except:
                print("error occured,try again")
            else:
                print("success")

        elif choice=='2':
            try:
                with open(u,'rb') as f:
                    data=pickle.load(f)
                for i,j in data.items():
                    print('movie:',i,',genre:',j)
            except:
                print("error occured,try again")
            else:
                print("success")
        elif choice=='3':
            try:
                with open(u,'rb') as f:
                    data=pickle.load(f)
                n=int(input("enter no. of movies you want to cutoff"))
                for i in range(n):
                    x=input("enter movie name")
                    for j in data.keys():
                        if x==j:
                            key=j
                    data.pop(key)
                with open(u,'wb') as f:
                    pickle.dump(data,f)
            except:
                print("error occured,try again")
            else:
                print("success")
            
        elif choice=='4':
            try:
                typ=input("enter choice (1:random,2:your genre):")
                if typ=='2':
                    g=input("enter genre")
                    with open(u,'rb') as f:
                        data=pickle.load(f)
                    print("movies in watchlist in given genre:")
                    for i,j in data.items():
                        if j==g:
                            print("movie:",i)
                elif typ=='1':
                    with open(u,'rb') as f:
                        data=pickle.load(f)
                    print("random suggestion from watchlist:")
                    lt=list(data.keys())
                    rnd=random.choice(lt)
                    print("movie:",rnd,",genre:",data[rnd])
            except:
                print("error occured,try again")
            else:
                print("success")
            
        elif choice=='5':
            try:
                data.clear()
                m.clear()
                u=input("enter user:")
                #u=input("enter user:")
                #f=u+'.txt'
            except:
                print("error occured,try again")
            else:
                print("success")
        elif choice=='6':
            b=1
            print("thanks,visit again")
        else:
            print("wrong chocie.try again")
