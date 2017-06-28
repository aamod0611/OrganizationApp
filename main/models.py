from django.db import models
from django.core.urlresolvers import reverse
import datetime
from django import forms

class CciGroups(models.Model):
    GroupName = models.CharField(db_column='Name',max_length=200,default=None)
    DateCreated = models.DateTimeField(auto_now_add = False,default=datetime.datetime.now(),editable=False)
    DateModified = models.DateTimeField(auto_now_add = False,default=datetime.datetime.now(),editable=False)

    def get_absolute_url(self):
        return reverse('main:GroupTeamDetails', kwargs={'pk': self.pk})

    def __str__(self):
        return self.GroupName

    class Meta:
        db_table = "Group"

class Teams(models.Model):
    TeamName = models.CharField(db_column='Name',max_length=200)
    TeamLead = models.CharField(max_length=200,null=True)
    ClientName = models.CharField(max_length=200)
    Tech = models.CharField(max_length=200,null=True)
    Group = models.ForeignKey(CciGroups,db_column='GroupId', blank=False, default=1)
    DateCreated = models.DateTimeField(auto_now_add=False, default=datetime.datetime.now(),editable=False)
    DateModified = models.DateTimeField(auto_now_add=False, default=datetime.datetime.now(),editable=False)


    def get_absolute_url(self):
        return reverse('main:TeamDetails', kwargs={'pk': self.pk})

    def __str__(self):
        return self.TeamName

    class Meta:
        db_table = "Team"

class Designations(models.Model):
    DesignationName = models.CharField(max_length=200)

    def __str__(self):
        return self.DesignationName

class Employee_Status(models.Model):
    Status = models.CharField(max_length=20)

    def __str__(self):
        return self.Status

class Billable_Status(models.Model):
    BillableStatus = models.CharField(max_length=20)

    def __str__(self):
        return self.BillableStatus


class TeamMembers(models.Model):
    Name = models.CharField(max_length=200)
    DOB =  models.DateField(max_length=8,default=None)
    Designation = models.ForeignKey(Designations,db_column='Designation', blank=False, default=1,null=True)

# this extra is for romino's database
    #Desigtn = models.IntegerField(db_column='Designation',max_length=200,null=True)
    DateCreated = models.DateTimeField(auto_now_add=False, default=datetime.datetime.now(), editable=False)
    DateModified = models.DateTimeField(auto_now_add=False, default=datetime.datetime.now(), editable=False)
    Gmail = models.EmailField(max_length=50, db_column='GmailId', default=None)
    IsTeanLead = models.BooleanField(db_column='IsTeanLead',null=False,default=0)

#######################

    Pic = models.FileField(db_column='Image',default='Images/default.png')
    Team = models.ForeignKey(Teams,db_column='TeamId', blank=False, default=1, on_delete=models.PROTECT)
    Email = models.EmailField(max_length=50,db_column='EmailId',default=None,error_messages={'required': 'this Email Id does not exist'},)
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))
    Year_of_passing = models.IntegerField(('Year_of_passing'), max_length=4,db_column='YearOfPassing', choices=YEAR_CHOICES)
    Date_of_joining_CCI = models.DateField(max_length=8,db_column='YearofJoiningCCI',default=None)
    Date_of_joining_Team = models.DateField(max_length=8,db_column='YearofJoiningTeam',default=None)
    Phone_No = models.CharField(db_column='phoneNumber',max_length=10)
    Skype_Id = models.EmailField(max_length=50,db_column='SkypeId',default=None)
    Address = models.CharField(max_length=200,default=None)
    Qualification = models.CharField(max_length=200,db_column='HighestQualification',default=None)
    Technologies = models.CharField(max_length=200,default=None)
    Description = models.CharField(max_length=200,db_column='BriefDescription',default=None)
    Employeestatus = models.ForeignKey(Employee_Status,db_column='EmployeeStatus', blank=False, default=1,null=True)
    Billablestatus = models.ForeignKey(Billable_Status,db_column='BillableStatus', blank=False, default=1,null=True)

    def get_absolute_url(self):
        return reverse('main:details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.Name

    class Meta:
        db_table = "TeamMember"


class Laptop(models.Model):
    Device_Tag = models.CharField(max_length=20,default=None)
    Sr_No = models.CharField(max_length=20,default=None)
    Manufacturer = models.CharField(max_length=20,default=None)
    Model = models.CharField(max_length=20,default=None)
    Processor = models.CharField(max_length=20,default=None)
    RAM = models.CharField(max_length=20,default=None)
    OS = models.CharField(max_length=20,default=None)
    Mem_Speed = models.CharField(max_length=20,default=None)
    Purchased_Date = models.DateField(max_length=8,default=None)
    Purchased_From = models.CharField(max_length=20,default=None)
    Service_Date = models.DateField(max_length=8,default=None)

    def __str__(self):
        return self.Sr_No

class KeyBoard(models.Model):
    Device_Tag = models.CharField(max_length=20, default=None)
    Model = models.CharField(max_length=20, default=None)

    def __str__(self):
        return self.Device_Tag


class Mouse(models.Model):
    Device_Tag = models.CharField(max_length=20, default=None)
    Model = models.CharField(max_length=20, default=None)

    def __str__(self):
        return self.Device_Tag


class Dongle(models.Model):
    PhoneNO = models.CharField(max_length=20, default=None)
    Provider = models.CharField(max_length=20, default=None)

    def __str__(self):
        return self.Provider


class CompanyAssets(models.Model):
    Name = models.ForeignKey(TeamMembers, blank=False, default=1)
    laptop = models.ForeignKey(Laptop,blank=False, default=1)
    keyboard = models.ForeignKey(KeyBoard, blank=False, default=1)
    mouse = models.ForeignKey(Mouse, blank=False, default=1)
    dongle = models.ForeignKey(Dongle, blank=False, default=1)



class UserAssignedAccessories(models.Model):
    Name = models.ForeignKey(TeamMembers, blank=False, default=1)
    Webcam = models.BooleanField(null=False, default=0)
    Dock = models.BooleanField(null=False, default=0)
    Adopter = models.BooleanField(null=False, default=0)
    SpikeGuard = models.BooleanField(null=False, default=0)
    HeadPhone = models.BooleanField(null=False, default=0)
    Quantity = models.CharField(max_length=20, default=None)
