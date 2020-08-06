from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    # allows users to edit their own profile

    def has_object_permission(self, request, view, obj):
        # the user is trying to edit their own profile
        if request.method in permissions.SAFE_METHODS:
            return True
        # do the validations if the id or the user try to edit his own object in the dba with services
        return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission):
    # allow users to update their own status

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id