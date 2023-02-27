from django.shortcuts import render, redirect
from signup.models import USER
import mysql.connector as sql
from django.http import JsonResponse



fn=''
ln=''
s=''
em=''
pwd=''


# def create_user2(fn,ln,sex,em,pwd):
#     my_model = USER(first_name=fn, last_name=ln, sex=sex, email=em )
#     my_model.save()



def create_user(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        print(first_name)
        user = USER(first_name=request.POST['first_name'],last_name=request.POST['last_name'], sex=request.POST['sex'],email=request.POST['email'],password=request.POST['password'])
        print(user)
        print("china")
        user.save()
        return JsonResponse({'success': True})    
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})

# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method == "POST":




        first_name=request.POST['first_name']
        print(first_name)
        user = USER(first_name=request.POST['first_name'],last_name=request.POST['last_name'], sex=request.POST['sex'],email=request.POST['email'],password=request.POST['password'])
        print(user)
        print("china")
        user.save()
        return render(request,'login_page.html')
        # return JsonResponse({'success': True})    
    else:
        return render(request,'signup_page.html')

        # return JsonResponse({'success': False, 'error': 'Invalid request method'})
    


    #mysql database connection
    '''
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

    '''

