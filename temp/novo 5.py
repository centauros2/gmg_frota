def lista_car(request):  
  novo_car = Veiculo()
    novo_car.placa = request.POST.get('placa').upper()
    novo_car.marca = request.POST.get('marca')
    novo_car.modelo = request.POST.get('modelo')
    novo_car.cor = request.POST.get('cor')
    novo_car.combustivel = request.POST.get('combustivel')
    novo_car.data = request.POST.get('data')
    novo_car.save()
    # exibir veículos em uma nova página
    veiculos = {
        'veiculos': Veiculo.objects.all()
    }
    # retornar para para lista_car
    return render(request, "cadastro/lista_car.html", veiculos)