from typing import Dict, Any, List, Optional
from .base import MarketoBase

class Asset(MarketoBase):
    def __init__(self, auth):
        super().__init__(auth)
        self.base_endpoint = "asset/v1"

    def get_emails(self, max_return: int = 200, offset: int = 0) -> Dict[str, Any]:
        """Get all emails"""
        return self._get(f"{self.base_endpoint}/emails.json", 
                        params={"maxReturn": max_return, "offset": offset})

    def get_email_by_id(self, email_id: int) -> Dict[str, Any]:
        """Get an email by ID"""
        return self._get(f"{self.base_endpoint}/email/{email_id}.json")

    def get_landing_pages(self, max_return: int = 200, offset: int = 0) -> Dict[str, Any]:
        """Get all landing pages"""
        return self._get(f"{self.base_endpoint}/landingPages.json",
                        params={"maxReturn": max_return, "offset": offset})

    def get_landing_page_by_id(self, page_id: int) -> Dict[str, Any]:
        """Get a landing page by ID"""
        return self._get(f"{self.base_endpoint}/landingPage/{page_id}.json")

    def get_forms(self, max_return: int = 200, offset: int = 0) -> Dict[str, Any]:
        """Get all forms"""
        return self._get(f"{self.base_endpoint}/forms.json",
                        params={"maxReturn": max_return, "offset": offset})

    def get_form_by_id(self, form_id: int) -> Dict[str, Any]:
        """Get a form by ID"""
        return self._get(f"{self.base_endpoint}/form/{form_id}.json")

    def create_email(self, name: str, subject: str, from_name: str, 
                    from_email: str, reply_to: str, content: str) -> Dict[str, Any]:
        """
        Create a new email
        
        Args:
            name: Email name
            subject: Email subject
            from_name: Sender name
            from_email: Sender email
            reply_to: Reply-to email
            content: Email content
        """
        data = {
            "name": name,
            "subject": subject,
            "fromName": from_name,
            "fromEmail": from_email,
            "replyTo": reply_to,
            "content": content
        }
        return self._post(f"{self.base_endpoint}/email.json", data=data)

    def create_landing_page(self, name: str, content: str) -> Dict[str, Any]:
        """
        Create a new landing page
        
        Args:
            name: Landing page name
            content: Landing page content
        """
        data = {
            "name": name,
            "content": content
        }
        return self._post(f"{self.base_endpoint}/landingPage.json", data=data)

    def create_form(self, name: str, fields: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Create a new form
        
        Args:
            name: Form name
            fields: List of form fields
        """
        data = {
            "name": name,
            "fields": fields
        }
        return self._post(f"{self.base_endpoint}/form.json", data=data) 