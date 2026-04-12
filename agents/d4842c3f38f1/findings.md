# SPY Options Chain Analysis — 04/06/2026 Expiry

## Overview
- **Spot Price (S):** $628.00 (approximate SPY close on 4/3/2026)
- **Expiry:** 04/06/2026
- **Days to Expiry:** 3 trading days
- **Risk-Free Rate:** 4.5%

---

## ATM Implied Volatility & Expected Moves

- **ATM IV:** ~30.36% (at 630 strike, nearest to spot)
- **Expected 1SD Move (3 days):** ±$5.47 pts
- **1 SD Range:** [622.53, 633.47]
- **2 SD Range:** [617.06, 638.94]
- **2.5 SD Range:** [614.33, 641.67]

**Interpretation:** With only 3 days to expiry, the market expects SPY to move approximately ±$5.47 (±0.87%) within 1 standard deviation. This is a relatively low expected move, suggesting market calm near-term.

---

## IV Smile Shape & Skew

- **Put Skew:** OTM puts (lower strikes) show elevated IV: 37.19% at 670 strike vs 31.30% at ATM
- **Call Wing:** OTM calls (higher strikes) show moderate IV elevation: 53.13% at 560 vs 30.36% at ATM
- **Put vs Call OTM Spread:** At equidistant OTM strikes (560 vs 670), puts show 53.19% vs calls at 31.97% — **significant put skew**

**Direction of Skew:** Classic "volatility smirk" with pronounced put skew, indicating market hedging demand for downside protection. Deep OTM puts command premium IV due to crash risk pricing.

---

## Gamma Risk Profile

- **Max Call Gamma:** 0.031 at 625 strike
- **Max Put Gamma:** 0.031 at 630 strike
- **Gamma Concentration:** Peaks near ATM (625-630 strikes)

**Market Maker Hedging Implications:**
- Gamma is highest at-the-money, meaning market makers have maximum delta sensitivity in the 625-630 zone
- If SPY moves sharply through 625-630, dealers must dynamically hedge, potentially amplifying volatility
- This is the "gamma pinning" zone where price tends to cluster near expiry

---

## Open Interest Analysis

### Call Open Interest
- **Max Call OI:** 1,527,407 contracts at **640 strike**
- **Secondary Peaks:** 1,266,455 at 635 strike, 1,135,742 at 630 strike
- **Call Wall:** 640 strike represents significant resistance overhead

### Put Open Interest
- **Max Put OI:** 4,481,508 contracts at **600 strike**
- **Secondary Peaks:** 4,015,097 at 610 strike, 3,890,721 at 620 strike
- **Put Wall:** 600 strike is the major support level

**OI Interpretation:**
- Massive put OI at 600 strike creates a "put wall" — potential magnet for expiry
- Call OI concentrated at 640 defines overhead resistance
- The 600-640 range encapsulates the expected trading range with structural support/resistance

---

## SD Band Implications for 04/06/2026 Expiry

| Band | Lower Bound | Upper Bound | Probability |
|------|-------------|-------------|-------------|
| 1 SD | 622.53 | 633.47 | 68.3% |
| 2 SD | 617.06 | 638.94 | 95.4% |
| 2.5 SD | 614.33 | 641.67 | 98.8% |

**Trading Observations:**
- Spot (628) sits within the 1 SD range, suggesting current pricing is fair
- Put wall at 600 is 2.5 SD below spot — unlikely to be breached statistically
- Call wall at 640 is 2 SD above spot — moderate resistance
- Short-term straddles/strangles priced around ATM IV of ~30% are fairly valued given the tight SD bands

---

## Notable Anomalies & Observations

1. **Zero Volume Across All Strikes:** All contracts show 0 volume — this may be a snapshot at market close or data capture issue. OI is the meaningful metric here.

2. **Deep OTM Call IV Spike:** 560 strike call shows 53.13% IV — unusually high. This may reflect tail risk pricing or data artifact.

3. **Put/Call OI Ratio:** Massive bearish positioning with 4.4M puts at 600 vs 1.5M calls at 640. The market is heavily hedged for downside.

4. **Gamma Asymmetry:** Similar gamma peaks for calls and puts near ATM, but put gamma extends further OTM due to higher IV in put wing.

---

## Files

- `spy_options_raw.csv` — Raw options chain data
- `spy_options_clean.csv` — Parsed data with IV as decimal
- `analysis.ipynb` — Jupyter notebook (outputs cleared for git)
- `final_report.html` — Executed HTML report (code hidden)
- `spy_options_analysis.png` — 3-panel plot: IV smile, Delta, Gamma
- `oi_by_strike.png` — Open Interest by strike for calls and puts
- `data_checksums.sha256` — SHA-256 hash of input data
- `requirements.txt` — Python environment snapshot

---

## Reproducibility

- Input data hashed: see `data_checksums.sha256`
- Analysis runs top-to-bottom in `analysis.ipynb`
- All parameters documented above
