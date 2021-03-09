"""This file will need to use the DataManager,FlightSearch, FlightData,
 NotificationManager classes to achieve the program requirements."""

from day_39.flight_tracker.notification_manager import NotificationManager
from day_39.flight_tracker.flight_search import FlightSearch
from day_39.flight_tracker.data_manager import DataManager

data_manager = DataManager()
budget_data = data_manager.get_budget_data()
print(budget_data)
flight_search = FlightSearch()
msgs = []
for budget in budget_data:
    details: str = flight_search.get_budget_flights(fly_to=budget['iata'], budget=budget['budget'])
    if details is None:
        continue
    msgs.append(details)

if len(msgs) > 0:
    notification = NotificationManager()
    mail = (50*'-' + '\n\n').join(msgs)
    notification.send_mail_notification(msg=mail)

print(msgs)
