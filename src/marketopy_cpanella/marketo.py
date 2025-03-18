from typing import Optional
from .authentication import Authentication
from .lead_database import LeadDatabase
from .asset import Asset
from .user_management import UserManagement
from .identity import Identity
from .activities import Activities
from .fields import Fields
from .named_accounts import NamedAccounts
from .opportunity_roles import OpportunityRoles
from .program_members import ProgramMembers

class Marketo:
    def __init__(self, munchkin_id: str, client_id: str, client_secret: str):
        """
        Initialize the Marketo client
        
        Args:
            munchkin_id: Your Marketo Munchkin ID
            client_id: Your Marketo Client ID
            client_secret: Your Marketo Client Secret
        """
        self.auth = Authentication(munchkin_id, client_id, client_secret)
        self._lead_database: Optional[LeadDatabase] = None
        self._asset: Optional[Asset] = None
        self._user_management: Optional[UserManagement] = None
        self._identity: Optional[Identity] = None
        self._activities: Optional[Activities] = None
        self._fields: Optional[Fields] = None
        self._named_accounts: Optional[NamedAccounts] = None
        self._opportunity_roles: Optional[OpportunityRoles] = None
        self._program_members: Optional[ProgramMembers] = None

    @property
    def lead_database(self) -> LeadDatabase:
        """Access the Lead Database API"""
        if self._lead_database is None:
            self._lead_database = LeadDatabase(self.auth)
        return self._lead_database

    @property
    def asset(self) -> Asset:
        """Access the Asset API"""
        if self._asset is None:
            self._asset = Asset(self.auth)
        return self._asset

    @property
    def user_management(self) -> UserManagement:
        """Access the User Management API"""
        if self._user_management is None:
            self._user_management = UserManagement(self.auth)
        return self._user_management

    @property
    def identity(self) -> Identity:
        """Access the Identity API"""
        if self._identity is None:
            self._identity = Identity(self.auth)
        return self._identity

    @property
    def activities(self) -> Activities:
        """Access the Activities API"""
        if self._activities is None:
            self._activities = Activities(self.auth)
        return self._activities

    @property
    def fields(self) -> Fields:
        """Access the Fields API"""
        if self._fields is None:
            self._fields = Fields(self.auth)
        return self._fields

    @property
    def named_accounts(self) -> NamedAccounts:
        """Access the Named Accounts API"""
        if self._named_accounts is None:
            self._named_accounts = NamedAccounts(self.auth)
        return self._named_accounts

    @property
    def opportunity_roles(self) -> OpportunityRoles:
        """Access the Opportunity Roles API"""
        if self._opportunity_roles is None:
            self._opportunity_roles = OpportunityRoles(self.auth)
        return self._opportunity_roles

    @property
    def program_members(self) -> ProgramMembers:
        """Access the Program Members API"""
        if self._program_members is None:
            self._program_members = ProgramMembers(self.auth)
        return self._program_members 