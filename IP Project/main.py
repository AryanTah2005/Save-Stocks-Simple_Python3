import pandas as pd
import numpy as np
import getpass as gp
import uuid
import yfinance as yf
from validate_email_address import validate_email as ve
from getpass4 import getpass
from graphcreate import *
from plotly.subplots import make_subplots
import plotly.graph_objects as go
print('********************************')
print('Welcome To Company Stock Monitor!')
print('********************************\n')
n=3
while(n>2):
      abc = input('Do you wish to login or create a new account? \nEnter 1 to Login and 2 to Signing up: ')
      if(abc in ['1','2']):
         if(abc=='1'):
            user='login'
            print('')
            break
         else:
            user='new'
            print('')
            break
      else:
         print('Incorrect Input, please try again!')
         continue
if(user=='new'):
    print('*******') 
    print('Sign Up')
    print('*******\n')
    name=input('Name:')
    while(n>2):
        df=pd.read_csv('/Users/aryantah/Desktop/IP Project/database.csv',dtype='object')
        ss=df['Email']
        email=input('Email:')
        e2=email.lower()
        isvalid=ve(email)
        if(isvalid==True): 
            if(e2 in df['Email'].tolist()):
                print('An Account with this email address already exists, please login instead.')
                exit()
            break
        else:
            print('Please Enter A Valid Email Address!\n')
            continue  
    while(n>2):
        pwd=getpass('Password:')
        if(len(pwd)<9):
            print('Please Enter a password with atleast 8 characters!')
        else:
            p2=getpass('Confirm Password:')
            if(p2==pwd):
                break
            else:
                print("The password's do not match, please try again!\n")
                continue
    dict2 ={'no':len(df)+1,'Name':name,'Email':e2,'Password':p2}
    df=pd.DataFrame(dict2,index=[0])
    df.to_csv('database.csv', mode='a',index=False, header=False)
    print('Your Account Has Been Created Successfully. Login to access your account.')
else:
    df=pd.read_csv('/Users/aryantah/Desktop/IP Project/database.csv',dtype='object')
    while(n>2):
        print('*****')
        print('Login')
        print('*****\n')
        email=input('Email:')
        isvalid=ve(email)
        e2=email.lower()
        ss=df['Email']
        if(isvalid==True):
           while(n>2): 
                if(e2 in df['Email'].tolist()):
                    a='w'
                    break
                else:
                    print('No Account exists with this email, please enter a registered email or sign up if you are new!') 
                    a='l'
                    break 
        else:
            print('Please Enter A Valid Email Adress!\n')
            continue
        if(a=='w'):
            break
        else:
            continue
    while(n>2):
        pwd=getpass('Password:')
        p2 = df.at[ss[ss==e2].index[0],'Password']
        name= df.at[ss[ss==e2].index[0],'Name']
        if(pwd==p2):
            print('Hello', name)
            if(str(df.at[ss[ss==e2].index[0],'Stocks'])=='nan'):
                while(n>2):
                    if(str(df.at[ss[ss==e2].index[0],'Stocks'])=='nan'):
                        a = input("You havn't added any stocks in your account. Enter 1 to add new stocks or 2 to exit.")
                    if(a in ['1','2']):
                        if(a=='1'):
                            s=input('Please enter the ticker symbol for the stock you want to add: ')
                            s2 = yf.Ticker(s)
                            hist=s2.history(period='1y')
                            if(hist.index.size > 0):
                                    print(s,'added to your account!')
                                    ask= input('Enter 1 to add more stocks to your account or 2 to view your stocks stats or 3 to exit: ')
                                    if(str(df.at[ss[ss==e2].index[0],'Stocks'])=='nan'):
                                        l=[s]
                                        df.at[ss[ss==e2].index[0],'Stocks']=l
                                    else:
                                        df.at[ss[ss==e2].index[0],'Stocks'].append(s)

                                    if(ask=='1'):
                                            continue
                                    elif(ask=='2'):
                                            df.at[ss[ss==e2].index[0],'Stocks'] = l
                                            df.to_csv('database.csv')
                                            break
                                    else:
                                            exit()
                            else:
                                print('Enter a Valid Ticker Symbol!')
                        else:
                            print('Have a good day!')
                            exit()                           
            
            print('Hello', name)
            stocks = df.at[ss[ss==e2].index[0],'Stocks']
            if(type(stocks)==list):
                stocks=stocks
            else:
                stocks=stocks.replace("[","")
                stocks=stocks.replace("]","")
                stocks=stocks.replace("'","")
                stocks=stocks.split(',')
            print('************')
            print('Stocks Added')
            print('************')
            j=0
            for i in stocks:
                j=j+1
                print(j,'-->',i)
            print('')
            d= input('Enter 1 for statistics, 2 to add more stocks: ')
            if(d=='1'):
                while(n>2):
                    e=input('Enter the stock number for which you need the statistics graph for: ')
                    try:
                        t=stocks[int(e)-1]
                        t=t.replace(" ",'')
                        break
                    except:
                        print('Please enter a valid stock number!')
                        continue
                f=input('Enter the period of time for which you want a graph 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, max: ')
                creategraph(t,f)
            elif(d=='2'):
                      while(n>2):
                            s=input('Please enter the ticker symbol for the stock you want to add: ')
                            s2 = yf.Ticker(s)
                            hist=s2.history(period='1y')
                            if(hist.index.size > 0):
                                stocks.append(s)
                                print('Added',s,'to your account')
                                se = input('Enter 1 to add more stocks and 2 to exit: ')
                                if(se=='1'):
                                    continue
                                elif(se=='2'):
                                    df.at[ss[ss==e2].index[0],'Stocks']=stocks
                                    df.to_csv('database.csv')
                                    exit()

                            else:
                                print('Please enter a valid Ticker Symbol!')
                                continue
        else:
            print('Wrong Password, Try again')
            continue
        break
        

       

            

            
