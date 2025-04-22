from django.http import HttpResponse


def test_de_vue(request):
    return HttpResponse("<h1>Vue de test</h1>")