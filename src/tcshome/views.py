from django.shortcuts import render
from visits.models import PageVisit

def home_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        print(request.user.first_name,request.user.last_name)
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    # qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    total_visits = PageVisit.objects.count()
    page_visits = page_qs.count()
    try:
        percent = (page_qs.count() * 100) / PageVisit.objects.count()
    except:
        percent = 0
    my_title = "My_page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_visits,
        "total_visit_count": total_visits,
        "percent": percent
    }
    print(f"Page path: {request.path}")
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)


