from django.shortcuts import render
import mysql.connector as sql


fn=''
ln=''
s=''
em=''
pwd=''


# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method == "POST":
        m=sql.connect(host="localhost", user="root", passwd="admin123", database="website")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="INSERT INTO USERS VALUES('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        # c = "INSERT INTO USERS VALUES('MAD','J','FEMALE','jalagamslakshmi@gmail.com','1234');"
        cursor.execute(c)
        m.commit()
    return render(request,'signup_page.html')
