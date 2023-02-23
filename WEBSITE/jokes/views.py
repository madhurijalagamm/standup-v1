
from django.shortcuts import render
import mysql.connector as sql
from .models import JOKES


joke=''

def joke_list(request):
    jokeList=[]
    m = sql.connect(host="localhost", user="root", passwd="admin123", database="WEBSITE")
    cursor = m.cursor()
    # jokes_item = JOKES.objects.all()
    jokes_item = ["Why did the tomato turn red? Because it saw the salad dressing!", "What do you call a fake noodle? An impasta!"]
    context = {'jokes': jokes_item}
    print(jokes_item)
    # return render(request, 'jokes_disp.html', context)


    c="SELECT * FROM JOKES"
    cursor.execute(c)
    print(cursor)
    for row in cursor:
        jokeList.append(row)
        print(row)
    print(jokeList)
    # for j, u, d in t:
    #     render(request,'')

    return render(request, 'jokes_disp.html', {'jokes': jokeList})


def jokeaction(request):
    global joke
    m = sql.connect(host="localhost", user="root", passwd="admin123", database="website")
    cursor = m.cursor()



    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="admin123", database="website")
        cursor = m.cursor()
        d = request.POST
        for key,value in d.items():
            if key=="joke":
                joke=value

        
        c = "INSERT INTO JOKES VALUES('{}',0,0)".format(joke)
        # c = "INSERT INTO USERS VALUES('MAD','J','FEMALE','jalagamslakshmi@gmail.com','1234');"
        cursor.execute(c)
        m.commit()

    

    return render(request,'jokes_page.html')
