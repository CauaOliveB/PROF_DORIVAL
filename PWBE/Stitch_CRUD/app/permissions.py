from rest_framework.permissions import BasePermission

class IsHumano(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user == 'H'

class IsAlien(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user == 'A'

class IsExperimento(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user == 'E'

class IsHumanoOuMorador(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.especie == 'H':
            return True
        return obj.id == request.user.planeta.id

