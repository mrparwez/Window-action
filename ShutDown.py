import os 
  
shutdown = input("Do you wish to make action your computer such Shutdown/Restart/Hibernet/Stop App/Abort ? (yes / no): ") 
shutdown=shutdown.lower()
if shutdown == 'no': 
    exit() 
elif shutdown=='yes':
    user=input("Do you want to ? (Shutdown 1 / Restart 2 / Hibernate 3 / force stop application 4 / Abort 5 ) ")
    user=user.lower()
    if user=='Shutdown' or user=='1':
        os.system("shutdown /s /t 1 :")
    elif user=='Restart' or user=='2':
        os.system("shutdown /r /t 1")
    elif user=='Hibernate' or user=='3':
        os.sysem("shutdown /h /t 1")
    elif user=='stop' or user=='4':
        os.system("shutdown  /a /t 1")
    elif user=='Abort' or user=='5':
        os.system("shutdown /a /t 1")
    else:
        print('No action matched :')
else:
    print('Choose yes or no ')
    
