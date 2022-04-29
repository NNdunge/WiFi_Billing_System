from django.contrib import admin
from .models import Sms_in, Sms_out,Voucher_type,Voucher

# Register your models here.
class Sms_inAdmin(admin.ModelAdmin):
    list_display= ('sms_txt', 'sender_number', 'sent_dt')

class Voucher_typeAdmin(admin.ModelAdmin):
    list_display= ('voucherType', 'voucherPrice')

class VoucherAdmin(admin.ModelAdmin):
     list_display= ('voucherID','voucherType', 'voucherStatus', 'boughtTime','generatedTime')

class Sms_outAdmin(admin.ModelAdmin):
    list_display= ('corresponding_request', 'currentTime_dt','voucherID')
     
admin.site.register(Sms_in,Sms_inAdmin)
admin.site.register(Voucher_type,Voucher_typeAdmin)
admin.site.register(Voucher,VoucherAdmin)
admin.site.register(Sms_out,Sms_outAdmin)