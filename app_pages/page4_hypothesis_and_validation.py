import streamlit as st

def page4_hypothesis_and_validation_body():

    st.write("### Project Hypothesis and Validation")
	
    st.success(
    f"**1.** Houses that have the greatest overall Living Space would have "
    f"a higher `SalePrice`: **True**. \n "
    f"- The correlation study on **House Sale Price Study** supports the "
    f"strong correlation between the two. \n\n"

    f"**2.** Newer builds have a better Overall Quality in terms of finishings "
    f"and materials which in turn increases `SalePrice`: **True**.\n "
    f"- The correlation study on the **House Sale Price Study** supports a "
    f"a moderate correlation between the two. \n\n"

    f"**3.** House with more storeys have a higher `SalePrice`: **False**.\n"
    f"- Number of storeys transpired to have very little impact on `SalePrice`, "
    f"60% of the dataset do not have a 2nd storey in their house.\n\n"

    f"**4.** Houses with larger Square Foot of Basement space generally "
    f" have a higher `Sale Price`: **True**. \n"
    f"- The correlation study on **House Sale Price Study** supports the "
    f"strong correlation between the two. \n\n"
    )

# The code above was copied from the Churnometer Project from Code Institute with some adjustments