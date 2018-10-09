from django.shortcuts import render


# Create your views here.
def token_view(request):
    url = request.get_full_path()
    return render(request,'tokens/temp.html', {'Token':url[6:]})

