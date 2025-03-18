from typing import Dict, Any, List, Optional
from .base import MarketoBase

class CustomObjects(MarketoBase):
    def __init__(self, auth):
        super().__init__(auth)
        self.base_endpoint = "v1/customobjects"

    def list(self) -> Dict[str, Any]:
        """Get list of custom objects available in the instance"""
        return self._get(f"{self.base_endpoint}.json")

    def describe(self, api_name: str) -> Dict[str, Any]:
        """
        Get metadata about a specific custom object type
        
        Args:
            api_name: API name of the custom object type
        """
        return self._get(f"{self.base_endpoint}/{api_name}/describe.json")

    def get_custom_objects(self, api_name: str, filter_type: str, filter_values: List[str],
                          fields: Optional[List[str]] = None, batch_size: Optional[int] = None,
                          next_page_token: Optional[str] = None) -> Dict[str, Any]:
        """
        Get custom objects by filter criteria
        
        Args:
            api_name: API name of the custom object type
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
            
        return self._get(f"{self.base_endpoint}/{api_name}.json", params=params)

    def create_or_update_custom_objects(self, api_name: str, objects: List[Dict[str, Any]],
                                      action: str = "createOrUpdate",
                                      dedupe_by: str = "dedupeFields") -> Dict[str, Any]:
        """
        Create or update custom objects
        
        Args:
            api_name: API name of the custom object type
            objects: List of custom object dictionaries
            action: Action to take (createOnly, updateOnly, createOrUpdate)
            dedupe_by: Field to use for deduplication (dedupeFields or idField)
        """
        data = {
            "input": objects,
            "action": action,
            "dedupeBy": dedupe_by
        }
        return self._post(f"{self.base_endpoint}/{api_name}.json", data=data)

    def delete_custom_objects(self, api_name: str, objects: List[Dict[str, Any]],
                            delete_by: str = "dedupeFields") -> Dict[str, Any]:
        """
        Delete custom objects
        
        Args:
            api_name: API name of the custom object type
            objects: List of custom object identifiers
            delete_by: Method to identify objects (dedupeFields or idField)
        """
        data = {
            "input": objects,
            "deleteBy": delete_by
        }
        return self._post(f"{self.base_endpoint}/{api_name}/delete.json", data=data)

    def get_field_data_types(self) -> Dict[str, Any]:
        """Get list of available field data types"""
        return self._get(f"{self.base_endpoint}/schema/fieldDataTypes.json")

    def get_linkable_objects(self) -> Dict[str, Any]:
        """Get list of objects that can be linked to custom objects"""
        return self._get(f"{self.base_endpoint}/schema/linkableObjects.json")

    def get_dependent_assets(self, api_name: str) -> Dict[str, Any]:
        """
        Get list of assets that depend on a custom object type
        
        Args:
            api_name: API name of the custom object type
        """
        return self._get(f"{self.base_endpoint}/schema/{api_name}/dependentAssets.json") 