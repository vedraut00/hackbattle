from django.shortcuts import render
from django.http import HttpResponse
import requests
import mysql.connector as sql

# Create your views here.
def index(request):
    return render(request, 'index.html')

role=''
username=''
passwd=''

# Create your views here.
def index(request):
    context = {
        'message': 'Welcome to the Index Page!'
    }
    return render(request, 'index.html', context)
 
def signup(request):
    if request.method == "POST":
        m = sql.connect(host='localhost', passwd='2020', user='root', database='cctv_database')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "txt":
                role = value
            
            if key == "username":
                username = value
            
            if key == "pswd":
                passwd = value
                
        ins = "insert into users Values ('{}', '{}',  '{}')".format(username, passwd, role)
        cursor.execute(ins)
        m.commit()
    return render(request, 'signup.html') 

def login(request):
    if request.method == "POST":
        m = sql.connect(host='localhost', passwd='2020', user='root', database='test')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "email":
                email = value
            
            if key == "pswd":
                passwd = value
                
        query = "SELECT * FROM users WHERE email='{}' AND password='{}'".format(email, passwd)
        cursor.execute(query)
        result = cursor.fetchone()
        
        if result:
            # User authenticated, you can implement your logic here
            # For example, you could set a session or redirect to a dashboard
            return HttpResponse("Logged in successfully")
        else:
            # Authentication failed, you might want to show an error message
            return HttpResponse("Login failed")

    return render(request, 'login.html')



def videocheck(request):
    shareable_link = 'https://drive.google.com/file/d/1ObbJAlxrtVGQ4ihRx0UP3S5jf1d7r3vh/view?usp=sharing'

    try:
        response = requests.get(shareable_link)
        if response.status_code == 200:
            video_content = response.content
            # the video file is stored in video_content
            
            
            
            return HttpResponse('Video fetched successfully.')
        else:
            return HttpResponse('Failed to fetch video.')
    except Exception as e:
        return HttpResponse(f'Error: {str(e)}')


