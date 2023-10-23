import streamlit as st
import pandas as pd
import xgboost as xgb

def main():
    html_temp = """ 
    <div style = "background-color:lightblue;padding:16px">
    <h2 style = "color:black;text-align:center;"> Drex Dang House Price Prediction Web App </h2>
    </div>
    """
    
    model = xgb.XGBRegressor()
    model.load_model('xgb_model.json')
    
    st.markdown(html_temp, unsafe_allow_html = True)
    st.write ('')
    st.write ('')
    
    st.markdown("##### Are You Planning To Sell Your House In California!?\n##### Let's  Evaluate The Price")
    
    p1 = st.number_input ('On What Longitude Is The House Situated?', -5000, -10, step = -10)
    
    p2 = st.number_input('On What Latitude Is The House Situated?', 10, 2000, step = 10)
    
    p3 = st.number_input ('What Is The Median Age Of The House?', 00, 1000, step = 5)
    
    p4 = st.number_input ('Total Number Of Rooms Contain In The House', 0, 1000000, step = 50)
    
    p5 = st.number_input ('Total Number Of Bedrooms Contain In The House', 1, 1000000, step = 5)
    
    p6 = st.number_input ('What Is The Total Population Of People Living In The House', 10, 5000, step = 10)
    
    p7 = st.number_input ('What Is The Total Households Living In The House', 1, 5000, step = 10)
    
    p8 = st.number_input ('What Is The Median Income Of A Person Living In The House', 1, 5000, step = 1)
    
    s1 = st.selectbox ('What Is The Closeness Or Otherwise Of A House To An Ocean?', ('NEAR BAY', 'H OCEAN', 'INLAND', 'NEAR OCEAN', 'ISLAND'))
    
    if s1 == 'NEAR BAY':
        p9 = 0
    elif s1 == 'H OCEAN':
        p9 = 1
    elif s1 == 'INLAND':
        p9 = 2
    elif s1 == 'NEAR OCEAN':
        p9 = 3
    elif s1 == 'ISLAND':
        p9 = 4
        
    df = pd.DataFrame({
    'longitude': p1,
    'latitude': p2,
    'housing_median_age': p3,
    'total_rooms': p4,
    'total_bedrooms': p5,
    'population': p6,
    'households': p7,
    'median_income': p8,
    'ocean_proximity': p9
},index=[0])
    try:
        if st.button ('Predict'):
            pred = model.predict(df)
            if pred > 0:
                st.balloons()
                st.success('You can sell your house for $ {:.2f} '.format (pred[0]))
            else:
                st.Warning ("You can't be able to sell this house")
    except:
        st.warning('Something Went Wrong,Try again')

if __name__ == '__main__':
    main()
        
     