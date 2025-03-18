from typing import Dict, Any, List, Optional
from .base import MarketoBase

class Companies(MarketoBase):
    def __init__(self, auth):
        super().__init__(auth)
        self.base_endpoint = "v1/companies"

    def describe(self) -> Dict[str, Any]:
        """Get metadata about the company object and its fields"""
        return self._get(f"{self.base_endpoint}/describe.json")

    def get_companies(self, filter_type: str, filter_values: List[str],
                     fields: Optional[List[str]] = None, batch_size: Optional[int] = None,
                     next_page_token: Optional[str] = None) -> Dict[str, Any]:
        """
        Get companies by filter criteria
        
        Args:
            filter_type: Field to filter by (must be from searchableFields or dedupeFields)
            filter_values: Values to filter by
            fields: List of fields to return (default: id, dedupeFields, updatedAt, createdAt)
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

    def create_or_update_companies(self, companies: List[Dict[str, Any]], 
                                 action: str = "createOrUpdate",
                                 dedupe_by: str = "dedupeFields") -> Dict[str, Any]:
        """
        Create or update companies
        
        Args:
            companies: List of company dictionaries
            action: Action to take (createOnly, updateOnly, createOrUpdate)
            dedupe_by: Field to use for deduplication (dedupeFields or idField)
        """
        data = {
            "input": companies,
            "action": action,
            "dedupeBy": dedupe_by
        }
        return self._post(f"{self.base_endpoint}.json", data=data)

    def delete_companies(self, companies: List[Dict[str, Any]], 
                        delete_by: str = "dedupeFields") -> Dict[str, Any]:
        """
        Delete companies
        
        Args:
            companies: List of company identifiers
            delete_by: Method to identify companies (dedupeFields or idField)
        """
        data = {
            "input": companies,
            "deleteBy": delete_by
        }
        return self._post(f"{self.base_endpoint}/delete.json", data=data)

    def get_company_fields(self, batch_size: Optional[int] = None,
                          next_page_token: Optional[str] = None) -> Dict[str, Any]:
        """
        Get metadata for all fields on the company object
        
        Args:
            batch_size: Number of records to return per page (default: 300)
            next_page_token: Token for getting the next page of results
        """
        params = {}
        if batch_size:
            params["batchSize"] = batch_size
        if next_page_token:
            params["nextPageToken"] = next_page_token
            
        return self._get(f"{self.base_endpoint}/schema/fields.json", params=params)

    def get_company_field_by_name(self, field_name: str) -> Dict[str, Any]:
        """
        Get metadata for a specific company field
        
        Args:
            field_name: API name of the field
        """
        return self._get(f"{self.base_endpoint}/schema/fields/{field_name}.json") 