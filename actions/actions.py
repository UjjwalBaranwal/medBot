# # from typing import Any, Text, Dict, List
# # from rasa_sdk import Action, Tracker
# # from rasa_sdk.executor import CollectingDispatcher

# # class ActionStoreUserInput(Action):
# #     def name(self) -> Text:
# #         return "action_store_user_input"

# #     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #         # Get user input from the last user message
# #         user_input = tracker.latest_message.get('text')

# #         # Set the user input in the 'user_input' slot
# #         return [SlotSet('user_input', user_input)]
# # class ActionUseUserInput(Action):
# #     def name(self) -> Text:
# #         return "action_use_user_input"

# #     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #         # Get the stored user input from the slot
# #         user_input = tracker.get_slot('user_input')

# #         # Use the user input for further processing
# #         dispatcher.utter_message(f"User input is: {user_input}")

# #         return []
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import SlotSet

# class UserDetailsForm(Action):
#     def name(self) -> Text:
#         return "user_details_form"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message("Sure, let's get started. What's your name?")
#         return [SlotSet("requested_slot", "name")]
# class UserDetailsForm(Action):
#     def name(self) -> Text:
#         return "user_details_form"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
#     ) -> List[Dict[Text, Any]]:
#         requested_slot = tracker.get_slot("requested_slot")

#         if requested_slot == "name":
#             user_name = tracker.latest_message.get("text")
#             dispatcher.utter_message(f"Thanks, {user_name}! What's your gender?")
#             return [SlotSet("name", user_name), SlotSet("requested_slot", "gender")]

#         elif requested_slot == "gender":
#             user_gender = tracker.latest_message.get("text")
#             dispatcher.utter_message(f"Got it! How old are you, {user_gender}?")
#             return [SlotSet("gender", user_gender), SlotSet("requested_slot", "age")]

#         elif requested_slot == "age":
#             user_age = tracker.latest_message.get("text")
#             dispatcher.utter_message(f"Great! We have your details: Name: {user_name}, Gender: {user_gender}, Age: {user_age}")
#             return [SlotSet("age", user_age), SlotSet("requested_slot", None)]

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker,FormValidationAction
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import SlotSet
from rasa_sdk.types import DomainDict

class ActionAskForName(Action):
    def name(self) -> Text:
        return "action_ask_for_name"

    # def run(
    #     self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    # ) -> List[Dict[Text, Any]]:
    #     dispatcher.utter_message("What is your name?")
    #     return [SlotSet("requested_slot", "user_name")]
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        requested_slot = tracker.get_slot("requested_slot")

        if requested_slot == "user_name":
            dispatcher.utter_message("What is your name?")
            return [SlotSet("requested_slot", "user_name")]

        elif requested_slot == "user_age":
            dispatcher.utter_message("How old are you?")
            return [SlotSet("requested_slot", "user_age")]

        # Handle additional slots if needed

        return []
# class ValidationSimplecheckupform(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_simple_checkup"
class ConvoRestart(Action):
    def name(self) -> Text:
        return "restart_convo"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [Restarted()]
