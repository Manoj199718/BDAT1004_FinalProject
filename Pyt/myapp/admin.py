from django.contrib import admin

# Register your models here.
from .models import Flipkart,Amazon,Paytm,Snapdeal
from import_export.admin import ExportActionMixin
from import_export.admin import ImportExportModelAdmin




class FlipkartAdmin(ImportExportModelAdmin):
	pass

class AmazonAdmin(ImportExportModelAdmin):
	pass

class SnapdealAdmin(ImportExportModelAdmin):
	pass

class PaytmAdmin(ImportExportModelAdmin):
	pass

admin.site.register(Flipkart,FlipkartAdmin)
admin.site.register(Amazon,AmazonAdmin)
admin.site.register(Paytm,PaytmAdmin)
admin.site.register(Snapdeal,SnapdealAdmin)

