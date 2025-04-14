# bot/core/permission_manager.py

class PermissionManager:
    def __init__(self):
        pass

    def has_permission(self, member, required_roles):
        return any(role.id in required_roles for role in member.roles)
