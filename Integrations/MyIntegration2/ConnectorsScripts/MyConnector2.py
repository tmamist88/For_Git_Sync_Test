from SiemplifyConnectors import SiemplifyConnectorExecution
from SiemplifyConnectorsDataModel import AlertInfo
from SiemplifyUtils import output_handler, unix_now
from random import randrange

import uuid
import sys

#==============================================================================
# This is a Connector Template + mock generator. This file objective is to demonstrate how to build a connector, and exmplain the objective of each field.
# All the data generated here, is MOCK data. Enjoy.
#==============================================================================

CONNECTOR_NAME = "ConnectorTemplate"
VENDOR = "DummyVendor"
PRODUCT = "DummyProduct"
RULE_GENERATOR_EXAMPLE = "Example_Rule_1"
RANDOM_ALERT_COUNT_MAX = 3
RANDOM_EVENT_COUNT_PER_ALERT_MAX = 5

@output_handler
def main(is_test_run):
    alerts = [] # The main output of each connector run
    siemplify = SiemplifyConnectorExecution() # Siemplify main SDK wrapper
    siemplify.script_name = CONNECTOR_NAME

    if (is_test_run):
        siemplify.LOGGER.info("***** This is an \"IDE Play Button\"\\\"Run Connector once\" test run ******")

    siemplify.LOGGER.info("==================== Main - Param Init ====================")

    param_a = siemplify.extract_connector_param("Param A", default_value=None, input_type=int, is_mandatory=False, print_value=True)

    siemplify.LOGGER.info("------------------- Main - Started -------------------")

    # ... CUSTOM LOGIC HERE ....
    # In this template example, we create a random number of dummy alerts:
    for alert_id in [str(uuid.uuid4()) for i in range(randrange(RANDOM_ALERT_COUNT_MAX+1))]:
        try:
            # ... CUSTOM LOGIC HERE ....
            # ... CUSTOM LOGIC HERE ....
            alert_example = fetch_alert(siemplify, alert_id)
            # ... CUSTOM LOGIC HERE ....
            # ... CUSTOM LOGIC HERE ....

            if alert_example:
                alerts.append(alert_example)
                siemplify.LOGGER.info("Added Alert {} to package results".format(alert_id))

        except Exception as e:
            siemplify.LOGGER.error("Failed to process alert {}".format(alert_id), alert_id=alert_id)
            siemplify.LOGGER.exception(e)

    siemplify.LOGGER.info("------------------- Main - Finished -------------------")
    siemplify.return_package(alerts)


def fetch_alert(siemplify, alert_id):
    """Returns an alert, which is an aggregation of basic events. (ie: Arcsight's correlation, QRadar's Offense)"""
    siemplify.LOGGER.info("-------------- Started processing Alert {}".format(alert_id), alert_id=alert_id)

    alert_info = AlertInfo()

    # ----------------------------- Alert Fields initilization START -----------------------------
    # ... Replace this DUMMY VALUES !!! ...

    # Each alert_info has a unique key composed of alert_info.name+alert_info.display_id. This key is used to validate data is digested only once by the Siemplify System - to avoid duplicates.
    # If an alert_info has a uniqe_key that has already been digested, it will be ignored.
    # The uniqueness must be persistent, even after server restart\ refetching of the same alert, multiple runs of the same API queries, etc.
    alert_info.display_id = alert_id
    alert_info.ticket_id = alert_id  # In default, ticket_id = display_id. But, if for some reason the external alert id, is different then the composite's key display_id, you can save the original external alert id in this "ticket_id" field.
    alert_info.name = "Random Alert Name " + str(uuid.uuid4())
    alert_info.rule_generator = RULE_GENERATOR_EXAMPLE  # Describes the name of the siem's rule, that caused the aggregation of the alert.
    alert_info.start_time = unix_now()  # Times should be saved in UnixTime. You may use SiemplifyUtils.convert_datetime_to_unix_time, or SiemplifyUtils.convert_string_to_datetime
    alert_info.end_time = unix_now() # Times should be saved in UnixTime. You may use SiemplifyUtils.convert_datetime_to_unix_time, or SiemplifyUtils.convert_string_to_datetime
    alert_info.priority = 60  # Informative = -1,Low = 40,Medium = 60,High = 80,Critical = 100.
    alert_info.device_vendor = VENDOR  # This field, may be fetched from the Original Alert. If you build this alert manualy, Describe the source vendor of the data. (ie: Microsoft, Mcafee)
    alert_info.device_product = PRODUCT  # This field, may be fetched from the Original Alert. If you build this alert manualy, Describe the source product of the data. (ie: ActiveDirectory, AntiVirus)
    alert_info.environment = siemplify.context.connector_info.environment # This field, gets the Environment of the specific connector execution.
    # ----------------------------- Alert Fields initilization END -----------------------------

    siemplify.LOGGER.info("---------- Events fetching started for alert  {}".format(alert_id))

    # ... CUSTOM LOGIC HERE ....
    # In this template example, for each alert, we create a random number of dummy events:
    for event_id in [str(uuid.uuid4()) for i in range(randrange(RANDOM_EVENT_COUNT_PER_ALERT_MAX+1))]:
        try:

            # ... CUSTOM LOGIC HERE ....
            dummy_event = fetch_event(siemplify, alert_id, event_id)
            # ... CUSTOM LOGIC HERE ....

            if dummy_event:
                alert_info.events.append(dummy_event)
                siemplify.LOGGER.info("Added Event {} to Alert {}".format(event_id, alert_id))

        except Exception as e:
            siemplify.LOGGER.error("Failed to process event {}".format(event_id), alert_id=alert_id)
            siemplify.LOGGER.exception(e)

    siemplify.LOGGER.info("---------- Events fetching finished for alert {}".format(alert_id))

    siemplify.LOGGER.info("-------------- Finished processing Alert {}".format(alert_id), alert_id=alert_id)
    return alert_info


def fetch_event(siemplify, alert_id, event_id):
    siemplify.LOGGER.info("--- Started processing Event:  alert_id: {} | event_id: {}".format(alert_id, event_id))
    event = {}

    # ----------- Mandatory Fields ---------------
    # A valid event must have a "Start Time", "End Time", "Name", and "Device Product". Their name is not important (What ever it is, it will be mapped).
    # ie: "Start Time" may be called "Start Time", "StartTime", "start_time", "johnDoeStartTime"
    event["StartTime"] = unix_now() # Times should be saved in UnixTime. You may use SiemplifyUtils.convert_datetime_to_unix_time, or SiemplifyUtils.convert_string_to_datetime
    event["EndTime"] = unix_now() # Times should be saved in UnixTime. You may use SiemplifyUtils.convert_datetime_to_unix_time, or SiemplifyUtils.convert_string_to_datetime
    event["name"] = "RandomEventName " + str(uuid.uuid4())
    event["device_product"] = "RandomProductExample{}".format(randrange(3))  # ie: "device_product" is the field name in arcsight that describes the product the event originated from.
    # ----------------------------- ---------------

     # usually, the most intresting fields are (again, their precise name, may vary between siems.
    # You are not expected to fill them yourself, just pass them along from the siem. Since this is a dummy generator, We create them manaualy with made up name (PascalCase\CcmelCase doesn't matter)
    event["SourceHostName"] = "DummyHostSrc"
    event["DestinationHostName"] = "DummyHostDest"
    event["SourceAddress"] = "10.0.0."+str(randrange(254))
    event["DestinationAddress"] = "55.44.33."+str(randrange(254))
    # event["SourceUserName"] =
    # event["DestinationUserName"] =
    # event["FileName"] =

    siemplify.LOGGER.info("--- Finished processing Event: alert_id: {} | event_id: {}".format(alert_id, event_id))

    return event


if __name__ == "__main__":
    # Connectors are run in iterations. The interval is configurable from the ConnectorsScreen UI.
    is_test_run = not (len(sys.argv) < 2 or sys.argv[1] == 'True')
    main(is_test_run)