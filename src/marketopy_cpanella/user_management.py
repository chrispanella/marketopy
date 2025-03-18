from typing import Dict, Any, List, Optional
from .base import MarketoBase

class UserManagement(MarketoBase):
    def __init__(self, auth):
        super().__init__(auth)
        self.base_endpoint = "v1/users"

    def get_users(self, max_return: int = 200, offset: int = 0) -> Dict[str, Any]:
        """Get all users"""
        return self._get(f"{self.base_endpoint}.json",
                        params={"maxReturn": max_return, "offset": offset})

    def get_user_by_id(self, user_id: int) -> Dict[str, Any]:
        """Get a user by ID"""
        return self._get(f"{self.base_endpoint}/{user_id}.json")

    def invite_user(self, email: str, first_name: str, last_name: str, 
                   role_ids: List[int], permissions: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Invite a new user
        
        Args:
            email: User's email address
            first_name: User's first name
            last_name: User's last name
            role_ids: List of role IDs to assign
            permissions: Optional list of specific permissions
        """
        data = {
            "email": email,
            "firstName": first_name,
            "lastName": last_name,
            "roleIds": role_ids
        }
        if permissions:
            data["permissions"] = permissions
        return self._post(f"{self.base_endpoint}/invite.json", data=data)

    def update_user(self, user_id: int, first_name: Optional[str] = None,
                   last_name: Optional[str] = None, role_ids: Optional[List[int]] = None,
                   permissions: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Update a user's information
        
        Args:
            user_id: User ID to update
            first_name: New first name
            last_name: New last name
            role_ids: New list of role IDs
            permissions: New list of permissions
        """
        data = {}
        if first_name:
            data["firstName"] = first_name
        if last_name:
            data["lastName"] = last_name
        if role_ids:
            data["roleIds"] = role_ids
        if permissions:
            data["permissions"] = permissions
            
        return self._put(f"{self.base_endpoint}/{user_id}.json", data=data)

    def delete_user(self, user_id: int) -> Dict[str, Any]:
        """Delete a user by ID"""
        return self._delete(f"{self.base_endpoint}/{user_id}.json")

    def get_roles(self) -> Dict[str, Any]:
        """Get all available roles"""
        return self._get(f"{self.base_endpoint}/roles.json") 