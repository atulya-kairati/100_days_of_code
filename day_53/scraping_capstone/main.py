from day_53.scraping_capstone.get_data import GetRoomData
from day_53.scraping_capstone.write_data import FormFiller
from pprint import pprint

room_data = GetRoomData()
data = room_data.get_data()
pprint(data)
form_filler = FormFiller()
form_filler.fill_form(data)

