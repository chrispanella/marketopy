from typing import Dict, Any, List, Optional
from .base import MarketoBase

class NamedAccounts(MarketoBase):
    def __init__(self, auth):
        super().__init__(auth)
        self.base_endpoint = "v1/namedAccounts"
        self.list_endpoint = f"{self.base_endpoint}/lists"

    def get_named_accounts(self, max_return: int = 200, offset: int = 0) -> Dict[str, Any]:
        """
        Get all named accounts
        
        Args:
            max_return: Maximum number of records to return
            offset: Offset for pagination
        """
        return self._get(f"{self.base_endpoint}.json",
                        params={"maxReturn": max_return, "offset": offset})

    def get_named_account_by_id(self, account_id: int) -> Dict[str, Any]:
        """
        Get a named account by ID
        
        Args:
            account_id: ID of the named account
        """
        return self._get(f"{self.base_endpoint}/{account_id}.json")

    def create_or_update_named_accounts(self, accounts: List[Dict[str, Any]], 
                                      lookup_field: str = "externalCompanyId") -> Dict[str, Any]:
        """
        Create or update named accounts
        
        Args:
            accounts: List of named account dictionaries
            lookup_field: Field to use for deduplication (default: externalCompanyId)
        """
        return self._post(f"{self.base_endpoint}/upsert.json",
                         data={"input": accounts, "lookupField": lookup_field})

    def delete_named_account(self, account_id: int) -> Dict[str, Any]:
        """
        Delete a named account by ID
        
        Args:
            account_id: ID of the named account to delete
        """
        return self._delete(f"{self.base_endpoint}/{account_id}.json")

    def get_named_account_lists(self, max_return: int = 200, offset: int = 0) -> Dict[str, Any]:
        """
        Get all named account lists
        
        Args:
            max_return: Maximum number of records to return
            offset: Offset for pagination
        """
        return self._get(f"{self.list_endpoint}.json",
                        params={"maxReturn": max_return, "offset": offset})

    def get_named_account_list_by_id(self, list_id: int) -> Dict[str, Any]:
        """
        Get a named account list by ID
        
        Args:
            list_id: ID of the named account list
        """
        return self._get(f"{self.list_endpoint}/{list_id}.json")

    def create_named_account_list(self, name: str, description: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a new named account list
        
        Args:
            name: Name of the list
            description: Optional description of the list
        """
        data = {"name": name}
        if description:
            data["description"] = description
        return self._post(f"{self.list_endpoint}.json", data=data)

    def update_named_account_list(self, list_id: int, name: Optional[str] = None,
                                description: Optional[str] = None) -> Dict[str, Any]:
        """
        Update a named account list
        
        Args:
            list_id: ID of the list to update
            name: New name for the list
            description: New description for the list
        """
        data = {}
        if name:
            data["name"] = name
        if description:
            data["description"] = description
        return self._put(f"{self.list_endpoint}/{list_id}.json", data=data)

    def delete_named_account_list(self, list_id: int) -> Dict[str, Any]:
        """
        Delete a named account list
        
        Args:
            list_id: ID of the list to delete
        """
        return self._delete(f"{self.list_endpoint}/{list_id}.json")

    def add_accounts_to_list(self, list_id: int, account_ids: List[int]) -> Dict[str, Any]:
        """
        Add accounts to a named account list
        
        Args:
            list_id: ID of the list to add accounts to
            account_ids: List of account IDs to add
        """
        return self._post(f"{self.list_endpoint}/{list_id}/members.json",
                         data={"id": account_ids})

    def remove_accounts_from_list(self, list_id: int, account_ids: List[int]) -> Dict[str, Any]:
        """
        Remove accounts from a named account list
        
        Args:
            list_id: ID of the list to remove accounts from
            account_ids: List of account IDs to remove
        """
        return self._delete(f"{self.list_endpoint}/{list_id}/members.json",
                          data={"id": account_ids}) 