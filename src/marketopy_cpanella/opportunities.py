from typing import Dict, Any, List, Optional
from .base import MarketoBase

class Opportunities(MarketoBase):
    def __init__(self, auth):
        super().__init__(auth)
        self.base_endpoint = "v1/opportunities"

    def describe(self) -> Dict[str, Any]:
        """Get metadata about the opportunity object and its fields"""
        return self._get(f"{self.base_endpoint}/describe.json")

    def get_opportunities(self, filter_type: str, filter_values: List[str],
                         fields: Optional[List[str]] = None, batch_size: Optional[int] = None,
                         next_page_token: Optional[str] = None) -> Dict[str, Any]:
        """
        Get opportunities by filter criteria
        
        Args:
            filter_type: Field to filter by (must be from searchableFields or dedupeFields)
            filter_values: Values to filter by
            fields: List of fields to return
            batch_size: Number of records to return per page
            next_page_token: Token for getting the next page of results
        """
        params = {
            "filterType": filter_type,
            "filterValues": ",".join(filter_values)
        }
        if fields:
            params["fields"] = ",".join(fields)
        if batch_size:
            params["batchSize"] = batch_size
        if next_page_token:
            params["nextPageToken"] = next_page_token
            
        return self._get(f"{self.base_endpoint}.json", params=params)

    def create_or_update_opportunities(self, opportunities: List[Dict[str, Any]],
                                    action: str = "createOrUpdate",
                                    dedupe_by: str = "dedupeFields") -> Dict[str, Any]:
        """
        Create or update opportunities
        
        Args:
            opportunities: List of opportunity dictionaries
            action: Action to take (createOnly, updateOnly, createOrUpdate)
            dedupe_by: Field to use for deduplication (dedupeFields or idField)
        """
        data = {
            "input": opportunities,
            "action": action,
            "dedupeBy": dedupe_by
        }
        return self._post(f"{self.base_endpoint}.json", data=data)

    def delete_opportunities(self, opportunities: List[Dict[str, Any]],
                           delete_by: str = "dedupeFields") -> Dict[str, Any]:
        """
        Delete opportunities
        
        Args:
            opportunities: List of opportunity identifiers
            delete_by: Method to identify opportunities (dedupeFields or idField)
        """
        data = {
            "input": opportunities,
            "deleteBy": delete_by
        }
        return self._post(f"{self.base_endpoint}/delete.json", data=data)

    def get_opportunity_roles(self, opportunity_id: int,
                            batch_size: Optional[int] = None,
                            next_page_token: Optional[str] = None) -> Dict[str, Any]:
        """
        Get roles associated with an opportunity
        
        Args:
            opportunity_id: ID of the opportunity
            batch_size: Number of records to return per page
            next_page_token: Token for getting the next page of results
        """
        params = {}
        if batch_size:
            params["batchSize"] = batch_size
        if next_page_token:
            params["nextPageToken"] = next_page_token
            
        return self._get(f"{self.base_endpoint}/{opportunity_id}/roles.json", params=params)

    def add_roles_to_opportunity(self, opportunity_id: int,
                               roles: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Add roles to an opportunity
        
        Args:
            opportunity_id: ID of the opportunity
            roles: List of role dictionaries
        """
        data = {"input": roles}
        return self._post(f"{self.base_endpoint}/{opportunity_id}/roles.json", data=data)

    def remove_roles_from_opportunity(self, opportunity_id: int,
                                   roles: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Remove roles from an opportunity
        
        Args:
            opportunity_id: ID of the opportunity
            roles: List of role identifiers
        """
        data = {"input": roles}
        return self._post(f"{self.base_endpoint}/{opportunity_id}/roles/delete.json", data=data) 