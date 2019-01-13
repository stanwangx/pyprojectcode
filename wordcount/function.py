#from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	return render(request, 'home.html')


def count(request):
	req_text = request.GET['text']
	total_count = len(req_text)

	word_dict = {}

	for word in req_text:
		if word not in word_dict:
			word_dict[word] = 1
		else:
			word_dict[word] += 1

	sortedword = sorted(word_dict.items(), key = lambda w:w[1], reverse = True )

	return render(request, 'count.html', {'count': total_count, 'reqtext': req_text, 'wordict': word_dict , 'sortedword': sortedword})


def about(request):
	return render(request, 'about.html')


