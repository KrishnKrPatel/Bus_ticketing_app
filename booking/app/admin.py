from django.contrib import admin
from .models import Profile,Booking,Bus,BusRoute,BusTimeTable,Address
# Register your models here.

class BusAdmin(admin.ModelAdmin):
    list_display=['bus_name','bus_no','get_route','source','destination','arrivial_time','departure_time','fare']
    def get_route(self,obj):
        list_route=list()
        for element in obj.bus_route.all():
            list_route.append(element)
        return list_route

    class Meta:
        model = Bus


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['get_user','dob','get_address']

    def get_user(self,obj):
        return obj.user.username
    def get_address(self,obj):
        return obj.address
    class Meta:
        model = Profile


class BookingAdmin(admin.ModelAdmin):
    list_display = ['get_cust','get_bus','status','fare_category','fare','pay_status']

    def get_cust(self,obj):
        return obj.cust_id.user.username

    def get_bus(self,obj):
        return obj.bus_id.bus_no

    class Meta:
        model = Bus

class BusRouteAdmin(admin.ModelAdmin):
    list_display = ['route','arrival_time','departure_time']
    search_fields = ('route',)

class AddressAdmin(admin.ModelAdmin):
    list_display = ['address_1','address_2','state','city','pincode']
    search_fields = ('state','city','pincode')




admin.site.register(Address,AddressAdmin)
admin.site.register(BusRoute,BusRouteAdmin)
admin.site.register(Booking,BookingAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Bus,BusAdmin)
