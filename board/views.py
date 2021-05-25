from django.shortcuts import render
from .models import Board
from .forms import BoardForm

# Create your views here.


def board_write(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():

    else:
        form = BoardForm()
    return render(request, 'board_write.html', {'form': form})


def board_list(request):
    boards = Board.objects.all().order_by('-id')
    return render(request, 'board_list.html', {'boards': boards})
