from typing import Dict, Any, List, Optional
from .base import MarketoBase

class LeadDatabase(MarketoBase):
    def __init__(self, auth):
        super().__init__(auth)
        self.base_endpoint = "v1/leads"
        self.company_endpoint = "v1/companies"
        self.opportunity_endpoint = "v1/opportunities"
        self.custom_object_endpoint = "v1/customobjects"

    def describe(self) -> Dict[str, Any]:
        """Get metadata about the lead object and its fields"""
        return self._get(f"{self.base_endpoint}/describe.json")

    def get_leads(self, filter_type: str, filter_values: List[str],
                  fields: Optional[List[str]] = None, batch_size: Optional[int] = None,
                  next_page_token: Optional[str] = None) -> Dict[str, Any]:
        """
        Get leads by filter criteria
        
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

    def create_or_update_leads(self, leads: List[Dict[str, Any]],
                             action: str = "createOrUpdate",
                             dedupe_by: str = "dedupeFields") -> Dict[str, Any]:
        """
        Create or update leads
        
        Args:
            leads: List of lead dictionaries
            action: Action to take (createOnly, updateOnly, createOrUpdate)
            dedupe_by: Field to use for deduplication (dedupeFields or idField)
        """
        data = {
            "input": leads,
            "action": action,
            "dedupeBy": dedupe_by
        }
        return self._post(f"{self.base_endpoint}.json", data=data)

    def delete_leads(self, leads: List[Dict[str, Any]],
                    delete_by: str = "dedupeFields") -> Dict[str, Any]:
        """
        Delete leads
        
        Args:
            leads: List of lead identifiers
            delete_by: Method to identify leads (dedupeFields or idField)
        """
        data = {
            "input": leads,
            "deleteBy": delete_by
        }
        return self._post(f"{self.base_endpoint}/delete.json", data=data)

    def get_lead_activities(self, lead_id: int, activity_type_ids: Optional[List[int]] = None,
                          start_date: Optional[str] = None, end_date: Optional[str] = None,
                          batch_size: Optional[int] = None,
                          next_page_token: Optional[str] = None) -> Dict[str, Any]:
        """
        Get activities for a specific lead
        
        Args:
            lead_id: ID of the lead
            activity_type_ids: List of activity type IDs to filter by
            start_date: Start date for activities (ISO 8601 format)
            end_date: End date for activities (ISO 8601 format)
            batch_size: Number of records to return per page
            next_page_token: Token for getting the next page of results
        """
        params = {}
        if activity_type_ids:
            params["activityTypeIds"] = ",".join(map(str, activity_type_ids))
        if start_date:
            params["startDate"] = start_date
        if end_date:
            params["endDate"] = end_date
        if batch_size:
            params["batchSize"] = batch_size
        if next_page_token:
            params["nextPageToken"] = next_page_token
            
        return self._get(f"{self.base_endpoint}/{lead_id}/activities.json", params=params)

    def get_lead_changes(self, start_date: str, end_date: Optional[str] = None,
                        fields: Optional[List[str]] = None, batch_size: Optional[int] = None,
                        next_page_token: Optional[str] = None) -> Dict[str, Any]:
        """
        Get changes to leads within a date range
        
        Args:
            start_date: Start date for changes (ISO 8601 format)
            end_date: End date for changes (ISO 8601 format)
            fields: List of fields to return
            batch_size: Number of records to return per page
            next_page_token: Token for getting the next page of results
        """
        params = {"startDate": start_date}
        if end_date:
            params["endDate"] = end_date
        if fields:
            params["fields"] = ",".join(fields)
        if batch_size:
            params["batchSize"] = batch_size
        if next_page_token:
            params["nextPageToken"] = next_page_token
            
        return self._get(f"{self.base_endpoint}/activities.json", params=params)

    def get_lead_by_id(self, lead_id: int) -> Dict[str, Any]:
        """Get a lead by ID"""
        return self._get(f"{self.base_endpoint}/{lead_id}.json")

    def get_lead_by_email(self, email: str) -> Dict[str, Any]:
        """Get a lead by email"""
        return self._get(f"{self.base_endpoint}/lookup.json", params={"email": email})

    def create_or_update_lead(self, leads: List[Dict[str, Any]], 
                            lookup_field: str = "email") -> Dict[str, Any]:
        """
        Create or update leads
        
        Args:
            leads: List of lead dictionaries
            lookup_field: Field to use for deduplication (default: email)
        """
        return self._post(f"{self.base_endpoint}/upsert.json", 
                         data={"input": leads, "lookupField": lookup_field})

    def delete_lead(self, lead_id: int) -> Dict[str, Any]:
        """Delete a lead by ID"""
        return self._delete(f"{self.base_endpoint}/{lead_id}.json")

    def get_lead_attributes(self) -> Dict[str, Any]:
        """Get all available lead attributes"""
        return self._get(f"{self.base_endpoint}/describe.json")

    # Company methods
    def get_companies(self, max_return: int = 200, offset: int = 0) -> Dict[str, Any]:
        """Get all companies"""
        return self._get(f"{self.company_endpoint}.json",
                        params={"maxReturn": max_return, "offset": offset})

    def get_company_by_id(self, company_id: int) -> Dict[str, Any]:
        """Get a company by ID"""
        return self._get(f"{self.company_endpoint}/{company_id}.json")

    def create_or_update_companies(self, companies: List[Dict[str, Any]], 
                                 lookup_field: str = "externalCompanyId") -> Dict[str, Any]:
        """
        Create or update companies
        
        Args:
            companies: List of company dictionaries
            lookup_field: Field to use for deduplication (default: externalCompanyId)
        """
        return self._post(f"{self.company_endpoint}/upsert.json",
                         data={"input": companies, "lookupField": lookup_field})

    def delete_company(self, company_id: int) -> Dict[str, Any]:
        """Delete a company by ID"""
        return self._delete(f"{self.company_endpoint}/{company_id}.json")

    # Opportunity methods
    def get_opportunities(self, max_return: int = 200, offset: int = 0) -> Dict[str, Any]:
        """Get all opportunities"""
        return self._get(f"{self.opportunity_endpoint}.json",
                        params={"maxReturn": max_return, "offset": offset})

    def get_opportunity_by_id(self, opportunity_id: int) -> Dict[str, Any]:
        """Get an opportunity by ID"""
        return self._get(f"{self.opportunity_endpoint}/{opportunity_id}.json")

    def create_or_update_opportunities(self, opportunities: List[Dict[str, Any]], 
                                    lookup_field: str = "externalOpportunityId") -> Dict[str, Any]:
        """
        Create or update opportunities
        
        Args:
            opportunities: List of opportunity dictionaries
            lookup_field: Field to use for deduplication (default: externalOpportunityId)
        """
        return self._post(f"{self.opportunity_endpoint}/upsert.json",
                         data={"input": opportunities, "lookupField": lookup_field})

    def delete_opportunity(self, opportunity_id: int) -> Dict[str, Any]:
        """Delete an opportunity by ID"""
        return self._delete(f"{self.opportunity_endpoint}/{opportunity_id}.json")

    # Custom Object methods
    def get_custom_objects(self, api_name: str, max_return: int = 200, 
                          offset: int = 0) -> Dict[str, Any]:
        """
        Get all custom objects of a specific type
        
        Args:
            api_name: API name of the custom object type
            max_return: Maximum number of records to return
            offset: Offset for pagination
        """
        return self._get(f"{self.custom_object_endpoint}/{api_name}.json",
                        params={"maxReturn": max_return, "offset": offset})

    def get_custom_object_by_id(self, api_name: str, object_id: int) -> Dict[str, Any]:
        """
        Get a custom object by ID
        
        Args:
            api_name: API name of the custom object type
            object_id: ID of the custom object
        """
        return self._get(f"{self.custom_object_endpoint}/{api_name}/{object_id}.json")

    def create_or_update_custom_objects(self, api_name: str, objects: List[Dict[str, Any]], 
                                      lookup_field: str = "marketoGUID") -> Dict[str, Any]:
        """
        Create or update custom objects
        
        Args:
            api_name: API name of the custom object type
            objects: List of custom object dictionaries
            lookup_field: Field to use for deduplication (default: marketoGUID)
        """
        return self._post(f"{self.custom_object_endpoint}/{api_name}/upsert.json",
                         data={"input": objects, "lookupField": lookup_field})

    def delete_custom_object(self, api_name: str, object_id: int) -> Dict[str, Any]:
        """
        Delete a custom object by ID
        
        Args:
            api_name: API name of the custom object type
            object_id: ID of the custom object
        """
        return self._delete(f"{self.custom_object_endpoint}/{api_name}/{object_id}.json")

    def get_custom_object_schema(self, api_name: str) -> Dict[str, Any]:
        """
        Get the schema for a custom object type
        
        Args:
            api_name: API name of the custom object type
        """
        return self._get(f"{self.custom_object_endpoint}/{api_name}/describe.json") 