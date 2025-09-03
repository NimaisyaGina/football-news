from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406429885',
        'name': 'Nimaisya Gina Herapati',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)

# Create your views here.
