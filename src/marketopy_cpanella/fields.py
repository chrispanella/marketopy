from typing import Dict, Any, List, Optional
from .base import MarketoBase

class Fields(MarketoBase):
    def __init__(self, auth):
        super().__init__(auth)
        self.base_endpoint = "v1/leads"
        self.field_types_endpoint = "v1/leads/fieldtypes"

    def get_field_list(self, max_return: int = 200, offset: int = 0) -> Dict[str, Any]:
        """
        Get all available fields in the lead database
        
        Args:
            max_return: Maximum number of records to return
            offset: Offset for pagination
        """
        return self._get(f"{self.base_endpoint}/fields.json",
                        params={"maxReturn": max_return, "offset": offset})

    def get_field_by_name(self, field_name: str) -> Dict[str, Any]:
        """
        Get a specific field by name
        
        Args:
            field_name: Name of the field to retrieve
        """
        return self._get(f"{self.base_endpoint}/field/{field_name}.json")

    def create_field(self, name: str, display_name: str, data_type: str,
                    length: Optional[int] = None, description: Optional[str] = None,
                    is_required: bool = False, is_hidden: bool = False,
                    is_primary_key: bool = False) -> Dict[str, Any]:
        """
        Create a new field in the lead database
        
        Args:
            name: API name of the field
            display_name: Display name of the field
            data_type: Data type of the field
            length: Length of the field (for string types)
            description: Description of the field
            is_required: Whether the field is required
            is_hidden: Whether the field is hidden
            is_primary_key: Whether the field is a primary key
        """
        data = {
            "name": name,
            "displayName": display_name,
            "dataType": data_type,
            "isRequired": is_required,
            "isHidden": is_hidden,
            "isPrimaryKey": is_primary_key
        }
        if length:
            data["length"] = length
        if description:
            data["description"] = description
            
        return self._post(f"{self.base_endpoint}/fields.json", data=data)

    def update_field(self, field_name: str, display_name: Optional[str] = None,
                    description: Optional[str] = None, is_required: Optional[bool] = None,
                    is_hidden: Optional[bool] = None) -> Dict[str, Any]:
        """
        Update an existing field
        
        Args:
            field_name: Name of the field to update
            display_name: New display name
            description: New description
            is_required: New required status
            is_hidden: New hidden status
        """
        data = {}
        if display_name:
            data["displayName"] = display_name
        if description:
            data["description"] = description
        if is_required is not None:
            data["isRequired"] = is_required
        if is_hidden is not None:
            data["isHidden"] = is_hidden
            
        return self._put(f"{self.base_endpoint}/field/{field_name}.json", data=data)

    def delete_field(self, field_name: str) -> Dict[str, Any]:
        """
        Delete a field from the lead database
        
        Args:
            field_name: Name of the field to delete
        """
        return self._delete(f"{self.base_endpoint}/field/{field_name}.json")

    def get_field_types(self) -> Dict[str, Any]:
        """Get all available field types"""
        return self._get(f"{self.field_types_endpoint}.json")

    def get_field_type_by_name(self, field_type_name: str) -> Dict[str, Any]:
        """
        Get a specific field type by name
        
        Args:
            field_type_name: Name of the field type to retrieve
        """
        return self._get(f"{self.field_types_endpoint}/{field_type_name}.json") 