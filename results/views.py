from django.shortcuts import render
from candidatereg.models import Candidates as c



def result(request):
    candidate= c.objects.all().values()
    context = {'candidate': candidate}
    max = 0
    for i in candidate:
       if i['votes'] > max:
           max = i['votes']
    
    return render(request,'result.html', context)