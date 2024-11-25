from django.shortcuts import render
from .forms import BirthdayForm
# Импортируем из utils.py функцию для подсчёта дней.
from .utils import calculate_birthday_countdown

def birthday(request):
    """
    Обрабатывает запрос на отображение страницы с формой ввода даты рождения.
    Если форма заполнена корректно, вычисляет количество дней до следующего дня рождения 
    и добавляет результат в контекст для отображения на странице.
    """
    # Инициализируем форму, передавая данные из GET-запроса, если они есть.
    form = BirthdayForm(request.GET or None)

    # Создаём словарь контекста для передачи данных в шаблон.
    context = {'form': form}

    # Проверяем, является ли форма валидной (все поля заполнены корректно).
    if form.is_valid():
        # Если форма валидна, вызываем функцию для расчёта дней до следующего дня рождения.
        birthday_countdown = calculate_birthday_countdown(
            # Передаём в функцию дату из очищенных данных формы (cleaned_data).
            form.cleaned_data['birthday']
        )
        # Добавляем результат расчёта в словарь контекста.
        context.update({'birthday_countdown': birthday_countdown})

    # Рендерим HTML-шаблон, передавая в него контекст с данными.
    return render(request, 'birthday/birthday.html', context)
