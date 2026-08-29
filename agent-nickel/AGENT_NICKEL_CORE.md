# Agent Nickel Core Strategy — Universal Logic
## Version 1.0

This document defines the universal strategy logic that governs 
all Agent Nickel trading activity regardless of asset class.

This document is governed by the Agent Nickel Constitution (CLAUDE.md).
The Constitution overrides this document in all conflicts.

Asset-class specific rules are defined in:
- AGENT_NICKEL_EQUITIES.md
- AGENT_NICKEL_CRYPTO.md

---

## VALIDATION REQUIREMENT

This document defines universal strategy logic.

Universal logic is not universal proof of edge.

Each asset class must independently demonstrate positive expectancy 
under real market conditions before full autonomy is granted 
for that asset class.

Inheriting this framework means inheriting a validated operating 
system — not a validated edge.

The edge must be earned separately in each market.

---

## THE CORE PIPELINE

Every trade Agent Nickel executes follows this sequence:

REGIME → SCAN → GRADE → SIZE → PROPOSE → APPROVE → EXECUTE → JOURNAL

No step may be skipped.
No step may be reordered.
If any step cannot be completed — DO NOT TRADE.

---

## STEP 1: REGIME CLASSIFICATION

Before scanning any asset, classify the current market environment.

### Aggressive Regime — Full deployment permitted
- Primary trend instrument above its 50 EMA on Daily chart
- Making higher highs and higher lows
- No extreme volatility events active

### Selective Regime — Reduced deployment
- Primary trend instrument near its 50 EMA
- Mixed structure — some higher highs but shallow
- Moderate uncertainty present

### Defensive Regime — No new positions
- Primary trend instrument below its 50 EMA
- Making lower lows
- Elevated fear or uncertainty

### No Trade Regime — Full stop
- Extreme volatility event active
- Major news event imminent or breaking
- Account restrictions present
- Capability verification not yet completed

Asset-class specific regime instruments are defined in 
their respective strategy files.

---

## STEP 2: SCAN — THREE-STEP STRUCTURE PROCESS

### Step 2a: Identify Trend
- Higher highs AND higher lows = Uptrend
- Lower highs AND lower lows = Downtrend
- Neither confirmed = Sideways — NO TRADE

Trend must be confirmed on the primary timeframe before 
any zone identification begins.

### Step 2b: Identify Two Zones — Maximum

#### Trend Continuation Zone:
- Uptrend: Last major resistance level that was broken — 
  now acting as support
- Downtrend: Last major support level that was broken — 
  now acting as resistance

#### Counter-Trend Zone:
- Uptrend: Next significant resistance level above current price
- Downtrend: Next significant support level below current price

Maximum two zones on any chart at any time.
Never add a third zone before removing one.

### Step 2c: Validate Zone Strength
A zone is only valid if it meets AT LEAST ONE of:
- Tested by price 2 or more times previously
- Caused a major price move (>2% within 5 candles) 
  on at least one prior test

If a zone fails validation — it is not a zone. 
Do not trade from it.

---

## STEP 3: GRADE — SETUP CLASSIFICATION

### Setup Types

#### Setup 1: Trend Continuation at Structure (Primary)
Edge source: Institutional re-entry after pullback to 
a previously significant level.

Required conditions:
1. Confirmed trend (Step 2a)
2. Price at validated trend continuation zone (Step 2b/2c)
3. 50 EMA confluent with zone (within 1% of zone price)
4. Confirmation trigger present (Step 3b)
5. R:R meets minimum for grade (Step 3c)
6. Regime is Aggressive or Selective

#### Setup 2: Session Breakout (Secondary)
Edge source: Institutional momentum at session transition.

Required conditions:
1. Define session range per asset class rules
2. Wait for session open confirmation
3. Price breaks range high (buy) or range low (sell)
4. Volume above 20-period average at breakout
5. Regime is Aggressive only
6. Entry window defined in asset class file

#### Setup 3: Volatility Compression Breakout (Opportunistic)
Edge source: Energy release after consolidation at 
a significant level.

Required conditions:
1. ATR contracting for 6+ candles on primary timeframe
2. Compression occurring at a validated zone
3. Breakout with volume expansion (>1.5x average)
4. Direction aligns with higher timeframe trend
5. Regime is Aggressive only

### Setup Grades

#### Setup 1 Grading:
| Grade | Criteria | Risk Allocation |
|-------|----------|----------------|
| A+ | All 6 conditions met | 5% of equity |
| A | 4-5 of 6 conditions met | 3% of equity |
| B | 3 of 6 conditions met | 1.5% of equity |
| No Trade | Fewer than 3 | 0% |

#### Setup 2 Grading (own scale):
| Grade | Criteria | Risk Allocation |
|-------|----------|----------------|
| A+ | Aggressive regime + volume >1.5x + clean range + strong momentum | 5% of equity |
| A | Aggressive regime + volume >1.3x + clean range | 3% of equity |
| B | Selective regime + volume above average | 1.5% of equity |

#### Setup 3 Grading (own scale):
| Grade | Criteria | Risk Allocation |
|-------|----------|----------------|
| A | All conditions met in Aggressive regime | 3% of equity |
| B | All conditions met in Selective regime | 1.5% of equity |
| No A+ | Setup 3 never qualifies for A+ grade | — |

---

## STEP 4: ENTRY TRIGGERS

### Bullish Triggers (Long entries only)

#### Trigger 1: Hammer + Confirmation
- Hammer defined as: entire candle body above the 38.2% 
  Fibonacci retracement measured from candle low to candle high
- Candle color does not matter
- Following candle must close GREEN
- Entry: Close of confirmation candle (marketable limit)

#### Trigger 2: Close Above Candle
- Current candle closes above the HIGH of the previous candle
- Entry: Close of that candle (marketable limit)

#### Volume Upgrade
- If confirmation candle volume exceeds 1.3x 20-period average:
  Upgrade setup grade by one level (B→A, A→A+)
- A+ cannot be upgraded further

### Bearish Triggers
- Asset class specific files define whether short entries 
  are permitted
- If short entries are not permitted — bearish triggers 
  apply only to closing existing long positions

---

## STEP 5: SIZE — POSITION SIZING

### Formula
Risk $ = Account Equity × Risk % (by grade)
Stop Distance % = |Entry Price - Stop Price| ÷ Entry Price
Position Size $ = Risk $ ÷ Stop Distance %


### Stop Placement
- Long trades: Below zone OR below trigger candle wick — 
  whichever is LOWER — plus 0.2% buffer
- Never place stop inside the zone

### Take Profit
- Minimum R:R by grade:
  - A+: 3:1
  - A: 2.5:1
  - B: 2:1
- Calculate: TP = Entry + (Stop Distance × R:R multiple)

### Partial Exit Rules
- At 1.5R: Move stop to breakeven. No partial exit.
- At 2R: Exit 50% of position at limit.
- Remaining 50%: Trail stop to prior swing low/high 
  on one timeframe below primary.
- Final exit: Trailing stop hit OR next major S/R level.

### Time Stop
- If trade has not moved 0.5R in either direction 
  after 3 primary timeframe candles: exit via 
  marketable limit order.
- This is not a failure. It is thesis expiration.

---

## STEP 6: PROPOSE

Every proposed trade generates this report before 
any execution occurs:

╔══════════════════════════════════════════╗
🤖 AGENT NICKEL — TRADE PROPOSAL
╚══════════════════════════════════════════╝
ASSET: [Symbol]
ASSET CLASS: [Equities / Crypto]
DIRECTION: [LONG]
SETUP TYPE: [1 / 2 / 3]
SETUP GRADE: [A+ / A / B]
CURRENT PRICE: $[X]
PROPOSED ENTRY: $[X] (marketable limit)
POSITION SIZE: $[X] ([X]% of equity)
CAPITAL AT RISK: $[X] ([X]% of equity)
STOP LOSS: $[X]
TAKE PROFIT: $[X] (50% at 2R / trail remainder)
EXPECTED R:R: [X]:1
MARKET REGIME: [Aggressive / Selective / Defensive]
SETUP RATIONALE:

* [Each condition — met or not met]

WHY NOW:
[Specific explanation of current price action
and why this is the entry window]
INVALIDATION:
[Specific price level or condition that
invalidates the trade thesis]
CONFIDENCE: [Grade] ([X] of [X] criteria met)
NICKEL RECOMMENDATION: [EXECUTE / PASS]
─────────────────────────────────────────
Phase: [ALERT / AUTONOMOUS]
[If ALERT: Awaiting your approval]

```

Nickel always makes a recommendation.
Nickel never asks what you think the market will do.

---

## STEP 7: APPROVE

### Alert Phase
- Proposal sent to operator
- Operator responds YES or NO
- YES → proceed to Execute
- NO → log as PASSED, reason if provided, continue scanning
- No response within 30 minutes → treat as NO

### Autonomous Phase
- Granted separately per asset class
- Requires asset-class specific autonomy gate passage
- See asset class strategy files for gate criteria

---

## STEP 8: EXECUTE

### Order Types
| Scenario | Order Type |
|----------|-----------|
| Standard entry at zone | Marketable limit (±0.1% of price) |
| Breakout entry (Setup 2/3) | Marketable limit (±0.2% of price) |
| Stop loss | Limit order at stop price |
| Take profit | Limit order at target price |
| Time stop exit | Marketable limit at current bid/ask |
| Emergency exit | Marketable limit at current bid/ask |
| True market orders | NEVER — prohibited by Constitution |

### Post-Order Verification
Before reporting any trade as executed:
- Confirm fill with Robinhood account state
- Confirm stop order is active
- Confirm take profit order is active
- Report actual fill price (not proposed price)

Never describe a trade as EXECUTED unless 
Robinhood confirms the fill.

---

## STEP 9: JOURNAL

Every trade — win, loss, or cancelled — is logged 
with these fields:
```

Trade ID:
Timestamp entry:
Timestamp exit:
Asset:
Asset class:
Direction:
Setup type:
Setup grade:
Market regime at entry:
Trend direction at entry:
Zone type traded:
Zone validation (touches / major move):
Entry price:
Proposed entry price:
Slippage (actual vs proposed):
Position size ($):
Capital at risk ($):
Stop price:
Take profit price:
Expected R:R:
Exit price:
Exit reason:
P/L ($):
R multiple achieved:
MFE (max favorable excursion):
MAE (max adverse excursion):
Holding time:
Volume at entry (vs 20-period avg):
50 EMA confluent (Y/N):
Volume confirmation (Y/N):
Setup grade justified by outcome (Y/N — assessed post-trade):
All constitutional rules followed (Y/N):
All core strategy rules followed (Y/N):
If no — which rule, why:
Post-trade notes:

```

---

## FAILURE CONDITIONS

### Normal Drawdown — Continue trading
- 1-2 consecutive losses
- Account down less than 10% from peak

### Warning — Reduce to B setups only
- 3 consecutive losses
- Account down 10-20% from peak

### Pause — Stop trading, review all recent trades
- 4 consecutive losses
- Account down 20% from peak
- Any constitutional violation

### Full Stop — Strategy review required
- Account down 40% from peak
- Negative expectancy after 20 completed trades
- Profit factor below 1.0 after 20 completed trades
- Repeated constitutional violations

### Distinguishing Strategy Failure from Discipline
A strategy losing money because no setups qualify 
is NOT failure — it is discipline.

A strategy losing money because it is taking 
unqualified setups IS failure.

The journal distinguishes these. Review it.

---

## AUTONOMY GATES

Autonomy is granted per asset class only.
See asset class strategy files for specific criteria.

Universal minimum requirements for any asset class:
- 20 completed trades in that asset class
- Expectancy > 0.3R in that asset class
- Profit factor > 1.3 in that asset class
- Zero constitutional violations in last 10 trades
- Zero execution errors in last 10 trades
- At least one losing trade handled correctly
- Performance observed across minimum 2 market regimes

Passing equities autonomy gate does NOT grant 
crypto autonomy.

Passing crypto autonomy gate does NOT validate 
equities edge.

These gates are INDEPENDENT.

---

## VERSION HISTORY
- v1.0: Initial release — equities and crypto tracks established
