from django.shortcuts import render,redirect
from groupApp.forms import GroupCreationForm
from groupApp.models import GroupModelClass

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
            #userClassGroupCount = UserModelClass.objects.raw('select count(selectedGroup) from user_details where selectedGroup =  %s', [groupModel.title])
            # for x in userClassGroupCount:
            #     print(x)
            #print(userClassGroupCount)
            groupModel.save()
            data2 = GroupModelClass.objects.all()
            return render(request, 'user_group_page.html', {'data2': data2})
            # return render(request, 'user_group_page.html', {'data2': data2,'test':userClassGroupCount})
            #return redirect('user_page')
    data2 = GroupModelClass.objects.all()
    return render(request,'user_group_page.html',{'data2':data2})



# Create your views here.
