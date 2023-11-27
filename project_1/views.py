from django.http import HttpResponse

def about(request):
    return HttpResponse("This is project/about page")
def contact(request):
    return HttpResponse("this is contact page/project")
