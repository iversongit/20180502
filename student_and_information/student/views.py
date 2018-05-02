from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
# Create your views here.
from student.models import Student, StudentInfo
from uauth.models import User


def addStu(request):
    if request.method == "GET":
        return render(request,"addstu.html")
    if request.method == "POST":
        # 跳转到学生详情方法中去
        name = request.POST.get("name")
        tel = request.POST.get("tel")
        stu = Student.objects.create(
            s_name=name,
            s_tel=tel
        )
        return HttpResponseRedirect(
            reverse("stu:addinfo",kwargs={'stu_id':stu.id})
        )

def index(request):
    if request.method == "GET":
        # 获取所有学生信息
        # ticket = request.COOKIES.get("ticket")
        # if not ticket:
        #     return HttpResponseRedirect('/uauth/login/')
        # if User.objects.filter(u_ticket=ticket).exists():
        #     stuinfos = StudentInfo.objects.all()
        #     return render(request,'index.html',{'stuinfos':stuinfos})
        # else:
        #     return HttpResponseRedirect('/uauth/login/')
        stuinfos = StudentInfo.objects.all()
        return render(request, 'index.html', {'stuinfos': stuinfos})

def addStuInfo(request,stu_id):
    if request.method == "GET":
        return render(request,'addstuinfo.html',{"stu_id":stu_id})
    if request.method == "POST":
        s_id = request.POST.get("stu_id")
        s_addr = request.POST.get("addr")
        # 添加头像图片
        img = request.FILES.get('img')
        StudentInfo.objects.create(
            s_addr = s_addr,
            s_id=s_id,
            s_image=img
        )
        return HttpResponseRedirect("/stuapp/index/")

def stuPage(request):
    if request.method == "GET":
        page_id = request.GET.get('page_id',1) # 1:默认页数，str类型
        stus = Student.objects.all()
        paginator = Paginator(stus,3)  #参数1：所有学生信息  参数2：按照每页几条数据分页
        page = paginator.page(int(page_id)) # 获取第page_id页数据
        return render(request, 'index_page.html', {'stus':page})
