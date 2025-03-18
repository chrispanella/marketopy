from typing import Dict, Any, List, Optional
from .base import MarketoBase

class ProgramMembers(MarketoBase):
    def __init__(self, auth):
        super().__init__(auth)
        self.base_endpoint = "v1/programs"

    def get_program_members(self, program_id: int, max_return: int = 200, 
                          offset: int = 0) -> Dict[str, Any]:
        """
        Get all members of a program
        
        Args:
            program_id: ID of the program
            max_return: Maximum number of records to return
            offset: Offset for pagination
        """
        return self._get(f"{self.base_endpoint}/{program_id}/members.json",
                        params={"maxReturn": max_return, "offset": offset})

    def get_program_member_by_id(self, program_id: int, member_id: int) -> Dict[str, Any]:
        """
        Get a specific program member
        
        Args:
            program_id: ID of the program
            member_id: ID of the program member
        """
        return self._get(f"{self.base_endpoint}/{program_id}/member/{member_id}.json")

    def add_members_to_program(self, program_id: int, leads: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Add leads to a program
        
        Args:
            program_id: ID of the program
            leads: List of lead dictionaries with required fields
        """
        return self._post(f"{self.base_endpoint}/{program_id}/members.json",
                         data={"input": leads})

    def remove_members_from_program(self, program_id: int, lead_ids: List[int]) -> Dict[str, Any]:
        """
        Remove leads from a program
        
        Args:
            program_id: ID of the program
            lead_ids: List of lead IDs to remove
        """
        return self._delete(f"{self.base_endpoint}/{program_id}/members.json",
                          data={"id": lead_ids})

    def get_program_member_status(self, program_id: int, lead_id: int) -> Dict[str, Any]:
        """
        Get the status of a lead in a program
        
        Args:
            program_id: ID of the program
            lead_id: ID of the lead
        """
        return self._get(f"{self.base_endpoint}/{program_id}/member/{lead_id}/status.json")

    def update_program_member_status(self, program_id: int, lead_id: int, 
                                   status: str, reason: Optional[str] = None) -> Dict[str, Any]:
        """
        Update the status of a lead in a program
        
        Args:
            program_id: ID of the program
            lead_id: ID of the lead
            status: New status for the lead
            reason: Optional reason for the status change
        """
        data = {"status": status}
        if reason:
            data["reason"] = reason
        return self._put(f"{self.base_endpoint}/{program_id}/member/{lead_id}/status.json",
                        data=data) 