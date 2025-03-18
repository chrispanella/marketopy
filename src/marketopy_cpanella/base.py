import requests
from typing import Dict, Any, Optional
from .authentication import Authentication

class MarketoBase:
    def __init__(self, auth: Authentication):
        self.auth = auth
        self.base_url = f"https://{auth.munchkin_id}.mktorest.com/rest"
        self.headers = {
            "Authorization": f"Bearer {auth.getAuthToken()}",
            "Content-Type": "application/json"
        }

    def _make_request(self, method: str, endpoint: str, params: Optional[Dict[str, Any]] = None, 
                     data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Make a request to the Marketo API
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint
            params: Query parameters
            data: Request body data
            
        Returns:
            Dict containing the API response
        """
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(
            method=method,
            url=url,
            headers=self.headers,
            params=params,
            json=data
        )
        response.raise_for_status()
        return response.json()

    def _get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a GET request"""
        return self._make_request("GET", endpoint, params=params)

    def _post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Make a POST request"""
        return self._make_request("POST", endpoint, data=data)

    def _put(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Make a PUT request"""
        return self._make_request("PUT", endpoint, data=data)

    def _delete(self, endpoint: str) -> Dict[str, Any]:
        """Make a DELETE request"""
        return self._make_request("DELETE", endpoint) 