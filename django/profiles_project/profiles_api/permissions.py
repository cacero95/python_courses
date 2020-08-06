from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    # allows users to edit their own profile

    def has_object_permission(self, request, view, obj):
        # the user is trying to edit their own profile
        if request.method in permissions.SAFE_METHODS:
            return True
        # do the validations if the id or the user try to edit his own object in the dba with services
        return obj.id == request.user.id