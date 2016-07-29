# Contact Tool SDK

Python SDK used to interact with [TOP-IX Contact Tool](https://github.com/topix-hackademy/contact-tools).

## Install

Install the package with `pip` from Github (release branch):
 
    pip install git+git://github.com/topix-hackademy/python-contact-tool-sdk@release
    
Or download the repo and run from the root of the package:

    python setup.py develop
    
Now you're ready to go!

## Usage

To have access to the package we need to import our API CONNECTOR:

    from contactsdk.connector import Connector

Now we have to create an instance of the Connector class passing three informations:

* ACCESS-TOKEN

* BASE-URL

* API-ENDPOINT

Here an example:

    connector = Connector(YOUR-ACCESS-TOKEN, YOUR-BASE-URL, API-ENDPOINT)
    
Now, we are ready to contact the APIs passing through 4 end points:

* company

* company_type

* contact

* contact_type

For each endpoint we have access to the following methods:

### GET ALL

Return the complete list of elements. Example of usage:

    connector.company.get_all()

### GET ONE

Return a company by id. We need to pass as argument the `id` of the resource. Example of usage:

    connector.company.get_one(1)

### CREATE

Create a new company. We need to pass as argument a new `data`. Example of usage:

    data = {
        "company_custom_id": 111, "company_short_name": "shortName", "company_name": "CompName", 
        "company_business_name": "CompName", "company_tax_code": "123",
        "company_city": "Turin", "company_province": "Turin", 
        "company_country": "Italy",  "company_address": "via delle vie", 
        "company_cap": "123",
        "company_phone_number": "123", "company_fax": "123",  
        "company_website": "example.com", "company_notes": "just a simple note", 
        "company_type":[{"id":1, "type_name":"PEERING"}]
    }
    connector.company.create(data)

### UPDATE

Update a company. We need to pass as argument the `id` of the resource and a new `data`. Example of usage:

    data = {
        "company_custom_id": 111, "company_short_name": "shortName", "company_name": "CompName", 
        "company_business_name": "CompName", "company_tax_code": "123",
        "company_city": "Turin", "company_province": "Turin", 
        "company_country": "Italy",  "company_address": "via delle vie", 
        "company_cap": "123",
        "company_phone_number": "123", "company_fax": "123",  
        "company_website": "example.com", "company_notes": "just a simple note", 
        "company_type":[{"id":1, "type_name":"PEERING"}]
    }
    connector.company.create(1, data)


## Example

Here some code examples:

    from contactsdk.connector import Connector
    connector = Connector(YOUR-ACCESS-TOKEN, YOUR-BASE-URL, API-ENDPOINT)
    
    # GET ALL THE COMPANIES
    print connector.company.get_all()
    
    # GET ONE COMPANY
    print connector.company.get_one(1)
    
    # CREATE NEW COMPANY
    data = {
        "company_custom_id": 111, "company_short_name": "shortName", "company_name": "CompName", 
        "company_business_name": "CompName", "company_tax_code": "123",
        "company_city": "Turin", "company_province": "Turin", 
        "company_country": "Italy",  "company_address": "via delle vie", 
        "company_cap": "123",
        "company_phone_number": "123", "company_fax": "123",  
        "company_website": "example.com", "company_notes": "just a simple note", 
        "company_type":[{"id":1, "type_name":"PEERING"}]
    }
    new_company = connector.company.create(data)
    
    # UPDATE COMPANY
    new_company_updated = connector.company.update(1, data)

## Company By Code

To retrieve a company by taxcode or VAT number we can use the method `get_by_code` owned by the company object:
 
    from contactsdk.connector import Connector
    connector = Connector(YOUR-ACCESS-TOKEN, YOUR-BASE-URL, API-ENDPOINT)
    
    # GET COMPANY BY CODE
    print connector.company.get_by_code(VAT_NUMBER)
    
## Contact By Email

To retrieve a contact by his email we can use the method `get_by_email` owned by the contact object:
 
    from contactsdk.connector import Connector
    connector = Connector(YOUR-ACCESS-TOKEN, YOUR-BASE-URL, API-ENDPOINT)
    
    # GET COMPANY BY CODE
    print connector.contact.get_by_email(EMAIL_TO_SEARCH)