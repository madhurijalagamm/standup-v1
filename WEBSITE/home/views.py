# from pyexpat.errors import messages
# from django.shortcuts import render,redirect
# from django.contrib.auth import authenticate, login, logout


# # Create your views here.
# def homeaction(request):
#     return render(request, 'home.html')



# # def testaction(request):
# #     return render(request, 'test1.html')

# def home_view(request):
#     if not request.session.get('is_logged_in'):
#         # User is not logged in
#         return redirect('login')
#     else:
#         # User is logged in
#         user_id = request.session.get('user_id')
#         username = request.session.get('username')
#         return render(request, 'home.html', {'user_id': user_id, 'username': username})