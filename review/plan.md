# Data Repo Review Plan
Branch: agent/review-6ef10ce593

## Survey Summary

### Datasets Identified

| Dataset | File Path | Rows | Status | Agent Folder |
|---------|-----------|------|--------|--------------|
| Sales Data | ./sales_data.csv | 1000 | PENDING | None |
| SPY Options (b0e80fbb41bc) | ./agents/b0e80fbb41bc/spy_options_clean.csv | 54 | COMPLETE | agents/b0e80fbb41bc/ |
| SPY Options (c544b30d937c) | ./agents/c544b30d937c/spy_options_clean.csv | 54 | COMPLETE | agents/c544b30d937c/ |

### Sales Data Schema
- **Columns**: date, product_id, region, sales_amount
- **Date Range**: 2025-01-01 to 2025-12-30
- **Regions**: East (226), North (250), South (257), West (267)
- **Products**: 10 product IDs (1-10)
- **Sales Range**: $100 - $5,000

---

## Tasks

### TASK-01: Analyze Sales Dataset
- **Data file**: ./sales_data.csv (1000 rows)
- **Analysis Required**:
  - Descriptive statistics (mean, median, std dev, quartiles)
  - Distribution analysis by region
  - Outlier detection (2-sigma and IQR methods)
  - Correlation analysis (product_id vs sales_amount)
  - Normality tests (Shapiro-Wilk, Kolmogorov-Smirnov)
  - Time-series trends if applicable
  - Visualizations: histogram, boxplot by region, correlation heatmap
- **Skill**: data-analyst-state-machine
- **Status**: PENDING
- **Output Requirements**:
  - findings.md with executive summary and key metrics
  - PNG charts (min 3 visualizations)
  - final_report.html
  - data_checksums.sha256
  - Copy of cleaned data if transformations applied

### TASK-02: Review SPY Options Analysis (b0e80fbb41bc)
- **Data file**: ./agents/b0e80fbb41bc/spy_options_clean.csv (54 rows)
- **Status**: COMPLETE
- **Findings**: IV smile analysis, gamma risk profile, standard deviation bands

### TASK-03: Review SPY Options Analysis (c544b30d937c)
- **Data file**: ./agents/c544b30d937c/spy_options_clean.csv (54 rows)
- **Status**: COMPLETE
- **Findings**: ATM IV analysis, put-call IV spread, delta/gamma profiles

---

## Delegation Notes

- Only TASK-01 requires a new data-analyst agent
- TASK-02 and TASK-03 are already complete with findings.md in respective agent folders
- All outputs must be pushed to branch agent/review-6ef10ce593
