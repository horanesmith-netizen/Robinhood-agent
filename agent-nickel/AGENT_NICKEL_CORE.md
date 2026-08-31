# Agent Nickel Core Strategy — Universal Logic
## Version 1.4

This document defines the universal strategy logic that governs 
all Agent Nickel trading activity regardless of asset class.

This document is governed by the Agent Nickel Constitution (CLAUDE.md).
The Constitution overrides this document in all conflicts.

Asset-class specific rules are defined in:
- AGENT_NICKEL_EQUITIES.md
- AGENT_NICKEL_CRYPTO.md

---

## OPERATING PHILOSOPHY

### Mission

DISCIPLINED, EVIDENCE-BASED GROWTH.

Agent Nickel exists to grow a micro-account by a meaningful amount 
while generating credible evidence of positive expectancy. Growth 
and evidence are equally necessary objectives — a track record with 
no growth is not success, and growth with no statistical basis is 
not evidence, it is luck.

### The Micro-Account Mandate

A micro-account cannot compound meaningfully at capital-preservation- 
only position sizes. Agent Nickel is authorized to size positions 
aggressively enough, within the Constitution's limits, to pursue 
meaningful account growth — not merely to survive.

### Bounded Aggression

Aggression is bounded by the Constitution and by this framework — 
never by feel, never by market conditions "looking favorable," and 
never by frustration with a slow account. A setup either qualifies 
under the defined rules at its defined grade, or it does not. 
Bounded aggression means taking every qualifying setup at its full 
authorized size — not taking unqualified setups, and not undersizing 
qualified ones out of excess caution.

### Opportunity Exploitation vs. Excessive Caution

No trade is the correct outcome when no qualifying setup exists. 
That is discipline, not failure. But declining a qualifying setup, 
or sizing it below its authorized grade, purely because a smaller 
risk feels safer, is not discipline — it is excessive caution, and 
excessive caution is not itself a strategy. The purpose of every 
risk control in this framework is to constrain ruin, not to 
suppress a legitimate, qualifying opportunity.

### Growth, Edge, Execution Quality, and Statistical Confidence

These are four distinct things, and conflating them is a common 
failure mode:
- **Growth** is the account's realized change in equity. It can 
  rise from a real edge, from variance, or from oversizing — the 
  P/L number alone does not distinguish which.
- **Edge** is a demonstrated, positive-expectancy relationship 
  between a setup's conditions and its outcomes, established through 
  a sufficient sample of completed trades.
- **Execution quality** is whether Agent Nickel actually followed 
  its own rules — correct sizing, correct order types, correct 
  stops, correct grading — independent of whether the trade won or 
  lost.
- **Statistical confidence** is how much the sample size and 
  consistency of results justify trusting the measured edge and 
  grade over the small-sample noise that any 5- or 10-trade sequence 
  produces.

Growth without edge, execution quality, and statistical confidence 
is not validation — it is an unexamined winning streak.

### Universal Logic Is Not Universal Proof of Edge

This document defines universal strategy logic.

Universal logic is not universal proof of edge.

Each asset class must independently demonstrate positive expectancy 
under real market conditions before full autonomy is granted 
for that asset class.

Inheriting this framework means inheriting a validated operating 
system — not a validated edge.

The edge must be earned separately in each market.

### Risk Scales With Account Size

The percentage-of-equity risk allocations in this framework are 
calibrated for a micro-account, where even a full-risk loss is a 
small absolute dollar amount. As account equity grows materially 
larger, the same percentage represents a much larger absolute loss 
for the same statistical confidence in the underlying edge. 
Percentage risk per grade must be reassessed and scaled downward as 
equity grows past thresholds materially larger than the account's 
starting size — asset-class strategy files define the specific 
thresholds and revised allocations when that reassessment occurs. 
Growth in account size is not, by itself, evidence that higher 
absolute risk is warranted.

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
4. Confirmation trigger present (Step 4)
5. R:R meets minimum for grade (Step 5) — measured against an independently-identified target, never assumed from the stop distance
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

**Risk-allocation status (Constitution V1.5 Section 4):** the "Differential Risk Allocation" figures below describe a candidate future schedule, not a currently authorized operating allocation. No current strategy is authorized above the Constitution's 3.0% unvalidated/uniform stop-risk ceiling, and any differential schedule above that ceiling requires completed Grade Validation, a specifically defined differential-risk schedule, quantitative risk analysis, and explicit authorization — none of which has occurred for these figures. Until then, every qualifying setup at every grade is sized uniformly at the ceiling authorized by the Constitution and the governing asset-class strategy (currently 3.0% or lower, per Step 5), regardless of grade. Grade classification itself remains fully in effect and is the basis for Grade Validation research — only the capital-at-risk figures below are inactive.

#### Setup 1 Grading:
| Grade | Criteria | Differential Risk Allocation (not currently authorized) |
|-------|----------|----------------|
| A+ | All 6 conditions met | 5% of equity |
| A | 4-5 of 6 conditions met | 3% of equity |
| B | 3 of 6 conditions met | 1.5% of equity |
| No Trade | Fewer than 3 | 0% |

#### Setup 2 Grading (own scale):
| Grade | Criteria | Differential Risk Allocation (not currently authorized) |
|-------|----------|----------------|
| A+ | Aggressive regime + volume >1.5x + clean range + strong momentum | 5% of equity |
| A | Aggressive regime + volume >1.3x + clean range | 3% of equity |
| B | Selective regime + volume above average | 1.5% of equity |

#### Setup 3 Grading (own scale):
| Grade | Criteria | Differential Risk Allocation (not currently authorized) |
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
- Entry: Close of confirmation candle, order type per Step 8

#### Trigger 2: Close Above Candle
- Current candle closes above the HIGH of the previous candle
- Entry: Close of that candle, order type per Step 8

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
Risk $ = Account Equity × Risk % (by grade, subject to Constitution V1.5 Section 4 — currently the 3.0% unvalidated/uniform ceiling or lower, uniform across grades; NOT the Differential Risk Allocation figures in Step 3, which are not currently authorized)
Stop Distance % = |Entry Price - Stop Price| ÷ Entry Price
Risk-Based Position Size $ = Risk $ ÷ Stop Distance %

### Exposure Ceiling (Constitution V1.5 Section 5)

Risk-based sizing alone is not sufficient — a very tight stop distance can otherwise produce a risk-based position size far larger than any reasonable notional exposure. Per the Constitution's most-restrictive-rule, position size is also bounded by the applicable single-position notional exposure ceiling:

Exposure-Based Position Size $ = Exposure Ceiling % × Account Equity

Final Position Size $ = MIN(Risk-Based Position Size $, Exposure-Based Position Size $, available unleveraged buying power)

Whichever constraint binds determines the actual position size. If the exposure ceiling binds, effective planned account risk is lower than the nominal risk-based figure — this is a deterministic reduction, not discretionary undersizing, and must be recorded in the journal (Step 9).

The applicable exposure ceiling is defined by the governing asset-class strategy file, subject to the Constitution's 60% absolute never-exceed boundary — CORE does not set or infer one. If no asset-class-authorized exposure ceiling exists for the instrument being traded, exposure cannot be verified:

**DO NOT TRADE.**

### Stop Placement
- Long trades: Below zone OR below trigger candle wick — 
  whichever is LOWER — plus 0.2% buffer
- Never place stop inside the zone

### Take Profit

Take Profit is set independently of the required R:R minimum — it is never calculated by applying an R:R multiple to the stop distance. Doing so makes the R:R gate tautological: projected R:R would always exactly equal whichever minimum it is checked against, and could never actually fail.

Instead, Take Profit is the nearest genuine, independently-identified market structure level beyond entry in the trade's direction:

- **Setup 1 (Trend Continuation at Structure):** the Counter-Trend Zone already identified in Step 2b — the next significant opposing structure level. If no valid Counter-Trend Zone exists, condition 5 (Step 3) cannot be evaluated and Setup 1 does not qualify: NO TRADE.
- **Setup 2 (Session Breakout) and Setup 3 (Volatility Compression Breakout):** the nearest independently-identified major support/resistance level beyond the breakout point, per the asset-class strategy's defined target methodology. If no such level can be identified, the setup does not qualify: NO TRADE.

Never predict or estimate the target level in place of an actual identified structure level, and never widen or move the target merely to force a required R:R to be met.

Projected R:R is then MEASURED, not assumed:

Projected R:R = (Take Profit − Entry) ÷ (Entry − Stop)

Minimum R:R by grade:
- A+: 3:1
- A: 2.5:1
- B: 2:1

This is now a genuine, falsifiable qualification gate — a setup with an independently-identified target too close to entry can and will fail it. To determine the grade a setup actually qualifies for:

1. Measure Projected R:R once, from the independently-identified target.
2. Starting from the highest grade the setup's *other* conditions (excluding the R:R condition itself) would otherwise support, check whether measured R:R meets that grade's minimum.
3. If it does not, step down one grade (A+ → A → B) and recheck, provided the setup's other conditions still support that lower grade.
4. If measured R:R does not meet even B's 2:1 minimum, the setup does not qualify at any grade: NO TRADE.

Report the measured R:R — not an assumed one — in the trade proposal (Step 6).

### Partial Exit Rules
- At 1.5R: Move stop to breakeven. No partial exit.
- At 2R: Exit 50% of position at limit.
- Remaining 50%: Trail stop to prior swing low/high 
  on one timeframe below primary.
- Final exit: Trailing stop hit OR next major S/R level.

### Time Stop
- If trade has not moved 0.5R in either direction 
  after 3 primary timeframe candles: exit via the
  order type authorized for this scenario (Step 8).
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
PROPOSED ENTRY: $[X] (order type per Step 8)
POSITION SIZE: $[X] ([X]% of equity — binding constraint: risk-based / exposure-based / buying power)
CAPITAL AT RISK: $[X] ([X]% of equity)
STOP LOSS: $[X]
TAKE PROFIT: $[X] (independently-identified target, Step 5; 50% exit at 2R / trail remainder)
PROJECTED R:R (measured against target, not assumed): [X]:1
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

Per Constitution V1.5 Section 8: passive bounded execution is the default. Marketable-limit execution is an exception — the Constitution does not enumerate a fixed list of eligible scenarios; it requires only (1) explicit authorization in the governing strategy and (2) a documented execution-speed rationale, with any authorized tolerance capped at the Constitution's absolute 1.0% ceiling. CORE, itself a governing document under the Constitution's hierarchy (Section 1), exercises that delegated authority below for the scenarios where a universal rationale applies; anything not explicitly authorized here or by the applicable asset-class strategy remains passive limit by default. An asset-class strategy may impose a stricter rule than CORE's defaults below (e.g., passive-limit-only for a given scenario), but may not authorize a scenario or tolerance beyond what CORE and the Constitution permit.

| Scenario | Order Type |
|----------|-----------|
| Standard entry at zone (Setup 1) | Passive limit, within the asset-class strategy's authorized entry range |
| Breakout entry (Setup 2/3) | Passive limit by default. Marketable limit only if the asset-class strategy explicitly authorizes it for this scenario with a documented execution-speed rationale, at a tolerance it sets — never exceeding the Constitution's absolute 1.0% ceiling |
| Stop loss | Limit order at stop price |
| Take profit | Limit order at target price |
| Time stop exit | Passive limit by default. Marketable limit only if the asset-class strategy explicitly authorizes it for this scenario (passive limits not filling is CORE's rationale for permitting this exception), at a tolerance it sets — never exceeding the Constitution's absolute 1.0% ceiling |
| Emergency exit | Marketable limit, authorized directly by CORE — see rationale below. Tolerance set by the asset-class strategy, or the Constitution's absolute 1.0% ceiling if the asset-class strategy sets none |
| True market orders | NEVER — prohibited by Constitution |

**Emergency exit — CORE authorization.** Constitution V1.5 Section 8 does not enumerate a fixed list of scenarios eligible for marketable-limit execution; it requires only explicit authorization in the governing strategy plus a documented execution-speed rationale, capped at the absolute 1.0% tolerance ceiling. CORE exercises that delegated authority here: marketable-limit execution is explicitly authorized for emergency/fail-safe exits triggered by a constitutional circuit breaker. Documented rationale: during an emergency exit, execution speed is paramount, and the risk of a passive limit failing to fill is the least acceptable outcome of any exit scenario in this framework — the entire purpose of an emergency exit is to guarantee the position closes, not to optimize the closing price. Tolerance is capped at the Constitution's absolute 1.0% ceiling; an asset-class strategy may authorize a tighter tolerance for its instrument, or may impose a stricter rule (e.g., passive-limit-only) if warranted for that instrument's liquidity characteristics, but may not exceed 1.0% or extend this authorization to any scenario other than an emergency/circuit-breaker exit.

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
Sizing constraint that bound (risk-based / exposure-based / buying power):
Capital at risk ($):
Stop price:
Take profit price (independently-identified target used):
Projected R:R (measured against target, not assumed):
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

## LEVELS OF VALIDATION

Agent Nickel's validation is not a single pass/fail — it operates at 
four independent levels, and passing one does not imply passing 
another:

### Framework Validation
Confirms that the CORE pipeline itself — regime classification, 
scanning, grading, sizing, proposal, approval, execution, and 
journaling — operates correctly and produces well-formed, 
rule-following proposals. This validates the operating system, not 
any market edge.

### Strategy Validation
Confirms that a specific approved setup (e.g., a particular reclaim 
or breakout pattern in a specific asset class) demonstrates positive 
expectancy over a sufficient sample of completed trades in that 
market. Framework validation does not imply strategy validation — a 
well-run pipeline can still execute a setup with no real edge.

### Grade Validation
Confirms that the A+/A/B grading tiers within a validated strategy 
actually correlate with better real-world outcomes — i.e., that A+ 
setups genuinely outperform B setups by enough to justify their 
larger risk allocation. Grade validation is independent of, and 
comes after, strategy validation: a strategy can show positive 
expectancy overall while its internal grading scheme remains 
unproven. Until grade validation is achieved for a given strategy, 
that strategy's asset-class file may elect to size all qualifying 
setups uniformly rather than by grade — that is a valid, 
evidence-respecting choice, not a deviation requiring justification.

### Autonomy Validation
Confirms that a specific asset class has met the numeric autonomy 
gate defined below and been granted explicit authorization to trade 
without per-trade approval. Autonomy validation is asset-class- 
specific and does not transfer.

Passing a lower level does not grant a higher one. Framework 
validation does not imply strategy validation. Strategy validation 
does not imply grade validation. None of the three imply autonomy 
validation, which additionally requires explicit user authorization.

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

## INITIAL VALIDATION HORIZON

Agent Nickel's initial live-validation program should be evaluated
over approximately 60–90 calendar days.

The purpose of this horizon is not to achieve a predetermined dollar
account balance.

The objective is to accumulate sufficient live evidence to evaluate:

- strategy expectancy;
- execution reliability;
- drawdown behavior;
- regime dependence;
- setup-grade predictive value;
- and readiness for continued validation, expanded scope, increased
  capital allocation, or autonomy.

### Classification

At the end of the evaluation horizon, results must be classified as
one of the following, based on the totality of evidence rather than
trade count or calendar elapsed alone:

- **PROMISING** — positive expectancy with supporting execution,
  regime, and grade evidence. Warrants continuing or expanding
  validation.
- **INCONCLUSIVE** — the available sample or evidence is not
  sufficient to make a responsible determination. Validation
  continues unchanged; the strategy is not altered merely to force
  an answer.
- **NEGATIVE** — evidence indicates the tested strategy likely lacks
  sufficient expectancy under the conditions observed. The strategy
  is not scaled; it is diagnosed before any further live deployment.

A small sample with weak, noise-level effect size (e.g., marginally
positive expectancy over very few trades) should generally be
classified INCONCLUSIVE, not PROMISING — a positive number alone is
not evidence of edge, per the growth/edge/execution-quality/
statistical-confidence distinction above. Conversely, a strong,
consistent effect across regimes with a modest sample may be
classified PROMISING even if it falls short of any specific
trade-count target.

### Benchmark Reference

This section does not define its own numeric thresholds for what
qualifies as PROMISING. Evaluate results against the Universal
Autonomy Gate minimums defined above, as specialized by the
applicable active asset-class strategy file (e.g.,
AGENT_NICKEL_EQUITIES.md's autonomy gate section for Track 1). Those
numbers are the operative benchmark; this section governs only how
the calendar horizon and evidence quality are weighed together
against them — not what specific expectancy or profit-factor figures
qualify. If the Universal Autonomy Gate or an asset-class file's
specialization of it changes, classification under this section
changes with it automatically; this section does not need to be
re-amended to stay in sync.

### Classification Is a Human Decision

Agent Nickel may calculate the relevant metrics, summarize the
evidence, and recommend a classification at the end of the horizon.
The final PROMISING / INCONCLUSIVE / NEGATIVE determination is made
by the user, not autonomously by Agent Nickel or by Claude Code
acting on its behalf.

A classification, however determined, grants no additional authority
by itself. It does not itself authorize increased risk, expanded
scope, additional capital allocation, or autonomy — any of those
still requires its own separate, explicit authorization per the
Constitution and the applicable strategy file.

### Calendar Discipline

Expiration of the 60–90-day horizon does not itself authorize
increased risk, expanded scope, or autonomy, nor does it require
abandonment of an otherwise promising strategy when the available
sample remains insufficient.

Calendar pressure must never be used to manufacture trades, weaken
setup requirements, increase unauthorized risk, or otherwise alter
strategy discipline. If the horizon elapses with an INCONCLUSIVE
result, the correct response is to continue validation under
unchanged rules — not to loosen the strategy in search of a faster
answer. This is the same principle as Distinguishing Strategy
Failure from Discipline above, applied to the calendar instead of to
a losing streak.

---

## VERSION HISTORY
- v1.4: Correction to v1.3's characterization of Constitution V1.5
  Section 8, not a new architectural change. v1.3 described Section 8
  as naming a fixed list of two marketable-limit exceptions (breakout
  entries, time-stop exits) and treated "emergency exit" as therefore
  unauthorizable by CORE. That was wrong: the actual ratified Section
  8 text imposes a general rationale-based standard -- explicit
  authorization in the governing strategy plus a documented
  execution-speed rationale, capped at the 1.0% absolute tolerance
  ceiling -- with no enumerated list at all. That enumeration was
  V1.4-Constitution language, removed during the V1.5 rearchitecture.
  Corrected every place in this document that carried the false
  "named exceptions" framing (Step 8's intro note and table, and the
  v1.3 Version History entry above). Emergency/fail-safe exits under
  a constitutional circuit breaker are now explicitly authorized for
  marketable-limit execution as one of CORE's own defined execution
  scenarios (Step 8), exercising CORE's own delegated tier-2 authority
  under Section 8's general standard -- not CORE granting itself
  something the Constitution withheld. Documented rationale: during
  an emergency exit, execution speed is paramount and a passive
  limit's non-fill risk is the least acceptable outcome of any exit
  scenario in this framework. Tolerance remains capped at the
  Constitution's absolute 1.0% ceiling; an asset-class strategy may
  still impose a stricter rule for its instrument.
- v1.3: Reconciled against Constitution V1.5. Three fixes:
  1. **R:R tautology (Step 5, Take Profit).** Take Profit was
     previously calculated as Entry + (Stop Distance × R:R multiple)
     — meaning projected R:R always exactly equaled whatever minimum
     it was checked against, and could never actually fail. Take
     Profit is now set independently, from a genuine identified
     market-structure level (Setup 1: the Counter-Trend Zone already
     identified in Step 2b, previously defined but unused; Setup 2/3:
     the nearest independently-identified S/R level per the
     asset-class strategy). Projected R:R is now measured against
     that target, not assumed, and the minimum-R:R-by-grade table is
     a genuine, falsifiable gate with an explicit grade-recalculation
     procedure. No independent target identifiable = NO TRADE.
  2. **Marketable-limit defaults swept against Constitution V1.5
     Section 8 (Step 8's Order Types table, Step 4's entry triggers,
     Step 5's Time Stop, and Step 6's proposal template).** [Note:
     this entry's original characterization of Section 8 as naming a
     fixed list of two exceptions was corrected in v1.4 below --
     Section 8 actually imposes a general rationale-based standard,
     not an enumerated list.] Marketable-limit execution requires the
     asset-class strategy's own explicit authorization, documented
     execution-speed rationale, and tolerance (capped at the
     Constitution's absolute 1.0% ceiling) for scenarios CORE has not
     itself authorized -- CORE no longer pre-authorizes a tolerance
     for any scenario on its own initiative. "Standard entry at
     zone," which CORE previously defaulted to marketable limit, is
     now passive limit by default, matching what
     AGENT_NICKEL_EQUITIES.md had already independently done to stay
     compliant.
  3. **Setup-grading risk tables (Step 3) and the SIZE step (Step 5)
     reconciled against V1.5 Sections 4 and 5.** The Step 3 A+/A/B
     "Risk Allocation" figures (5%/3%/1.5%) are relabeled as a
     candidate future differential schedule, explicitly not currently
     authorized -- matching V1.5 Section 4's replacement of the old
     permanent A+/A/B ceilings and its requirement that any future
     differential schedule pass Grade Validation plus explicit
     authorization first. Step 5's SIZE formula now applies the
     Constitution's most-restrictive-rule explicitly: Final Position
     Size = MIN(risk-based size, exposure-based size, buying power).
     This is the CORE-level mechanism for V1.5 Section 5's new
     notional-exposure-risk category; it does not depend on knowing
     any asset-class file's actual exposure ceiling number, and
     correctly forces "DO NOT TRADE" for any asset class -- currently
     equities -- that has not yet authorized one, structurally
     enforcing the blocker already flagged in
     AGENT_NICKEL_EQUITIES.md v2.2.
  Pipeline step order, regime classification, setup-type definitions
  (aside from the R:R condition described above), partial-exit and
  time-stop mechanics (aside from order-type sourcing), and autonomy
  gate criteria are otherwise unchanged.
- v1.2: Added INITIAL VALIDATION HORIZON — establishes that Agent
  Nickel's initial live-validation program is evaluated over
  approximately 60–90 calendar days against a PROMISING /
  INCONCLUSIVE / NEGATIVE classification based on evidence quality,
  not a dollar target or raw trade count. Placed here rather than in
  an asset-class strategy file because it is an experiment-level
  objective, not a setup-specific trading mechanic — it applies
  uniformly to any current or future asset class. References the
  existing Universal Autonomy Gate minimums as its benchmark rather
  than defining new numeric thresholds, so the two stay in sync
  automatically. Makes explicit that classification is a human
  decision, that it grants no authority by itself, and that calendar
  pressure must never be used to manufacture trades, weaken setup
  criteria, or increase risk. Motivated by an explicit decision to
  decouple Agent Nickel's validation window from any personal dollar
  deadline.
- v1.0: Initial release — equities and crypto tracks established
- v1.1: Reconciled with the updated Agent Nickel mission (disciplined,
  evidence-based growth of a micro-account, bounded aggression).
  Added OPERATING PHILOSOPHY (mission, micro-account mandate, bounded
  aggression, opportunity exploitation vs. excessive caution,
  growth/edge/execution-quality/statistical-confidence distinction,
  risk-scales-with-account-size principle) and LEVELS OF VALIDATION
  (framework / strategy / grade / autonomy validation are independent
  and do not imply one another). Pipeline mechanics, setup grading,
  position sizing, failure conditions, and autonomy gate criteria are
  unchanged.
