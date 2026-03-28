import nbformat as nbf

nb = nbf.v4.new_notebook()

# Cell 1: Imports and setup
cell1 = "import pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nfrom pathlib import Path\n\n# Set plotting style\nplt.style.use('seaborn-v0_8-whitegrid')"
nb.cells.append(nbf.v4.new_code_cell(cell1))

# Cell 2: Load data with explicit types
cell2_md = "## Load Sales Data"
nb.cells.append(nbf.v4.new_markdown_cell(cell2_md))

cell2 = '''# Define dtypes for efficient loading
dtypes = {
    'product_id': 'int8',
    'region': 'category',
    'sales_amount': 'float32'
}

# Load data with explicit types
df = pd.read_csv(
    '/workspace/sales_data.csv',
    parse_dates=['date'],
    dtype=dtypes
)

print(f"Dataset shape: {df.shape}")
print("Data types:")
print(df.dtypes)
print("First 5 rows:")
df.head()'''
nb.cells.append(nbf.v4.new_code_cell(cell2))

# Cell 3: Descriptive statistics by region
cell3_md = "## Descriptive Statistics by Region"
nb.cells.append(nbf.v4.new_markdown_cell(cell3_md))

cell3 = '''# Calculate descriptive statistics for sales_amount by region
region_stats = (
    df.groupby('region', observed=True)['sales_amount']
    .agg(['count', 'mean', 'median', 'std', 'min', 'max'])
    .round(2)
)

# Add IQR and quartiles
region_stats['q1'] = df.groupby('region', observed=True)['sales_amount'].quantile(0.25).round(2)
region_stats['q3'] = df.groupby('region', observed=True)['sales_amount'].quantile(0.75).round(2)
region_stats['iqr'] = (region_stats['q3'] - region_stats['q1']).round(2)

print("Descriptive Statistics by Region:")
print("=" * 50)
print(region_stats.to_string())'''
nb.cells.append(nbf.v4.new_code_cell(cell3))

# Cell 4: Outlier detection (2 std from mean)
cell4_md = "## Outlier Detection"
nb.cells.append(nbf.v4.new_markdown_cell(cell4_md))

cell4 = '''# Calculate overall mean and std
overall_mean = df['sales_amount'].mean()
overall_std = df['sales_amount'].std()

print(f"Overall sales statistics:")
print(f"  Mean: ${overall_mean:,.2f}")
print(f"  Std Dev: ${overall_std:,.2f}")
print(f"  2-Sigma range: ${overall_mean - 2*overall_std:,.2f} to ${overall_mean + 2*overall_std:,.2f}")

# Define outlier bounds
lower_bound = overall_mean - 2 * overall_std
upper_bound = overall_mean + 2 * overall_std

# Identify outliers
outliers = df[(df['sales_amount'] < lower_bound) | (df['sales_amount'] > upper_bound)]

print("Outliers identified:", len(outliers), f"records ({len(outliers)/len(df)*100:.2f}%)")
print(f"  Below lower bound: {len(df[df['sales_amount'] < lower_bound])}")
print(f"  Above upper bound: {len(df[df['sales_amount'] > upper_bound])}")

# Display sample outliers
print("Sample outliers:")
print(outliers[['date', 'product_id', 'region', 'sales_amount']].head(10).to_string(index=False))'''
nb.cells.append(nbf.v4.new_code_cell(cell4))

# Cell 5: Visualization - Sales by Region
cell5_md = "## Sales Visualization by Region"
nb.cells.append(nbf.v4.new_markdown_cell(cell5_md))

cell5 = '''# Calculate total sales by region
total_sales = df.groupby('region', observed=True)['sales_amount'].sum().sort_values(ascending=False)

print("Total Sales by Region:")
for region, total in total_sales.items():
    print(f"  {region}: ${total:,.2f}")

# Create figure with proper sizing
fig, ax = plt.subplots(figsize=(12, 7))

# Define colors for each region
colors = {'North': '#1f77b4', 'South': '#ff7f0e', 'East': '#2ca02c', 'West': '#d62728'}
bar_colors = [colors[r] for r in total_sales.index]

# Create bar chart
bars = ax.bar(
    total_sales.index,
    total_sales.values,
    color=bar_colors,
    edgecolor='black',
    linewidth=1.2,
    alpha=0.85
)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax.annotate(
        f'${height:,.0f}',
        xy=(bar.get_x() + bar.get_width() / 2, height),
        xytext=(0, 5),
        textcoords="offset points",
        ha='center',
        va='bottom',
        fontsize=12,
        fontweight='bold'
    )

# Formatting
ax.set_title('Total Sales Amount by Region (2025)', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Region', fontsize=12, fontweight='bold')
ax.set_ylabel('Total Sales Amount ($)', fontsize=12, fontweight='bold')
ax.set_ylim(0, max(total_sales.values) * 1.15)

# Add gridlines
ax.grid(True, axis='y', alpha=0.4, linestyle='--', linewidth=0.8)
ax.set_axisbelow(True)

# Format y-axis with comma separators
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))

# Tight layout
plt.tight_layout()

# Save figure
plt.savefig('/workspace/sales_by_region.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.show()

print(f"Chart saved to: /workspace/sales_by_region.png")'''
nb.cells.append(nbf.v4.new_code_cell(cell5))

# Cell 6: Summary
cell6_md = "## Summary"
nb.cells.append(nbf.v4.new_markdown_cell(cell6_md))

cell6 = '''# Generate summary statistics
print("=" * 60)
print("SALES DATA ANALYSIS SUMMARY")
print("=" * 60)
print(f"Dataset: 1,000 sales records from 2025")
print(f"Date range: {df['date'].min().strftime('%Y-%m-%d')} to {df['date'].max().strftime('%Y-%m-%d')}")
print(f"Products: {df['product_id'].nunique()} unique product IDs")
print(f"Regions: {df['region'].nunique()} regions")

print("Overall Sales Statistics:")
print(f"  Total Sales: ${df['sales_amount'].sum():,.2f}")
print(f"  Mean: ${df['sales_amount'].mean():,.2f}")
print(f"  Median: ${df['sales_amount'].median():,.2f}")
print(f"  Std Dev: ${df['sales_amount'].std():,.2f}")

print(f"Top Region by Total Sales: {total_sales.index[0]} (${total_sales.iloc[0]:,.2f})")
print(f"Outliers Detected: {len(outliers)} records ({len(outliers)/len(df)*100:.1f}%)")
print("=" * 60)'''
nb.cells.append(nbf.v4.new_code_cell(cell6))

# Write notebook
with open('/workspace/analysis.ipynb', 'w') as f:
    nbf.write(nb, f)

print("Notebook created at /workspace/analysis.ipynb")
