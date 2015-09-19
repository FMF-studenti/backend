from rest_framework.permissions import BasePermission, SAFE_METHODS

ADMIN_METHODS = ('PUT', 'DELETE')

class AuthenticatedAddAdminEditOrReadOnly(BasePermission):
    """
    Users can add, admins can edit, or is a read-only request.
    """

    def has_permission(self, request, view):
    	if request.method in ADMIN_METHODS:
    		return request.user and request.user.is_staff
    	else:
	        return (
	            request.method in SAFE_METHODS or
	            request.user and
	            request.user.is_authenticated()
	        )
