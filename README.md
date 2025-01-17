# Field Maps Scripts

A set of Python scripts and notebooks to help configure maps and manage data for ArcGIS Field Maps.

## Features

### Scripts

| Functionality                                                        | Script
|----------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [Copy Form Between Maps](readmes/copy_form_between_maps.md)               | [copy_form_between_maps.py](scripts/copy_form_between_maps.py)              |
| [Download Attachments from Feature Layer](readmes/download_attachments.md) | [download_attachments.py](scripts/download_attachments.py)

### Notebooks

- [Add Field Maps App ID to ArcGIS Enterprise](notebooks/Add%20Field%20Maps%20App%20ID%20to%20ArcGIS%20Enterprise.ipynb)
- [Bulk Update Maps for Use in Collector or Field Maps](notebooks/Bulk%20Update%20Maps%20for%20Use%20in%20Collector%20or%20Field%20Maps.ipynb)
- [Field Apps Deployment Using Python](notebooks/Field%20Apps%20Deployment%20Using%20Python.ipynb)
- [Generate PDF Report](notebooks/Generate%20PDF%20Report/Generate%20PDF%20Report.ipynb)
- [Add GPS Metadata Fields (Pro)](notebooks/Add%20GPS%20Metadata%20Fields.ipynb)
- [Add Offset Metadata Fields (Pro)](notebooks/Add%20Offset%20Metadata%20Fields.ipynb)
- [Add GPS Metadata Fields](notebooks/Add%20GPS%20Metadata%20Fields_FS.ipynb)
- [Configure Search](notebooks/Configure%20Search.ipynb)
- [Location Sharing Status](notebooks/Location%20Sharing%20Status.ipynb)
- [Create Offline Areas from Feature Layer](notebooks/Create%20Offline%20Areas%20from%20Feature%20Layer.ipynb)
- [Manage Map Areas with Group and Index](notebooks/Manage%20Map%20Areas%20with%20Group%20and%20Index.ipynb)
- [Watermark photo attachments with Exif data](notebooks/Watermark%20photo%20attachments%20with%20Exif%20data.ipynb)

### Requirements

- ArcGIS API for Python 2.3.1
- Python 3.9.x to 3.11.x is required to use the ArcGIS API for Python 2.3.1.
- ArcGIS Field Maps (web and mobile applications)
- ArcGIS Pro 2.9+ (Add `GPS Metadata Fields (Pro)` and `Add Offset Metadata Fields (Pro)` only)

### Instructions

This repository recommends the ArcGIS API for Python version 2.3.1. We recommend setting up your
local environment via Anaconda.

1. [Install Anaconda](https://developers.arcgis.com/python/guide/install-and-set-up/)
2. Run `conda env create --file environment.yml` to create the virtual environment with the correct dependencies
3. Run `conda activate field-maps-scripts` to activate the environment
4. (Optional - dev only) Configure pre-commit to run flake8 linting on pushes
   - `pre-commit install --hook-type pre-push`

## Resources

- [ArcGIS Field Maps](https://www.esri.com/arcgis-blog/products/apps/field-mobility/introducing-arcgis-field-maps/)
- [ArcGIS API for Python](https://developers.arcgis.com/python)

## Issues

Although we do our best to ensure these scripts and notebooks work as expected, they are provided as is and there is no official support.

If you find a bug, please let us know by submitting an issue.

## Contributing

Esri welcomes contributions from anyone and everyone.
Please see our [guidelines for contributing](https://github.com/esri/contributing).

## Licensing

Copyright 2022 Esri

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

A copy of the license is available in the repository's
[LICENSE](LICENSE) file.
