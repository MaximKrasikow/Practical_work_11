from django import forms

class BirthdayForm(forms.Form):
    # Поле для имени пользователя. Ограничиваем максимальную длину имени до 20 символов.
    first_name = forms.CharField(label="Имя", max_length=20)
    
    # Поле для фамилии пользователя. Это поле необязательное, что указано через параметр `required=False`.
    # Также добавлено вспомогательное текстовое описание (help_text), которое будет отображаться на форме.
    last_name = forms.CharField(
        label="Фамилия", required=False, help_text="Необязательное поле"
    )
    
    # Поле для даты рождения. В нем указывается тип поля `DateField`, который автоматически ожидает формат даты.
    # Виджет для этого поля настроен так, чтобы форма использовала элемент `<input>` с атрибутом `type='date'`.
    # Это позволяет браузеру предоставлять пользователю удобный календарный интерфейс для выбора даты.
    birthday = forms.DateField(
        label="Дата рождения",
        widget=forms.DateInput(attrs={'type': 'date'})  # Устанавливаем виджет с типом 'date' для ввода даты
    )