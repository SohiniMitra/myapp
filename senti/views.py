from django.shortcuts import render,render_to_response
from fetch import sentiment_analysis,tweet_pol
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, RequestContext
#from django.views.generic.base import TemplateView

def firstpage(request):
    if request.method=='POST':
	movie_name=request.POST['movie']
	ans = sentiment_analysis([movie_name],10)
	print ans
	if ans:
		result="Watch It !"
		return render_to_response('result.html',{'result':result,'tweet_pol':tweet_pol},RequestContext(request))
	else:
		result="Dont Watch It !"
		return render_to_response('result.html',{'result':result,'tweet_pol':tweet_pol},RequestContext(request))
    elif request.method=='GET':
    	return render_to_response('home.html',RequestContext(request))
    #return HttpResponse('hello')

# Create your views here.
