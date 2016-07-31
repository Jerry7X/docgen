from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .forms import NameForm

def index(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = NameForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			#return HttpResponseRedirect('/thanks/')
			name = form.cleaned_data['your_name']
			return HttpResponse("Your name is %s." % name)

	# if a GET (or any other method) we'll create a blank form
	else:
		form = NameForm()

	return render(request, 'name.html', {'form': form})
