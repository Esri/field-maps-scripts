## Copy Form Between Maps

This script allows a user to copy a smart form between different maps to avoid needing to create forms multiple times.
You can provide the item id (found in the URL when viewing that webmap in the Portal or Field Maps) of both the origin
map where the form has been created and the destination map where you would like the form copied to. 

The script will then search for the same layer being present in both maps (as you must use the same feature service in 
both maps for this script to work) and, if a matching layer is found, copy the formInfo object from the source map's 
operational layer to the destination map's operational layer. You should then be able to use your smart form in the
destination map.

By default, this script will copy forms for any matching layers found (so for example, if the same two layers are in the
source and destination maps, both layers will see its form copied over from the source to the destination map. Note that
any form for those matching layers on your destination map will get overwritten. If you'd only like to copy the form
for one map, simply provide the name of that layer as a parameter to the script.

**This script requires the logged in user to have editing privileges on both maps**

Supports Python 3.6+

----

In addition to the authentication arguments, the script specific arguments are as follows:

- -source-item-id - The item ID of the map where your form(s) live that you'd like to copy to the same layer in a different map
- -dest-item-id - The item ID of the map where you want your form to be copied to
- -layer-name - If you'd like to restrict copying over forms to only certain layers in each map, provide the title of the layer whose form you'd like to copy here (Optional)
- --overwrite - If you'd like to overwrite existing forms in the destination map using this script, please pass this parameter
- -log-file - The log file to use for logging messages (Optional)

```bash
python copy_form_between_maps.py -org https://arcgis.com -u username -p password -source-map-id d2295f09f97945c9b447417ba27bcb38 -dest-map-id 4392801d9c8341ce9038614ff240e877 -layer-name "Inspections" --overwrite
```
