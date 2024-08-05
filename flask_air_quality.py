#create env first : python3 -m venv venv
#activate : source venv/bin/activate
# install needed lyb first 
# pip install flask pandas matplotlib seaborn

from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Load and process the data
    data_path = 'data/filtered_data.csv'  # Assume you've saved the notebook's final data as a CSV
    df = pd.read_csv(data_path)

    # Generate a plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='PM2.5', y='AQI', data=df)
    plt.title('PM2.5 vs AQI')
    plt.xlabel('PM2.5')
    plt.ylabel('AQI')
    plot_path = os.path.join('static', 'plot.png')
    plt.savefig(plot_path)
    plt.close()

    return render_template('index.html', plot_url=plot_path)

if __name__ == '__main__':
    app.run(debug=True)