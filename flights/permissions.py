from email import message
from rest_framework.permissions import BasePermission
import datetime

class HasAuthority(BasePermission):
    message = " You are not authorized to view this "
    def has_object_permission(self,request,view,obj):
        return request.user == obj.owner or request.user.is_staff



class IsNotTooSoon(BasePermission):
    message = " can not be changed after 3 days."
    def has_object_permission(self,request,view,obj):
        # today = datetime.date.today()
        # diff = obj.date - today
        return obj.date >= datetime.date.today()+3
