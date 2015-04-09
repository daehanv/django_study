# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

def main_page(request):
	template = get_template('index.html')
	
	variable = Context({
	'head_title' : 'django | bookmark',
	'page_title' : 'Welcome to django bookmark!',
	'page_body' : 'Save and share your bookmark here'
	})
	
	output = template.render(variable)

	return HttpResponse(output)