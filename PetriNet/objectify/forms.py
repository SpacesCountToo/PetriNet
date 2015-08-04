from django.forms import ModelForm,HiddenInput
from django.forms.models import modelformset_factory
from models import Unit

class AddUnitForm(ModelForm):
    class Meta:
        model = Unit
        exclude = (
            'uuid_name',
            'x_val',
            'y_val',
        )

class SaveUnitForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(SaveUnitForm, self).__init__(*args, **kwargs)
    #     self.unitname = self.instance.uuid_name
    class Meta:
        model = Unit
        fields = (
            'x_val',
            'y_val',
        )
        widgets = {
            'x_val':HiddenInput(),
            'y_val':HiddenInput(),
        }


SaveUnitFormSet = modelformset_factory(
    Unit,
    form=SaveUnitForm
)
