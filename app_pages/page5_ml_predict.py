import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_house_data, load_pkl_file
from src.machine_learning.evaluate_regression import regression_performance


def page5_ml_predict_body():

    # Load sale price pipeline files
    version = 'v1'
    sale_price_pipe = load_pkl_file(f"outputs/ml_pipeline/predict_sale_price/{version}/best_regressor_pipeline.pkl")
    sale_price_features = pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
    sale_price_importance = plt.imread(f"outputs/ml_pipeline/predict_sale_price/{version}/features_importance.png")
    X_train = pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
    X_test = pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/X_test.csv")
    y_train =  pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/y_train.csv")
    y_test =  pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/y_test.csv")

    
    st.write("### ML Pipeline: Predict Sale Price")
    # Display pipeline training summary conclusions
    st.info(
        f"* A **Regressor** model was chosen to predict the **`Sale Price`** for the houses. \n \n"
        f"* The **ExtraTreesRegressor** model returned the best initial R2 score of 0.82. \n"
        f"* The client has requested a model with at least an R2 of 0.75. \n"
        f"* A **PCA Regressor** was added to the model but this resulted in a very "
        f"high R2 for the train set but saw a marked decrease in the performance of "
        f"the test set of data which means it was overfitting and not appropriate. \n"
        f"* The data for the pipeline was tuned by taking several steps "
        f"to clean and engineer it. The highest performing steps "
        f"and hyperparameters on the most critical features "
        f"are listed below: ")

    # Show pipeline steps
    st.write("#### ML Pipeline To Predict Sale Price")
    
    st.info(
        f"* Numerical Transformations and addressing outliers maximum values: \n \n")
    st.code(sale_price_pipe)

    # Show best features
    st.write("* The Features The Model Was Trained And Their Importance")
    st.write(X_train.columns.to_list())
    st.image(sale_price_importance)

    # evaluate performance on both sets
    
    st.write("### Pipeline Performance")
    regression_performance(X_train=X_train, y_train=y_train,
                        X_test=X_test, y_test=y_test,
                        pipeline=sale_price_pipe)

    st.success(
        f"* The resulting R2 value for our model on unseen data is 0.84 and satisfies our clients request.")


# The code above was copied from the Churnometer Project from Code Institute 
# with some adjustments