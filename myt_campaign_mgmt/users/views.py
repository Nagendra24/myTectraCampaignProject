from django.shortcuts import render,redirect
from users.forms import CoreForms,UserCreationForm,GroupCreationForm
from django.contrib.auth import logout,login,authenticate
# from django.contrib.auth.models import User
from django.db.models import Count
from users.models import UserModelClass,GroupModelClass
from django.db import connection

def user_login(request):
    coreForms = CoreForms()
    if request.method == 'POST':
        coreForms = CoreForms(request.POST)
        if coreForms.is_valid():
            username = coreForms.cleaned_data['username']
            password = coreForms.cleaned_data['password']
            userAuthenticate = authenticate(username = username, password = password)
            if userAuthenticate is None:
                return redirect('userLogin')
            else:
                login(request,userAuthenticate)
                return redirect('homePage')
    return render(request, 'login_page.html',{'coreForms':coreForms})

def home_page(request):
    return render(request,'home_page.html')

def user_page(request):
    userCreationForm = UserCreationForm()
    if request.method == 'POST':
        print("here")
        print("here too")
        userCreationForm = UserCreationForm(request.POST)
        print(userCreationForm.is_valid())
        print("next line")
        if userCreationForm.is_valid():
        #     print("here too")
            userModel = UserModelClass()
            userModel.email = userCreationForm.cleaned_data['email']
            #print(request.POST.get('email'))
            userModel.first_name = userCreationForm.cleaned_data['first_name']
            userModel.last_name = userCreationForm.cleaned_data['last_name']
            userModel.mobile_number = userCreationForm.cleaned_data['mobile_number']
            userModel.user_name = userCreationForm.cleaned_data['user_name']
            userModel.password = userCreationForm.cleaned_data['password']
            userModel.group = userCreationForm.cleaned_data['group']
            userModel.selectedGroup = userModel.group
            # userModel.email = request.POST.get('email')
            # print(request.POST.get('email'))
            # userModel.first_name = request.POST.get('first_name')
            # userModel.last_name = request.POST.get('last_name')
            # userModel.mobile_number = request.POST.get('mobile_number')
            # userModel.user_name = request.POST.get('user_name')
            # userModel.password = request.POST.get('password')
            # userModel.group = request.POST.get('group')
            userModel.save()
            data = UserModelClass.objects.all()
            return render(request,'user_group_page.html',{'data':data})
    data = UserModelClass.objects.all()
    return render(request,'user_group_page.html',{'userCreationForm':userCreationForm,'data':data})


def group_page(request):
    print(request.POST.get('title'))
    print("ikkada")
    group_details = GroupCreationForm()
    if request.method == "POST":
        print("here")
        print("ttt")
        group_details = GroupCreationForm(request.POST)
        print(group_details.is_valid())
        if group_details.is_valid():
            groupModel = GroupModelClass()
            groupModel.title = request.POST.get('title')
            groupModel.description = request.POST.get('description')
            groupModel.groups = request.POST.getlist('infoitems')
            # userClassGroupCount = UserModelClass.objects.values('selectedGroup').annotate(Members=Count('selectedGroup'))
            # res = list(userClassGroupCount)
            # for groupItem in res:
            #     print(groupItem)
            #     for groupkey,groupVal in groupItem.items():
            #         print(groupkey,groupVal)
            #         if groupVal == groupModel.title:
            #             print(groupVal)

            # query = 'select count(selectedGroup) from user_details where selectedGroup =  %s', [groupModel.title]
            # objs = UserModelClass.objects.raw(query)
            # with connection.cursor() as cursor:
            #     cursor.execute('select count(selectedGroup) from user_details where selectedGroup =  %s', [groupModel.title])
            #     row = cursor.fetchone()
            #     print(row)
            userClassGroupCount = UserModelClass.objects.raw('select count(selectedGroup) from user_details where selectedGroup =  %s', [groupModel.title])
            # for x in userClassGroupCount:
            #     print(x)
            print(userClassGroupCount)
            groupModel.save()
            data2 = GroupModelClass.objects.all()
            return render(request, 'user_group_page.html', {'data2': data2,'test':userClassGroupCount})
            #return redirect('user_page')
    data2 = GroupModelClass.objects.all()
    return render(request,'user_group_page.html',{'data2':data2})


def user_edit(request,pk):
    data = UserModelClass.objects.get(id=pk)
    user_form = UserCreationForm(instance=data)  # map values from database and fill data

    if (request.method == 'POST'):
        user_form = UserCreationForm(request.POST,instance=data)
        if user_form.is_valid():
            # form.save()
            user_details = UserModelClass()
            user_details.id = pk  # else new record is created
            user_details.email = user_form.cleaned_data['email']
            user_details.first_name = user_form.cleaned_data['first_name']
            user_details.last_name = user_form.cleaned_data['last_name']
            user_details.mobile_number = user_form.cleaned_data['mobile_number']
            user_details.user_name = user_form.cleaned_data['user_name']
            user_details.password = user_form.cleaned_data['password']
            user_details.group = user_form.cleaned_data['group']
            user_details.save()
            return redirect('/home_page/user')
    return render(request, 'user_edit.html', {'user_form': user_form})

def delete(request, pk):
    data = UserModelClass.objects.get(id = pk)
    data.delete()
    return redirect('/home_page/user')

def logOut(request):
    logout(request)
    return redirect('userLogin')