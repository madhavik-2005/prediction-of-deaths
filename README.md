**Death Prediction Model**

*Overview*

This project predicts future death counts for both males and females over a specified range of years. The predictions are based on historical data extracted through web scraping and modeled using a polynomial regression approach. The tool allows users to input a range of years and outputs the predicted total, female, and male deaths for each year. The predictions are displayed as both text and visualized through graphs for better understanding.

*Features*
1. Web Scraping: Data is collected from a reliable source through web scraping techniques to extract historical death statistics.
   
2. Prediction Model: A polynomial regression model is used to predict future death counts based on the historical data.
   
3. Dynamic Year Range: The user can specify a start year and an end year for which predictions are made.
   
4. Data Visualization: The predictions are presented through line and area charts, providing a clear visualization of the predicted trends over time.
   
5. Incremental Death Predictions: The model ensures that the predicted number of deaths increases over time, making the predictions realistic and in line with global trends.

*Technologies Used*
-Python: The project is implemented using Python, with key libraries including:
   -NumPy: For numerical calculations and handling arrays.
   -Matplotlib: For plotting the predicted death trends.
   -Scikit-Learn: For implementing polynomial regression models.
   
-Web Scraping: Python's BeautifulSoup and Requests libraries (not included in the provided code but assumed for scraping purposes) are used to extract historical death data from websites.

-Polynomial Regression: A polynomial regression model (of degree 3) is used for predicting future deaths based on historical data.
