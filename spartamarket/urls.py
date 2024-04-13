"""
URL configuration for spartamarket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),

    path('accounts/', include('accounts.urls'))
]


"""
1. 회원가입을 기능을 구현
2. 로그인 로그아웃 기능 구현
3. 글 CRUD구현 하기 ( 회원의 PK 값을 보유 하고 있어야 함)
4. 프로필 페이지 만들기
"""