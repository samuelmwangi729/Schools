from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class SuccessfulLogins(models.Model):
    username=models.CharField(max_length=100)
    browser=models.CharField(max_length=1000)
    ip=models.CharField(max_length=100)

    def __str__(self):
        return self.username
class Sliders(models.Model):
    Intro=models.CharField(max_length=1000)
    Desc=models.CharField(max_length=1000)
    Image=models.ImageField(upload_to='Sliders')
    Active=models.IntegerField(default=0)

    def __str__(self):
        return self.Image
    def __isActive(self):
        if self.Status:
            return True
        else:
            return False
class Menus(models.Model):
    Name=models.CharField(max_length=100)
    hasSub=models.IntegerField(default=0)
    Status=models.IntegerField(default=1)

    def __str__(self):
        return self.Name
    def hasSubMenu(self):
        if self.hasSub:
            return True
        else:
            return False
    def getSubs(self):
        subs=SubMenus.objectss.filter(MainMenu=self.id)
        return subs
class SubMenus(models.Model):
    MainMenu=models.ForeignKey(Menus,on_delete=models.DO_NOTHING)
    SubmenuName=models.CharField(max_length=100)
    Status=models.IntegerField(default=1)

    #this makes sure tat the model returns back the subcategory Name 
    def __str__(self):
        return self.SubmenuName
    #get the Main category name 
    def getMain(self):
        Main=Menus.objects.filter(id=self.MainMenu)[0]
        return MainMenu
    def __getStatus(self):
        if self.Status:
            return True
        else:
            return False
class Pages(models.Model):
    PageTitle=models.CharField(max_length=300)
    PageSlug=models.CharField(max_length=1000)
    ArticleMenu=models.ForeignKey(Menus,on_delete=models.DO_NOTHING)
    ArticleSubMenu=models.ForeignKey(SubMenus,on_delete=models.DO_NOTHING)
    PageContent=RichTextField(blank=True,null=True)
    FeaturedImage=models.ImageField(upload_to='Pages')
    Status=models.IntegerField(default=1)

    def __str__(self):
        return self.PageTitle
    def __getPageMenu(self):
        menu=Menus.objects.filter(id=self.ArticleMenu)[0]
        return menu
    def __getStatus(self):
        if self.Status:
            return "Active"
        else:
            return "Drafted"
class Abouts(models.Model):
    Motto=RichTextField(blank=True,null=True)
    Vision=RichTextField(blank=True,null=True)
    Mission=RichTextField(blank=True,null=True)
    CoreValues=RichTextField(blank=True,null=True)
    content=RichTextField(blank=True,null=True)

    def __str__(self):
        return self.Motto
    def __getVision(self):
        return self.Vision
    def __getMission(self):
        return self.Mission
    def __getCore(self):
        return self.CoreValues

class Departments(models.Model):
    Name=models.CharField(max_length=100)
    Topics=RichTextField(blank=True,null=True)
    DepartmentHead=models.CharField(max_length=100)
    HoDPic=models.ImageField(upload_to='Departments')
    Status=models.IntegerField(default=1)

    def __str__(self):
        return self.Name
    def __isActive(self):
        if self.Status:
            return True
        else:
            return False
class Careers(models.Model):
    Title=models.CharField(max_length=500)
    Description=RichTextField(blank=True,null=True)
    Status=models.IntegerField(default=1)

    def __str__(self):
        return self.Title
    def __isActive(self):
        if self.Status:
            return True
        else:
            return False
class Contacts(models.Model):
    SchoolName=models.CharField(max_length=1000)
    SchoolLogo=models.ImageField(upload_to='Contacts')
    PhoneNumbers=models.CharField(max_length=100)
    Location=models.CharField(max_length=200)
    Emails=models.CharField(max_length=200)
    PrincipalName=models.CharField(max_length=500)
    PrincipalWords=RichTextField(blank=True,null=True)
    PrincipalPic=models.ImageField(upload_to='Contacts')

    def __str__(self):
        return self.SchoolName
    def __getEmails(self):
        return self.Emails
    def __getLocation(self):
        return self.Location
    def __getPrincipal(self):
        return self.PrincipalName()
    def __getQuote(self):
        return self.PrincipalWords
class Subscribers(models.Model):
    Name=models.CharField(max_length=1000)
    Email=models.CharField(max_length=1000)
    Status=models.IntegerField(default=1)

    def __str__(self):
        return self.Email
    def __getName(self):
        return self.Name
    def __isActive(self):
        if self.Status:
            return True
        else:
            return False

class Links(models.Model):
    Name=models.CharField(max_length=2000)
    Link=models.CharField(max_length=1000)