from typing import Dict, Any, List, Optional
from .base import MarketoBase

class OpportunityRoles(MarketoBase):
    def __init__(self, auth):
        super().__init__(auth)
        self.base_endpoint = "v1/opportunityRoles"

    def get_opportunity_roles(self, max_return: int = 200, offset: int = 0) -> Dict[str, Any]:
        """
        Get all opportunity roles
        
        Args:
            max_return: Maximum number of records to return
            offset: Offset for pagination
        """
        return self._get(f"{self.base_endpoint}.json",
                        params={"maxReturn": max_return, "offset": offset})

    def get_opportunity_role_by_id(self, role_id: int) -> Dict[str, Any]:
        """
        Get an opportunity role by ID
        
        Args:
            role_id: ID of the opportunity role
        """
        return self._get(f"{self.base_endpoint}/{role_id}.json")

    def create_or_update_opportunity_roles(self, roles: List[Dict[str, Any]], 
                                         lookup_field: str = "externalOpportunityRoleId") -> Dict[str, Any]:
        """
        Create or update opportunity roles
        
        Args:
            roles: List of opportunity role dictionaries
            lookup_field: Field to use for deduplication (default: externalOpportunityRoleId)
        """
        return self._post(f"{self.base_endpoint}/upsert.json",
                         data={"input": roles, "lookupField": lookup_field})

    def delete_opportunity_role(self, role_id: int) -> Dict[str, Any]:
        """
        Delete an opportunity role by ID
        
        Args:
            role_id: ID of the opportunity role to delete
        """
        return self._delete(f"{self.base_endpoint}/{role_id}.json")

    def get_opportunity_role_types(self) -> Dict[str, Any]:
        """Get all available opportunity role types"""
        return self._get(f"{self.base_endpoint}/types.json")

    def get_opportunity_role_type_by_name(self, type_name: str) -> Dict[str, Any]:
        """
        Get a specific opportunity role type by name
        
        Args:
            type_name: Name of the opportunity role type
        """
        return self._get(f"{self.base_endpoint}/type/{type_name}.json") 