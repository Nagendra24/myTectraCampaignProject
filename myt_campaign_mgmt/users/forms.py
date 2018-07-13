from django import forms
from users.models import UserModelClass,GroupModelClass

class CoreForms(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50,widget=forms.PasswordInput)


class UserCreationForm(forms.ModelForm):
    # gn = (
    #     ('', 'male'), ('f', 'female')
    # )
    #group = forms.ChoiceField(widget=forms.RadioSelect())
    password = forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=20)
    class Meta:
        model = UserModelClass
        fields = ('email','first_name','last_name','mobile_number','user_name','password','group')


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