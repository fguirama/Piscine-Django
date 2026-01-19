from datetime import datetime
from readline import read_history_file

from django.db.models.fields import return_None
from django.shortcuts import render

from d05.settings import LOG_FILE_PATH
from ex02.forms import InputForm


def ex02_form(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            try:
                _add_new_log(form.cleaned_data.get('text_ipt', '**empty input**'))
            except (FileNotFoundError, PermissionError):
                pass

    else:
        form = InputForm()

    h = _read_history()

    return render(request, 'form.html', {'form': form, 'history': h})


def _add_new_log(user_ipt):
    new_log = f'{datetime.now():%Y-%m-%d %H:%M:%S},{user_ipt}'
    with open(LOG_FILE_PATH, 'a') as f:
        f.write(new_log + '\n')


def _read_history():
    result = []
    try:
        with open(LOG_FILE_PATH) as f:
            lines = f.read().split('\n')
            for line in lines:
                try:
                    date, user_ipt = line.split(',', 1)
                    result.append({'timestamp': date, 'text': user_ipt})
                except ValueError:
                    pass
    except (FileNotFoundError, PermissionError):
        pass
    return result
