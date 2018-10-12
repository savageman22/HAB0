from django.shortcuts import render


# Create your views here.
def token_view(request, token=None):
    x = request.GET.get('token', '')
    print(x)
    url = request.get_full_path()
    return render(request,'tokens/temp.html', {'Token':url[6:]})

def token_variable_view(request,  token=None):
    x = request.GET.get('token', '')
    print(x)
    return render(request,'tokens/temp.html', {'Token':x})
