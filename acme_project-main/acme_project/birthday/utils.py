from datetime import date

def calculate_birthday_countdown(birthday):
    """
    Вычисляет количество дней до следующего дня рождения.
    Если день рождения приходится на текущую дату, возвращает 0.

    :param birthday: Дата рождения (объект datetime.date).
    :return: Количество дней до следующего дня рождения (int).
    """
    # Получаем текущую дату.
    today = date.today()

    # Рассчитываем дату дня рождения в текущем году.
    # Используется вспомогательная функция get_birthday_for_year.
    this_year_birthday = get_birthday_for_year(birthday, today.year)

    # Проверяем, прошёл ли день рождения в текущем году.
    if this_year_birthday < today:
        # Если уже прошёл, рассчитываем день рождения в следующем году.
        next_birthday = get_birthday_for_year(birthday, today.year + 1)
    else:
        # Если ещё не прошёл, он считается ближайшим.
        next_birthday = this_year_birthday

    # Вычисляем разницу между текущей датой и ближайшим днём рождения в днях.
    birthday_countdown = (next_birthday - today).days

    # Возвращаем количество оставшихся дней.
    return birthday_countdown

def get_birthday_for_year(birthday, year):
    """
    Вычисляет дату дня рождения для заданного года.
    Если дата рождения приходится на 29 февраля, а год не високосный,
    дата дня рождения корректируется на 1 марта.

    :param birthday: Дата рождения (объект datetime.date).
    :param year: Год, для которого требуется рассчитать дату дня рождения (int).
    :return: Дата дня рождения в заданном году (объект datetime.date).
    """
    try:
        # Пытаемся заменить год в дате рождения на указанный.
        calculated_birthday = birthday.replace(year=year)
    except ValueError:
        # Обработка исключения для случаев, когда дата рождения — 29 февраля,
        # а указанный год не является високосным. В этом случае устанавливается 1 марта.
        calculated_birthday = date(year=year, month=3, day=1)

    # Возвращаем рассчитанную дату.
    return calculated_birthday
