from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Bem-vindo à Home!")

def contato(request):
    return HttpResponse("Página de Contato")