# This is a Marimo interactive notebook.
# Author email (required): 24f2005506@ds.study.iitm.ac.in

import marimo

app = marimo.App()


# ------------------------------------------------------------
# CELL 1: Import libraries and define dataset
# Data flow: This cell creates data used by later cells.
# ------------------------------------------------------------
@app.cell
def cell1():
    import numpy as np
    import pandas as pd

    # Generate sample dataset
    x = np.linspace(0, 10, 100)
    y = 2 * x + 3 + np.random.normal(0, 2, 100)

    df = pd.DataFrame({"x": x, "y": y})

    df
    return df, x, y


# ------------------------------------------------------------
# CELL 2: Slider controlling slope multiplier
# Data flow: Slider value affects downstream markdown and plot.
# ------------------------------------------------------------
@app.cell
def cell2(mo):
    slope_factor = mo.ui.slider(start=0, stop=3, step=0.1, value=1.0, label="Slope multiplier:")
    slope_factor
    return slope_factor


# ------------------------------------------------------------
# CELL 3: Dynamic markdown output
# Data flow: Uses slider value from Cell 2
# ------------------------------------------------------------
@app.cell
def cell3(slope_factor):
    import marimo as mo
    mo.md(f"""
    ## 🔄 Dynamic Analysis Summary  
    **Current slope multiplier:** `{slope_factor.value}`  
    This multiplier dynamically scales the model slope to show how  
    changes in slope affect the linear relationship between variables.
    """)


# ------------------------------------------------------------
# CELL 4: Plot depending on slider + data
# Data flow: Uses df from Cell 1 and slider from Cell 2
# ------------------------------------------------------------
@app.cell
def cell4(df, slope_factor):
    import matplotlib.pyplot as plt
    import numpy as np

    plt.figure(figsize=(6, 4))
    plt.scatter(df["x"], df["y"], alpha=0.5, label="Data points")

    # computed model
    model_y = (2 * slope_factor.value) * df["x"] + 3
    plt.plot(df["x"], model_y, color="red", label="Model curve")

    plt.title("Interactive Regression Model Demo")
    plt.legend()
    plt.show()


# Required
if __name__ == "__main__":
    app.run()
