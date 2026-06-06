from django.shortcuts import render
from django.contrib.auth.models import User


def home(request):
    usuarios = User.objects.all()
    if request.method == 'POST':
        nome = request.POST.get('name')
        email = request.POST.get('email')
        user = User.objects.filter(username=nome, email=email).first()
        if not user:
            user = User(username=nome, email=email)
            user.save()
            return render(request, 'index.html', {'usuarios': usuarios})
        else:
            usuario_existente = "Usuário já existe!"
            return render(request, 'index.html', {'usuarios': usuarios, 'usuario_existente': usuario_existente})

    return render(request, 'index.html', {'usuarios': usuarios})