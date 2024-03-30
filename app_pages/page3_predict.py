import streamlit as st
import pandas as pd
from src.data_management import load_house_data, load_pkl_file, load_inherited_house_data
from src.machine_learning.predictive_analysis_ui import predict_sale_price
from datetime import date

# Adapted from van-essa and Code Institute's Churnometer walkthrough project

def page3_predict_body():
    # load predict sale_price files
    version = 'v1'
    sale_price_pipe = load_pkl_file(f"outputs/ml_pipeline/predict_sale_price/{version}/best_regressor_pipeline.pkl")
    sale_price_features = (pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
                                        .columns
                                        .to_list())

    st.write("### Predict House Sale Price")
    # display client's query and its data
    st.info(
        f"#### Business Requirement 2\n"
        f"* The client is interested in predicting the house sale price for "
        f"her 4 inherited houses, and any other house in Ames, Iowa. ")

    st.write("The table below represents the relevant data supplied by the client to predict Sale Price:")
	
    in_df = load_inherited_house_data()
    filtered_df = in_df[["OverallQual", "GrLivArea", "TotalBsmtSF", "GarageArea", "YearBuilt", "YearRemodAdd"]]	
		
    st.write(filtered_df)

    st.write("---")
    st.write("Enter the relevant values of the property below to generate a predicted Sale Price.\n"
			"Missing values are autofilled as Median.")
	
    # Generate Live Data
    X_live = DrawInputsWidgets()

    # Predict live data
    if st.button("Run Predictive Analysis"): 
        predict_sale_price(X_live, sale_price_features, sale_price_pipe)

    st.write("---")

    st.write("The predicted Sales Price for our client's houses are: \n\n "
			"* Property 1: $125,832 \n"
			"* Property 2: $142,449 \n"
			"* Property 3: $168,930 \n"
			"* Property 4: $128,318 ")
	
    st.write("---")


def DrawInputsWidgets():

	# Load the dataset
	df = load_house_data()
	percentageMin, percentageMax = 0.4, 2.0

    # Create input widgets for the most important features	
	col1, col2 = st.beta_columns(2)
	col3, col4 = st.beta_columns(2)
	col5, col6 = st.beta_columns(2)

	# Feed the ML pipeline by using these features
		
	# Create an empty DataFrame, to be displayed in the live data
	X_live = pd.DataFrame([], index=[0]) 
	
	# Then draw the widget based on the numerical or categorical type
	# and set initial values

	with col1:
		feature = "OverallQual"
		st_widget = st.number_input(
			label= feature,
			min_value= 0, 
			max_value= 10,
			value= int(df[feature].median()), 
            step = 1       
			)
	X_live[feature] = st_widget

	with col2:
		feature = "GrLivArea"
		st_widget = st.number_input(
			label= feature,
			min_value= int(df[feature].min()*percentageMin), 
			max_value= int(df[feature].max()*percentageMax),
			value= int(df[feature].median()), 
            step= 100
			)
	X_live[feature] = st_widget

	with col3:
		feature = "TotalBsmtSF"
		st_widget = st.number_input(
			label= feature,
			min_value= int(df[feature].min()*percentageMin), 
			max_value= int(df[feature].max()*percentageMax),
			value= int(df[feature].median()), 
            step= 50
			)
	X_live[feature] = st_widget

	with col4:
		feature = "GarageArea"
		st_widget = st.number_input(
			label= feature,
			min_value= int(df[feature].min()*percentageMin), 
			max_value= int(df[feature].max()*percentageMax),
			value= int(df[feature].median()), 
            step= 50
			)
	X_live[feature] = st_widget

	with col5:
		feature = "YearBuilt"
		st_widget = st.number_input(
			label= feature,
			min_value= int(df[feature].min()*percentageMin), 
			max_value= date.today().year,
			value= int(df[feature].median()), 
            step= 1
			)
	X_live[feature] = st_widget

	with col6:
		feature = "YearRemodAdd"
		st_widget = st.number_input(
			label= feature,
			min_value= int(df[feature].min()*percentageMin), 
			max_value= date.today().year,
			value= int(df[feature].median()), 
            step= 1
			)
	X_live[feature] = st_widget

	return X_live
                    

# The code above was copied from the Churnometer Project from Code Institute 
# with some adjustments