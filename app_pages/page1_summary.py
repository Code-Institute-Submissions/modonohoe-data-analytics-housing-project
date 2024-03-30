import streamlit as st

def page1_summary_body():

    st.write("### Project Summary")

    # text based on README file - "Dataset Content" section
    """"Project Dataset"""
    st.info(
        f"**Project Terms & Jargon**\n"
        f"* The dataset is sourced from **[Kaggle]"
        f"(https://www.kaggle.com/codeinstitute/housing-prices-data)** "
        f"provided by Code Institute.\n"
        f"**Project Dataset**\n"
        f"* The dataset consists of 1,461 rows each and represents houses "
        f"in from Ames, Iowa. \n"
        f"* The dataset typically contains a house profile, "
        f"ie. Floor Area, Basement, Garage, Kitchen, Lot, Porch, "
        f"Wood Deck, Year Built "
        f"and their respective Sale Price."
        f"The houses in this dataset were built between 1872 and 2010.\n\n"
        f"* **SalePrice** is the price a house sold for and is our target variable.\n\n"
    )

    st.info(
        f"**Dataset Content Abbreviations**\n\n"
        f"|Variable|Meaning|Units|\n"
        f"|:----|:----|:----|\n"
        f"|1stFlrSF|First Floor square feet|(Min - Max > Sq. ft.) "
        f"334 - 4692|\n"
        f"|2ndFlrSF|Second floor square feet|(Min - Max > Sq. ft.) "
        f"0 - 2065|\n"
        f"|BedroomAbvGr|Bedrooms above grade (does NOT include "
        f"basement bedrooms)|(Min - Max > Bedrooms) 0 - 8|\n"
        f"|BsmtExposure|Refers to walkout or garden level walls|Gd: "
        f"Good Exposure; Av: Average Exposure; Mn: Mimimum Exposure; "
        f"No: No Exposure; None: No Basement|\n"
        f"|BsmtFinType1|Rating of basement finished area|GLQ: Good "
        f"Living Quarters; ALQ: Average Living Quarters; BLQ: Below "
        f"Average Living Quarters; Rec: Average Rec Room; LwQ: Low "
        f"Quality; Unf: Unfinshed; None: No Basement|\n"
        f"|BsmtFinSF1|Type 1 finished square feet|(Min - Max > Sq. ft.) "
        f"0 - 5644|\n"
        f"|BsmtUnfSF|Unfinished square feet of basement area|(Min - "
        f"Max > Sq. ft.) 0 - 2336|\n"
        f"|TotalBsmtSF|Total square feet of basement area|(Min - "
        f"Max > Sq. ft.) 0 - 6110|\n"
        f"|GarageArea|Size of garage in square feet|(Min - Max > "
        f"Sq. ft.) 0 - 1418|\n"
        f"|GarageFinish|Interior finish of the garage|Fin: Finished; "
        f"RFn: Rough Finished; Unf: Unfinished; None: No Garage|\n"
        f"|GarageYrBlt|Year garage was built|(Min - Max > Year) "
        f"1900 - 2010|\n"
        f"|GrLivArea|Above grade (ground) living area square feet|"
        f"(Min - Max > Sq. ft.) 334 - 5642|\n"
        f"|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: "
        f"Typical/Average; Fa: Fair; Po: Poor|\n"
        f"|LotArea| Lot size in square feet|(Min - Max > Sq. ft.) "
        f"1300 - 215245|\n"
        f"|LotFrontage| Linear feet of street connected to property|"
        f"(Min - Max > Lin. ft.) 21 - 313|\n"
        f"|MasVnrArea|Masonry veneer area in square feet|(Min - Max "
        f"> Sq. ft.) 0 - 1600|\n"
        f"|EnclosedPorch|Enclosed porch area in square feet|"
        f"(Min - Max > Sq. ft.) 0 - 286|\n"
        f"|OpenPorchSF|Open porch area in square feet|(Min - "
        f"Max > Sq. ft.) 0 - 547|\n"
        f"|OverallCond|Rates the overall condition of the house|"
        f"10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; "
        f"6: Above Average; 5: Average; 4: Below Average; 3: Fair; "
        f"2: Poor; 1: Very Poor|\n"
        f"|OverallQual|Rates the overall material and finish of the "
        f"house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: "
        f"Good; 6: Above Average; 5: Average; 4: Below Average; 3: "
        f"Fair; 2: Poor; 1: Very Poor|\n"
        f"|WoodDeckSF|Wood deck area in square feet|(Min - Max > "
        f"Sq. ft.) 0 - 736|\n"
        f"|YearBuilt|Original construction date|(Min - Max > Year) "
        f"1872 - 2010|\n"
        f"|YearRemodAdd|Remodel date (same as construction date "
        f"if no remodeling or additions)|(Min - Max > Year) 1950 - 2010|\n"
        f"|SalePrice|Sale Price|(Min - Max > Price in $) 34900 - 755000|\n"
        )
    
    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"For additional information, please visit and **read** the "
        f"**[Project's README file](https://github.com/modonohoe/data-analytics-housing-project)**.")
    
     # copied from README file - "Business Requirements" section
    st.success(
        f"#### The project has two business requirements:\n\n"
        f"**1.**  The client is interested in discovering how house attributes correlate with "
        f"the house Sale Price. Therefore, the client expects data visualizations "
        f"of the correlated variables against Sale Price to show that.\n\n"
        f"**2.** The client is interested to predict the house sales price from their 4 "
        f"inherited houses, and any other house in Ames, Iowa. "
        )

# The code above was copied from the Churnometer Project from Code Institute 
# with some adjustments