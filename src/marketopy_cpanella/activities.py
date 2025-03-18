from typing import Dict, Any, List, Optional
from .base import MarketoBase

class Activities(MarketoBase):
    def __init__(self, auth):
        super().__init__(auth)
        self.base_endpoint = "v1/activities"
        self.external_endpoint = f"{self.base_endpoint}/external"

    def get_activity_types(self) -> Dict[str, Any]:
        """Get all available activity types and their definitions"""
        return self._get(f"{self.base_endpoint}/types.json")

    def get_paging_token(self, since_datetime: str) -> Dict[str, Any]:
        """
        Get a paging token for activities since a specific datetime
        
        Args:
            since_datetime: ISO 8601 datetime string
        """
        return self._get(f"{self.base_endpoint}/pagingToken.json",
                        params={"sinceDatetime": since_datetime})

    def get_activities(self, next_page_token: str, 
                      activity_type_ids: Optional[List[int]] = None,
                      list_id: Optional[int] = None,
                      lead_ids: Optional[List[int]] = None) -> Dict[str, Any]:
        """
        Get activities using a paging token
        
        Args:
            next_page_token: Token from get_paging_token
            activity_type_ids: List of activity type IDs to filter by (max 10)
            list_id: Filter activities to leads in this list
            lead_ids: List of lead IDs to filter by (max 30)
        """
        params = {"nextPageToken": next_page_token}
        if activity_type_ids:
            params["activityTypeIds"] = ",".join(map(str, activity_type_ids))
        if list_id:
            params["listId"] = list_id
        if lead_ids:
            params["leadIds"] = ",".join(map(str, lead_ids))
            
        return self._get(f"{self.base_endpoint}.json", params=params)

    def get_lead_changes(self, next_page_token: str, fields: List[str]) -> Dict[str, Any]:
        """
        Get data value change activities for specific fields
        
        Args:
            next_page_token: Token from get_paging_token
            fields: List of fields to get changes for
        """
        return self._get(f"{self.base_endpoint}/leadchanges.json",
                        params={
                            "nextPageToken": next_page_token,
                            "fields": ",".join(fields)
                        })

    def get_deleted_leads(self, next_page_token: str) -> Dict[str, Any]:
        """
        Get deleted lead activities
        
        Args:
            next_page_token: Token from get_paging_token
        """
        return self._get(f"{self.base_endpoint}/deletedleads.json",
                        params={"nextPageToken": next_page_token})

    def create_custom_activity_type(self, api_name: str, name: str, description: str,
                                  primary_attribute: Dict[str, Any],
                                  attributes: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Create a new custom activity type
        
        Args:
            api_name: API name for the activity type
            name: Display name
            description: Description of the activity type
            primary_attribute: Primary attribute definition
            attributes: List of additional attribute definitions
        """
        data = {
            "apiName": api_name,
            "name": name,
            "description": description,
            "primaryAttribute": primary_attribute,
            "attributes": attributes
        }
        return self._post(f"{self.external_endpoint}/type.json", data=data)

    def create_custom_activity_attributes(self, api_name: str, 
                                        attributes: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Create attributes for a custom activity type
        
        Args:
            api_name: API name of the custom activity type
            attributes: List of attribute definitions
        """
        return self._post(f"{self.external_endpoint}/type/{api_name}/attributes/create.json",
                         data={"attributes": attributes})

    def update_custom_activity_attributes(self, api_name: str,
                                        attributes: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Update attributes for a custom activity type
        
        Args:
            api_name: API name of the custom activity type
            attributes: List of updated attribute definitions
        """
        return self._post(f"{self.external_endpoint}/type/{api_name}/attributes/update.json",
                         data={"attributes": attributes})

    def delete_custom_activity_attributes(self, api_name: str,
                                        attributes: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Delete attributes from a custom activity type
        
        Args:
            api_name: API name of the custom activity type
            attributes: List of attributes to delete
        """
        return self._post(f"{self.external_endpoint}/type/{api_name}/attributes/delete.json",
                         data={"attributes": attributes})

    def add_custom_activities(self, activities: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Add custom activities to lead records
        
        Args:
            activities: List of activity records to add (max 300)
        """
        return self._post(f"{self.external_endpoint}.json",
                         data={"input": activities}) 