# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import Restarted
from rasa_sdk.events import SlotSet
from .api_hotel import book_hotel




class ActionHotel(Action):
    '''Book Hotel'''
    def name(self) -> Text:
        return "action_hotel"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        try:
            city_name = tracker.get_slot("city_name")
            country_name = tracker.get_slot("country_name")
            data = book_hotel(city_name,country_name)
            response = f"The Hotel name is '{data['name']}'. This hotel rating is '{data['rating']}'. If you want to book this hotel please follow the link - \n'{data['link']}'"
            dispatcher.utter_message(response)

        except:
            dispatcher.utter_message("Please give me right information.")

        return [SlotSet('city_name',city_name),SlotSet('country_name',country_name)]


class ActionClear(Action):
    '''Reset All'''
    def name(self) -> Text:
        return "action_clear"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [AllSlotsReset()]

