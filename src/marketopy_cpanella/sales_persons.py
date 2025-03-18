from typing import Dict, Any, List, Optional
from .base import MarketoBase

class SalesPersons(MarketoBase):
    def __init__(self, auth):
        super().__init__(auth)
        self.base_endpoint = "v1/salespersons"

    def get_sales_persons(self, batch_size: Optional[int] = None,
                         next_page_token: Optional[str] = None) -> Dict[str, Any]:
        """
        Get list of sales persons
        
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

    def get_sales_person_by_id(self, sales_person_id: int) -> Dict[str, Any]:
        """
        Get a specific sales person
        
        Args:
            sales_person_id: ID of the sales person
        """
        return self._get(f"{self.base_endpoint}/{sales_person_id}.json")

    def create_or_update_sales_persons(self, sales_persons: List[Dict[str, Any]],
                                     action: str = "createOrUpdate") -> Dict[str, Any]:
        """
        Create or update sales persons
        
        Args:
            sales_persons: List of sales person dictionaries
            action: Action to take (createOnly, updateOnly, createOrUpdate)
        """
        data = {
            "input": sales_persons,
            "action": action
        }
        return self._post(f"{self.base_endpoint}.json", data=data)

    def delete_sales_persons(self, sales_persons: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Delete sales persons
        
        Args:
            sales_persons: List of sales person identifiers
        """
        data = {"input": sales_persons}
        return self._post(f"{self.base_endpoint}/delete.json", data=data)

    def get_sales_person_opportunities(self, sales_person_id: int,
                                     batch_size: Optional[int] = None,
                                     next_page_token: Optional[str] = None) -> Dict[str, Any]:
        """
        Get opportunities associated with a sales person
        
        Args:
            sales_person_id: ID of the sales person
            batch_size: Number of records to return per page
            next_page_token: Token for getting the next page of results
        """
        params = {}
        if batch_size:
            params["batchSize"] = batch_size
        if next_page_token:
            params["nextPageToken"] = next_page_token
            
        return self._get(f"{self.base_endpoint}/{sales_person_id}/opportunities.json", params=params) 