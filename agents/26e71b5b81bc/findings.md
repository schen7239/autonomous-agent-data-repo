# SPY Options Analysis Findings — 04/06/2026 Expiry

## Overview
- **Spot Price (S):** 628.0 (approximate SPY close on 4/3/2026)
- **Expiry:** 04/06/2026
- **Days to Expiry (T):** 3 trading days (T = 3/365)
- **Risk-Free Rate (r):** 4.5%

## Implied Volatility Analysis

### ATM Implied Volatility
- **ATM IV:** ~30.36% (630 strike call, nearest to spot)
- **Expected 1SD Move (3 days):** ±5.55 pts

### SD Band Levels
| Band | Lower Bound | Upper Bound |
|------|-------------|-------------|
| 1 SD | 622.45 | 633.55 |
| 2 SD | 616.90 | 639.10 |
| 2.5 SD | 614.12 | 641.88 |

### IV Smile Shape
- **Skew Direction:** Volatility skew is present — OTM puts show higher IV than OTM calls
- **Put vs Call IV Spread:**
  - Deep OTM calls (560 strike): ~53.1% IV
  - Deep OTM puts (670 strike): ~37.2% IV
  - The skew is **inverse** — higher IV for downside puts near the money, but deep OTM calls show elevated IV as well
- **IV Minimum:** Around 640-650 strike calls (~29.2-29.3%), indicating the "kink" in the smile is slightly OTM

## Greeks Analysis

### Delta Profile
- Call delta ranges from ~0.98 (deep ITM) to ~0.04 (deep OTM)
- Put delta ranges from ~-0.98 (deep ITM) to ~-0.02 (deep OTM)
- ATM delta: Call ~0.45-0.55, Put ~-0.45 to -0.55

### Gamma Concentration
- **Max Gamma:** Concentrated around ATM strikes (625-635)
- **Peak Gamma Value:** ~0.012-0.015 per 1% move
- **Implication:** Market makers will need to hedge aggressively if SPY moves within the 625-635 zone. Gamma scalping activity expected near these levels.

## Open Interest Analysis

### Call Open Interest
- **Max Call OI Strike:** 640 (1,527,407 contracts)
- **Notable Call Walls:**
  - 630 strike: 1,137,742 OI
  - 635 strike: 1,266,455 OI
  - 640 strike: 1,527,407 OI (call wall)
  - 650 strike: 1,035,067 OI

### Put Open Interest
- **Max Put OI Strike:** 600 (4,481,508 contracts) — **major put wall**
- **Notable Put Walls:**
  - 600 strike: 4,481,508 OI (dominant put support)
  - 605 strike: 3,472,827 OI
  - 610 strike: 4,015,097 OI
  - 615 strike: 3,558,283 OI
  - 620 strike: 3,890,721 OI

### Key Observations
1. **Put Wall at 600:** The 600 strike has the highest OI across both calls and puts (~4.48M), representing a critical support level
2. **Call Wall at 640:** The 640 strike has the highest call OI (~1.53M), suggesting resistance
3. **OI Concentration:** Heavy put OI in the 600-620 zone suggests strong institutional hedging or put-selling strategies

## Trading Implications

### For 04/06/2026 Expiry
1. **Support Zone:** 600-615 (heavy put OI, potential pinning)
2. **Resistance Zone:** 640-650 (call wall concentration)
3. **Gamma Risk:** Highest gamma exposure around 625-635; expect volatile moves if spot enters this zone
4. **1SD Range:** 622.45 - 633.55 (68% probability of closing within this range by expiry)

### Notable Anomalies
- Deep OTM calls (560-570 strike) show unusually high IV (~50%+) — likely due to tail risk hedging
- Zero volume across all strikes (data snapshot condition)
- The 600 put OI is nearly 3x the next largest put strike, indicating a strong pinning level

## Files
- `spy_options_raw.csv` — Raw options chain data
- `spy_options_clean.csv` — Parsed data with IV as decimal
- `analysis.ipynb` — Jupyter notebook (outputs cleared)
- `final_report.html` — Executed HTML report
- `spy_options_analysis.png` — 3-panel Greeks chart
- `oi_by_strike.png` — Open interest bar charts
- `data_checksums.sha256` — SHA-256 hash of raw data
