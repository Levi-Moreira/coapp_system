from django.shortcuts import render


def config(request):
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'config.html',
    )
