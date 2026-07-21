import pandas as pd

inspiration = {
    'name': ['Ada Lovelace', 'Alan Turing', 'Grace Hopper', 'Margaret Hamilton'],
    'age': [36, 41, 85, 83],
    'phone_number': ['123-456-7890', '987-654-3210', '555-555-5555', '111-222-3333'],
    'astrological_signs': ['Taurus', 'Scorpio', 'Virgo', 'Libra']
}

contacts = pd.DataFrame(inspiration)

print(contacts)