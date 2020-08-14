# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from requests.auth import HTTPBasicAuth
import requests
import json
import urllib3
import urllib.parse
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class GetAction(Action):
    def name(self) -> Text:
        return "action_get_incidents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = "https://coe.servicedesk.inspirisys.org:8090/api/v3/requests?TECHNICIAN_KEY=B21C907A-C903-465E-8A8A-BB8C4D63D549"
        print("Hello........")
        headers = {"Content-Type": "application/json"}
        req = requests.get(url, data=json.dumps({"list_info": {"row_count": 20, "start_index": 1,
                                                               "sort_field": "subject", "sort_order": "asc",
                                                               "get_total_count": True,
                                                               "search_fields": {"subject": "", "priority.name": ""}}}),
                           headers=headers, verify=False)
        print(req.content)
        print(req.status_code)
        dispatcher.utter_message(req.content)
        return []


class PrinterIssue(Action):
    def name(self) -> Text:
        return "action_printer_incidents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        with open('E:\\ANAKAGE_TEST\\InputJSON\\Printerissue.json', 'r') as myfile:
            data = myfile.read()
            print(data)
            datavalue = urllib.parse.quote(data)
            url = "https://coe.servicedesk.inspirisys.org:8090/api/v3/requests?TECHNICIAN_KEY=B21C907A-C903-465E-8A8A-BB8C4D63D549&input_data="+datavalue
            headers = {"Content-Type": "application/json"}
            print(url)
            print("PrinterIssue")
            req = requests.post(url, headers=headers, verify=False)
            print(req.status_code)
            dispatcher.utter_message(req.status_code)
            return []


class AdobeReader(Action):
    def name(self) -> Text:
        return "action_adobe_incidents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        with open('E:\\ANAKAGE_TEST\\InputJSON\\AdobeReaderExplorer.json', 'r') as myfile:
            data = myfile.read()
            print(data)
            datavalue = urllib.parse.quote(data)
            url = "https://coe.servicedesk.inspirisys.org:8090/api/v3/requests?TECHNICIAN_KEY=B21C907A-C903-465E-8A8A-BB8C4D63D549&input_data="+datavalue
            headers = {"Content-Type": "application/json"}
            print(url)
            print("AdobeReader")
            req = requests.post(url, headers=headers, verify=False)
            print(req.status_code)
            dispatcher.utter_message(req.status_code)
            return []


class ArchiveFile(Action):
    def name(self) -> Text:
        return "action_archive_incidents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        with open('E:\\ANAKAGE_TEST\\InputJSON\\ArchiveFile.json', 'r') as myfile:
            data = myfile.read()
            print(data)
            datavalue = urllib.parse.quote(data)
            url = "https://coe.servicedesk.inspirisys.org:8090/api/v3/requests?TECHNICIAN_KEY=B21C907A-C903-465E-8A8A-BB8C4D63D549&input_data="+datavalue
            print(url)
            headers = {"Content-Type": "application/json"}
            print("ArchiveFile")
            req = requests.post(url, headers=headers, verify=False)
            print(req.status_code)
            dispatcher.utter_message(req.status_code)
            return []


class CleanTemp(Action):
    def name(self) -> Text:
        return "action_cleantemp_incidents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        with open('E:\\ANAKAGE_TEST\\InputJSON\\CleanTempMobility.json', 'r') as myfile:
            data = myfile.read()
            print(data)
            datavalue = urllib.parse.quote(data)
            url = "https://coe.servicedesk.inspirisys.org:8090/api/v3/requests?TECHNICIAN_KEY=B21C907A-C903-465E-8A8A-BB8C4D63D549&input_data="+datavalue
            headers = {"Content-Type": "application/json"}
            print(url)
            print("CleanTemp")
            req = requests.post(url, headers=headers, verify=False)
            print(req.status_code)
            dispatcher.utter_message(req.status_code)
            return []


class CleanUpExplorer(Action):
    def name(self) -> Text:
        return "action_cleanup_incidents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        with open('E:\\ANAKAGE_TEST\\InputJSON\\CleanUpExplorer.json', 'r') as myfile:
            data = myfile.read()
            print(data)
            datavalue = urllib.parse.quote(data)
            url = "https://coe.servicedesk.inspirisys.org:8090/api/v3/requests?TECHNICIAN_KEY=B21C907A-C903-465E-8A8A-BB8C4D63D549&input_data="+datavalue
            headers = {"Content-Type": "application/json"}
            print(url)
            print("CleanUp")
            req = requests.post(url, headers=headers, verify=False)
            print(req.status_code)
            dispatcher.utter_message(req.status_code)
            return []


class Popup(Action):
    def name(self) -> Text:
        return "action_popup_incidents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        with open('E:\\ANAKAGE_TEST\\InputJSON\\PopUpExplorer.json', 'r') as myfile:
            data = myfile.read()
            print(data)
            datavalue = urllib.parse.quote(data)
            url = "https://coe.servicedesk.inspirisys.org:8090/api/v3/requests?TECHNICIAN_KEY=B21C907A-C903-465E-8A8A-BB8C4D63D549&input_data="+datavalue
            headers = {"Content-Type": "application/json"}
            print(url)
            print("PopUpExplorer")
            req = requests.post(url, headers=headers, verify=False)
            print(req.status_code)
            dispatcher.utter_message(req.status_code)
            return []


class RecoverEmail(Action):
    def name(self) -> Text:
        return "action_recoveremail_incidents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        with open('E:\\ANAKAGE_TEST\\InputJSON\\RecoverEmail.json', 'r') as myfile:
            data = myfile.read()
            print(data)
            datavalue = urllib.parse.quote(data)
            url = "https://coe.servicedesk.inspirisys.org:8090/api/v3/requests?TECHNICIAN_KEY=B21C907A-C903-465E-8A8A-BB8C4D63D549&input_data="+datavalue
            headers = {"Content-Type": "application/json"}
            print(url)
            print("RecoverEmail")
            req = requests.post(url, headers=headers, verify=False)
            print(req.status_code)
            dispatcher.utter_message(req.status_code)
            return []

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

