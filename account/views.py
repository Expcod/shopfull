from django.shortcuts import render

def edit_profile(request):
    if request.method == "POST":
        ...
    return render(request,'account/edit.html')