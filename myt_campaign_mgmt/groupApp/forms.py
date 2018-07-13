from django import forms
from groupApp.models import GroupModelClass

class GroupCreationForm(forms.ModelForm):
    ch = (
        ('GAdds Python','GAdds Python'),
        ('myTectra Fcaebook','myTectra Fcaebook'),
        ('myTectra.com Newsletter','myTectra.com Newsletter'),
        ('Python Webinar','Python Webinar'),
        ('myTectra.com-Python','myTectra.com-Python'),
        ('Gadds PHP','Gadds PHP'),

    )
    groups = forms.MultipleChoiceField(choices=ch,widget=forms.CheckboxSelectMultiple,required=False)
    class Meta:
        model = GroupModelClass
        fields = ('title','description','groups')