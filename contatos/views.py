from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Contact
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages

# Create your views here.
def index(request):
    messages.add_message(request, messages.ERROR, "Ocorreu um ERROR!")
    contatos = Contact.objects.order_by('id').filter(
        mostrar=True
    )
    paginator = Paginator(contatos, 2)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })

def ver_contato(request, contato_id):

    # contato = Contact.objects.get(id=contato_id)
    contato = get_object_or_404(Contact, id=contato_id)
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })
    
def busca(request):
    termo = request.GET.get('termo')
    campos = Concat('nome', Value(''), 'sobrenome')

    print(termo)
    contatos = Contact.objects.order_by('-id').filter(
        Q(nome__icontains=termo) | Q(sobrenome__icontains=termo),
        mostrar=True
    )
    paginator = Paginator(contatos, 25)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })        