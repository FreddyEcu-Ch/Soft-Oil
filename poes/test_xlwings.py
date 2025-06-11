# %% Import python libraries
import xlwings as xw
import numpy as np
import pandas as pd

# %% Create an Excel workbook using xlwings
wb = xw.Book()


# %% Select sheet to work
sheet = wb.sheets["Hoja1"]


# %% Modify an excell cell from Python
sheet["D6"].value = "Hola Mundo"


# %% Call an excell cell from Excel to Python
saludo = sheet["D6"].value
print(saludo)


# %% Create a numpy array from Python to Excel
sheet["E10"].options(np.array, Transpose=True).value = np.array([1, 2, 3, 4, 5, 6, 7])


# %% Call excell array to Python
array_values = sheet["E10:K10"].value
print(array_values)


# %% Create a Pandas Dataframe from Python to Excel
sheet["E13"].options(pd.DataFrame, expand="table", index=False).value = pd.DataFrame(
    {
        "Field": ["Auca", "Sacha", "Pucuna"],
        "Oil Production (stb/d)": [70000, 65000, 12500],
        "Wells": ["Au10", "Sa12", "Pu15"],
    }
)


# %% Call the table from Excel to Python
df = sheet["E13:G16"].options(pd.DataFrame, expand="table", index=False).value
print(df)
