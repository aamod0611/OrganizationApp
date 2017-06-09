from django.db import models
from django.core.urlresolvers import reverse
import datetime
from django import forms

class CciGroups(models.Model):

    GroupName = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('main:GroupTeamDetails', kwargs={'pk': self.pk})

    def __str__(self):
        return self.GroupName


class Teams(models.Model):
    TeamName = models.CharField(max_length=200)
    TeamLead = models.CharField(max_length=200)
    ClientName = models.CharField(max_length=200)
    Tech = models.CharField(max_length=200)
    Group = models.ForeignKey(CciGroups, blank=False, default=1)

    def get_absolute_url(self):
        return reverse('main:TeamDetails', kwargs={'pk': self.pk})

    def __str__(self):
        return self.TeamName


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
    Designation = models.ForeignKey(Designations, blank=False, default=1)
    Pic = models.FileField(default='Images/default.png')
    Team = models.ForeignKey(Teams, blank=False, default=1, on_delete=models.PROTECT)
    Email = models.EmailField(max_length=50,default=None,error_messages={'required': 'this Email Id does not exist'},)
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))
    Year_of_passing = models.IntegerField(('Year_of_passing'), max_length=4, choices=YEAR_CHOICES)
    Date_of_joining_CCI = models.DateField(max_length=8,default=None)
    Date_of_joining_Team = models.DateField(max_length=8,default=None)
    Phone_No = models.IntegerField()
    Skype_Id = models.EmailField(max_length=50,default=None)
    Address = models.CharField(max_length=200,default=None)
    Qualification = models.CharField(max_length=200,default=None)
    Technologies = models.CharField(max_length=200,default=None)
    Description = models.CharField(max_length=200,default=None)
    Employeestatus = models.ForeignKey(Employee_Status, blank=False,default=1)
    Billablestatus = models.ForeignKey(Billable_Status, blank=False,default=1)


    def get_absolute_url(self):
        return reverse('main:details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.Name




