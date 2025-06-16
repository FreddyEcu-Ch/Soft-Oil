# %% Import Python Libraries
import xlwings as xw
import pandas as pd
import numpy as np
from poes.model.utils import param_stoiip


# %% Call POES Workbook
wb = xw.Book("poes/controller/poes.xlsm")
sheet = wb.sheets["Summary"]

# %%
# Call DataFrame from Ms. Excel
df_poes = sheet["A2"].options(pd.DataFrame, expand="table", index=False).value


# %% Test param_stoiip function
area_stoc = param_stoiip(
    df_poes, 0, "Distribution", "Loc", "Scale", 1000, "C", "Lim Min", "Lim max"
)

h_stoc = param_stoiip(
    df_poes, 1, "Distribution", "Loc", "Scale", 100, "C", "Lim Min", "Lim max"
)

porosity_stoc = param_stoiip(
    df_poes, 2, "Distribution", "Loc", "Scale", 100, "C", "Lim Min", "Lim max"
)

swi_stoc = param_stoiip(
    df_poes, 3, "Distribution", "Loc", "Scale", 100, "C", "Lim Min", "Lim max"
)

boi_stoc = param_stoiip(
    df_poes, 4, "Distribution", "Loc", "Scale", 100, "C", "Lim Min", "Lim max"
)
