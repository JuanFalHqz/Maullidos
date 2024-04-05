from django.shortcuts import render


def my_custom_404_view(request, exception):
    return render(request, 'base/404.html', status=404)
