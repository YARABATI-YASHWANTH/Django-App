from django.shortcuts import render,redirect
from crudapp.models import student
from django.http import HttpResponse
# Create your views here.
def insertion(request):
	if request.method=='POST':
		name=request.POST['name']
		roll=request.POST['rollnum']
		age=request.POST['age']
		mb=request.POST['mobile']
		em=request.POST['email']
		ad=request.POST['address']
		student.objects.create(name=name,rollnum=roll,age=age,mobile=mb,email=em,address=ad)
	
		return HttpResponse("your data is added successfully!")

	return render(request,'crudapp/insertion.html')
	return redirect('/retrieve')
def retrieve(request):
	data=student.objects.all()
	return render(request,'crudapp/retrieve.html',{'info':data})

def update(request,id):
	data=student.objects.get(id=id)
	if request.method=='POST':
		data.name=request.POST['name']
		data.roll=request.POST['rollnum']
		data.age=request.POST['age']
		data.mb=request.POST['mobile']
		data.em=request.POST['email']
		data.ad=request.POST['address']
		data.save()
	return render(request,'crudapp/update.html',{'data':data})
def mypage(request):
	
	return render(request,'crudapp/mypage.html',{})

def delete(request,id):
	ob=student.objects.get(id=id)
	if request.method=="POST":
		ob.delete()
		return redirect('/retrieve')

	return render(request,'crudapp/delete.html',{'ob':ob})
