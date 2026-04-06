# SPY Options Chain Analysis Findings

## Overview
- **Agent branch:** agent/c06ab0f320ea
- **Analysis date:** April 3, 2026
- **Expiry:** April 6, 2026 (3 trading days)
- **Spot price assumption:** $628.00
- **Risk-free rate:** 4.5%

## ATM Implied Volatility & Expected Moves
- **ATM IV:** 30.36% (from 630 strike call, nearest to spot)
- **Expected 1SD move (3 days):** ±5.39 pts
- **SD band levels:**
  - 1 SD: [622.61, 633.39] — 68% probability range
  - 2 SD: [617.22, 638.78] — 95% probability range
  - 2.5 SD: [614.52, 641.48] — ~99% probability range

## IV Smile Shape & Skew
- **Direction of skew:** Pronounced volatility smile/skew with higher IV at OTM strikes
- **Call IV range:** 29.20% (645 strike) to 53.13% (560 strike) — steep increase at deep ITM/OTM
- **Put IV range:** 30.73% (635 strike) to 53.19% (560 strike) — similar pattern
- **Put vs Call IV spread at OTM strikes:**
  - At 560 strike: Put IV 53.19% vs Call IV 53.13% — nearly parity
  - At 670 strike: Put IV 37.19% vs Call IV 31.97% — puts trade at ~5% premium
- **Interpretation:** Typical "smile" pattern with elevated OTM put IV indicating downside protection demand. The skew is more pronounced on the put side at higher strikes.

## Gamma Concentration & Market Maker Hedging
- **Max gamma location:** Near ATM strikes (625-630)
- **Call max gamma:** 0.0048 at 630 strike
- **Put max gamma:** 0.0048 at 630 strike
- **Hedging implications:** Market makers have highest gamma exposure near the 630 strike. Any move through this level will force aggressive delta hedging, potentially amplifying price moves. The gamma profile suggests "pin risk" around 625-630 at expiry.

## Key Open Interest Levels
### Call Open Interest (Call Wall)
- **Max call OI:** 1,527,407 contracts at 640 strike
- **Second highest:** 1,266,455 at 635 strike
- **Interpretation:** 640 strike represents major resistance / call wall. Dealers are likely short these calls, meaning they buy deltas as price rises above 640 (supportive of further upside).

### Put Open Interest (Put Wall)
- **Max put OI:** 4,481,508 contracts at 600 strike
- **Second highest:** 4,015,097 at 610 strike
- **Interpretation:** 600 strike is the "put wall" — massive support level. Dealers are long puts here, meaning they sell deltas as price drops toward 600 (providing support).

## SD Band Implications for 04/06/2026 Expiry
- **Current spot (628) is within 1 SD band** — normal trading range
- **Put wall at 600 sits at ~2.5 SD lower** — strong structural support
- **Call wall at 640 sits at ~1.4 SD upper** — resistance level within expected move
- **Probability context:** ~68% chance SPY expires between 622.61 and 633.39

## Notable Anomalies & Trading Observations
1. **Zero volume across all strikes** — data snapshot at close, no intraday trading
2. **Put/call OI ratio skewed bearish:** Total put OI (~28M) exceeds call OI (~10M) by ~2.8x
3. **Massive put OI at 600-610:** Suggests institutional hedging or structured product levels
4. **IV compression at ATM:** Lowest IV at 640-645 strikes (29.2-29.3%), typical for near-ATM options
5. **OTM put premium:** Puts at 670 trade at 37.19% IV vs calls at 31.97% — ~5% put skew
6. **Delta hedging zone:** 625-630 strike range has highest gamma, expect dealer activity here

## Files Generated
- `analysis.ipynb` — Jupyter notebook (outputs cleared for git)
- `final_report.html` — Executed report (code hidden)
- `spy_options_analysis.png` — 3-panel IV smile, Delta, and Gamma charts
- `oi_by_strike.png` — Open Interest bar charts for calls and puts
- `requirements.txt` — Python environment snapshot
- `data_checksums.sha256` — SHA-256 hashes of input data files

## Reproducibility
- Input files hashed in `data_checksums.sha256`
- Notebook runs top-to-bottom without manual intervention
- All parameters documented above
