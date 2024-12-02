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

*Requirements*

      1. Python 3.x
         
      2.NumPy
      
      3.Matplotlib
      
      4.Scikit-learn
      
      5.BeautifulSoup4 (for web scraping, if you are scraping data)
      
      6.Requests (for sending HTTP requests to retrieve data)

*Setup and Installation*

      1.Clone the repository or download the project files.
      
      2.Install the required libraries:
   
            pip install numpy matplotlib scikit-learn beautifulsoup4 requests
         
      3. Ensure that the models (model_total, model_female, model_male) and the polynomial transformer (poly) are already trained and saved as objects. These models are used to make predictions based on the historical data.

*How to Run*

   1. Once you have the required dependencies and models in place, run the script.
      
   2. The script will prompt you to enter the start and end year for the predictions.
      
   3. Enter the desired year range, and the program will output the predicted total, female, and male deaths for each year within that range.
      
   4. The predictions will be displayed in the console, and graphs will be shown for a better understanding of the trends.

*Example Usage*

   Enter the start year: 2025
   
   Enter the end year: 2030
   
   Predictions for the Years 2025 to 2030:

      Year 2025:
     Total Deaths: 9,251,643
     Female Deaths: 5,102,088
     Male Deaths: 4,149,554
      ------------------------------
      Year 2026:
     Total Deaths: 9,235,504
     Female Deaths: 5,103,813
     Male Deaths: 4,131,691
      ------------------------------
      ...
