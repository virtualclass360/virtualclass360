from django.db import models

# Create your models here.
class Plans(models.Model):
    Plan_Name=models.CharField(max_length=100)
    Plans_Price=models.CharField(max_length=100)
    Plans_Days_Limit=models.CharField(max_length=100)
    Plans_Creates_At=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Plan_Name
    class Meta:
        verbose_name = "Plan"




class Intrest_Category(models.Model):
    Category_Name=models.CharField(max_length=100)
    Category_Image=models.ImageField(upload_to='images/category')
    Created_date_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Category_Name

    class Meta:
        verbose_name = "Interst Category"


class Intrest_Sub_Category(models.Model):
    Category=models.ForeignKey(Intrest_Category,on_delete=models.CASCADE,null=True)
    Sub_Category_Name=models.CharField(max_length=100)
    Sub_Category_Image=models.ImageField(upload_to='images/subcategory')
    Created_date_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Sub_Category_Name

    class Meta:
        verbose_name = "Interst Sub Category"


class Users(models.Model):
    Users_Name=models.CharField(max_length=100)
    Users_Email=models.CharField(max_length=100,unique=True)
    Users_Password=models.CharField(max_length=100)
    Users_Join_Date=models.DateTimeField(auto_now_add=True)
    Is_User_Active=models.BooleanField("Is User Active",default=True)
    Users_Current_Plan=models.ForeignKey(Plans,on_delete=models.CASCADE,null=True)
    Intrest_Category=models.ManyToManyField(Intrest_Category)

    def __str__(self):
        return self.Users_Name

    class Meta:
        verbose_name = "App User"


class Videos(models.Model):
    Titel=models.CharField(max_length=100)
    Category=models.ForeignKey(Intrest_Category,on_delete=models.CASCADE,null=True)
    Videos=models.FileField(upload_to='videos')
    Author_Name=models.CharField(max_length=1000)
    Descriptions=models.TextField(max_length=3000)

    def __str__(self):
        return self.Titel


    class Meta:
        verbose_name = "Video"
