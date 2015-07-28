from django.forms import ModelForm
from models import Unit

class AddUnitForm(ModelForm):
    class Meta:
        model = Unit
        exclude = ('uuid_name',
                   'x_val',
                   'y_val',)

# class SaveUnitForm(ModelForm):
#     class Meta:
#         model = Unit
#         fields = ['uuid_name',
#                   'x_val',
#                   'y_val',]
