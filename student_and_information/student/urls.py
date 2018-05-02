from django.conf.urls import url

from student import views

urlpatterns = [
    url(r'^addstu/',views.addStu,name='add'),
    url(r'^index/',views.index,name='index'),# 返回所有学生信息
    url(r'^stupage/',views.stuPage),
    url(r'^addstuinfo/(?P<stu_id>\d+)',views.addStuInfo,name="addinfo")
]