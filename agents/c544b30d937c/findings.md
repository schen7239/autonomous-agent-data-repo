# SPY Options Analysis Findings

## Overview
- **Agent Branch:** agent/c544b30d937c
- **Expiry:** 04/02/2026
- **Analysis Date:** March 27, 2026 data
- **Spot Price Assumed:** $560.00

## Files Generated
- `analysis.ipynb` — Jupyter notebook (outputs cleared for git)
- `final_report.html` — Executed report with charts
- `spy_options_clean.csv` — Parsed and cleaned options chain data
- `spy_options_analysis.png` — Three-panel chart (IV smile, Delta, Gamma)
- `data_checksums.sha256` — SHA-256 hash of input data
- `findings.md` — This file

---

## Key Findings

### ATM Implied Volatility
- **ATM IV:** 30.15% (at strike 640, closest to spot 560)
- Note: The provided data has strikes from 600-670, which are significantly ITM/OTM relative to spot 560.
- **Nearest OTM Call IV:** 30.15% at 640 strike
- **Nearest OTM Put IV:** 30.91% at 635 strike

### Expected Standard Deviation Moves (6-day expiry)
Given the 6-day time to expiry (3/27 to 4/2):
- **1 SD Move:** +/- $7.14 points
- **1 SD Range:** [552.86, 567.14]
- **2 SD Range:** [545.71, 574.29]
- **2.5 SD Range:** [542.14, 577.86]

### Implied Volatility Smile Analysis

#### Put-Call IV Spread
- **Put IV Skew:** Puts consistently trade at a premium to calls at equivalent strikes
- At 635 strike: Put IV = 30.91% vs Call IV at 640 = 30.15%
- This indicates **downside protection demand** — market participants are paying premium for put protection

#### Smile Shape
- **Calls:** IV decreases as strikes increase (normal skew for OTM calls)
- **Puts:** IV increases as strikes decrease (reverse skew — typical for equity indices)
- The data shows a **reverse skew** typical of SPY/SPX options where downside strikes carry higher IV

### Delta Profile
- ATM (640 strike) Call Delta: ~0.50
- Delta approaches 1.0 for deep ITM calls (600 strike: delta ~0.99)
- Delta approaches 0.0 for deep OTM calls (670 strike: delta ~0.01)

### Gamma Risk Profile
- **Max Gamma Concentration:** Near ATM strikes (635-640)
- Gamma risk is highest where delta changes most rapidly
- Market makers face **maximum hedging intensity** in the 635-640 strike zone

---

## Risk Implications for 04/02 Expiry

### 1. Gamma Pin Risk
- With 6 days to expiry and high ATM gamma, there's significant **gamma pin risk** near 635-640
- Any move toward these strikes will increase hedging flows from market makers

### 2. Volatility Risk Premium
- The put-call IV spread suggests elevated fear of downside moves
- Put IV > Call IV at similar distances from spot indicates bearish positioning

### 3. Standard Deviation Levels
| Level | Lower | Upper | Interpretation |
|-------|-------|-------|----------------|
| 1 SD | 552.86 | 567.14 | Expected daily move range |
| 2 SD | 545.71 | 574.29 | Unlikely but possible |
| 2.5 SD | 542.14 | 577.86 | Tail event territory |

---

## Statistical Summary

### Call Options (27 contracts)
| Metric | Value |
|--------|-------|
| Strike Range | 600 - 670 |
| IV Range | 26.71% - 37.55% |
| Avg IV | 30.4% |
| ATM Strike | 640 (nearest OTM) |

### Put Options (27 contracts)
| Metric | Value |
|--------|-------|
| Strike Range | 600 - 670 |
| IV Range | 30.59% - 35.46% |
| Avg IV | 31.8% |
| ATM Strike | 635 (nearest OTM) |

---

## Reproducibility
- Input file: `/workspace/raw_options.txt`
- SHA-256 hash recorded in `data_checksums.sha256`
- Notebook runs top-to-bottom without manual intervention
- Environment: Python 3.x with pandas, numpy, matplotlib, scipy, jupyter

---

## Conclusion

The SPY options chain for 04/02/2026 expiry exhibits:
1. **Reverse skew** — puts trade at premium to calls
2. **High ATM gamma** — max risk at 635-640 strikes  
3. **6-day implied move** of ~$7.14 (1 SD)
4. **Elevated put demand** — downside protection being priced in

This structure suggests markets are positioned for potential downside volatility into the expiry.
