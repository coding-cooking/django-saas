from django.shortcuts import render

def home_page_view(request, *args, **kwargs):
    html_template = "home.html"
    return render(request, html_template)

