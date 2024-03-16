# Predicting Housing Prices 

Introduction information

---

## Contents
* [Dataset Content](#dataset-content) 🗃️
* [Business Requirements](#business-requirements) 📋
* [Hypothesis and How To Validate](#hypothesis-and-how-to-validate) 💡
* [Rationale](#rationale) ✍
* [ML Business Case](#ml-business-case) 📊
* [Dashboard Design](#dashboard-design) 📐
* [Unfixed Bugs](#unfixed-bugs) 🛠️
* [Deployment](#deployment) 🖥️
* [Data Analysis and ML Libraries](#data-analysis-and-ml-libraries) 📚
* [Credits and Acknowledgments](#credits-and-acknowledgments) 💐

## Dataset Content 🗃️

The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data). 

The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profiles (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and their respective sale price. 

The dataset includes data for houses built between 1872 and 2010 exclusively in Ames, Iowa.


<details>
<summary>The dataset's variable names, meanings and units can be inspected below: </summary> 

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

</details>

## Business Requirements 📋

Our client 'Lydia Doe' who is based in Belgium, has inherited four houses located in Ames, Iowa, from their great-grandfather. They are requesting help to maximise the sales price for these properties.

1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.

2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.


## Hypothesis and How To Validate 💡

List here your project hypothesis(es) and how you envision validating it (them).
1. 

2. 

3. 


## Rationale ✍

- **Business Requirement 1:** Data Visualisation and Correlation Study

* As a client, I want to inspect the data related to the house records so that I can discover how the house attributes correlate with the sale price

* As a client, I want to conduct a correlation study (Pearson and Spearman) to understand better how the variables are correlated to Sale Price so that I can discover how the house attributes correlate with the sale price

* As a client, I want to plot the main variables against Sale Price to visualize insights so that I can discover how the house attributes correlate with the sale price.

- **Business Requirement 2:** House Price Prediction

* As a client, I want to predict the sale price for a given house in Ames, Iowa.  

The rationale to map the business requirements to the Data Visualisations and ML tasks

List your business requirements and a rationale to map them to the Data Visualisations and ML tasks.

## ML Business Case 📊

In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.

- We want an ML model to predict ...

- Our ideal outcome is ...

- The model success metrics are ... R VALUE

- The output is defined ...

- Heuristic ...

- The training data ...


## Dashboard Design 📐

List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items that your dashboard library supports.

Eventually, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but eventually you needed to use another plot type)

## Unfixed Bugs 🛠️

You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not valid reason to leave bugs unfixed.

## Deployment 🖥️

### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Data Analysis and ML Libraries 📚

Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.

## Credits and Acknowledgments 💐

## Credits 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open Source site
- The images used for the gallery page were taken from this other open-source site

### Acknowledgements
* In case you would like to thank the people that provided support through this project.





1. Open a new terminal and <code>pip3 install -r requirements.txt</code>

1. In the terminal type <code>pip3 install jupyter</code>

1. In the terminal type <code>jupyter notebook --NotebookApp.token='' --NotebookApp.password=''</code> to start the jupyter server.

1. Open port 8888 preview or browser

1. Open the jupyter_notebooks directory in the jupyter webpage that has opened and click on the notebook you want to open.

1. Click the button Not Trusted and choose Trust.

Note that the kernel says Python 3. It inherits from the workspace so it will be Python-3.8.12 as installed by our template. To confirm this you can use <code>! python --version</code> in a notebook code cell.


## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In your Cloud IDE, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.


