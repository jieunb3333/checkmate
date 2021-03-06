"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# """
from django.contrib import admin
from django.urls import path, include
from checkmate import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main ,name='main'),
    path('infoWrite/', views.infoWrite, name='infoWrite'),
    path('dom_infoWrite/', views.dom_infoWrite, name='dom_infoWrite'),
    path('account/', include('account.urls')),
    path('survey/', include('survey.urls')),
    path('roommate/', include('roommate.urls')),
    path('mypageScrap/',views.mypageScrap, name='mypageScrap'),
    path('mypageScrap_dom/',views.mypageScrap_dom, name='mypageScrap_dom'),
    path('mypageScrap_off/',views.mypageScrap_off, name='mypageScrap_off'),
    path('mypageWritten/',views.mypageWritten, name='mypageWritten'),
    path('mypageWritten_off/',views.mypageWritten_off, name='mypageWritten_off'),
    path('offcampusCommunity/',views.offcampusCommunity, name='offcampusCommunity'),
    path('domitoryCommunity/',views.domitoryCommunity, name='domitoryCommunity'),
    path('offcampusView/<int:post_id>',views.offcampusView, name='offcampusView'),
    path('domitoryView/<int:post_id>',views.domitoryView, name='domitoryView'),
    path('offcampusDelete/<int:post_id>',views.offcampusDelete, name='offcampusDelete'),
    path('domitoryDelete/<int:post_id>',views.domitoryDelete, name='domitoryDelete'),
    path('offcampusUpdate/<int:post_id>',views.offcampusUpdate, name='offcampusUpdate'),
    path('domitoryUpdate/<int:post_id>',views.domitoryUpdate, name='domitoryUpdate'),
    path('domitory_popular/',views.domitory_popular, name='domitory_popular'),
    path('offcampus_popular/',views.offcampus_popular, name='offcampus_popular'),
    path('commnet_action_dom/<int:post_id>', views.commnet_action_dom, name='commnet_action_dom'),
    path('commnet_action_off/<int:post_id>', views.commnet_action_off, name='commnet_action_off'),
    path('comment_del_dom/<int:post_id>/<int:comment_id>', views.comment_del_dom, name="comment_del_dom"),
    path('comment_del_off/<int:post_id>/<int:comment_id>', views.comment_del_off, name="comment_del_off")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)