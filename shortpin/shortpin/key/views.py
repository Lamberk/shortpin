from shortpin.key.forms import CheckKeyForm
from shortpin.key.models import Key

from django.shortcuts import render, redirect


def index(request):
    if request.method == 'GET':
        form = CheckKeyForm()
        return render(request, 'index.html', {'form': form})


def generate_key():
    import string
    from random import choice

    chars = string.letters + string.digits
    length = 4
    key_id = ''.join(choice(chars) for _ in range(length))
    return key_id


def key_view(request, **kwargs):
    key_id = kwargs.get('key_id')
    if key_id:
        try:
            key = Key.objects.get(id=key_id)
            return render(request, 'key.html', {'key': key})
        except Key.DoesNotExist:
            err_msg = 'The key was not granted.'
            return render(request, 'error.html', {'err_msg': err_msg})
    else:
        err_msg = 'The key was not granted.'
        return render(request, 'error.html', {'err_msg': err_msg})


def grant_key(request):
    if request.method == 'POST':

        is_key_generated = False
        keys = [x.id for x in Key.objects.all()]
        while not is_key_generated:
            key_id = generate_key()
            if key_id not in keys:
                is_key_generated = True

        key = Key.objects.create(
            id=key_id,
            status='granted',
        )
        return redirect('key_view', key_id=key.id)


def repay_key(request, **kwargs):
    key_id = kwargs.get('key_id')
    try:
        key = Key.objects.get(id=key_id)
        if key.status == 'repaid':
            err_msg = 'Key already repaid.'
            return render(request, 'error.html', {'err_msg': err_msg})
        else:
            key.status = 'repaid'
            key.save()
        return redirect('key_view', key_id=key.id)
    except Key.DoesNotExist:
        err_msg = 'The key was not granted.'
        return render(request, 'error.html', {'err_msg': err_msg})


def logic(request):
    key_id = request.POST.get('key')
    if key_id:
        if 'repay' in request.POST:
            return redirect('repay_key', key_id=key_id)
        elif 'info' in request.POST:
            return redirect('key_view', key_id=key_id)
    else:
        err_msg = 'You didnt input a key.'
        return render(request, 'error.html', {'err_msg': err_msg})
