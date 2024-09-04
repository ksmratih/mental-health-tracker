from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306256406',
        'name': 'Ratih',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)