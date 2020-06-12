from django.contrib import admin
from . models import *
# Register your models here.
class Plansadminmodel(admin.ModelAdmin):
  list_display = ("Plan_Name","Plans_Price","Plans_Days_Limit","Plans_Creates_At")
  search_fields = ["Plan_Name"]
admin.site.register(Plans,Plansadminmodel)


class Intrest_Categoryadminmodel(admin.ModelAdmin):
  list_display = ("Category_Name","Created_date_time")
  search_fields = ["Category_Name"]
admin.site.register(Intrest_Category,Intrest_Categoryadminmodel)

class Intrest_Sub_Categoryadminmodel(admin.ModelAdmin):
  list_display = ("Sub_Category_Name","Category","Created_date_time")

  search_fields = ["Sub_Category_Name"]
admin.site.register(Intrest_Sub_Category,Intrest_Sub_Categoryadminmodel)


class Usersadminmodel(admin.ModelAdmin):
  list_display = ("Users_Email","Users_Name","Users_Password","Users_Current_Plan","Users_Join_Date","Is_User_Active")
  list_filter = ("Intrest_Category","Is_User_Active","Users_Current_Plan")
  search_fields = ["Users_Name","Users_Email"]
admin.site.register(Users,Usersadminmodel)

class Videosadminmodel(admin.ModelAdmin):
  list_display = ("Titel","Category","Author_Name")
  list_filter = ("Author_Name","Category")
  search_fields = ["Titel","Author_Name","Category"]
admin.site.register(Videos,Videosadminmodel)

