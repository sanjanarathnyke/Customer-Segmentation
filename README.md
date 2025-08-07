# SpendWise Segmentation Tool

This is a Flask-based web application for customer segmentation using a pre-trained K-Means clustering model. Users can input their annual income and spending score to find out which customer segment they belong to.

## Features

- Predicts customer segment based on annual income and spending score.
- Uses a pre-trained K-Means model and scaler.
- Simple web interface built with Flask and HTML.

## Requirements

All required Python libraries are listed in [requirements.txt](requirements.txt):

- Flask
- joblib
- pandas
- numpy

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Ensure the following files are present in the project directory:**
   - `kmeans_model.pkl` (pre-trained K-Means model)
   - `scaler.pkl` (pre-fitted scaler)
   - `app.py`
   - `templates/index.html`

## Usage

1. **Run the Flask app:**
   ```sh
   python app.py
   ```

2. **Open your browser and go to:**
   ```
   http://127.0.0.1:5000/
   ```

3. **Enter the required details (Annual Income and Spending Score) and click "Check" to see the predicted customer segment.**

## License

This project is licensed under the [MIT License](LICENSE).

---

**Note:**  
Make sure `kmeans_model.pkl` and `scaler.pkl` are compatible with the input features:  
- `Annual Income (k$)`
- `Spending Score (1-100)`

If you need to retrain the model, ensure the same feature names and scaling
