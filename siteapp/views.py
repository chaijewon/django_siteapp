from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'site/index.html')

def board(request):
    return render(request,'site/board.html')
