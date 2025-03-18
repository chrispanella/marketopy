from typing import Dict, Any, List, Optional
from .base import MarketoBase

class FieldList(MarketoBase):
    def __init__(self, auth):
        super().__init__(auth)
        self.base_endpoint = "v1/fields"

    def get_fields(self, batch_size: Optional[int] = None,
                   next_page_token: Optional[str] = None) -> Dict[str, Any]:
        """
        Get list of fields available in the instance
        
        Args:
            batch_size: Number of records to return per page
            next_page_token: Token for getting the next page of results
        """
        params = {}
        if batch_size:
            params["batchSize"] = batch_size
        if next_page_token:
            params["nextPageToken"] = next_page_token
            
        return self._get(f"{self.base_endpoint}.json", params=params)

    def get_field_by_name(self, field_name: str) -> Dict[str, Any]:
        """
        Get metadata for a specific field
        
        Args:
            field_name: API name of the field
        """
        return self._get(f"{self.base_endpoint}/{field_name}.json")

    def create_field(self, field_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new field
        
        Args:
            field_data: Dictionary containing field metadata
        """
        return self._post(f"{self.base_endpoint}.json", data=field_data)

    def update_field(self, field_name: str, field_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update an existing field
        
        Args:
            field_name: API name of the field to update
            field_data: Dictionary containing updated field metadata
        """
        return self._post(f"{self.base_endpoint}/{field_name}.json", data=field_data)

    def delete_field(self, field_name: str) -> Dict[str, Any]:
        """
        Delete a field
        
        Args:
            field_name: API name of the field to delete
        """
        return self._delete(f"{self.base_endpoint}/{field_name}.json") 