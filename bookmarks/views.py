# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def main_page(request):
	output = '''
		<html>
			<head><title>%s</title></head>
				<body>
					<h1>%s</h1><p>%s</p>
				</body>
		</html>
		'''%(
			'django | Bookmarks',
			'Welcome to django bookmarks!',
			'Save and share bookmark here.'
			)

	return HttpResponse(output)