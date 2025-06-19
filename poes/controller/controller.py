import xlwings as xw
import numpy as np
import poes.model.poes import Poes
import pandas as np
import matplotlib.pyplot as plt
import seaborn as sns

SUMMARY ="Summary"
RESULTS="Results"

VARIABLES="Variables"
VALUES="Values"
DISTRIBUTIONS="Distributions"
LOC="Loc"
SCALE="Scale"
C="c"
LIM_MIN="Lim Min"
LIM_MAX="Lim Max"

DF_POES="df_poes"
DET_POES="det_values"
REALIZATION="realizations"
SEED="seed"

POES_DET="df_poes"
POES_PROB="poes_prob"
POES_ARRA="poes_array"

AREA_IDX, H_IDX, PORO_IDX, SWI_IDX, BOI_IDX=0,1,2,3,4

def main():
    wb=xw.Book.caller()
    sheet=wb.sheets[SUMMARY]
    params=sheet[DET_POES].options(np.array, Transpose=True).value
    sheet[POES_DET].value=Poes(*params)

if __name__ == "__main__":
    xw.Book("poes.xlsm").set_mock_caller()
    main()
