from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from web_session.form import UserForm


# 用户登录
def login_view(request):
    # 过滤 POST 方法的请求
    if request.method == 'POST':
        userfrom = UserForm(request.POST)
        # 验证表单
        if userfrom.is_valid():
            username = userfrom.cleaned_data['username']
            password = userfrom.cleaned_data['password']
            # ... 执行验证登录信息操作

            # 将等你信息传递给 Session 对象, 实际应用中不建议这么操作
            request.session['username'] = username
            # 跳转到页面
            return HttpResponseRedirect('/index/')
    else:
        # 不是 GET 请求则显示表单
        userfrom = UserForm()
    template_view = 'login.html'
    return render(request, template_view, {'userfrom': userfrom})


# 成功登录之后, 跳转首页
def index_view(request):
    username = request.session.get('username', '')
    # print(username)
    template_view = 'index.html'
    return render(request, template_view, {'username': username})


# 登出操作
def logout_view(request):
    # 删除 session
    del request.session['username']
    return HttpResponse('登出成功')
