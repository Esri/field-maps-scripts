## Download Attachments from Feature Layer

A user may want to download attachments that have been collected by their mobile workforce in ArcGIS Field Maps or ArcGIS Workforce. 

This script allows users to download (either all or a subset) attachments from a particular feature layer or item to a folder on their computer.

You can either specify an item id or feature layer url to use for this particular script.

Supports Python 3.6+

----

In addition to the authentication arguments, the script specific arguments are as follows:

- -item-id (Optional) - The item ID with the layer or table whose attachments you'd like to download. If an item has multiple layers / tables, it will attempt to download attachments for all layers / tables
- -layer-url (Optional) - The feature layer url whose attachments you'd like to download
- -out-folder (Optional)- The path on your computer where you'd like to direct the attachments. If not passed, will download to present working directory to a folder called "attachments"
- -where (Optional) - The where clause that defines which features' attachments you'd like to download. If not passed, will download all attachments.
- -log-file - The log file to use for logging messages (Optional)

Example 1:
```bash
python download_attachments.py -org https://arcgis.com -u username -p password -item-id d2295f09f97945c9b447417ba27bcb38 -where "status = 'Completed'" -out-folder "/Users/johndoe/Documents/my-attachments"
```

Example 2:
```bash
python download_attachments.py -org https://arcgis.com -u username -p password -layer-url https://services.arcgis.com/US6xjA1Nd8bW1aoA/arcgis/rest/services/workforce_e6c540083fec4b46b193bb040a556d41/FeatureServer/0
```

