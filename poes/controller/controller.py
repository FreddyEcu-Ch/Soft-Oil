import xlwings as xw
from poes.model.poes import Poes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Define Sheet names
SUMMARY = "Summary"
RESULTS = "Results"


# Define Column Names
VARIABLES = "Variables"
VALUES = "Values"
DISTRIBUTION = "Distribution"
LOC = "Loc"
SCALE = "Scale"
C = "C"
LIM_MIN = "Lim Min"
LIM_MAX = "Lim max"

# Call cells from Ms Excell
DF_POES = "df_poes"
DET_POES = "det_values"
REALIZATIONS = "realizations"
SEED = "seed"

# Write values in Excel from Python
POES_DET = "det_result"
POES_PROB = "poes_prob"
POES_ARRA = "poes_array"

# Index of POES Parameters
AREA_IDX, H_IDX, PORO_IDX, SWI_IDX, BOI_IDX = 0, 1, 2, 3, 4


def main():
    wb = xw.Book.caller()

    # Define sheet to use
    sheet = wb.sheets[SUMMARY]

    # Call values (cells) for deterministic POES
    params = sheet[DET_POES].options(np.array, Transpose=True).value

    # Calculation of Deterministic POES
    sheet[POES_DET].value = Poes(*params)


if __name__ == "__main__":
    xw.Book("poes.xlsm").set_mock_caller()
    main()
