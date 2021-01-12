# Field Maps Scripts
A set of Python scripts and notebooks to help configure maps and manage data for ArcGIS Field Maps.

### Features

#### Scripts
| Functionality                                                        | Script                                                                            
|----------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [Copy Form Between Maps ](readmes/copy_form_between_maps.md)               | [copy_form_between_maps.py](scripts/copy_form_between_maps.py)              |

#### Notebooks
- [Add Field Maps App ID to ArcGIS Enterprise](notebooks/Add%20Field%20Maps%20App%20ID%20to%20ArcGIS%20Enterprise.ipynb)
- [Bulk Update Maps for Use in Collector or Field Maps](notebooks/Bulk%20Update%20Maps%20for%20Use%20in%20Collector%20or%20Field%20Maps.ipynb)

### Requirements
- Python 3.6+
- ArcGIS API for Python 1.8.2+
- ArcGIS Field Maps (web and mobile applications)

### Instructions
This repository requires the ArcGIS API for Python version 1.8.2 or greater to run. We recommend setting up your
local environment via Anaconda.

1. [Install Anaconda](https://developers.arcgis.com/python/guide/install-and-set-up/)
2. Run `conda env create --file environment.yml` to create the virtual environment with the correct dependencies
3. Run `conda activate field-maps-scripts` to activate the environment
4. (Optional - dev only) Configure pre-commit to run flake8 linting on pushes
   * `pre-commit install --hook-type pre-push`

## Resources

 * [ArcGIS Field Maps](https://www.esri.com/arcgis-blog/products/apps/field-mobility/introducing-arcgis-field-maps/)
 * [ArcGIS API for Python](https://developers.arcgis.com/python)


## Issues

Find a bug or want to request a new feature?  Please let us know by submitting an issue.

## Contributing

Esri welcomes contributions from anyone and everyone.
Please see our [guidelines for contributing](https://github.com/esri/contributing).

## Licensing

Copyright 2020 Esri

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

A copy of the license is available in the repository's
[LICENSE](LICENSE) file.
