# SPY Options Analysis Report

## Data Overview
- **Underlying**: SPY
- **Expiration**: 2026-06-12
- **Days to Expiration**: 7
- **Total Options**: 356 (180 calls, 176 puts)
- **Strike Range**: $400 - $900

## Key Findings

### Spot Price Estimate
Using put-call parity, the estimated SPY spot price is **$734.40**.

### Volatility Smile
The volatility smile shows implied volatility across strikes. ATM IV is approximately **16.14%**.

### Standard Deviation Moves
Based on ATM implied volatility and time to expiration:
- **1σ move**: ±$16.42 (2.24%) → Range: $717.98 - $750.82
- **2σ move**: ±$32.84 (4.47%) → Range: $701.56 - $767.24

### Gamma Flip Level
The maximum gamma (gamma flip point) occurs at strike **$737.00**, which is **$2.60** (0.35%) from spot.

## Charts Generated
1. `volatility_smile.png` - Implied volatility vs strike
2. `volatility_smile_with_sd.png` - IV smile with 1σ and 2σ levels
3. `gamma_flip.png` - Gamma distribution by strike
4. `combined_analysis.png` - Combined view of IV, gamma, and SD levels

## Data Checksum
```
501f2c88e890d2d0d9107d82b29d598c92eaca166dfb0c98685f9b68d1fbf03a  /workspace/input/spy_options.csv
```
