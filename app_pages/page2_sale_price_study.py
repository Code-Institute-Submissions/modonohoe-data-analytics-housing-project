import streamlit as st
from src.data_management import load_house_data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(context='notebook', style='darkgrid', palette='flare')

# functions taken from 2nd Jupyter Notebook
def plot_yearbuilt_saleprice_quality(df):
    sns.lmplot(data=df, x='YearBuilt', y='SalePrice', ci=None, hue='OverallQual',
               height=7, aspect=1.5, palette='viridis')
    plt.title('SalePrice vs. YearBuilt (Colored by OverallQuality)', fontsize=20)
    st.pyplot(plt)
    plt.clf()

def page2_sale_price_study_body():
    df = load_house_data()  
    target_var = 'SalePrice'
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
        f"*Finally, houses with larger basements ('TotalBsmtSF') and garages ('GarageArea') "
        f"are generally shown to increase the Sale Price"
    )

    if st.checkbox("Show Regression Plots"):
            regr_level_per_variable(df, target_var, vars_to_study)

    if st.checkbox("Show SalePrice vs. YearBuilt (Colored by Overall Quality)"):
        plot_yearbuilt_saleprice_quality(df)

def plot_numerical(df, col, target_var):
    plt.figure(figsize=(8, 5))
    sns.regplot(data=df, x=col, y=target_var, line_kws={"color": "red", "linewidth": 1})
    plt.title(f"{col} vs {target_var}", fontsize=20, y=1.05)
    st.pyplot(plt)  # Render the plot in Streamlit
    plt.clf() 


def regr_level_per_variable(df_eda, target_var, vars_to_study):
    for col in vars_to_study:
        plot_numerical(df_eda, col, target_var)
        st.write("\n")


def main():
    st.title('Numerical Data Visualization')
    page2_sale_price_study_body()  # Call the function that contains the study body and visualization logic

if __name__ == "__main__":
    main()
# The code above was copied from the Churnometer Project from Code Institute 
# with some adjustments