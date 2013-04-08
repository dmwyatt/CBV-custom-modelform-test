from django import forms
from test_app.models import ClassB


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
			self.cleaned_data['our_class_a'] = self.the_foreignkey
		return self.cleaned_data
