from django.shortcuts import render,redirect
import mysql.connector as sql
from signup.views import USER
from django.contrib.auth import authenticate, login


em=''
pwd=''

# Create your views here.
def loginaction(request):
    global em,pwd
    if request.method == "POST":
        # userData=USER.objects.all()
        entered_user=request.POST
        em=entered_user['email']
        pwd=entered_user['password']
        entered_user = USER.objects.filter(email=em, password=pwd).first()
        # entered_user = USER.objects.filter()
        if entered_user is not None:
            # login(request, entered_user)
            return render(request,'welcome.html')
        else:
            return render(request,'error.html')

        print(entered_user)
    return render(request,'login_page.html')













'''
        m=sql.connect(host="localhost", user="root", passwd="admin123", database="website")
        cursor=m.cursor()
        d=request.POST
        print(d)
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c = "SELECT * FROM USERS WHERE EMAIL='{}' AND PASSWORD='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        print(t)
        if t==():
            return render(request,'error.html')
        else:
            return render(request,'welcome.html')
        m.commit()
    return render(request,'login_page.html')
    '''
