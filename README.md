# MarketoPy

A Python client library for the Marketo REST API. This library provides a simple and intuitive interface to interact with Marketo's various APIs.

## Installation

```bash
pip install marketopy-cpanella
```

## Quick Start

```python
from marketopy_cpanella import Marketo

# Initialize the client
marketo = Marketo(
    munchkin_id="your-munchkin-id",
    client_id="your-client-id",
    client_secret="your-client-secret"
)

# Example: Get leads by email
leads = marketo.lead_database.get_leads(
    filter_type="email",
    filter_values=["example@email.com"]
)
```

## Available APIs

### Lead Database API

The Lead Database API provides access to leads, companies, opportunities, and custom objects.

```python
# Get lead metadata
metadata = marketo.lead_database.describe()

# Get leads by filter
leads = marketo.lead_database.get_leads(
    filter_type="email",
    filter_values=["example@email.com"],
    fields=["id", "email", "firstName", "lastName"]
)

# Create or update leads
new_leads = marketo.lead_database.create_or_update_leads([
    {
        "email": "new@example.com",
        "firstName": "John",
        "lastName": "Doe"
    }
])

# Get lead activities
activities = marketo.lead_database.get_lead_activities(
    lead_id=123,
    start_date="2024-01-01T00:00:00Z",
    end_date="2024-02-01T00:00:00Z"
)

# Get lead changes
changes = marketo.lead_database.get_lead_changes(
    start_date="2024-01-01T00:00:00Z",
    fields=["email", "firstName", "lastName"]
)
```

### Custom Objects API

The Custom Objects API allows you to work with custom objects in Marketo.

```python
# List custom objects
objects = marketo.custom_objects.list()

# Get custom object metadata
metadata = marketo.custom_objects.describe("car_c")

# Get custom objects by filter
cars = marketo.custom_objects.get_custom_objects(
    api_name="car_c",
    filter_type="vin",
    filter_values=["123456789"]
)

# Create or update custom objects
new_cars = marketo.custom_objects.create_or_update_custom_objects(
    api_name="car_c",
    objects=[
        {
            "vin": "123456789",
            "make": "Toyota",
            "model": "Camry",
            "year": 2024
        }
    ]
)

# Get field data types
field_types = marketo.custom_objects.get_field_data_types()

# Get linkable objects
linkable = marketo.custom_objects.get_linkable_objects()
```

### Field List API

The Field List API provides access to field metadata and management.

```python
# Get list of fields
fields = marketo.field_list.get_fields()

# Get field metadata
field = marketo.field_list.get_field_by_name("email")

# Create new field
new_field = marketo.field_list.create_field({
    "name": "customField",
    "displayName": "Custom Field",
    "dataType": "string",
    "length": 255
})

# Update field
updated = marketo.field_list.update_field(
    "customField",
    {"displayName": "Updated Field Name"}
)

# Delete field
marketo.field_list.delete_field("customField")
```

### Field Types API

The Field Types API provides information about available field types.

```python
# Get list of field types
types = marketo.field_types.get_field_types()

# Get field type metadata
type_info = marketo.field_types.get_field_type_by_name("string")
```

### Named Account Lists API

The Named Account Lists API allows you to manage named account lists.

```python
# Get list of named account lists
lists = marketo.named_account_lists.get_lists()

# Get list metadata
list_info = marketo.named_account_lists.get_list_by_id(123)

# Create new list
new_list = marketo.named_account_lists.create_list({
    "name": "New List",
    "description": "A new named account list"
})

# Get list members
members = marketo.named_account_lists.get_list_members(123)

# Add members to list
marketo.named_account_lists.add_members_to_list(123, [
    {"externalCompanyId": "123", "name": "Company A"}
])

# Remove members from list
marketo.named_account_lists.remove_members_from_list(123, [
    {"externalCompanyId": "123"}
])
```

### Opportunities API

The Opportunities API provides access to opportunity management.

```python
# Get opportunity metadata
metadata = marketo.opportunities.describe()

# Get opportunities by filter
opportunities = marketo.opportunities.get_opportunities(
    filter_type="externalOpportunityId",
    filter_values=["123", "456"]
)

# Create or update opportunities
new_opportunities = marketo.opportunities.create_or_update_opportunities([
    {
        "externalOpportunityId": "789",
        "name": "New Opportunity",
        "amount": 10000
    }
])

# Get opportunity roles
roles = marketo.opportunities.get_opportunity_roles(123)

# Add roles to opportunity
marketo.opportunities.add_roles_to_opportunity(123, [
    {"role": "Decision Maker", "leadId": 456}
])

# Remove roles from opportunity
marketo.opportunities.remove_roles_from_opportunity(123, [
    {"role": "Decision Maker", "leadId": 456}
])
```

### Sales Persons API

The Sales Persons API allows you to manage sales person records.

```python
# Get list of sales persons
sales_persons = marketo.sales_persons.get_sales_persons()

# Get sales person metadata
person = marketo.sales_persons.get_sales_person_by_id(123)

# Create or update sales persons
new_persons = marketo.sales_persons.create_or_update_sales_persons([
    {
        "externalSalesPersonId": "789",
        "name": "John Doe",
        "email": "john@example.com"
    }
])

# Get sales person opportunities
opportunities = marketo.sales_persons.get_sales_person_opportunities(123)
```

## Error Handling

The library includes built-in error handling for API responses. All API calls return a dictionary containing:
- `success`: Boolean indicating if the request was successful
- `result`: The actual response data
- `requestId`: Unique identifier for the request
- `errors`: List of error messages (if any)

```python
try:
    response = marketo.lead_database.get_leads(
        filter_type="email",
        filter_values=["example@email.com"]
    )
    if response["success"]:
        leads = response["result"]
    else:
        print(f"Error: {response['errors']}")
except Exception as e:
    print(f"Exception: {str(e)}")
```

## Pagination

Many API endpoints support pagination using `batchSize` and `nextPageToken` parameters:

```python
# Get first page of results
response = marketo.lead_database.get_leads(
    filter_type="email",
    filter_values=["example@email.com"],
    batch_size=200
)

# Get next page if available
if "nextPageToken" in response:
    next_page = marketo.lead_database.get_leads(
        filter_type="email",
        filter_values=["example@email.com"],
        batch_size=200,
        next_page_token=response["nextPageToken"]
    )
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 