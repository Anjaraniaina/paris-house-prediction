from sklearn.tree import DecisionTreeRegressor
import load_and_clean_data

def build_model():
    df = load_and_clean_data.load_and_transform()
    y = df.price
    features = ['squareMeters', 'numberOfRooms', 'hasYard', 'hasPool', 'floors',
       'numPrevOwners', 'made', 'hasStormProtector', 
       'basement', 'attic','garage']
    X = df[features]
    model = DecisionTreeRegressor(random_state = 1)
    model.fit(X, y)
    return model

