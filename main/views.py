from django.views import generic
from django.views.generic.edit import CreateView, DeleteView,UpdateView
from django.core.urlresolvers import reverse_lazy
from . models import TeamMembers, Teams, CciGroups,CompanyAssets,UserAssignedAccessories
from django.db.models.deletion import ProtectedError
from django.shortcuts import render,redirect,render_to_response
from django.http import Http404
from django.views.generic import View
from . forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage,InvalidPage
from django.core.paginator import PageNotAnInteger
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from cci import settings

@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = 'index.html'
    paginate_by = 5
    context_object_name = 'all_album'

    def get_queryset(self):
        return TeamMembers.objects.filter(Employeestatus_id = 1,Billablestatus_id = 1)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        bench = TeamMembers.objects.filter(Employeestatus_id = 2 )
        paginator = Paginator(bench, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            all_teamMembers = paginator.page(page)
        except PageNotAnInteger:
            all_teamMembers = paginator.page(1)
        except EmptyPage:
            all_teamMembers = paginator.page(paginator.num_pages)
        context['bench'] = all_teamMembers



        nonbillable = TeamMembers.objects.filter(Employeestatus_id=1, Billablestatus_id=2)
        paginator = Paginator(nonbillable, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            all_teamMembers = paginator.page(page)
        except PageNotAnInteger:
            all_teamMembers = paginator.page(1)
        except EmptyPage:
            all_teamMembers = paginator.page(paginator.num_pages)

        context['nonbillable'] = all_teamMembers
        return context





@method_decorator(login_required, name='dispatch')
class DetailView(generic.DetailView):
    model = TeamMembers
    context_object_name = 'TeamMembers'
    template_name = 'details.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['Assets'] = CompanyAssets.objects.filter(Name_id=self.kwargs['pk'])
        context['Accessories'] = UserAssignedAccessories.objects.filter(Name_id=self.kwargs['pk'])
        return context


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('main:password_change_done')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_change.html', {
        'form': form
    })


class TeamMemberCreate(CreateView):
    model = TeamMembers
    template_name = 'TeamMember_form.html'
    fields = ['Name', 'DOB','Email','Date_of_joining_CCI','Year_of_passing','Date_of_joining_Team','Phone_No','Technologies','Address','Qualification','Team','Skype_Id','Gmail','Pic','Designation','Description','Employeestatus','Billablestatus']


class TeamMemberUpdate(UpdateView):
    model = TeamMembers
    template_name = 'TeamMember_form.html'
    fields = ['Name', 'DOB', 'Designation', 'Gmail','Pic', 'Team','Email','Skype_Id','Date_of_joining_CCI','Date_of_joining_Team','Phone_No','Year_of_passing','Address','Qualification','Technologies','Description','Billablestatus','Employeestatus']


class TeamMemberDelete(DeleteView):
    model = TeamMembers
    success_url = reverse_lazy('main:index')


class TeamsCreate(CreateView):
    model = Teams
    template_name = 'Teams_form.html'
    fields = ['TeamName', 'TeamLead', 'ClientName', 'Tech','Group']


class TeamUpdate(UpdateView):
    model = Teams
    template_name = 'Teams_form.html'
    fields = ['TeamName', 'TeamLead', 'ClientName', 'Tech','Group']


@method_decorator(login_required, name='dispatch')
class TeamDetailView(generic.DetailView):
    model = Teams
    context_object_name = 'TeamsDetail'
    template_name = 'TeamDetails.html'
    paginate_by = 1


    def get_context_data(self, **kwargs):
        context = super(TeamDetailView, self).get_context_data(**kwargs)
        All_TeamMembers = TeamMembers.objects.filter(Team_id=self.kwargs['pk'])
        paginator = Paginator(All_TeamMembers, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            all_teamMembers = paginator.page(page)
        except PageNotAnInteger:
            all_teamMembers = paginator.page(1)
        except EmptyPage:
            all_teamMembers = paginator.page(paginator.num_pages)

        context['All_TeamMembers'] = all_teamMembers
        return context



@method_decorator(login_required, name='dispatch')
class TeamMemberDetailView(generic.DetailView):
    model = TeamMembers
    context_object_name = 'TeamMembers'
    template_name = 'TeamDetails.html'

@method_decorator(login_required, name='dispatch')
class TeamView(generic.ListView):
    template_name = 'AllTeams.html'
    context_object_name = 'teams'

    def get_queryset(self):
        return Teams.objects.all()



@method_decorator(login_required, name='dispatch')
class TeamsDelete(DeleteView):
    model = Teams
    success_url = reverse_lazy('main:AllTeams')

    def get_object(self,queryset=None,):
        obj = super(TeamsDelete, self).get_object()
        if obj.teammembers_set.count() != 0:
            raise Http404("You cannot Delete it")
        else:
            return obj


    # def get_object(self, queryset=None):
    #     obj = super(TeamsDelete, self).get_object(TeamMembers.objects.filter(id=self.kwargs['pk'])).count()
    #     if obj is not None:
    #         raise Http404
        # return obj
    # def get_object(self, queryset=None):
    #     obj = super(TeamsDelete, self).get_object(id=pk).count()
    #     # obj = TeamMembers.objects.filter(Team_id=self.kwargs['pk']).count()
    #     if obj == 0:
    #         return obj
    #     else:
    #         raise Http404("cannot delete")

@login_required
def search(req):
    if req.GET:
        search_term = req.GET['search_box']
        results = TeamMembers.objects.filter(Name__istartswith=search_term)
        #return render_to_response('ErrorDelete.html', {'results': results})
        return render(req,'ErrorDelete.html', {'results': results})
    return render('ErrorDelete.html', {})




class GroupCreate(CreateView):

    model = CciGroups
    template_name = 'Group_form.html'
    fields = ['GroupName']

@method_decorator(login_required, name='dispatch')
class GroupDelete(DeleteView):
    model = CciGroups
    success_url = reverse_lazy('main:GroupDetails')


class GroupUpdate(UpdateView):
    model = CciGroups
    template_name = 'Group_form.html'
    fields = ['GroupName']

@method_decorator(login_required, name='dispatch')
class GroupView(generic.ListView):
    template_name = 'GroupDetails.html'
    context_object_name = 'GroupsDetail'

    def get_queryset(self):
        return CciGroups.objects.all()




@method_decorator(login_required, name='dispatch')
class GroupDetailView(generic.DetailView):
    model = CciGroups
    context_object_name = 'Groups'
    template_name = 'GroupTeamDisplay.html'

    def get_context_data(self, **kwargs):
        context = super(GroupDetailView, self).get_context_data(**kwargs)
        context['GroupTeams'] = Teams.objects.filter(Group_id=self.kwargs['pk'])
        # require for tabs to display teammembers else not require
        context['all'] = TeamMembers.objects.filter(Team_id__Group_id = self.kwargs['pk'])
        return context





class UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'


    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form} )



    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request,user)
                    return redirect('main:index')
                else:
                    return HttpResponse("Inactive user.")
            else:
                return render(request, 'registration_form.html', {'registration_form': 'Username already exist'})

        return render(request, self.template_name, {'form': form,'registration_form': 'Username already exist'})


def Login(request):
    if not request.user.is_authenticated():
        next = request.GET.get('next', '/main/index/')
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(next)
                else:
                    return HttpResponse("Inactive user.")
            else:
            #return HttpResponseRedirect(settings.LOGIN_URL)
                return render(request, 'Login.html', {'login_form': 'Username or password is Invalid'})

        return render(request, "Login.html", {'redirect_to': next})
    else:
        return redirect('main:index')


def Logout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

@login_required
def Home(request):
    return render(request, "home.html", {})

























