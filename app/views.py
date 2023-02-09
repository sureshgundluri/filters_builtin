from django.shortcuts import render

import datetime

def builtinfilters(request):
    t=datetime.datetime.now()
    d={'data':'I am VERy haPPy To INtroDUction My sELF','t':t,'c':3}
    return render(request,'builtinfilters.html',d)
