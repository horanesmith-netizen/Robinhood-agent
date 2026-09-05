# AGENT NICKEL — CRYPTO STRATEGY
## Version 1.1 — RATIFIED — BTC Initial Validation / CR-1

This document defines the active cryptocurrency strategy for Agent Nickel.

It is governed by:
1. `CLAUDE.md` — Agent Nickel Constitution V1.5
2. `AGENT_NICKEL_CORE.md` — Universal Trading Methodology v1.6

Where this document is stricter than CORE or the Constitution, this document governs the Crypto strategy. Where this document conflicts with higher authority, the conflicting provision is void and the affected mechanic may not be used until reconciled.

---

# 1. ACTIVE SCOPE

## 1.1 Initial Validation Cohort

The active Crypto Initial Validation cohort is:

- Instrument: **BTC/USD only**
- Direction: **LONG only**
- Setup: **CR-1 — Trend Continuation at Structure only**
- CORE setup mapping: **Setup 1**
- Maximum concurrent open positions: **1**
- Phase: **Initial Validation**
- Human approval: **Required before every live entry**
- Trading availability: **24/7, subject to all regime, capability, account, approval, and risk gates**

ETH/USD is Constitution-authorized but **inactive** for this cohort.

No other cryptocurrency, direction, or setup is authorized.

Low BTC trade frequency does not authorize ETH, additional setups, weaker qualification standards, or wider execution tolerances.

---

# 2. VALIDATION OBJECTIVE

The purpose of Crypto Initial Validation is to determine whether CR-1 on BTC/USD demonstrates credible positive expectancy under live conditions while Agent Nickel executes the governing framework correctly.

The expected evaluation horizon is approximately **60–90 calendar days**, subject to CORE.

The horizon is an evidence window, not a trade-count quota or dollar deadline.

At the end of the horizon, the evidence may be classified:

- **PROMISING**
- **INCONCLUSIVE**
- **NEGATIVE**

No classification itself expands authority.

---

# 3. AUTHORIZED MARKET DATA AND TIME STANDARD

## 3.1 Market-Data Authority

The exact live market-data source used for BTC/USD qualification must be explicitly identified and capability-verified before live trading.

The authorized source must provide, or permit deterministic construction of:

- completed Daily BTC/USD OHLC candles;
- completed 4H BTC/USD OHLC candles;
- completed 1H BTC/USD OHLCV candles;
- sufficient history for the Daily 50 EMA;
- sufficient 4H history for confirmed structure and zone construction;
- sufficient 1H history for confirmation, volume, and extreme-volatility calculations.

Until the source is identified and verified:

**DO NOT TRADE.**

The broker's account state remains authoritative for account and execution state. The authorized strategy market-data source governs technical qualification.

## 3.2 UTC Standard

All Crypto strategy timestamps use **UTC**.

Daily candles are defined by the authorized source's candle closing at **00:00 UTC**.

4H candles use fixed UTC boundaries:

- 00:00–04:00
- 04:00–08:00
- 08:00–12:00
- 12:00–16:00
- 16:00–20:00
- 20:00–00:00

1H candles begin and end on the UTC hour.

Only **completed candles** may establish regime, structure, zones, validation, confirmation triggers, volume ratios, or extreme-volatility state unless this strategy explicitly says otherwise.

## 3.3 Continuous Technical History

Technical calculations use continuous BTC/USD history across calendar days.

UTC midnight is an accounting and Daily-candle boundary. It does not reset EMA, swing, zone, volume, or volatility history.

## 3.4 Data Integrity

Missing, stale, duplicated, malformed, or materially gapped required market data creates a qualification failure.

If the required calculation cannot be reconstructed deterministically from verified data:

**NO TRADE.**

---

# 4. TIMEFRAME HIERARCHY

CR-1 uses:

- **Daily:** regime trend context
- **4H:** primary structure, swing confirmation, zone construction and zone interaction
- **1H:** entry confirmation, volume research, extreme-volatility filter

The **4H chart is CR-1's primary structure timeframe**.

No lower timeframe may override a failed higher-timeframe requirement.

---

# 5. REGIME CLASSIFICATION

Regime is classified before CR-1 scanning.

Classification follows the precedence below. The first applicable state governs.

## 5.1 NO TRADE — Highest Precedence

Classify **NO TRADE** if any of the following applies:

- required broker/account capability cannot be verified;
- required market-data capability cannot be verified;
- required data are stale, incomplete, or materially gapped;
- account restriction prevents compliant execution;
- an Extreme Volatility Event is active;
- a separately authorized catalyst/news block is active;
- required execution liquidity/spread state cannot be verified where that verification is required;
- any other governing rule requires NO TRADE.

A catalyst/news block is not live-authorized until its source, event categories, lead time, and reset rule are explicitly defined and capability-verified. Until then, Agent Nickel may not invent a news filter during live operation.

## 5.2 DEFENSIVE — No New Positions

If NO TRADE does not apply, classify **DEFENSIVE** when:

- the most recent completed Daily close is below the Daily 50 EMA; **and**
- confirmed 4H structure is bearish: the two most recent confirmed swing highs form a lower high and the two most recent confirmed swing lows form a lower low.

No new CR-1 position may be initiated in Defensive regime.

## 5.3 AGGRESSIVE

If neither NO TRADE nor Defensive applies, classify **AGGRESSIVE** when:

- the most recent completed Daily close is above the Daily 50 EMA;
- confirmed 4H structure is bullish: the two most recent confirmed swing highs form a higher high and the two most recent confirmed swing lows form a higher low;
- no Extreme Volatility Event is active.

## 5.4 SELECTIVE

If none of the states above applies, classify **SELECTIVE** only when:

- the most recent completed Daily close is within **1.0%** of the Daily 50 EMA; and
- confirmed 4H structure remains bullish HH/HL.

For CR-1 Initial Validation, requiring confirmed bullish 4H HH/HL structure in Selective is an explicitly ratified strategy-level **narrowing** of CORE's broader Selective concept, not a redefinition of the universal regime hierarchy. CR-1 intentionally does not activate a broader mixed/shallow-structure Selective state during this cohort.

The Daily-close predicates for Aggressive and Selective can overlap when price is above the Daily 50 EMA while also within 1.0% of it. This overlap is intentional and is resolved deterministically by the stated first-applicable-state precedence: **Aggressive is evaluated before Selective and therefore governs when both predicates are satisfied.**

## 5.5 FALLBACK

Any state that satisfies none of the deterministic classifications above is:

**NO TRADE.**

This fallback prevents subjective interpretation of "mixed," "uncertain," or otherwise undefined market conditions.

---

# 6. EXTREME VOLATILITY FILTER

For each completed 1H candle:

`True Range = max(High − Low, |High − Previous Close|, |Low − Previous Close|)`

`Mean TR20 = arithmetic mean of True Range for the 20 completed 1H candles immediately preceding the candle being tested`

An **Extreme Volatility Event** occurs when:

`Completed 1H True Range > 3.0 × Mean TR20`

The event becomes active immediately after that 1H candle completes.

The event remains active until **three consecutive subsequent completed 1H candles** each have True Range `<= 3.0 ×` their own trailing Mean TR20.

While active:

**NO NEW POSITION.**

This threshold and reset rule are Initial Validation parameters to be logged and researched, not assumed to be validated edge.

---

# 7. 4H STRUCTURE

## 7.1 Confirmed Swing High

A 4H candle is a confirmed swing high when:

- its high is strictly greater than the highs of the two completed 4H candles immediately before it; and
- its high is strictly greater than the highs of the two completed 4H candles immediately after it.

The swing becomes confirmed only after both following candles complete.

Equal highs do not satisfy the strict comparison.

## 7.2 Confirmed Swing Low

A 4H candle is a confirmed swing low when:

- its low is strictly lower than the lows of the two completed 4H candles immediately before it; and
- its low is strictly lower than the lows of the two completed 4H candles immediately after it.

The swing becomes confirmed only after both following candles complete.

Equal lows do not satisfy the strict comparison.

## 7.3 Bullish Structure

Bullish 4H structure requires:

- most recent confirmed swing high > immediately preceding confirmed swing high; and
- most recent confirmed swing low > immediately preceding confirmed swing low.

If both conditions are not present, CR-1 does not have confirmed bullish structure.

## 7.4 Confirmed 1H Swing High

A 1H candle is a confirmed swing high when:

- its high is strictly greater than the highs of the two completed 1H candles immediately before it; and
- its high is strictly greater than the highs of the two completed 1H candles immediately after it.

The swing becomes confirmed only after both following candles complete.

Equal highs do not satisfy the strict comparison.

## 7.5 Confirmed 1H Swing Low

A 1H candle is a confirmed swing low when:

- its low is strictly lower than the lows of the two completed 1H candles immediately before it; and
- its low is strictly lower than the lows of the two completed 1H candles immediately after it.

The swing becomes confirmed only after both following candles complete.

Equal lows do not satisfy the strict comparison.

---

# 8. CR-1 TREND-CONTINUATION ZONE

## 8.1 Zone Creation

A confirmed 4H swing high becomes a candidate broken-resistance reference only when a later completed 4H candle closes strictly above that swing-high price.

The reference price is the broken confirmed swing-high price.

The zone is:

- Upper Bound = `Reference Price × 1.0015`
- Lower Bound = `Reference Price × 0.9985`

The ±0.15% band is an Initial Validation parameter subject to later empirical review. It may not be altered during live validation without formal strategy amendment.

## 8.2 Zone Touch

A completed 4H candle constitutes a zone touch when:

- its range intersects the zone; and
- its close is not more than 0.15% below the zone's Lower Bound.

A touch is recognized only after the 4H candle completes.

## 8.3 Zone Validation

A zone is Validated only from evidence that existed **before the current trade-qualifying touch**.

It qualifies if either:

1. at least **two prior completed touches** occurred; or
2. on at least one prior completed touch, BTC subsequently moved more than **2.0%** above that touch candle's close within the next five completed 4H candles without a completed 4H close below the zone's invalidation threshold.

Future candles may never retroactively validate a current setup.

## 8.4 Zone Invalidation

A zone is invalidated when a completed 4H candle closes more than **0.15% below the Lower Bound**.

Once invalidated, it cannot be traded as CR-1 unless a new qualifying broken-resistance zone is independently created and validated.

## 8.5 Maximum Two Zones / Deterministic Lifecycle

At most two active candidate/validated trend-continuation zones may exist.

When a newly created zone would create a third active zone:

1. remove any already-invalidated zone first;
2. if three non-invalidated zones remain, retain the **two highest reference prices below the most recent completed 4H close**;
3. any other zone is retired from active scanning but remains in the research log.

A retired zone does not automatically reactivate.

---

# 9. CR-1 QUALIFICATION PIPELINE

CR-1 qualification is evaluated in the following fixed order:

1. Candidate Existence Qualification
2. Preliminary Grade
3. Volume Upgrade
4. Independent Target
5. Measured Projected R:R
6. Grade Recalculation / Step-Down
7. Final Trade Qualification

A later step may disqualify a candidate established by an earlier step. No later requirement may be used retroactively to manufacture an earlier qualification.

## 9.1 Step 1 — Candidate Existence Qualification

A BTC/USD CR-1 candidate exists only when all of the following are true:

1. BTC/USD is the active instrument.
2. Direction is LONG.
3. Regime is Aggressive or Selective.
4. Confirmed 4H structure is bullish HH/HL.
5. A previously Validated trend-continuation zone exists.
6. A completed 4H candle has produced a current qualifying Zone Touch.
7. The zone was already Validated before that current touch.
8. The zone remains valid.
9. A qualifying 1H confirmation occurs during the Confirmation Window.
10. All then-applicable risk, exposure, execution, account, data, and capability requirements are satisfied.

Failure of any mandatory Candidate Existence requirement:

**NO TRADE.**

Candidate existence does not itself authorize entry. The candidate must complete Steps 2–7 below.

---

# 10. CONFIRMATION WINDOW

The Confirmation Window begins when the qualifying 4H Zone Touch candle completes.

It ends at the earliest of:

- completion of the next **three 1H candles** after the 4H touch candle;
- zone invalidation;
- regime becoming Defensive or No Trade;
- a new completed 4H candle closing without a qualifying zone touch.

Only 1H candles completed during this window may trigger entry.

This prevents an incomplete 4H interaction from being used to qualify a completed 1H signal and prevents stale confirmations from being attached to old touches.

---

# 11. 1H ENTRY CONFIRMATION

CR-1 authorizes either of two confirmation triggers.

## 11.1 Trigger CR-1A — Upper-Body Rejection + Green Confirmation

A completed 1H signal candle qualifies when:

- its range is non-zero;
- `Body Low = min(Open, Close)`;
- `38.2% Level = Low + 0.382 × (High − Low)`;
- `Body Low > 38.2% Level`.

The immediately following completed 1H candle must close above its open.

The trigger occurs at the completion of that following green confirmation candle.

This mechanic is intentionally named **Upper-Body Rejection**, not "Hammer," because the rule does not independently require traditional hammer wick/body proportions.

## 11.2 Trigger CR-1B — Close Above Prior High

A completed 1H candle qualifies when:

`Current Close > Immediately Prior Completed 1H High`

The trigger occurs when that candle completes.

## 11.3 Trigger Price

The trigger price is the completed confirmation candle's close.

The trigger price is a qualification reference, **not a guaranteed fill price**.

---

# 12. PRELIMINARY GRADE AND VOLUME UPGRADE

Grade remains a research classification during Initial Validation. It does not change capital allocation.

## 12.1 Step 2 — Preliminary Grade

Two pre-volume grade conditions are evaluated:

**Condition D — Daily EMA Confluence**
- Daily 50 EMA is within **1.0% of the active zone Reference Price**.

**Condition R — Aggressive Regime**
- Current regime is Aggressive.

Preliminary grade:

- both conditions true → **A**
- exactly one true → **B**
- neither true → **NO TRADE**

If neither condition is true:

**NO TRADE.**

## 12.2 Step 3 — Volume Upgrade

For the completed 1H confirmation candle:

`Volume Ratio = confirmation-candle volume ÷ arithmetic mean volume of the 20 immediately preceding completed 1H candles`

If Volume Ratio > **1.30**:

- B → A
- A → A+

No grade exceeds A+.

The volume calculation is valid only if all 21 candles use the same authorized data source and volume field.

Volume is treated as a **venue/source-specific research variable**. This document does not describe it as universal BTC volume or proof of institutional participation.

The resulting grade is the **volume-adjusted grade** used when the independent target and projected R:R are evaluated.

## 12.3 Uniform Initial-Validation Treatment

All qualifying grades use the same intended stop-risk authorization:

**2.5% of current account equity maximum intended stop-defined risk.**

A+, A, and B do not receive different capital authority during Initial Validation.

## 12.4 CORE Setup 1 Grading Specialization — Explicit Ratification and Traceability

Under CORE v1.6's **Setup 1 Asset-Class Grading Specialization** authority, the Condition D / Condition R + Volume Upgrade methodology in this §12 is explicitly ratified as the BTC/USD CR-1 specialization of CORE Setup 1 grading for this Initial Validation cohort.

The specialization remains materially traceable to CORE Setup 1 as follows:

1. **CORE Setup 1 condition 1 — Confirmed trend:** retained as a mandatory Candidate Existence requirement through §9.1's confirmed bullish 4H HH/HL structure requirement.
2. **CORE Setup 1 condition 2 — Price at a validated trend-continuation zone:** retained as mandatory Candidate Existence requirements through §9.1's previously Validated trend-continuation zone, current qualifying Zone Touch, prior Validation, and continuing-validity requirements.
3. **CORE Setup 1 condition 3 — 50 EMA confluence with zone:** operationalized as **Condition D — Daily EMA Confluence** in §12.1.
4. **CORE Setup 1 condition 4 — Confirmation trigger present:** retained as a mandatory Candidate Existence requirement through §9.1 and the deterministic §10–§11 Confirmation Window / 1H trigger mechanics.
5. **CORE Setup 1 condition 5 — R:R meets the minimum for grade:** retained through §13's independently identified target, measured Projected R:R, and CORE grade-recalculation / step-down procedure. It is evaluated after the volume-adjusted preliminary grade rather than counted as a preliminary-grade input.
6. **CORE Setup 1 condition 6 — Regime is Aggressive or Selective:** Candidate Existence requires Aggressive or Selective in §9.1, while **Condition R — Aggressive Regime** in §12.1 provides the grading distinction within that already-qualified regime set.

The §12.2 **Volume Upgrade** is inherited from CORE Step 4's universal Volume Upgrade mechanic and is not an independently invented grading input.

This specialization preserves CORE's **A+ / A / B / NO TRADE** hierarchy. It does not create, increase, or modify grade-dependent stop-risk, exposure, execution, or other capital authority. Grades generated under this explicitly ratified specialization may serve as Grade Validation evidence subject to the Constitution and CORE, but passing Grade Validation does not itself authorize differential capital treatment.

---

# 13. INDEPENDENT TARGET, PROJECTED R:R, AND FINAL QUALIFICATION

CR-1 inherits CORE's non-tautological target methodology.

## 13.1 Step 4 — Independent Target

Before the trade may qualify, identify the nearest genuine 4H resistance structure above the proposed entry that satisfies CORE's Counter-Trend Zone methodology.

The target must exist independently of:

- stop distance;
- setup grade;
- required R:R;
- desired profit.

If no valid Counter-Trend Zone can be identified:

**NO TRADE.**

The target may never be moved farther away merely to manufacture qualifying R:R.

## 13.2 Step 5 — Measured Projected R:R

Using the current proposed executable entry:

`Projected R:R = (Target − Proposed Entry) ÷ (Proposed Entry − Initial Stop)`

Grade thresholds are:

- A+ → 3.0R
- A → 2.5R
- B → 2.0R

Projected R:R is measured only after the target has been independently identified.

## 13.3 Step 6 — Grade Recalculation / Step-Down

Apply CORE's grade-recalculation procedure to the volume-adjusted grade using the measured projected R:R.

If the measured projected R:R does not satisfy the current grade threshold, step the grade down only as permitted by CORE and retest against the lower grade threshold.

If projected R:R fails B's 2.0R minimum:

**NO TRADE.**

No target may be moved and no stop may be widened to preserve a grade.

The grade surviving this process is the **final research grade**.

## 13.4 Step 7 — Final Trade Qualification

A candidate becomes a qualifying CR-1 trade only after all of the following are true:

- Candidate Existence Qualification passed;
- a Preliminary Grade existed;
- the Volume Upgrade step was completed;
- an independent Counter-Trend Target was identified;
- projected R:R was measured;
- grade recalculation was completed;
- the final research grade remains A+, A, or B;
- all risk, exposure, execution, account, data, capability, daily-brake, higher-level failure-state, and approval requirements are satisfied.

Failure of any mandatory final requirement:

**NO TRADE.**

## 13.5 Entry and Fill Revalidation

Projected R:R must be recalculated using the actual proposed execution price immediately before order submission.

If a fill occurs at a different price, actual fill-based R:R must be recorded.

A fill may never be accepted if the resulting actual entry would violate an authorized entry boundary, risk limit, or other hard constraint.

---

# 14. INITIAL PROTECTIVE STOP

For a LONG CR-1 trade define:

- `Structural Stop Reference = min(Zone Lower Bound, Confirmation Trigger Candle Low)`
- `Initial Stop = Structural Stop Reference × 0.998`

The 0.2% buffer is therefore applied **below** the lower structural reference.

The stop may never be widened after entry.

Live protective execution must comply with CORE Step 8: the protective stop must be a broker-side conditional stop, must not be a plain resting limit before trigger, and must not depend on Nickel remaining online to detect the trigger. Upon trigger, it converts to an authorized marketable-limit order and never to a true market order.

For BTC/USD Initial Validation, the protective-stop-trigger marketable-limit tolerance is:

**maximum 0.5% from the applicable verified execution reference price.**

This is an asset-level tightening within the Constitution's 1.0% absolute ceiling. It is numerically equal to Crypto's Emergency Exit tolerance but is an independent authorization for a distinct execution scenario; neither trigger depends on or activates the other.

The exact supported order type, trigger behavior, execution reference price, fill behavior, gap behavior, precision, and state visibility remain capability blockers until verified with the broker.

If compliant protective execution cannot be verified:

**DO NOT TRADE.**

---

# 15. R DEFINITION

After execution:

`1R = |Actual Filled Entry Price − Initial Protective Stop Price| × Actual Filled Quantity`

1R is fixed from the actual filled entry quantity and initial authorized stop.

Later stop movement does not redefine 1R.

For partial fills, each filled unit shares the same authorized initial stop. Trade-level 1R is calculated from the final accepted filled quantity after the entry order is complete or canceled.

---

# 16. POSITION SIZING

## 16.1 Intended Stop Risk

`Intended Risk $ = Current Account Equity × 0.025`

## 16.2 Risk-Based Size

`Stop Distance $/BTC = Proposed Entry − Initial Stop`

`Risk-Based BTC Quantity = Intended Risk $ ÷ Stop Distance $/BTC`

`Risk-Based Notional $ = Risk-Based BTC Quantity × Proposed Entry`

## 16.3 BTC Operating Exposure Ceiling

During Initial Validation:

**Maximum BTC/USD single-position notional exposure = 40% of current Agent Nickel account equity.**

`Exposure-Based Notional $ = Current Account Equity × 0.40`

`Exposure-Based BTC Quantity = Exposure-Based Notional $ ÷ Proposed Entry`

## 16.4 Final Quantity

`Buying-Power Quantity = verified available unleveraged buying power ÷ Proposed Entry`

`Final BTC Quantity = MIN(Risk-Based BTC Quantity, Exposure-Based BTC Quantity, Buying-Power Quantity)`

Then apply only broker-required deterministic precision rounding **toward smaller quantity / less risk**.

If the 40% exposure ceiling or buying power binds, effective planned stop-defined risk will be below 2.5%.

That is required most-restrictive-rule behavior, not discretionary undersizing.

## 16.5 No Minimum Forced Risk

Agent Nickel may never:

- widen the stop;
- increase exposure;
- add leverage;
- alter entry;
- or otherwise modify the trade

merely to force effective risk to reach 2.5%.

---

# 17. PROPOSAL AND HUMAN APPROVAL

During Initial Validation, every qualifying trade must be fully formed before approval.

The proposal must include at minimum:

- Proposal ID
- BTC/USD
- LONG
- CR-1
- grade
- regime
- active zone reference and bounds
- zone-validation basis
- confirmation trigger
- trigger price and timestamp
- proposed entry range
- proposed order type
- intended quantity
- position notional and % equity
- sizing constraint that binds
- intended stop-defined risk $
- intended stop-defined risk % equity
- effective planned risk after exposure/buying-power constraint
- initial stop
- independently identified target
- measured projected R:R
- applicable marketable-limit tolerance, if any
- current daily brake state
- setup invalidation conditions
- capability/account verification state
- recommendation: EXECUTE or PASS

Agent Nickel proposes the complete trade.

Human response is:

- **YES** → authorization to proceed only if the proposal remains valid;
- **NO** → proposal rejected and logged;
- no response → no authorization.

Approval does not authorize redesign.

---

# 18. PROPOSAL EXPIRATION AND ENTRY REVALIDATION

A proposal expires immediately if any of the following occurs before order submission:

- price leaves the authorized entry range;
- zone invalidates;
- Confirmation Window expires;
- regime changes in a way that disqualifies entry;
- grade changes;
- independently identified target changes;
- projected R:R falls below the final grade minimum;
- stop changes;
- final quantity or binding sizing constraint changes materially;
- required account/capability state changes;
- a daily brake activates;
- **30 minutes** pass after proposal generation.

The authorized entry range's lower bound governs **pre-submission proposal freshness**. Once a valid passive limit order has been submitted at the authorized Trigger Price under §19.2, execution at that resting limit does not itself cause proposal expiration merely because traded price reaches or moves below the range's lower bound; all other cancellation, invalidation, expiry, risk, and protective-execution rules remain in force.

An expired proposal cannot be revived by a late YES.

A new qualifying setup requires a new Proposal ID and new approval.

---

# 19. ENTRY EXECUTION

## 19.1 Default Method

CR-1 is a standard zone entry under CORE.

Default execution is therefore:

**PASSIVE LIMIT.**

## 19.2 Authorized Entry Range

The strategy reference price is the completed 1H trigger candle close.

For Initial Validation, the authorized entry range is:

`Trigger Price` through `Trigger Price × 1.003`

for a long entry.

Price above the upper boundary is **not chaseable**.

For ordinary CR-1 entry:

`Entry Limit Price = Trigger Price`

The passive buy limit may be submitted only if the Trigger Price is **strictly below the verified live best ask at submission** and every setup condition remains valid.

If the verified live best ask cannot be obtained, or if Trigger Price is not strictly below the verified live best ask:

**PASS / NO ENTRY.**

The 0.3% range remains an Initial Validation authorization boundary and is not a marketable-limit authorization. It does not permit Nickel to choose another submission price within the range.

## 19.3 Marketable-Limit Entry

CR-1 does **not** authorize marketable-limit execution for ordinary entry during Initial Validation.

Any future change requires formal strategy amendment and documented execution-speed rationale under higher authority.

## 19.4 Partial Fills

If an entry order partially fills:

- do not submit a duplicate replacement order;
- filled quantity becomes real exposure immediately;
- verify filled quantity, average fill price, notional exposure, effective stop risk, and protective-exit capability;
- remaining unfilled quantity may remain working only while the original proposal remains valid and the total possible filled quantity remains within all authorized limits;
- if the proposal expires or setup invalidates, cancel the unfilled remainder;
- never increase quantity to compensate for an incomplete fill.

If the partial fill itself cannot be protected according to the authorized stop mechanic:

**DO NOT INCREASE THE POSITION; execute the authorized fail-safe handling once broker capability is defined.**

Until that protective handling is capability-verified, live CR-1 execution remains blocked.

---

# 20. PROTECTIVE EXIT EXECUTION

A protective stop is mandatory for every live position.

Before live trading, the broker capability review must establish:

- supported BTC broker-side conditional protective order type(s);
- trigger behavior and conversion to bounded marketable-limit execution;
- the deterministic execution reference price used for the authorized 0.5% protective-stop-trigger tolerance;
- precision/minimum-size rules;
- behavior during partial fills;
- cancellation/replacement behavior;
- API/tool state visibility;
- compliance with CORE Step 8's protective/target mutual-exclusion requirement.

When protective and target orders coexist, live execution is governed by CORE Step 8. Broker-native OCO is preferred where supported. If broker-native OCO is unavailable, any equivalent deterministic cancel-on-fill procedure must satisfy CORE's requirements, including an explicitly defined maximum cancellation-confirmation window before live trading.

If compliant protective execution, OCO/mutual exclusion, or the required equivalent cancel-on-fill behavior cannot be verified:

**DO NOT TRADE.**

No unsupported order type or broker behavior may be assumed.

---

# 21. POSITION MANAGEMENT

Management rules are deterministic.

## 21.1 Breakeven Rule

When price first reaches **+1.5R**:

- move the protective stop to the actual filled entry price;
- do not take a partial exit solely because +1.5R was reached.

The stop may move only toward less risk.

## 21.2 +2R Partial Exit

When price first reaches **+2.0R**:

- exit **50% of the then-open position** using an authorized bounded exit;
- begin trailing the remainder.

If the independently identified target lies below +2R, the trade would already have failed the minimum B R:R gate and therefore could not exist.

### Simultaneous +1.5R / +2R Recognition

If verified price movement causes both +1.5R and +2.0R to become newly satisfied before the management state has processed either threshold, apply the following fixed sequence:

1. recognize +1.5R;
2. move the protective stop to breakeven;
3. recognize +2.0R;
4. exit 50% of the then-open position;
5. begin trailing the remainder.

## 21.3 Trailing Stop

After the +2R partial exit:

Only 1H swing lows **whose defining candle's own timestamp is strictly after the actual trade entry timestamp** are eligible for the trailing-stop mechanic. Confirmation of the swing may occur later, but the underlying swing-low candle itself must postdate entry.

`Candidate Trail Stop = most recently confirmed swing low whose defining candle occurred after entry`

If no eligible 1H swing low has confirmed since entry, `Candidate Trail Stop` is undefined and `Current Stop` is retained unchanged until an eligible 1H swing low confirms.

For a long position, when `Candidate Trail Stop` is defined:

`New Stop = max(Current Stop, Candidate Trail Stop)`

The stop may **never move downward**.

A newly confirmed 1H swing low that would widen the existing stop is ignored.

No additional trailing-stop buffer is authorized.

## 21.4 Final Target and Exit-Order Interaction

The independently identified Counter-Trend Target remains the structural final target.

For live trading, simultaneous protective/trailing-stop and target-order interaction is governed by CORE Step 8's OCO / mutual-exclusion requirement and broker-confirmed execution state. Crypto does not create a parallel rule for deciding which resting order "wins."

If the trailing stop exits the remaining position first, the trade is closed.

If the target is reached first, close the remaining position according to the authorized bounded exit mechanic.

For backtest or research using data that cannot establish intrabar path order, if the target and trailing/protective stop are both reachable within the same candle and no finer authorized data can establish which occurred first:

- classify the trade outcome as **AMBIGUOUS** for that event;
- use the conservative smaller-R outcome for aggregate statistics;
- explicitly flag the trade so it can be isolated or excluded in sensitivity analysis.

The conservative research convention does not assert that the smaller-R event actually occurred live.

---

# 22. TIME STOP

The 4H candle containing the actual entry timestamp does **not** count toward the three-candle Time Stop.

Count the next three fully completed 4H candles after entry.

If BTC has not reached at least **+0.5R MFE** by the completion of the third counted 4H candle:

**EXIT THE REMAINING POSITION.**

For this rule, "+0.5R MFE" means traded price reached Entry + 0.5R at any time after entry, as measured from verified market data.

Time-stop exit execution is passive limit by default under CORE.

CR-1 does not initially authorize marketable-limit execution for the Time Stop. If evidence shows passive execution materially fails, a future strategy amendment may authorize a bounded marketable limit with documented rationale and tolerance within higher authority.

---

# 23. EMERGENCY / FAIL-SAFE EXIT

CR-1 inherits CORE's authorization for marketable-limit execution during an authorized emergency/fail-safe exit.

For purposes of CORE Step 8 Emergency Exit authorization, the Crypto §24.3 emergency daily-loss trigger is the asset-class strategy's exercise of Constitution §7's express delegation ("An asset-class strategy may define a stricter daily loss rule"), and therefore constitutes the applicable constitutional circuit breaker for BTC/USD under this Initial Validation cohort — not an independently invented control.

Activation of §24.3 therefore authorizes the CORE Emergency Exit procedure, subject to Crypto's 0.5% marketable-limit tolerance and all applicable capability requirements.

This linkage does not modify, replace, or merge with the Constitution's own 10% realized-only threshold, which remains independently binding on its own basis. §24.3's broader realized-plus-unrealized measure and lower 9% threshold operate as a separate, stricter evaluation, with either boundary triggering its own consequence independently.

For BTC/USD Initial Validation, the emergency marketable-limit tolerance is:

**maximum 0.5% from the applicable verified execution reference price.**

This is stricter than the Constitution's 1.0% absolute ceiling.

The reference price must be deterministically defined by the verified broker/execution interface before live use.

If the required exit cannot execute within the authorized 0.5% tolerance, Agent Nickel may not widen the tolerance autonomously or convert to a true market order.

The condition must be treated according to the fail-safe and broker-capability procedures then in force.

---

# 24. DAILY BRAKES

The applicable Crypto trading day is the UTC calendar day.

## 24.1 Entry Count Brake

Maximum:

**3 completed live entries per UTC day.**

A completed live entry means an entry order that receives any fill and creates BTC exposure.

Rejected, canceled, expired, or wholly unfilled proposals do not count as completed live entries but remain logged.

## 24.2 Two-Loss Brake

After **two completed CR-1 trades closed at a negative realized R** during the same UTC day:

**NO NEW POSITION INITIATION FOR THE REMAINDER OF THAT UTC DAY.**

This rule counts completed losing trades, regardless of whether the final loss came from initial stop, trailing stop, time stop, or another authorized exit.

## 24.3 Crypto Emergency Daily-Loss Brake

At the start of each UTC day record Start-of-Day Equity.

If:

`Realized P/L for UTC day + Open Unrealized P/L <= −9.0% of Start-of-Day Equity`

then:

- no new positions may be initiated;
- if a BTC position is open, trigger the authorized **Crypto Emergency Exit**;
- after closure, no new position may be initiated until the next UTC day;
- log the event as an emergency-risk event.

This is a stricter strategy-level control exercised under Constitution §7's express delegation permitting an asset-class strategy to define a stricter daily loss rule.

The Constitution's 10% realized-loss breaker remains independently binding and independently evaluated.

CORE's Warning, Pause, and Full Stop failure tiers operate independently of all Crypto daily brakes. They are not reset by UTC midnight, are not satisfied or cleared merely because a Crypto daily brake clears, and retain their own governing review and resumption requirements. A new UTC day therefore does not authorize new Crypto entries while any higher-level CORE state continues to prohibit them.

---

# 25. NO DISCRETIONARY BEARISH EXIT

Bearish price action, bearish candles, subjective weakness, fear, news interpretation, or a view that BTC "looks bad" does not create an exit authority.

A long position may exit only through an explicitly authorized mechanic, including:

- initial protective stop;
- breakeven stop;
- trailing stop;
- +2R partial;
- structural final target;
- Time Stop;
- authorized emergency/fail-safe exit;
- another future formally approved rule.

No undefined discretionary exit is permitted.

---

# 26. JOURNAL AND RESEARCH RECORD

Every executed trade, rejected proposal, expired proposal, canceled order, and unfilled qualifying proposal must be retained.

In addition to CORE fields, Crypto records:

- authorized market-data source;
- Daily/4H/1H candle identifiers;
- regime inputs and classification;
- Daily 50 EMA value;
- Extreme Volatility Event state;
- confirmed 4H swings used;
- active zone reference/bounds;
- zone creation timestamp;
- prior-touch validation evidence;
- current touch timestamp;
- confirmation-window start/end;
- confirmation trigger type;
- trigger candle OHLCV;
- Volume Ratio;
- pre-volume grade;
- final research grade;
- independently identified target;
- proposed-entry R:R;
- actual-fill R:R;
- intended 2.5% risk $;
- risk-based quantity/notional;
- 40% exposure-based quantity/notional;
- buying-power quantity;
- binding sizing constraint;
- final rounded quantity;
- effective planned stop risk;
- partial-fill state;
- initial stop;
- 1R value;
- reached +1R Y/N;
- reached +1.5R Y/N;
- reached +2R Y/N;
- reached +3R Y/N;
- MFE in R;
- MAE in R;
- time to +1R/+2R/+3R where reached;
- exit reason;
- realized R;
- execution slippage;
- rule/capability exceptions or errors.

Grade research must use treatment-independent outcomes wherever practicable.

Grade-specific target achievement is not itself evidence of grade quality.

---

# 27. INITIAL VALIDATION RESEARCH QUESTIONS

At minimum evaluate:

1. CR-1 expectancy in realized R.
2. Profit factor.
3. Win/loss distribution.
4. MFE and MAE distributions.
5. Outcome by Aggressive vs Selective regime.
6. Outcome by A+/A/B research grade.
7. Predictive value of the >1.30 Volume Ratio upgrade.
8. Frequency and outcome of each confirmation trigger.
9. Zone-band behavior around ±0.15%.
10. Zone-validation method performance: two-touch vs >2% move.
11. Extreme-volatility filter behavior.
12. Frequency with which the 40% exposure ceiling binds.
13. Effective planned risk when exposure binds.
14. Entry slippage and passive-limit fill quality.
15. Partial-fill frequency.
16. Time Stop effect.
17. +1.5R breakeven and +2R partial-management effect.
18. Frequency of rejected/expired proposals and whether human availability creates sample bias.
19. Frequency of daily brakes.
20. Any broker/API/data reliability failure.

These are research questions. Their results do not automatically alter live rules.

---

# 28. AUTONOMY GATE

Crypto autonomy requires at minimum:

- **20 completed live BTC/USD CR-1 trades**;
- expectancy > **+0.3R**;
- profit factor > **1.3**;
- zero constitutional violations in the most recent 10 trades;
- zero execution errors in the most recent 10 trades;
- at least one losing trade managed correctly;
- completed trade evidence from both **Aggressive and Selective** regimes;
- complete required journal;
- no unresolved broker, data, protective-order, execution, or compliance capability blocker;
- explicit human authorization after review.

Meeting these requirements does not itself grant autonomy.

If the sample lacks qualifying Selective-regime trades, the autonomy gate is not satisfied merely by substituting additional Aggressive trades. The result may remain INCONCLUSIVE.

Twenty trades is a minimum gate, not proof of persistent alpha.

---

# 29. CAPABILITY BLOCKERS — LIVE TRADING PROHIBITED UNTIL RESOLVED

Before the first live CR-1 trade, verify and document:

1. BTC/USD is legally/account-eligible in the applicable Robinhood account and jurisdiction.
2. Exact authorized market-data source.
3. Availability and deterministic boundaries of Daily, 4H, and 1H OHLCV data.
4. Sufficient history and continuity for all required calculations.
5. BTC minimum order size.
6. BTC quantity precision and price precision.
7. Passive limit behavior.
8. Partial-fill behavior and state reporting.
9. Supported broker-side conditional protective-exit order type(s), including trigger and marketable-limit conversion behavior.
10. Protective-order behavior after partial fills.
11. A deterministic procedure for any partial fill that cannot immediately be protected under the authorized stop mechanic; until verified, an unprotected partial fill remains a live-trading blocker.
12. Compliance with CORE Step 8's protective/target mutual-exclusion standard: verified broker-native OCO, or an equivalent deterministic cancel-on-fill procedure with an explicitly defined maximum cancellation-confirmation window.
13. Cancel/replace semantics.
14. Marketable-limit behavior and deterministic execution reference price for the authorized 0.5% protective-stop-trigger tolerance.
15. Marketable-limit behavior for authorized emergency exits.
16. Deterministic emergency-exit reference price.
17. Applicable API/tool rate limits, maintenance windows, stale-state behavior, and outage handling.
18. Account restriction/compliance state required by the Constitution.
19. Any catalyst/news-filter mechanism before such a filter is treated as an active deterministic gate.

If any required live mechanic depends on an unverified capability:

**DO NOT TRADE.**

No broker feature may be invented from assumption.

---

# 30. CHANGE CONTROL

During Initial Validation, Agent Nickel may not autonomously change:

- active instrument;
- setup;
- direction;
- timeframes;
- regime thresholds;
- swing definitions;
- zone width;
- zone-validation rules;
- confirmation rules;
- grade rules;
- volume threshold;
- stop buffer;
- intended risk;
- exposure ceiling;
- target methodology;
- R:R thresholds;
- management rules;
- execution ranges or tolerances;
- daily brakes;
- autonomy requirements.

Research findings are logged first.

Any material live-rule change requires formal review and explicit authorization under the governing hierarchy.

---

# 31. AUTHORIZED INITIAL-VALIDATION PARAMETERS — SUMMARY

| Parameter | Authorization |
|---|---|
| Active instrument | BTC/USD only |
| Direction | Long only |
| Active setup | CR-1 / CORE Setup 1 only |
| Regime timeframe | Daily |
| Structure timeframe | 4H |
| Confirmation timeframe | 1H |
| Confirmation Window | next 3 completed 1H candles after qualifying 4H touch, subject to earlier §10 termination conditions |
| Intended stop-defined risk | 2.5% current equity |
| Single-position notional exposure ceiling | 40% current equity |
| Concurrent positions | 1 |
| Zone band | ±0.15% |
| Zone invalidation | completed 4H close >0.15% below Lower Bound |
| Extreme volatility | completed 1H TR >3× preceding 20-candle mean TR |
| Volume upgrade | confirmation volume >1.30× preceding 20-candle mean |
| Initial structural-stop buffer | 0.2% below lower structural reference |
| Ordinary entry | passive limit at Trigger Price only; Trigger Price must be strictly below verified live best ask |
| Entry upper range | trigger close +0.3% authorization boundary; not submission-price discretion |
| True market order | prohibited |
| Protective-stop-trigger marketable-limit tolerance | 0.5% maximum |
| Emergency marketable-limit tolerance | 0.5% maximum |
| +1.5R | stop to breakeven |
| +2R | exit 50%, then trail remainder using confirmed 1H swing lows |
| Time Stop | no +0.5R MFE after next 3 completed 4H candles |
| Daily entry maximum | 3 filled entries |
| Two-Loss Brake | 2 completed negative-R trades in UTC day |
| Crypto emergency daily-loss trigger | realized + unrealized ≤ −9% start-of-day equity |
| Initial Validation horizon | approximately 60–90 days |
| Human approval | required for every Initial Validation entry |

---

# 32. VERSION HISTORY

## v1.1 — RATIFIED

Ratified reconciliation of the v1.0 Clean Rebuild against ratified Agent Nickel Constitution V1.5 and ratified CORE v1.6 without redesigning the CR-1 strategy.

Changes are limited to the adjudicated reconciliation patch set:

- updates the governing CORE reference from v1.4 to v1.6;
- explicitly ratifies Crypto Selective's bullish-HH/HL requirement as a legitimate narrowing of CORE and documents deterministic Aggressive-before-Selective precedence for overlapping EMA predicates;
- adds deterministic confirmed 1H swing definitions for trailing-stop use;
- restructures candidate, grade, volume, target, projected-R:R, grade-recalculation, and final-qualification logic into the fixed seven-step pipeline;
- removes the undefined Confirmation Window catch-all;
- makes ordinary passive entry deterministic at Trigger Price and requires it to be strictly below verified live best ask;
- specializes the CORE protective-stop trigger to a 0.5% maximum marketable-limit tolerance and preserves broker-side conditional-stop requirements;
- adds explicit +1.5R / +2R simultaneous-recognition sequencing;
- changes the post-+2R trail from 4H to confirmed 1H swing lows and removes the undefined trailing buffer;
- delegates live target/stop interaction to CORE's OCO/mutual-exclusion rule and adds the adjudicated AMBIGUOUS conservative convention for research data lacking intrabar path order;
- grounds Crypto §24.3 Emergency Exit authority in Constitution §7's express delegation for stricter asset-class daily-loss rules while preserving independent 9% realized-plus-unrealized and 10% realized-only evaluation;
- states that CORE Warning/Pause/Full Stop states remain independent of Crypto daily brakes and do not reset at UTC midnight;
- adds standalone unprotected-partial-fill and CORE OCO/cancel-on-fill capability blockers;
- explicitly ratifies CR-1's Condition D / Condition R + Volume Upgrade grading methodology under CORE v1.6's Setup 1 specialization authority and maps all six CORE Setup 1 conditions to the CR-1 qualification / grading pipeline;
- limits post-+2R trailing-stop swing references to confirmed post-entry 1H swing lows and retains Current Stop unchanged until an eligible swing confirms;
- clarifies that the entry-range lower bound governs pre-submission proposal freshness rather than invalidating a valid already-submitted resting passive order;
- adds the 3-completed-1H Confirmation Window and 0.2% initial structural-stop buffer to the authorized-parameters summary.

No new instrument, direction, setup, differential-risk authority, leverage authority, or autonomous strategy-change authority is created by this reconciliation.

## v1.0 — Clean Rebuild

Clean rebuild of `AGENT_NICKEL_CRYPTO.md` under Agent Nickel Constitution V1.5 and CORE v1.4.

This version intentionally does not patch or inherit authority from any prior unratified Crypto draft.

Major design decisions include:

- BTC/USD-only Cohort 1;
- CR-1 / Setup 1 only;
- long-only operation;
- Daily / 4H / 1H hierarchy;
- 2.5% uniform intended stop-defined risk;
- 40% BTC operating notional exposure ceiling;
- deterministic most-restrictive sizing;
- explicit partial-fill handling;
- completed-candle-only structural qualification;
- deterministic 4H swing definitions;
- deterministic zone creation, validation, invalidation, and two-zone lifecycle;
- explicit no-look-ahead zone validation;
- bounded confirmation window linking completed 4H touch to 1H trigger;
- Trigger CR-1A renamed from "Hammer" to match its actual mathematical definition;
- exhaustive regime precedence and fallback;
- independent structure-derived target and falsifiable projected R:R gate;
- actual-fill revalidation and fixed 1R definition;
- stop buffer made directionally explicit;
- no-widen trailing-stop rule;
- Time Stop candle counting made explicit;
- ordinary entry returned to passive limit under CORE;
- emergency marketable-limit execution specialized to a 0.5% BTC ceiling, subject to capability verification;
- two-loss and daily-entry brakes defined deterministically;
- 9% realized-plus-unrealized Crypto emergency brake separated from the Constitution's 10% realized-loss breaker;
- treatment-independent grade research;
- rejected/expired proposal logging;
- explicit market-data and broker-capability blockers;
- no discretionary bearish-exit authority.

---

**END — AGENT NICKEL CRYPTO STRATEGY v1.1 — RATIFIED**
