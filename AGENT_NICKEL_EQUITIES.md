AGENT NICKEL — EQUITIES STRATEGY

Version 2.2 — Constitutional Reconciliation Blocker Flagged

Track 1 — Equities / SPY

⚠️ CONSTITUTIONAL RECONCILIATION BLOCKER — NOT EXECUTION-READY UNDER CONSTITUTION V1.5

Agent Nickel Constitution V1.5 Section 5 requires every active asset-class strategy to operate under an explicitly authorized hard single-position notional exposure ceiling appropriate to that asset and validation phase.

This document does not yet define one. No exposure ceiling number is proposed here.

Until an operating exposure ceiling is explicitly authorized and reconciled into this document, Equities is NOT execution-ready under Constitution V1.5. This is a tracked reconciliation blocker, not a silent gap — it is also recorded in CLAUDE.md V1.5's Version History. Live trading remains additionally gated by the Technical Preconditions in Section 28 / README.md regardless of this blocker's resolution.

This document defines the equities- and ETF-specific trading rules for Agent Nickel.

It is governed by:

1. CLAUDE.md — Agent Nickel Constitution
2. AGENT_NICKEL_CORE.md — Universal operating framework
3. This document — Equities-specific strategy rules

In any conflict, the higher-level governing document controls.

This document supersedes AGENT_NICKEL_STRATEGY.md v0.2 for risk sizing, grading, circuit breakers, approval logic, and autonomy requirements.

The PDL reclaim mechanics established in AGENT_NICKEL_STRATEGY.md v0.2 remain incorporated by reference except where explicitly modified below.

**Reconciliation note (v2.0):** the repository's committed history only contains v1.0 of this document — a first draft written before this strategy's risk model, timeframe definitions, and validation framing were fully worked out. Versions v1.1 through v1.5 were produced across separate work sessions (one in Claude Code, several in a planning conversation) but never reached this repository. This version, v2.0, is the reconciled result: it supersedes v1.0 in full and consolidates everything from that intervening work — the flat-risk validation design (v1.1), the B-grade constitutional compliance fix (v1.2), the determinism pass defining 1R/swing structure/volume confirmation/loss triggers (v1.3), the realized-vs-unrealized loss-basis clarification (v1.4), and the 3.0% flat-risk mission realignment (v1.5) — into the single version now being committed. It is written against the newly-reconciled CLAUDE.md V1.4 (see that document's Version History for why V1.3 needed reconciling in the first place).

⸻

1. STRATEGY PRINCIPLE

Agent Nickel is operating under a validation requirement.

The existence of a logically coherent setup does not establish an edge.

The purpose of this strategy version is to test whether the defined SPY PDL Support Reclaim produces positive expectancy under real market conditions while simultaneously validating Agent Nickel's execution architecture.

Accordingly:

Setup grades are observations before they are privileges.

A+, A, and B classifications must initially be recorded and evaluated without automatically receiving different capital allocations.

Grade-weighted risk may be introduced only after sufficient observed data demonstrates that setup grade has meaningful predictive value.

⸻

2. SCOPE

Asset class: Equities and ETFs only.

Authorized instrument: SPY only.

No other equity, ETF, option, inverse product, leveraged product, or derivative may be evaluated for live execution without explicit user authorization pursuant to the Constitution.

Direction: LONG ONLY.

Prohibited:

* Short selling
* Put positions
* Inverse ETFs
* Margin
* Leverage
* Options
* Any synthetic short exposure

Bearish conditions are used only for:

* regime classification,
* risk reduction,
* position exit,
* or NO TRADE decisions.

⸻

3. TIMEFRAME HIERARCHY

Timeframes must be deterministic.

Agent Nickel may never select or change a timeframe because an alternative timeframe makes a setup qualify.

The equities strategy uses three distinct timeframe functions:

Regime Timeframe

Daily

Used exclusively for broad-market regime classification and Daily 50 EMA analysis.

Primary Structure Timeframe

5-minute

Used for:

* higher-high / higher-low determination,
* primary trend confirmation,
* structural swing identification,
* time-stop measurement,
* trailing-stop structure.

Execution / Reclaim Timeframe

1-minute

Used exclusively for:

* PDL reclaim confirmation,
* confirmation candle evaluation,
* entry timing,
* immediate setup invalidation.

These roles may not be substituted for one another during live evaluation.

⸻

4. DEFINITION OF 1R

All risk multiples used throughout this document (0.5R, 1.5R, 2.0R, minimum R:R, expectancy in R, profit factor) are computed from a single deterministic definition:

**1R (dollars) = |Actual Filled Entry Price − Initial Protective Stop Price| × Actual Filled Quantity**

Where:

* **Actual Filled Entry Price** = the volume-weighted average price of all fills constituting the entry — never the proposed price or the limit price.
* **Actual Filled Quantity** = the total filled share quantity — never the originally proposed position size.
* **Initial Protective Stop Price** = the stop price set per Section 16 (0.15% below PDL), fixed at the moment of entry.

1R is finalized once the entry order is fully filled and does not change afterward — not when the stop is later moved to breakeven or trailed per Section 18. Stop movement after entry affects realized P/L; it never changes the 1R denominator used to measure that P/L.

If the entry fills at a different price than the proposed entry (within the permitted entry range per Section 15), 1R is calculated from the actual fill, not the original proposal. This keeps two distinct things from being silently conflated:

* **Proposed risk** — used pre-trade for position sizing and projected R:R (Section 17). An estimate.
* **Actual risk** — used post-trade for every R-multiple in the journal, in expectancy calculations, and in autonomy-gate math (Section 24). Computed only from Actual Filled Entry Price and Actual Filled Quantity as defined above.

⸻

5. REGIME CLASSIFICATION

SPY itself is the regime instrument.

Regime is determined before any setup evaluation.

AGGRESSIVE

Required characteristics:

* SPY above Daily 50 EMA,
* bullish primary structure,
* higher highs and higher lows (per Section 9's mechanical definition),
* no extreme volatility event,
* no disqualifying major catalyst.

SELECTIVE

Characteristics may include:

* SPY near Daily 50 EMA,
* mixed broader structure,
* but qualifying bullish 5-minute structure exists.

Trades are permitted only when all Setup EQ-1 baseline requirements are satisfied.

DEFENSIVE

Characteristics include:

* SPY below Daily 50 EMA,
* lower highs/lower lows,
* materially deteriorating market structure.

No new live positions permitted.

Observation and shadow logging continue.

NO TRADE

Triggered by:

* extreme volatility event,
* major scheduled news/event within the prohibited window,
* breaking market-moving news,
* abnormal spread/liquidity behavior,
* trading halt,
* account restriction,
* execution capability uncertainty,
* incomplete Robinhood capability verification,
* or constitutional circuit breaker.

⸻

6. APPROVED SETUP — EQ-1

PDL SUPPORT RECLAIM

Strategy Hypothesis

EQ-1 tests whether a confirmed reclaim of the Previous Day Low during qualifying bullish intraday structure produces positive expectancy in SPY.

PDL is a widely observed market reference.

However:

PDL is not presumed to possess predictive edge merely because it is widely observed.

Its usefulness as an entry structure is a hypothesis Agent Nickel must validate through recorded outcomes.

⸻

7. PDL ZONE AND INVALIDATION

PDL Support Zone

PDL ± 0.10%.

Maximum Pre-Reclaim Breach

Price may trade below PDL before reclaiming it, but may not trade more than:

0.15% below PDL

A breach beyond this threshold invalidates the setup.

Once invalidated, that occurrence of EQ-1 may not be resurrected by reinterpretation.

A later independent setup must satisfy all requirements anew.

⸻

8. RECLAIM CONFIRMATION

A valid reclaim requires:

1. A completed 1-minute candle closes above PDL.
2. The following completed 1-minute candle does NOT close back below PDL.

Incomplete candles may never be evaluated as complete.

Agent Nickel may never:

* predict a candle close,
* anticipate confirmation,
* enter because confirmation appears likely,
* or reinterpret an incomplete candle after the fact.

⸻

9. BASELINE QUALIFICATION GATE

Before grading occurs, BOTH conditions below must be satisfied.

Condition 1 — Valid PDL Reclaim

The reclaim must satisfy Sections 7 and 8.

Condition 2 — Confirmed Bullish Primary Structure

The 5-minute chart must demonstrate:

* higher highs,
    AND
* higher lows,

determined per the mechanical definition below. Both are required.

**Mechanical Definition of Swing High / Swing Low (5-minute chart)**

A **swing high** is a completed 5-minute candle whose high price exceeds the high price of the 2 completed candles immediately preceding it AND the high price of the 2 completed candles immediately following it. A swing high is not confirmed — and may not be used in any determination — until both of the 2 following candles have completed. Prediction of an unconfirmed swing high is prohibited.

A **swing low** is defined identically using low price and the inverse relationship (lower than the 2 candles immediately before and after it).

An equal high or equal low does not create a new swing point; the earlier candle retains the swing designation.

**Higher High (HH):** the most recently confirmed swing high has a strictly higher high price than the immediately preceding confirmed swing high.

**Higher Low (HL):** the most recently confirmed swing low has a strictly higher low price than the immediately preceding confirmed swing low.

**Session window:** only confirmed swing highs/lows formed during the current regular trading session (9:30 AM ET forward) are eligible. Pre-market and prior-session swings do not count.

**Insufficient data:** if fewer than 2 confirmed swing highs or fewer than 2 confirmed swing lows exist in the current session at time of evaluation, Condition 2 cannot be satisfied. This defaults to NO TRADE — it never defaults to an assumed pass.

If either baseline condition fails:

NO TRADE.

A setup that fails the baseline gate receives no grade.

⸻

10. PDL ZONE-VALIDATION EXEMPTION

AGENT_NICKEL_CORE.md requires generic discretionary structure zones to demonstrate prior validation.

PDL is exempt from that requirement for EQ-1 because PDL itself is the variable being tested.

This exemption must NOT be interpreted as proof that PDL is inherently predictive.

Instead:

The PDL exemption is an explicit experimental hypothesis.

Agent Nickel must therefore record whether additional structural reinforcement existed at PDL.

Required research fields include:

* prior intraday touches near PDL,
* prior reaction magnitude,
* nearby 5-minute structure,
* Daily 50 EMA proximity,
* volume behavior,
* distance from VWAP if available,
* and whether PDL was a "naked" reference level or structurally reinforced.

This allows later comparison of:

Naked PDL Reclaim

versus

Structurally Reinforced PDL Reclaim

without changing live execution rules during the initial validation sample.

⸻

11. GRADE CONDITIONS

Once the baseline gate is satisfied, evaluate two base-grade conditions.

Condition A — Daily 50 EMA Confluence

Daily 50 EMA lies within 1% of PDL.

Condition C — Aggressive Regime

Current regime classification is Aggressive.

**Volume Upgrade Condition**

Volume Confirmation is not a base-grade condition. Per AGENT_NICKEL_CORE.md, it is evaluated separately and applied as a one-level grade upgrade after the base grade is determined (see Section 12).

Formula: **Volume Ratio = Candle Volume ÷ Trailing Average Volume**, evaluated independently for the reclaim candle and the confirmation candle.

**Either-candle rule:** Volume Confirmation is satisfied if EITHER the reclaim candle OR the confirmation candle independently has a Volume Ratio > 1.3. Both candles are not required to qualify.

**Trailing average definition:** for a given candle, Trailing Average Volume = the arithmetic mean volume of the 20 completed 1-minute candles immediately preceding that candle. The candle being evaluated is always excluded from its own average — the average is computed strictly from candles before it.

**Session boundary:** the trailing average may only be built from candles within the current regular trading session (9:30 AM ET forward). Premarket and prior-session candles are never included.

**Insufficient data:** if fewer than 20 completed 1-minute candles have occurred since session open at the time either the reclaim or confirmation candle forms, Volume Confirmation defaults to NOT SATISFIED for that candle. It does not fall back to a shorter average.

⸻

12. SETUP GRADING

Base Grade	Qualification
A	Baseline + both additional conditions (EMA Confluence + Aggressive Regime)
B	Baseline + 1 additional condition
No Trade	Baseline + 0 additional conditions

**Volume Upgrade (applied after base grade):**

If Volume Confirmation is satisfied, upgrade the base grade by one level:

* B → A
* A → A+

A+ is not reachable as a base grade — it is only reached via Volume Upgrade from base A.

No Trade is not upgrade-eligible. The CORE Volume Upgrade defines only B→A and A→A+; it does not create a No Trade→B transition. A setup must therefore independently qualify for at least a B base grade before Volume Confirmation can affect its grade.

Grades are mandatory research classifications.

During the Initial Validation Phase:

Grade does NOT determine position risk.

A+, A, and B setups receive identical risk treatment.

This separation exists deliberately so Agent Nickel can determine whether its grading framework actually predicts differences in expectancy.

⸻

13. INITIAL VALIDATION RISK

During the Initial Validation Phase:

Capital at risk per qualifying live trade: 3.0% of start-of-trade account equity.

This applies equally to:

* A+
* A
* B

**Constitutional authority:** this figure is authorized under CLAUDE.md V1.4 Section 2's Initial Validation Flat-Risk Exception, which permits an active strategy to run a single flat per-trade risk percentage — up to but not exceeding 3.0% — across all qualifying grades during a designated Initial Validation Phase. Without that exception, a flat 3.0% figure would exceed the Constitution's permanent B-grade ceiling (1.5%) the moment a B-grade setup fired; the exception exists specifically to make that not true during validation, without permanently loosening B's ceiling. See the v1.5 sign-off note above and CLAUDE.md V1.4 Version History for the authorization record.

**Why 3.0% and not 1.5%:** 1.5% was chosen in v1.2 primarily to fit inside the (then only available) B-grade ceiling — a compliance-driven number, not a mission-driven one. Two considerations favor 3.0% for what Initial Validation is actually meant to test:

1. **Compounding drawdown is still well short of ruin.** Even 10 consecutive full-risk stop-outs at 3.0% leaves roughly 74% of starting equity (compounding, not linear — see table below). Combined with the daily/emergency/constitutional brakes already in force (Sections 21–23), one concurrent position, human approval of every trade, and actual-fill R accounting, a run that bad would trip multiple brakes long before 10 straight losses could occur.
2. **Execution friction dominates at 1.5% on a micro account.** On a $100 account, 1.5% risk is $1.50 planned risk per trade; rounding and slippage become disproportionately large relative to that figure. 3.0% ($3.00) gives the strategy's actual expectancy more room to show up in the P/L before friction swamps it — relevant because the whole point of Initial Validation is measuring EQ-1's expectancy in R, not confirming that a specific risk percentage is safe.

| Consecutive full-risk losses | 1.5% risk (compounded) | 3.0% risk (compounded) |
|---|---|---|
| 2 | -3.0% | -5.9% |
| 3 | -4.4% | -8.7% |
| 5 | -7.3% | -14.1% |
| 8 | -11.4% | -21.6% |
| 10 | -14.0% | -26.3% |
| 15 | -20.3% | -36.7% |

This does not change the strategy's answer to whether EQ-1 has edge — a negative-expectancy setup fails at either risk level, sizing only changes the dollar cost of finding out.

Position size is determined by:

Position Size = Dollar Risk ÷ Stop Distance %

Where:

Dollar Risk = Account Equity × 3.0%

Capital at risk and position notional value are separate concepts. See Section 4 for how risk is measured post-fill, distinct from this pre-trade sizing calculation.

Position size may never exceed available unleveraged buying power.

No leverage may be introduced to achieve calculated theoretical position size.

If available buying power cannot support the calculated position size:

Position size is capped at available buying power.

Risk is thereby reduced, never increased.

⸻

14. GRADE-WEIGHTED RISK — LOCKED

The following framework is reserved for future evaluation:

* A+ — up to 5%
* A — up to 3%
* B — up to 1.5%

It is NOT authorized during Initial Validation.

Grade-weighted sizing may be considered only after observed data demonstrates that grade classification meaningfully predicts performance.

Until explicitly authorized:

3.0% fixed risk controls all qualifying grades, per the Initial Validation Flat-Risk Exception (Section 13).

No automatic promotion to grade-weighted sizing is permitted.

⸻

15. ENTRY

After valid reclaim confirmation:

Place a limit buy no higher than:

0.05% above the confirmed reclaim price.

If price moves beyond the permitted entry range before execution:

CANCEL — DO NOT CHASE.

A missed trade is preferable to an invalid trade.

⸻

16. STOP LOSS

Initial stop:

0.15% below PDL.

Stop must be defined before entry.

After entry, the stop may:

* remain unchanged,
* move toward breakeven,
* or tighten according to authorized management rules.

It may NEVER be widened to increase allowable loss.

⸻

17. MINIMUM REWARD-TO-RISK

During Initial Validation, grade does not alter risk allocation.

Minimum acceptable projected reward-to-risk for ANY live EQ-1 setup:

2.0R

Grade-specific R:R performance must still be recorded for research.

A trade with projected R:R below 2.0R is:

NO TRADE.

⸻

18. POSITION MANAGEMENT

At +1.5R

Move stop to breakeven.

No mandatory partial exit.

At +2.0R

Exit 50% of the position using the authorized execution method.

Remaining 50%

Trail using the most recently confirmed 5-minute swing low (per Section 9's mechanical definition).

A swing may not be predicted before confirmation.

Time Stop

If the trade has not moved at least +0.5R within:

3 completed 5-minute candles after entry

the thesis has expired.

Exit using the currently authorized protective execution method.

This is classified as:

THESIS EXPIRATION

not automatically as setup failure.

**Protective exit method — undefined pending capability check.** Every "authorized protective execution method" reference above (initial stop, time-stop exit) is a placeholder, not an operational instruction. The exact order type for each exit scenario has not yet been determined and must not be assumed or improvised at build time. See Section 28 — no live order of any kind may be submitted while this remains undefined.

⸻

19. APPROVAL VALIDITY — ALERT PHASE

During Alert Phase every proposed live trade requires explicit user approval.

Approval is an execution gate, not strategy input.

Agent Nickel must independently produce the complete trade proposal before requesting approval.

Approval applies ONLY to the exact proposal presented, including:

* symbol,
* setup,
* grade,
* entry range,
* position size,
* dollar risk,
* stop,
* target,
* projected R:R,
* regime,
* and invalidation conditions.

Approval expires immediately if:

* price leaves the permitted entry range,
* the setup invalidates,
* the stop calculation changes,
* position size changes materially,
* grade changes,
* regime changes,
* R:R falls below minimum,
* market conditions materially change,
* trading window closes,
* 30 minutes elapse from proposal with no response,
* or any constitutional condition changes.

The 30-minute timeout exists as a backstop alongside the condition-based triggers above, not a replacement for them — a proposal can expire earlier than 30 minutes if any condition above changes first.

Once approval expires:

NO EXECUTION.

A newly qualifying setup requires a new proposal and new approval.

Silence is never approval.

⸻

20. TRADING WINDOW

Window A

8:00–9:30 AM ET

Observation / shadow only.

Window B

9:30–9:45 AM ET

Observation / shadow only.

Window C

9:45–11:00 AM ET

Authorized live-trading window.

Shadow logging remains mandatory.

Window D

11:00 AM–12:00 PM ET

Observation / shadow only.

No new live position may be initiated outside Window C.

⸻

21. DAILY OPERATING BRAKES

Maximum Completed Live Entries

2 per trading day.

Once two live entries have occurred:

No additional live entries that day.

Two-Loss Brake

After two stopped-out live trades:

STOP LIVE TRADING FOR THE DAY.

Shadow observation continues.

Under 3.0% fixed risk, two ordinary full-stop losses should represent approximately 5.9% of starting equity before slippage (compounded — see Section 13's drawdown table).

This is the normal strategy-level daily brake.

**Basis (clarification, v1.4, carried forward):** this brake is realized-loss based by design — it counts only completed, closed-trade losses (two full stop-outs), not any open position's mark-to-market drawdown. That is deliberate: it exists as an early, lower-severity brake that fires well before Section 22's emergency trigger ever would in the normal case. It is not measuring the same quantity as Section 22, which continuously monitors realized-plus-open-unrealized loss. Do not read the two sections as interchangeable loss bases.

⸻

22. CONSTITUTIONAL EMERGENCY LOSS CEILING

The Constitution's:

10% daily loss limit

remains an absolute emergency ceiling.

It is NOT a daily loss target or normal operating allowance.

**Deterministic trigger (replaces "approach or reach"):**

If realized-plus-open-unrealized daily loss reaches **9.0% of start-of-day equity** (the Trigger Threshold): ALL TRADING STOPS IMMEDIATELY, and no new position may be opened for the remainder of the day.

The 9.0% Trigger Threshold is a deterministic operational proxy for the Constitution's 10% ceiling — a 1.0-percentage-point buffer to absorb the slippage and execution lag between the moment the threshold is crossed and the moment forced exits complete. This is a strategy-level safety margin, not a Constitutional amendment.

If, despite the buffer, realized daily loss ever reaches the Constitutional 10% ceiling itself, that event is treated as a **constitutional violation** requiring escalation per CLAUDE.md — not merely a strategy-level stop triggered late.

The distinction that matters operationally:

Normal strategy brake (Section 21): approximately 5.9% maximum planned loss from two full-risk stop-outs.

Deterministic emergency trigger (this section): 9.0%, measured as realized-plus-open-unrealized loss — see Section 21's Basis note for why these two sections use different loss bases.

Constitutional hard ceiling: 10% — breach of this line is an escalation event, not a routine stop.

⸻

23. CONCURRENT POSITIONS

Maximum concurrent positions:

1

No exceptions during Initial Validation.

⸻

24. EQUITIES AUTONOMY GATE

Autonomy is asset-class specific.

Equities autonomy cannot grant crypto autonomy.

The minimum preliminary operational-autonomy gate for EQ-1 requires:

* at least 20 completed live equities trades,
* expectancy > +0.3R,
* profit factor > 1.3,
* zero constitutional violations in the most recent 10 trades,
* zero execution errors in the most recent 10 trades,
* at least one losing trade correctly managed,
* observed live performance in both Aggressive and Selective regimes,
* complete journal records,
* and no unresolved capability or execution issue.

All R-multiple figures in this gate (expectancy, profit factor) are computed using the Section 4 definition of 1R — actual filled entry and actual filled quantity, never proposed values.

Twenty trades constitute:

A preliminary operational-autonomy threshold — not statistical proof of persistent alpha.

Passing the gate means Agent Nickel has produced sufficient preliminary evidence to consider controlled autonomous execution.

It does NOT establish that the strategy possesses permanent or statistically robust edge.

Autonomy requires explicit authorization after review.

It is never granted automatically by software merely because numerical thresholds were reached.

⸻

25. AUTONOMY REVOCATION

Autonomy is reversible.

After autonomy is granted, Agent Nickel must continuously monitor:

* rolling expectancy,
* profit factor,
* drawdown,
* execution quality,
* constitutional compliance,
* regime-specific performance,
* and setup-grade performance.

Autonomy must immediately revert to Alert Phase upon:

* constitutional violation,
* unauthorized execution,
* material execution-system failure,
* breach of constitutional drawdown limits,
* inability to calculate valid risk,
* inability to verify account state,
* or other Constitution-defined fail-safe event.

Performance deterioration that does not constitute an emergency must trigger a review under thresholds defined in CORE.

Autonomy is a privilege maintained by continued performance and correct execution.

It is not permanent status.

⸻

26. RESEARCH OBJECTIVES

Initial Validation must answer more than:

"Did Agent Nickel make money?"

Required research questions include:

1. Does EQ-1 demonstrate positive expectancy?
2. Does A+ outperform A?
3. Does A outperform B?
4. Does grade correlate with expectancy at all?
5. Do structurally reinforced PDL reclaims outperform naked PDL reclaims?
6. Does EQ-1 perform differently in Aggressive vs Selective regimes?
7. What is actual win rate?
8. What is average win in R?
9. What is average loss in R?
10. What is realized expectancy?
11. What is realized profit factor?
12. What are MFE and MAE distributions?
13. How much performance is lost to spread/slippage?
14. Does the 1.5R breakeven rule improve or reduce expectancy?
15. Does the 2R partial exit improve or reduce expectancy?
16. Does the three-candle time stop improve or reduce expectancy?

Rules must not be altered mid-sample merely because early outcomes are unfavorable.

Material strategy changes create a new strategy version and a new validation cohort.

⸻

27. LIVE VS SHADOW DATA

Live and shadow results must remain separate.

Never combine:

* actual P/L
    with
* hypothetical shadow P/L.

Shadow trades may generate research hypotheses.

They do not count toward:

* live expectancy,
* live profit factor,
* autonomy qualification,
* or realized account performance.

⸻

28. TECHNICAL PRECONDITIONS

Live trading is NOT authorized until all technical preconditions in README.md are verified.

The Robinhood capability check must confirm, at minimum:

* authenticated account state,
* equity order capability,
* supported order types,
* buying-power retrieval,
* position retrieval,
* order-status retrieval,
* cancellation capability,
* protective-exit capability,
* market-data availability,
* and any relevant account restrictions.

**Additional required determination (v1.3):** capability_check.py must determine and record, by exact order type name, the execution method used for each of the following, distinctly:

* (a) normal initial-stop exit,
* (b) time-stop exit (Section 18),
* (c) emergency/fail-safe exit under a constitutional circuit breaker (Section 22).

AGENT_NICKEL_EQUITIES.md Section 18 must be updated to reference these exact order types by name once determined. Until named, "authorized protective execution method" remains a placeholder — it is not an instruction any code may act on.

Until capability verification is complete:

RESEARCH MODE ONLY.

Permitted:

* observation,
* market scanning,
* shadow proposals,
* shadow journaling,
* strategy testing.

Prohibited:

* live order submission,
* live order modification,
* live position creation.

⸻

29. VALIDATION DISCIPLINE

Agent Nickel must distinguish between:

Framework validation

Can the system correctly identify, calculate, propose, execute, manage, journal, and enforce its own rules?

Strategy validation

Does EQ-1 demonstrate positive expectancy in SPY?

Grade validation

Does A+/A/B classification predict meaningful differences in outcome?

Autonomy validation

Can Agent Nickel operate within its rules reliably enough to permit controlled autonomous execution?

These questions are related.

They are not interchangeable.

A validated operating framework does not prove trading edge.

Profitable trades do not prove correct execution.

Twenty successful trades do not prove persistent alpha.

And an A+ label does not make a setup A+ until the data says it does.

⸻

STATUS

Strategy: EQ-1 PDL Support Reclaim
Instrument: SPY
Direction: Long Only
Risk Mode: Fixed 3.0% Initial Validation (CLAUDE.md V1.4 Flat-Risk Exception)
Grade-Weighted Risk: LOCKED
Maximum Concurrent Positions: 1
Maximum Live Entries/Day: 2
Live Window: 9:45–11:00 AM ET
Approval Mode: ALERT — explicit approval required, expires on condition change or 30 minutes, whichever first
Protective Exit Method: UNDEFINED — blocks live trading until capability_check.py determines it (Section 28)
Live Trading: NOT AUTHORIZED
Current Mode: RESEARCH / SHADOW

Live authorization requires successful Robinhood capability verification and satisfaction of every applicable technical precondition.

⸻

VERSION HISTORY

v2.2 — Constitutional Reconciliation Blocker Flagged

* Added a top-of-file blocker notice: Constitution V1.5 Section 5 requires every active asset-class strategy to operate under an explicitly authorized hard single-position notional exposure ceiling. This document does not yet define one for equities. No number is proposed or derived by this change — it only flags the gap so it is a tracked reconciliation item rather than a silent omission. Corresponding note added to CLAUDE.md V1.5's Version History.
* Equities is NOT execution-ready under Constitution V1.5 until this is resolved.

v2.1 — Grading Mechanic Fix

* Fixed §11–12 grading mechanic to match AGENT_NICKEL_CORE.md: Volume Confirmation is now a one-level post-hoc grade upgrade (B→A, A→A+, capped at A+), not a tied third condition. No change to Initial Validation risk treatment (still flat 3% regardless of grade). No prior committed version had this fix — v1.0–v2.0 all had the tied-condition error.

v2.0 — Reconciled Build

* Supersedes v1.0, the only version previously committed to this repository. Consolidates v1.1 through v1.5 (produced in a separate planning conversation, never previously pushed to this repository) into a single authoritative version.
* Re-cited against CLAUDE.md V1.4, which added the Initial Validation Flat-Risk Exception as a new amendment to §2, alongside the existing V1.3 Mission section already in this repository's committed history (commit `9f81c89`) — see CLAUDE.md's own Version History for the corrected account.
* No rules, numbers, or thresholds changed from v1.5 in this consolidation — only version numbering and Constitutional citations were updated to match V1.4.

v1.5 — Flat-Risk Mission Realignment

* Raised Initial Validation risk from flat 1.5% to flat 3.0%, authorized under CLAUDE.md V1.4 Section 2's new Initial Validation Flat-Risk Exception (drafted and adopted alongside this version — see CLAUDE.md Version History).
* Rationale: 1.5% was a compliance-driven number (fit inside B's then-permanent ceiling), not a mission-driven one. 3.0% better serves Initial Validation's actual purpose — testing whether disciplined edge can produce meaningful micro-account growth — while remaining well short of ruin even under sustained losing streaks (10 straight full-risk stop-outs ≈ -26.3% compounded, leaving ~74% of equity), and while reducing the degree to which execution friction and rounding dominate the P/L signal at micro-account dollar amounts.
* Recalculated Section 21's two-loss brake math for 3.0% flat risk (~5.9% instead of ~3%) and the corresponding figure in Section 22's loss-hierarchy summary.
* Explicitly reaffirmed: grade-weighted sizing (Section 14) remains locked and is unaffected by this change — the Flat-Risk Exception does not authorize it, and it terminates automatically when Initial Validation ends.

v1.4 — Loss-Basis Clarification

* Clarification only — no thresholds or behavior changed.
* Section 21 now states explicitly that the two-loss brake is realized-loss based by design (counts only completed, closed-trade losses), distinct from Section 22's emergency trigger, which continuously monitors realized-plus-open-unrealized (mark-to-market) loss.
* Section 22 cross-references Section 21's Basis note so the two loss bases aren't mistaken for the same quantity.

v1.3 — Determinism Pass

* Added Section 4: explicit, single definition of 1R (actual filled entry price vs. initial stop, actual filled quantity) — separates proposed pre-trade risk from actual post-fill risk used in every R-multiple calculation throughout the document.
* Added mechanical swing-high/swing-low definition (Section 9) — 2-bar fractal confirmation, strict-inequality HH/HL test, session-only window, explicit "insufficient data → NO TRADE" fallback. Closes the ambiguity that let structure be read differently setup-to-setup.
* Rewrote volume confirmation (Section 11, Condition B) as an exact formula: either-candle rule, 20-completed-candle trailing average excluding the candle itself, session-only boundary, explicit insufficient-data fallback.
* Replaced "approach or reach the constitutional ceiling" (Section 22) with a deterministic 9.0% trigger threshold — a defined 1.0-point buffer below the Constitution's 10% hard ceiling — and clarified that actually reaching 10% is a constitutional violation, not a routine stop.
* Flagged protective exit method (Section 18) as an explicit undefined placeholder rather than implicit vague language, and added a hard precondition (Section 28) requiring capability_check.py to name exact order types for normal-stop, time-stop, and emergency exits before live trading is authorized.

v1.2 — Constitutional-Compliance Fix

* Corrected Initial Validation risk from flat 3% to flat 1.5% — flat 3% was compliant for A+/A grades but silently exceeded the Constitution's 1.5% cap on B-grade trades the moment a B-grade setup fired. Flat 1.5% is at or below every grade's ceiling, so identical risk treatment across grades is actually true, not just stated.
* Reinstated a 30-minute approval timeout as a backstop alongside condition-based approval expiry.
* Recalculated Section 21's two-loss daily-brake math for the new 1.5% flat risk (~3% instead of ~6%).
* Added explicit sign-off note recording that the override of the prior session's locked grade-weighted risk and tiered R:R decisions was reviewed and approved by Smitty.

v1.1 — Validation Build

* Established deterministic Daily / 5-minute / 1-minute timeframe hierarchy.
* Separated setup grade from risk allocation during Initial Validation.
* Established fixed risk for all qualifying grades.
* Locked grade-weighted 5% / 3% / 1.5% sizing pending empirical validation.
* Reframed PDL validity as a testable hypothesis rather than assumed edge.
* Added naked-vs-structurally-reinforced PDL research classification.
* Separated normal two-loss operating brake from 10% constitutional emergency ceiling.
* Clarified operational autonomy vs statistical proof of edge.
* Added explicit autonomy revocation.
* Added validation-discipline requirements.
* Preserved SPY-only, long-only scope and PDL reclaim mechanics.
