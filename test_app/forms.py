from django import forms
from test_app.models import ClassB, ClassA


class ClassBForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		self.the_foreignkey = kwargs.pop("the_foreignkey", 0)
		super(ClassBForm, self).__init__(*args, **kwargs)

		if self.the_foreignkey:
			self.fields.pop('our_class_a', None)

	class Meta:
		model = ClassB

	def clean(self):
		if self.the_foreignkey:
			self.cleaned_data['our_class_a'] = ClassA.objects.get(pk=self.the_foreignkey)
		return self.cleaned_data

	def save(self, commit=True):
		names = self.parse_multi_name(self.cleaned_data['name'])
		unparsed_name = self.cleaned_data['name']
		for name in names:
			self.cleaned_data['name'] = name
			print ClassB.objects.get_or_create(**self.cleaned_data)

	def parse_multi_name(self, name):
		start, end = [int(x) for x in name.split('-')]
		return [str(x) for x in range(start, end+1)]
