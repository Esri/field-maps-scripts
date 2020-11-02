# -*- coding: UTF-8 -*-
"""
   Copyright 2020 Esri

   Licensed under the Apache License, Version 2.0 (the "License");

   you may not use this file except in compliance with the License.

   You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software

   distributed under the License is distributed on an "AS IS" BASIS,

   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

   See the License for the specific language governing permissions and

   limitations under the License.​

    This sample copies a form from one map to another map if a matching layer is found
"""
import argparse
import logging
import logging.handlers
import traceback
import sys
from arcgis.gis import GIS


def initialize_logging(log_file=None):
    """
 Setup logging
 :param log_file: (string) The file to log to
 :return: (Logger) a logging instance
 """
    # initialize logging
    formatter = logging.Formatter(
        "[%(asctime)s] [%(filename)30s:%(lineno)4s - %(funcName)30s()][%(threadName)5s] [%(name)10.10s] [%(levelname)8s] %(message)s")
    # Grab the root logger
    logger = logging.getLogger()
    # Set the root logger logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    logger.setLevel(logging.DEBUG)
    # Create a handler to print to the console
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(formatter)
    sh.setLevel(logging.INFO)
    # Create a handler to log to the specified file
    if log_file:
        rh = logging.handlers.RotatingFileHandler(log_file, mode='a', maxBytes=10485760)
        rh.setFormatter(formatter)
        rh.setLevel(logging.DEBUG)
        logger.addHandler(rh)
    # Add the handlers to the root logger
    logger.addHandler(sh)
    return logger


def replace_form(source_objects, dest_objects, overwrite=False):
    modified = False
    for s_layer in source_objects:
        if "formInfo" in s_layer:
            # find matching layer based on url
            for d_layer in dest_objects:
                if d_layer.get("url", None) == s_layer.get("url", None):
                    # Check it's the correct layer or that no layer name was passed
                    if args.layer_name is None or args.layer_name == d_layer.get("title", None):
                        # Check overwrite was provided or there's no existing form
                        if overwrite or not d_layer.get("formInfo", None):
                            d_layer["formInfo"] = s_layer["formInfo"]
                            modified = True
                        else:
                            sys.exit("Existing form is detected. Pass --overwrite to the script to overwrite the form")
    return modified


def main(arguments):
    # initialize logger
    logger = initialize_logging(arguments.log_file)

    # Create the GIS
    logger.info("Authenticating...")

    # First step is to get authenticate and get a valid token
    gis = GIS(arguments.org_url,
              username=arguments.username,
              password=arguments.password,
              verify_cert=not arguments.skip_ssl_verification)

    # Get the maps
    source_item = gis.content.get(arguments.source)
    dest_item = gis.content.get(arguments.dest)
    if source_item is None or dest_item is None:
        raise ValueError("Your source or destination map was not found! Please check your item ids again")
    if source_item.type.lower() != "web map" or dest_item.type.lower() != "web map":
        raise ValueError("One of the items you passed is not a webmap. Please check again.")

    # Iterate through operational layers
    logger.info("Iterating through layers")
    source_layers = source_item.get_data().get("operationalLayers", [])
    source_tables = source_item.get_data().get("tables", [])
    dest_data = dest_item.get_data()
    dest_layers = dest_data.get("operationalLayers", [])
    dest_tables = dest_data.get("tables", [])

    # Swizzle in new form
    forms_modified = replace_form(source_layers, dest_layers, args.overwrite)
    tables_modified = replace_form(source_tables, dest_tables, args.overwrite)

    # Saving form
    if forms_modified or tables_modified:
        logger.info("Saving form(s) to destination map")
        dest_item.update(data=dest_data)
    else:
        logger.info("No matching layers were found! Your destination map was not modified")
    logger.info("Completed!")


if __name__ == "__main__":
    # Get all of the commandline arguments
    parser = argparse.ArgumentParser("Copy the same form between the same layer in two different maps")
    parser.add_argument('-u', dest='username', help="The username to authenticate with", required=True)
    parser.add_argument('-p', dest='password', help="The password to authenticate with", required=True)
    parser.add_argument('-org', dest='org_url', help="The url of the org/portal to use", required=True)
    # Parameters for workforce
    parser.add_argument('-source-map-id', dest='source', help="The item id of the map you want to copy the form(s) from",
                        required=True)
    parser.add_argument('-dest-map-id', dest='dest', help="The item id of the map you want to copy the form(s) to", required=True)
    parser.add_argument('-layer-name', dest='layer_name', help="An optional specific layer you want to copy. If this is not provided, "
                                                               "all matching layers will have their forms copied", required=False)
    parser.add_argument('--overwrite', dest='overwrite', action='store_true', help="Provide this parameter if you would like to overwrite an existing form")
    parser.add_argument('--skip-ssl-verification',
                        dest='skip_ssl_verification',
                        action='store_true',
                        help="Verify the SSL Certificate of the server")
    parser.add_argument('-log-file', dest='log_file', help="The log file to write to")
    args = parser.parse_args()
    try:
        main(args)
    except Exception as e:
        logging.getLogger().critical("Exception detected, script exiting")
        logging.getLogger().critical(e)
        logging.getLogger().critical(traceback.format_exc().replace("\n", " | "))
