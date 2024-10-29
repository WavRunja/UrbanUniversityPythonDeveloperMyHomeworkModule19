from django.shortcuts import render
from .forms import UserRegister
from .models import Game, Buyer

# Create your views here.


# task4/views.py
# Главная страница
def platform_view(request):
    return render(request, 'fourth_task/platform.html', {'title': 'Главная страница'})


# Страница "Магазин"
# Подтянуть игры из базы данных
def game_list_view(request):
    games = Game.objects.all()
    context = {
        'games': games,
        'title': 'Игры',
    }
    return render(request, 'fourth_task/games.html', context)


# Страница "Корзина"
def cart_view(request):
    return render(request, 'fourth_task/cart.html', {'title': 'Корзина'})


# task5/views.py
def sign_up_by_django(request):
    info = {}
    # Форма для запроса
    form = UserRegister(request.POST or None)
    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        repeat_password = form.cleaned_data['repeat_password']
        age = form.cleaned_data['age']

        if Buyer.objects.filter(name=username).exists():
            info['error'] = 'Пользователь уже существует'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        else:
            Buyer.objects.create(name=username, age=age, balance=0)
            info['success'] = f'Приветствуем, {username}!'

            # Проверить
            return render(request, 'fifth_task/registration_success.html', info)

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)
