from django.shortcuts import render

# Create your views here.

evenos = []

def home(request):
    return render(request, 'home.html',
    {'eventos': eventos})

    def novo(request):
        if request.method == 'POST':
            form = EventoForm(request.POST)
            if form.is_valid():
                eventos.append({ 'evento':
                form.cleaned_data['evento'],
                'local':
                form.cleaned_data['local']})

                return redirect('home')
            else:
                form = EventoForm()

            return render(request, 'novo.html', {'form': form})