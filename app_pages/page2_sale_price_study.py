import streamlit as st
from src.data_management import load_house_data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")



def page2_sale_price_study_body():

    
    # load data
    df = load_house_data()

    # hard copied from churned customer study notebook
    vars_to_study = ['OverallQual', 'GrLivArea', 'YearBuilt', '1stFlrSF', 'GarageArea']

    st.write("### House Sale Price Study")
    st.info(
        f"#### Business Requirement 1\n"
        f"* The client is interested in discovering how the house attributes "
        f"correlate with the sale price."
    )

    # inspect data
    if st.checkbox("Inspect Customer Base"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns."
            f"You can see the first 10 rows displayed below:")
        
        st.write(df.head(10))

    st.write("---")


    # Correlation Study Summary
    """Correlation Study Findings"""
    st.write(
        f"* Correlation studies were conducted to better understand how "
        f"the variables are correlated to  **`SalePrice`**. \n\n"
        f"* The most correlated variables to **`SalePrice`** are: **{vars_to_study}**"
    )

    # Text based on "02 - Sale Price Study" Notebook - "Conclusions and Next steps" section
    st.info(
        f"* Sale Price for a house increases with an increase in ground floor"
        f"living area ('GrLivArea') as well as first floor living area ('1stFlrSF.) \n"
        f"* Sale Price increases with the overall quality of the materials and "
        f"finishing ('OverallQual') \n"
        f"* The year the house ('YearBuilt') and garage ('GarageYrBlt') were built "
        f"appears to increase the Sale Price. \n"
        f"* It does not appear that having your garage retrofitted has any notable effect "
        f"on Sales Price. There is an overall indication however, that 'newer' houses "
        f"built more recently result in a higher Sales Price. \n"
        f"* Finally, houses with larger basements ('TotalBsmtSF') and garages ('GarageArea') "
        f"are generally shown to increase the Sale Price"
    )

    # Individual plots per variable
    if st.checkbox("Sale Price Correlation Per Variable"):
        df_eda = df.filter(vars_to_study + ['SalePrice'])
        target_var = 'SalePrice'
        regr_level_per_variable(df_eda, target_var)

    if st.checkbox("Overall Quality Correlation Against Year Built"):
        quality_to_study = ['SalePrice', 'YearBuilt']
        df_eda = df.filter(quality_to_study + ['OverallQual'])
        target_var = 'OverallQual'
        regr_level_per_variable(df_eda, target_var)

    if st.checkbox("Houses Of Similar Area Colored by Overall Quality"):
        fig, axes = plt.subplots(figsize=(8, 5))
        fig = sns.lmplot(data=df, x="GrLivArea", y="SalePrice", ci=None, hue='OverallQual')
        plt.title(f"Sale Price by General Living Area and OverallQual", fontsize=20,y=1.05)
        st.pyplot(fig) 


def regr_level_per_variable(df_eda, target_var):
    
    for col in df_eda.drop([target_var], axis=1).columns.to_list():
            plot_numerical(df_eda, col, target_var)


def plot_numerical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(8, 5))
    fig = sns.lmplot(data=df, x=col, y=target_var, ci=None) 
    plt.title(f"{col}", fontsize=20,y=1.05)
    st.pyplot(fig)

# The code above was copied from the Churnometer Project from Code Institute 
# with some adjustments