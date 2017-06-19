from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from . import views
from django.contrib.auth.views import login, password_reset, password_reset_done,password_change_done
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import views as auth_views

app_name = 'main'

urlpatterns = [
        #url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^main/registraion/$', views.UserFormView.as_view(), name='registration'),
        url(r'^password/$', views.change_password, name='change_password'),

        url(r'^password-change/done/$', password_change_done, name='password_change_done'),

        url(r'^main/index/search/?$', login_required(views.search), name='search'),
        url(r'^main/index/$', login_required(views.IndexView.as_view()), name='index'),


        url(r'^(?P<pk>[0-9]+)$', login_required(views.DetailView.as_view()), name='details'),
        #url(r'^(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='details'),
        #url(r'^main/add/$', views.TeamMemberCreate.as_view(), name='TeamMember'),
        url(r'^main/(?P<pk>[0-9]+)/delete/$', views.TeamMemberDelete.as_view(), name='TeamMember-delete'),
       # url(r'^main/teams/add/$', views.TeamsCreate.as_view(), name='Teams'),

      #  url(r'^main/team/update/(?P<pk>[0-9]+)/$', views.TeamUpdate.as_view(), name='Team-update'),
        #url(r'^main/team/(?P<pk>[0-9]+)/update/$', views.TeamUpdate.as_view(), name='Team-update'),

       # url(r'^main/teams/(?P<pk>[0-9]+)$', views.TeamDetailView.as_view(), name='TeamDetails'),
        url(r'^main/teams/(?P<pk>[0-9]+)$',  login_required(views.TeamDetailView.as_view()), name='TeamDetails'),
        #url(r'^main/teams/$', views.TeamView.as_view(), name='AllTeams'),
        url(r'^main/teams/$',login_required( views.TeamView.as_view()), name='AllTeams'),
       # url(r'^main/(?P<pk>[0-9]+)/teams/delete/', views.TeamsDelete.as_view(), name = 'Teams-delete'),
        url(r'^(?P<pk>[0-9]+)$', views.TeamMemberDetailView.as_view(), name='TeamMemberDetails'),
        url(r'^(?P<pk>[0-9]+)$', login_required(views.TeamMemberDetailView.as_view()), name='TeamMemberDetails'),
       # url(r'^main/groupadd/$', views.GroupCreate.as_view(), name='Groups'),

        #url(r'^main/groups/(?P<pk>[0-9]+)/delete/$', views.GroupDelete.as_view(), name='Group-delete'),
       # url(r'^main/group/(?P<pk>[0-9]+)/update/$', views.GroupUpdate.as_view(), name='Group-update'),

        #url(r'^main/groups/$',views.GroupView.as_view(), name='GroupDetails'),
       # url(r'^main/groupsDetail/(?P<pk>[0-9]+)$', views.GroupDetailView.as_view(), name='GroupTeamDetails'),
        url(r'^main/teammembers/(?P<pk>[0-9]+)/update/$', views.TeamMemberUpdate.as_view(), name='TeamMember-update'),


        url(r'^register/$', views.UserFormView.as_view(), name='register'),
        url(r'^main/groups/$',login_required(views.GroupView.as_view()), name='GroupDetails'),
        url(r'^main/groupsDetail/(?P<pk>[0-9]+)$', login_required(views.GroupDetailView.as_view()), name='GroupTeamDetails'),
        url(r'^main/(?P<pk>[0-9]+)/teams/delete/', login_required(views.TeamsDelete.as_view()), name = 'Teams-delete'),
        url(r'^main/groups/(?P<pk>[0-9]+)/delete/$', login_required(views.GroupDelete.as_view()), name='Group-delete'),
        url(r'^main/add/$', permission_required('is_superuser')(views.TeamMemberCreate.as_view()), name='TeamMember'),
        url(r'^main/teams/add/$', permission_required('is_superuser')(views.TeamsCreate.as_view()), name='Teams'),
        url(r'^main/groupadd/$', permission_required('is_superuser')(views.GroupCreate.as_view()), name='Groups'),
        url(r'^main/group/(?P<pk>[0-9]+)/update/$', permission_required('is_superuser')(views.GroupUpdate.as_view()), name='Group-update'),
        url(r'^main/team/(?P<pk>[0-9]+)/update/$', permission_required('is_superuser')(views.TeamUpdate.as_view()), name='Team-update'),
        url(r'^home/$', views.Home),
        url(r'^Login/$', views.Login,name = 'Login'),

        url(r'^$', views.Login,name = 'Login',),
        url(r'^logout/$', views.Logout),
        ]