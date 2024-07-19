# SafeSurfing: Phishing Website Detection Using Machine Learning

## Overview

SafeSurfing is a phishing domain detection tool designed to protect users from phishing attacks. By analyzing URLs through a machine learning model, SafeSurfing provides insights into the trustworthiness of websites and offers functionality to preview and review source code without visiting potentially harmful sites.

## Features

- **Phishing Detection**: Analyzes URLs to determine if they are phishing attempts or legitimate.
- **Trust Score**: Provides a trust score based on various factors to assess the reliability of a URL.
- **Preview Functionality**: Allows users to preview a URL within SafeSurfing's secure environment.
- **Source Code Viewing**: Enables users to view the source code of a URL safely.
- **Detailed Analysis**: Offers detailed information about the URL's global rank, HTTP status code, domain age, and other characteristics.
- **SSL Certificate and WHOIS Data**: Displays SSL certificate details and WHOIS information for additional security insights.
  ![image](https://github.com/user-attachments/assets/b19882dc-ce50-431b-b3b4-ddfa0197530a)


## Technology Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Machine Learning**: Various machine learning algorithms, including Decision Tree, Random Forest, Naive Bayes, Gradient Boosting, K-Neighbors Classifier, Support Vector Classifier, and a custom Hybrid LSD model.
- **Web Scraping**: BeautifulSoup, Requests.
- **Data Storage**: CSV files.

Input-1

  ![image](https://github.com/user-attachments/assets/3ac67586-943f-4875-9c74-0d243ccb2ee0)
  ![image](https://github.com/user-attachments/assets/ca6216b5-9c41-4af1-8d84-5f0808731a34)

Input-2

![image](https://github.com/user-attachments/assets/e271996e-e2d9-4b7f-ad1f-648e1c3654e7)
![image](https://github.com/user-attachments/assets/1bf5b499-8100-455e-af0c-8c8e4982b91b)


## Usage

1. **Home Page**
   - Enter a URL in the provided input field and click **"CHECK URL"** to get the phishing analysis.
   - The results will show the trust score, URL status, and detailed metrics.

2. **Preview URL**
   - After analysis, you can choose to preview the URL's content within SafeSurf by clicking the **"Preview URL within SafeSurf"** button.

3. **View Source Code**
   - View the source code of the URL by clicking the **"Show Source Code of URL"** button.

## Major Voting Model

The `major_voting.py` script trains and evaluates a voting classifier model using the Iris dataset. The model combines multiple classifiers to make predictions.

### Major Voting Model Features
- **Model Combination:** Uses Logistic Regression, Support Vector Classification, and Decision Tree Classifier.
- **Evaluation Metrics:** Provides accuracy, mean squared error (MSE), mean absolute error (MAE), precision, recall, F1 score, and R-squared metrics.
- **Visualization:** Generates a bar plot of the evaluation metrics.



### Prerequisites

- Python 3.x
- Flask
- Required Python libraries (listed in `requirements.txt`)


