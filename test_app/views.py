import pdb
from django.views.generic import CreateView
from test_app.forms import ClassBForm
from test_app.models import ClassB


class ClassBCreateView(CreateView):
	model = ClassB
	template_name = 'cb_form.html'
	form_class = ClassBForm

	def get(self, request, *args, **kwargs):
		self.the_foreignkey = kwargs.get('the_foreignkey') # get foreign key out of url
		return super(ClassBCreateView, self).get(request, *args, **kwargs)

	def get_form_kwargs(self):
		kwargs = super(ClassBCreateView, self).get_form_kwargs()
		kwargs.update({'the_foreignkey': getattr(self, 'the_foreignkey', 0)}) # put the foreign key into the form kwargs
		return kwargs
