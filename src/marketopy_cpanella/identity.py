from typing import Dict, Any, Optional
from .base import MarketoBase

class Identity(MarketoBase):
    def __init__(self, auth):
        super().__init__(auth)
        self.base_endpoint = "identity"

    def get_access_token(self, grant_type: str = "client_credentials",
                        client_id: Optional[str] = None,
                        client_secret: Optional[str] = None) -> Dict[str, Any]:
        """
        Get an access token
        
        Args:
            grant_type: Type of grant (default: client_credentials)
            client_id: Optional client ID (if not using auth object's)
            client_secret: Optional client secret (if not using auth object's)
        """
        params = {
            "grant_type": grant_type,
            "client_id": client_id or self.auth.client_id,
            "client_secret": client_secret or self.auth.client_secret
        }
        return self._get(f"{self.base_endpoint}/oauth/token.json", params=params)

    def get_identity(self, access_token: str) -> Dict[str, Any]:
        """
        Get identity information for an access token
        
        Args:
            access_token: The access token to get identity for
        """
        self.headers["Authorization"] = f"Bearer {access_token}"
        return self._get(f"{self.base_endpoint}/oauth/userinfo.json") 