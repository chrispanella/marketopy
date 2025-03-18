from typing import Dict, Any
from .base import MarketoBase

class FieldTypes(MarketoBase):
    def __init__(self, auth):
        super().__init__(auth)
        self.base_endpoint = "v1/fieldTypes"

    def get_field_types(self) -> Dict[str, Any]:
        """Get list of available field types"""
        return self._get(f"{self.base_endpoint}.json")

    def get_field_type_by_name(self, field_type_name: str) -> Dict[str, Any]:
        """
        Get metadata for a specific field type
        
        Args:
            field_type_name: Name of the field type
        """
        return self._get(f"{self.base_endpoint}/{field_type_name}.json") 