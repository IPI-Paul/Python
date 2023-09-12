from rest_framework import permissions

# Django Rest Framework Custom Permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
  def has_permission(self, request, view):
    user = request.user
    # print(user.get_all_permissions())
    if user.is_staff:
      if user.has_perm('products_06.add_product'): # "app_name.verb_model_name"
        return True
      if user.has_perm('products_06.change_product'):
        return True
      if user.has_perm('products_06.delete_product'):
        return True
      if user.has_perm('products_06.view_product'):
        return True
      return False
    return False