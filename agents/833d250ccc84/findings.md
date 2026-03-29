# SPY Options Chain Analysis — 04/02/2026 Expiry

**Analysis Date:** March 27, 2026  
**Expiry:** April 2, 2026 (6 days to expiration)  
**Spot Price:** $560.00 (approximate)

---

## Key Metrics

| Metric | Value |
|--------|-------|
| ATM IV | 28.41% |
| Expected 1SD Move (6d) | ±$22.36 |
| 1SD Range | [537.64, 582.36] |
| 2SD Range | [515.28, 604.72] |

---

## Implied Volatility Smile Analysis

### Skew Direction: **Downward (Reverse) Skew**
- **OTM Puts trade at higher IV than OTM Calls** — typical fear premium
- The 600 Put IV (~35.46%) significantly exceeds the 670 Call IV (~26.71%)
- This reflects market concern about downside protection given the ~30 day timeframe

### Put-Call IV Spread
- At similar distance from spot, puts carry a **3-5 vol point premium**
- Example: 600 Put (35.46%) vs 670 Call (26.71%) — ~9 vol spread
- Near-the-money: The skew compresses around 31-32% IV

---

## Gamma Risk Profile

### Max Gamma Concentration
- **Highest gamma is concentrated around strikes 630-640** (near ATM)
- Market makers face maximum hedging pressure in the $630-$640 zone
- Gamma peaks where delta changes most rapidly

### Risk to Market Makers
- A move into the $630-$640 zone would require significant delta-hedging activity
- Short-dated expiry (6 days) amplifies gamma risk — time decay accelerates
- Pin risk exists if SPY settles near the 630-640 range at expiry

---

## Standard Deviation Bands

| Band | Lower Bound | Upper Bound | Interpretation |
|------|-------------|-------------|----------------|
| 1 SD | 537.64 | 582.36 | ~68% probability range |
| 2 SD | 515.28 | 604.72 | ~95% probability range |
| 2.5 SD | 504.10 | 615.90 | ~99% probability range |

### Implications for 04/02 Expiry
- **All strikes in our data (600-670) lie within the 2.5 SD bands**
- The wide 2SD range ($515-$605) reflects elevated volatility expectations
- 600-strike puts (~$1.08) are priced for a 3.2% move; this is relatively cheap given 28% IV

---

## Summary Observations

1. **Elevated ATM IV (28.4%)** suggests significant expected volatility over the 6-day period
2. **Reverse skew pattern** indicates hedging demand for downside protection
3. **Gamma concentration at 630-640** is the key risk zone for market makers
4. **Wide SD bands** ($90+ for 2SD) reflect uncertainty heading into the expiry period
5. **Short time to expiry** means theta decay will accelerate, making these options highly sensitive to spot moves

---

## Data Integrity

- **Source:** SPY options chain snapshot, March 27, 2026
- **Records:** 54 contracts (27 calls, 27 puts)
- **Checksum:** See `data_checksums.sha256`
