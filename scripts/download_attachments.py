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

    This sample downloads attachments to a local machine from a feature layer or table based on user input
"""
import argparse
import logging
import logging.handlers
import traceback
import sys
from arcgis.gis import GIS
from arcgis.features import FeatureLayer


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

    if args.item_id is None and args.layer_url is None:
        raise Exception("Must pass either item id or layer url")
    if args.item_id:
        item = gis.content.get(args.item_id)
        if item:
            layers = item.layers + item.tables
        else:
            raise Exception("Bad item id, please check again")
    else:
        layers = [FeatureLayer(url=args.layer_url, gis=gis)]

    logger.info("Downloading attachments")

    for layer in layers:
        try:
            found_attach = layer.attachments.search(args.where)
            for attach in found_attach:
                try:
                    layer.attachments.download(attachment_id=attach['ID'], oid=attach['PARENTOBJECTID'], save_path=args.out_folder)
                except Exception:
                    try:
                        print(f"Failed to download attachment {attach['NAME']} from object id {attach['PARENTOBJECTID']}'")
                    except Exception as e:
                        print(e)
        except Exception:
            pass
    logger.info("Completed successfully!")


if __name__ == "__main__":
    # Get all of the commandline arguments
    parser = argparse.ArgumentParser("Download attachments from an ArcGIS hosted feature layer")
    parser.add_argument('-u', dest='username', help="The username to authenticate with", required=True)
    parser.add_argument('-p', dest='password', help="The password to authenticate with", required=True)
    parser.add_argument('-org', dest='org_url', help="The url of the org/portal to use", required=True)
    # Parameters for workforce
    parser.add_argument('-item-id', dest='item_id', help="The item ID with the layer or table whose attachments you'd like to download")
    parser.add_argument('-layer-url', dest='layer_url', help="The feature layer url where you'd like to download attachments")
    parser.add_argument('-out-folder', dest='out_folder', help="The path on your computer where you'd like to direct the attachments. If not passed, "
                                                               "will download to present working directory", required=False, default="./attachments")
    parser.add_argument('-where', dest='where', help="If not passed, will download all attachments.", default='1=1')
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
