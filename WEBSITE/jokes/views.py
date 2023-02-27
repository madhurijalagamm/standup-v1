
from django.shortcuts import render
import mysql.connector as sql
from jokes.models import JOKES


joke=''

# def create_user(request):
#     if request.method == 'POST':
#         first_name=request.POST['first_name']
#         print(first_name)
#         user = USER(first_name=request.POST['first_name'],last_name=request.POST['last_name'], sex=request.POST['sex'],email=request.POST['email'],password=request.POST['password'])
#         print(user)
#         print("china")
#         user.save()
#         return JsonResponse({'success': True})    
#     else:
#         return JsonResponse({'success': False, 'error': 'Invalid request method'})
    

def create_joke(request):
    if request.method == 'POST':
        user = JOKES(joke_text=request.POST['joke'])
        user.save()
    return render(request, 'jokes_page.html')





#this is for seejokes
def joke_list(request):
    # jokeList2=[]


    jokesData = JOKES.objects.all()
    # for j in jokesData:
    #     jokeList2.append([j.joke_text,j.upvote,j.downvote])
        

    #     print(j.joke_text)
    
    # print(jokeList2)
    print(jokesData[0].joke_text)







    # jokeList=[]
    # m = sql.connect(host="localhost", user="root", passwd="admin123", database="WEBSITE")
    # cursor = m.cursor()
    # # jokes_item = JOKES.objects.all()
    # jokes_item = ["Why did the tomato turn red? Because it saw the salad dressing!", "What do you call a fake noodle? An impasta!"]
    # context = {'jokes': jokes_item}
    # print(jokes_item)
    # # return render(request, 'jokes_disp.html', context)


    # c="SELECT * FROM JOKES"
    # cursor.execute(c)
    # print(cursor)
    # for row in cursor:
    #     jokeList.append(row)
    #     print(row)
    # print(jokeList)
    # for j, u, d in t:
    #     render(request,'')

    return render(request, 'jokes_disp.html', {'jokes': jokesData})


def jokeaction(request):
    if request.method == 'POST':



        j1=request.POST['joke']
        print(j1)



        user = JOKES(joke_text=request.POST['joke'])
        user.save()
    return render(request, 'jokes_page.html')





    #mysql database connection
    '''global joke
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
    '''
