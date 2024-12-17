
# AirTable

Airtable can store information in a spreadsheet that's visually appealing and easy-to-use, but it's also powerful enough to act as a database that businesses can use for customer-relationship management (CRM), task management, project planning, and tracking inventory.

Python Version - 2
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api key|The API key is used to create the connection with airtable|False|Password|None|
|Base id|.|False|String|None|
|Table name|.|False|String|None|


#### Dependencies
| |
|-|
|requests-2.24.0-py2.py3-none-any.whl|
|urllib3-1.25.10-py2.py3-none-any.whl|
|requests-2.23.0-py2.py3-none-any.whl|
|certifi-2019.11.28-py2.py3-none-any.whl|
|six-1.14.0-py2.py3-none-any.whl|
|airtable_python_wrapper-0.12.0-py2.py3-none-any.whl|
|chardet-3.0.4-py2.py3-none-any.whl|
|idna-2.9-py2.py3-none-any.whl|
|certifi-2020.6.20-py2.py3-none-any.whl|
|idna-2.10-py2.py3-none-any.whl|
|urllib3-1.25.8-py2.py3-none-any.whl|


## Actions
#### Search
Search specific fields (columns) in a table
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Field value|The value of a specific field in a table|True|String||
|Field name|The name of a specific field (column) in the table|True|String||
|Table name|A table stores similar (structured) data, and each base can have multiple tables.  This parameter indicates the name of the table within the base.|True|String||
|Base id|Base is a database in Airtable in which you store data.The base ID can be found in the URL of the API page of the base. |True|String||
|Max records|The maximum records (rows) that will be affected by the action|False|String|100|



##### JSON Results
```json
[  
  {  
    "id": "recCc2V3tpfStq4kh",  
    "fields": {  
      "Field_Name_1": "Field_Value_1",  
      "Field_Name_2": "Field_Value_2",  
      "Field_Name_3": "Field_Value_3"  
    },  
    "createdTime": "2019-06-27T06:22:10.000Z"  
  }  
]
```



#### Ping
Test connection to the AirTable product
Timeout - 300 Seconds



##### JSON Results
```json
{}
```



#### Enrich Entities From Table
Search specific fields (columns) in a table
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Enrichment Prefix|Prefix to use for entity enrichment|False|String|AT_|
|Max records|The maximum records (rows) that will be affected by the action|False|String|100|
|Base id|Base is a database in Airtable in which you store data.The base ID can be found in the URL of the API page of the base. |True|String||
|Table name|A table stores similar (structured) data, and each base can have multiple tables.  This parameter indicates the name of the table within the base.|True|String||
|Field name|The name of a specific field (column) in the table|True|String||
|Entity Field|Entity field to used for AirTable search (Can be Identifier or any other enrichment field). Default is Identifier|False|String|None|



##### JSON Results
```json
[  
  {  
    "id": "recCc2V3tpfStq4kh",  
    "fields": {  
      "Field_Name_1": "Field_Value_1",  
      "Field_Name_2": "Field_Value_2",  
      "Field_Name_3": "Field_Value_3"  
    },  
    "createdTime": "2019-06-27T06:22:10.000Z"  
  }  
]
```



#### AddOrUpdate

Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Base id|Base id|True|String|<Base id>|
|Table name|Table name|True|String|<Table name>|
|Field name|Field name|True|String|Field name|
|Json fields|Json fields|True|String|{}|



##### JSON Results
```json
{}
```



#### Update
Update specific fields  in a table
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Max records|The maximum records (rows) that will be affected by the action|True|String|100|
|Json fields|The fields (columns) and their value in a JSON format. |True|Content|{"Field_Name_1":"Value1"}|
|Field value|The value of a specific field in a table|True|String||
|Field name|The name of a specific field (column) in the table|True|String||
|Table name|A table stores similar (structured) data, and each base can have multiple tables.  This parameter indicates the name of the table within the base.|True|String||
|Base id|Base is a database in Airtable in which you store data.The base ID can be found in the URL of the API page of the base. |True|String||



##### JSON Results
```json

```



#### Delete All Records
Deletes all the records in a given table
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Base Id|Base is a database in Airtable in which you store data. The base ID can be found in the URL of the API page of the base.|True|String|<base_id>|
|Table name|Each Base can include multiple tables. The parameter indicates the name of the table within the base.|True|String|<table_name>|



##### JSON Results
```json
{}
```



#### Create
Create new records in a specific table
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Base id|Base is a database in Airtable in which you store data.The base ID can be found in the URL of the API page of the base. |True|String||
|Table name|A table stores similar (structured) data, and each base can have multiple tables.  This parameter indicates the name of the table within the base.|True|String||
|Json fields|The fields (columns) and their value in a JSON format. This action supports creation of multiple rows. |True|Content|[   {     "Field_Name_1": "Value1",     "Field_Name_2": "Value2",   },   {     "Field_Name_1": "Value1",     "Field_Name_2": "Value2",   } ]|



##### JSON Results
```json

```



#### Get All Records
Retrieves all the records from a given table
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Base Id|Base is a database in Airtable in which you store data. The base ID can be found in the URL of the API page of the base.|True|String|<base_id>|
|Table name|Each Base can include multiple tables. The parameter indicates the name of the table within the base.|True|String|<table_name>|
|Max Records|The maximum rows that will be affected by the action|True|String|5|
|Sort by|The column name you would like to sort by|False|String|<column_name>|
|Sort Direction|The direction of the records you would like to sort by - Descending\Ascending|True|List|Descending|



##### JSON Results
```json
{}
```



#### Delete
Delete specific fields (columns)  in a table
Timeout - 300 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Field value|The value of a specific field in a table|True|String||
|Field name|The name of a specific field (column) in the table|True|String||
|Table name|A table stores similar (structured) data, and each base can have multiple tables.  This parameter indicates the name of the table within the base.|True|String||
|Base id|Base is a database in Airtable in which you store data.The base ID can be found in the URL of the API page of the base. |True|String||
|Max records|The maximum records (rows) that will be affected by the action|True|String|100|



##### JSON Results
```json

```






## Jobs



## Connectors
#### AirTable Connector
The Connector ingests records from a given table in Airtable

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert name field|Determines the Alert name based on the airtable column name defined in the parameter|False|String|<alert_name_field>|
|Alert name prefix|The alert name prefix|False|String|<alert_name_prefix>|
|Alert type|Determines the Alert type based on the airtable column name defined in the parameter|True|String|<alert_type>|
|Api key|Your API Key can be found in your account overview under API|True|Password||
|Base id|Base is a database in Airtable in which you store data. The base ID can be found in the URL of the API page of the base.|True|String|<base_id>|
|DeviceProductField|The field name used to determine the device product|True|String|<none>|
|EventClassId|The field name used to determine the event name (sub-type)|True|String|<none>|
|Field name|The field name that you would like to search the value by|False|String|<field_name>|
|Field value|The value that you would like to search for under the relevant field name|False|String|<field_value>|
|Max records|The maximum rows in the table that will be affected by the action|True|String|300|
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|String|30|
|Table name|Each Base can include multiple tables. The parameter indicates the name of the table within the base.|True|String|<table_name>|




