from django.shortcuts import render

def home(request):
    return render(request, 'main/index.html', {'caption': "Django"})
def new_view(request):
    return render(request, 'main/new.html')

def test_view(request):
    return render(request, 'main/test.html')

def contacts_view(request):
    return render(request, 'main/contacts.html')