# SPY Options Chain Analysis — 04/06/2026 Expiry

## Parameters
- **Spot Price (S):** $628.00 (approximate SPY close on 4/3/2026)
- **Risk-Free Rate (r):** 4.5%
- **Days to Expiry:** 3 trading days (T = 3/365)
- **Expiry Date:** April 6, 2026

## ATM Implied Volatility & Expected Moves
- **ATM IV:** ~30.36% (at 630 strike, closest to spot)
- **Expected 1SD Move (3d):** ±5.48 pts
- **1 SD Range:** [622.52, 633.48]
- **2 SD Range:** [617.04, 638.96]
- **2.5 SD Range:** [614.30, 641.70]

## IV Smile Shape & Skew
- **Skew Direction:** Pronounced put skew — OTM puts exhibit significantly higher IV than OTM calls
- **Put vs Call IV Spread at OTM Strikes:**
  - At 560 strike: Put IV (53.19%) vs Call IV (53.13%) — roughly symmetric at deep wings
  - At 600 strike: Put IV (37.50%) vs Call IV (38.91%) — slight call premium
  - At 670 strike: Put IV (37.19%) vs Call IV (31.97%) — put skew emerges at higher OTM
- **Shape:** Classic volatility smile with elevated wings, moderate put skew at higher strikes

## Gamma Risk Profile
- **Max Gamma Concentration:** Near ATM strikes (625-630 region)
- **Peak Gamma:** ~0.015 per contract at 630 strike
- **Implication:** Market makers have highest gamma exposure near current spot. Any sharp move away from 628 will force significant delta hedging, potentially amplifying volatility.

## Open Interest Analysis
- **Max Call OI Strike:** 640 (1,527,407 contracts) — **Call Wall**
- **Max Put OI Strike:** 600 (4,481,508 contracts) — **Put Wall**
- **Interpretation:** Massive put OI at 600 creates strong support zone. Call wall at 640 acts as magnet/resistance. The 600 put wall is ~2x larger than the 640 call wall, indicating heavy downside hedging.

## SD Band Implications for 04/06/2026 Expiry
| Level | Lower Bound | Upper Bound | Significance |
|-------|-------------|-------------|--------------|
| 1 SD | 622.52 | 633.48 | ~68% probability price stays within |
| 2 SD | 617.04 | 638.96 | ~95% probability range |
| 2.5 SD | 614.30 | 641.70 | ~99% probability range |

- The **Put Wall (600)** sits below the 2.5 SD lower bound — extreme tail risk protection
- The **Call Wall (640)** aligns near the 2.5 SD upper bound — acts as potential ceiling

## Notable Observations
1. **Heavy Put Hedging:** 4.48M OI at 600 strike suggests institutional hedging against a 4.5% decline
2. **Volatility Compression:** Low ATM IV (~30%) for 3-day expiry indicates market expecting limited movement
3. **Gamma Risk:** Concentrated near spot; any move beyond 1 SD will trigger accelerated hedging flows
4. **Zero Volume:** All contracts show 0 volume — snapshot captured after market close, analysis based on OI only
5. **Bid-Ask Spreads:** Tight spreads (1-3 cents) across most strikes indicate liquid market

## Files Generated
- `spy_options_raw.csv` — Original data
- `spy_options_clean.csv` — Parsed data with IV as decimal
- `analysis.ipynb` — Jupyter notebook (outputs cleared)
- `final_report.html` — Executed HTML report
- `spy_options_analysis.png` — 3-panel IV/Delta/Gamma chart
- `oi_by_strike.png` — Open interest bar charts
- `data_checksums.sha256` — SHA-256 hash of input data
