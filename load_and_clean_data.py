import pandas as pd 

def load_and_transform():
    df = pd.read_csv(('./data/paris_house.csv'))
    df = df[['squareMeters', 'numberOfRooms', 'hasYard', 'hasPool', 'floors',
         #'cityCode', 'cityPartRange', 
        'numPrevOwners', 'made', 
         #'isNewBuilt',
        'hasStormProtector', 'basement', 'attic', 'garage', 
         #'hasStorageRoom',
         #'hasGuestRoom', 
         'price']].copy()
    return df