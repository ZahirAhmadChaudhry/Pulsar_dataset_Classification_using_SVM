# Pulsar Star Classification using SVM

This project focuses on classifying pulsar stars using the Support Vector Machine (SVM) algorithm, a powerful method in the realm of supervised learning. The goal is to automate the identification process of pulsar stars from candidates collected during surveys, based on predictive modeling.

## Project Structure

- `Datasets`: Holds the processed and raw datasets.
  - `Processed_data`: Contains processed data ready for analysis.
  - `Raw_data`: Contains raw data files.
- `v_pred_test`: Stores predicted outcomes on test data.
- `notebooks`: Jupyter notebooks for Exploratory Data Analysis (EDA) and model training.
- `venv`: A virtual environment directory for project dependencies.
- `.gitignore`: Specifies untracked files to ignore.
- `README.md`: Provides an overview of the project.
- `requirements.txt`: Lists all the necessary Python packages.

## Setup

To run this project, follow these steps:

1. Make sure Python 3.8 or later is installed on your machine.
2. Clone the repository to your local environment.
3. Navigate to the project's root directory and set up a Python virtual environment:

   ```sh
   python -m venv venv
   ```

4. Activate the virtual environment:

   On Windows:
   ```sh
   .\venv\Scripts\activate
   ```
   
   On macOS and Linux:
   ```sh
   source venv/bin/activate
   ```

5. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

To perform EDA or train the SVM model, open the Jupyter notebooks located in the `notebooks` directory:

- `EDA_Test_Data.ipynb`: For exploratory data analysis on test data.
- `EDA_Train_Data.ipynb`: For exploratory data analysis on training data.
- `MODEL_TRAINING.ipynb`: For training the SVM model.

Run the notebooks sequentially to explore the data and train the model.

## Data

The `Datasets` directory is organized as follows:

- `Processed_data`: Processed files like `pulsar_data_test_processed.csv` for use in modeling.
- `Raw_data`: The original, unprocessed data files.

Predictions from the test data are saved in `v_pred_test` with filenames indicating they are predictions, such as `Pulsar_data_test_Predicted.csv`.

## Contributing

If you'd like to contribute, please fork the repository and create a pull request with your features or changes.

## License

Open-sourced software licensed under the [MIT license](https://github.com/ZahirAhmadChaudhry/Pulsar_dataset_Classification_using_SVM/blob/main/LICENSE).