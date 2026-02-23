import nbformat

nb = nbformat.v4.new_notebook()
nb.cells = [
    nbformat.v4.new_code_cell("import pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt"),
    nbformat.v4.new_code_cell("df = pd.read_csv('sales_data.csv', dtype={'product_id': 'int32', 'region': 'category', 'sales_amount': 'float64'})"),
    nbformat.v4.new_code_cell("summary = df.groupby('region')['sales_amount'].agg(['mean', 'median', 'std'])"),
    nbformat.v4.new_code_cell("outliers = df[np.abs(df['sales_amount'] - df['sales_amount'].mean()) > 2 * df['sales_amount'].std()]"),
    nbformat.v4.new_code_cell("fig, ax = plt.subplots(figsize=(10, 6))\nregions = df['region'].cat.categories\nsales_by_region = df.groupby('region')['sales_amount'].sum().reindex(regions)\nax.bar(regions, sales_by_region)\nax.set_title('Total Sales by Region')\nax.set_xlabel('Region')\nax.set_ylabel('Total Sales')\nax.grid(True)\nplt.show()"),
]
with open('analysis.ipynb', 'w') as f:
    nbformat.write(nb, f)
