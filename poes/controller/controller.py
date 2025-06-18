import xlwings as xw
from poes.model.poes import Poes
from poes.model.utils import param_stoiip
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
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
POES_ARRAY = "poes_array"

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

    # Calculation of Stochastic POES
    df_poes = sheet[DF_POES].options(pd.DataFrame, expand="table", index=False).value

    # Call realizations cell
    realizations = int(sheet[REALIZATIONS].value)

    # Call seed cell
    seed = int(sheet[SEED].value)

    # Define random values for STOIIP Parameters
    input_col_names = df_poes[VARIABLES].to_list()
    area_col, h_col, poro_col, swi_col, boi_col = tuple(input_col_names)
    input_idx = [AREA_IDX, H_IDX, PORO_IDX, SWI_IDX, BOI_IDX]

    input_dict = dict(zip(input_col_names, input_idx))

    results_dict = {}

    for col, idx in input_dict.items():
        results_dict[col] = param_stoiip(
            df_poes,
            idx,
            DISTRIBUTION,
            LOC,
            SCALE,
            realizations,
            C,
            LIM_MIN,
            LIM_MAX,
            seed,
        )

    # Calculation of Stochastic Stoiip into results_dict
    results_dict[POES_PROB] = Poes(
        results_dict[area_col],
        results_dict[h_col],
        results_dict[poro_col],
        results_dict[swi_col],
        results_dict[boi_col],
    )

    # Calculate mean, std, P90, P50, P10 from STOIIP
    summary_stoc_results = [
        results_dict[POES_PROB].mean(),
        results_dict[POES_PROB].std(),
        np.percentile(results_dict[POES_PROB], 10),
        np.percentile(results_dict[POES_PROB], 50),
        np.percentile(results_dict[POES_PROB], 90),
    ]

    # Write sthocastic values to Ms. Excel
    sheet[POES_PROB].options(transpose=True).value = summary_stoc_results

    # Call sheet results
    sheet_re = wb.sheets[RESULTS]

    # Create a DataFrame from results_dict
    df_results = pd.DataFrame(results_dict)

    # Write df_results into Results sheet in Ms. Excel
    sheet_re[POES_ARRAY].options(pd.DataFrame, expand="table", index=False).value = (
        df_results
    )

    # Create Histogram from Stochastic Stoiip
    eng_formatter = ticker.EngFormatter()
    sns.set_style("white")
    fig = plt.figure(figsize=(8, 6))

    ax = sns.histplot(df_results[POES_PROB], color="lightgray", kde=True)

    plt.axvline(
        summary_stoc_results[2],
        ymax=0.85,
        color="darkorange",
        linewidth=1.5,
        linestyle="--",
        label="P90",
    )

    plt.axvline(
        summary_stoc_results[3],
        ymax=0.85,
        color="gold",
        linewidth=1.5,
        linestyle="--",
        label="P50",
    )

    plt.axvline(
        summary_stoc_results[4],
        ymax=0.85,
        color="green",
        linewidth=1.5,
        linestyle="--",
        label="P10",
    )

    ax.xaxis.set_major_formatter(eng_formatter)
    plt.xlabel("STOIIP (STB)")
    plt.suptitle("Stochastic STOOIP")
    plt.legend(loc=0)

    # Send Histogram to Ms. Excel
    sheet.pictures.add(fig, name="Histogram", update=True, left=sheet.range("J2").left)


if __name__ == "__main__":
    xw.Book("poes.xlsm").set_mock_caller()
    main()
