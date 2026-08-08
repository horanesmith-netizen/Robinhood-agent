Agent Nickel Strategy

Version: 0.2
Status: Research Approved
Live Trading: Not Authorized
Prerequisites: See README.md Technical Preconditions
Constitution: CLAUDE.md
Approved Instrument: SPY
Strategy: Previous-Day Low Support Reclaim — Long
Owner: Agent Nickel Capital

⸻

Strategy Name

Previous-Day Low Support Reclaim — Long

This document defines the ONLY autonomous trading setup currently approved for Agent Nickel.

All activity remains subject to the rules contained in CLAUDE.md.

If this strategy conflicts with the Agent Nickel Constitution, the Constitution takes precedence.

Live autonomous trading is not authorized until every Technical Precondition defined in README.md has been verified.

Until then, Agent Nickel remains in Research Mode.

⸻

1. Objective

Agent Nickel is testing whether a simple, rules-based support-reclaim strategy can produce positive expectancy while maintaining strict risk discipline.

The objective of Version 0.2 is NOT to maximize profits.

The objective is to:

* Execute one clearly defined setup consistently.
* Minimize subjective interpretation.
* Preserve capital.
* Collect useful live and shadow-trade data.
* Compare the same setup across different morning trading windows.
* Determine whether the setup demonstrates positive expectancy.
* Determine whether the currently proposed execution window is superior, inferior, or comparable to other morning windows.

Agent Nickel must prioritize rule adherence over trade frequency.

No qualifying setup = no trade.

⸻

2. Authorized Instrument

Agent Nickel may autonomously evaluate:

SPY — SPDR S&P 500 ETF Trust

No other symbol is authorized under Version 0.2.

Trading or evaluating another symbol requires explicit user authorization.

⸻

3. Direction

LONG ONLY

Agent Nickel may evaluate long SPY setups.

Agent Nickel may NOT:

* Short SPY.
* Buy puts.
* Trade inverse ETFs as a substitute for shorting.
* Use options.
* Use leverage.
* Use margin borrowing.

⸻

4. Research Observation Window

Agent Nickel must monitor the approved setup from:

8:00 AM – 12:00 PM Eastern Time

This entire period is the:

Research Observation Window

The morning session is divided into four research buckets.

Window A — Premarket

8:00 AM – 9:30 AM ET

* Observation only.
* No live trades.
* Log all qualifying or potentially qualifying PDL support-reclaim setups.

Window B — Opening Volatility

9:30 AM – 9:45 AM ET

* Observation only.
* No live trades.
* Log all qualifying or potentially qualifying PDL support-reclaim setups.

Window C — Proposed Live Trading Window

9:45 AM – 11:00 AM ET

* This is the proposed live execution window.
* Live execution remains disabled until all Technical Preconditions are verified.
* Shadow logging is still required.
* All strategy and Constitution rules apply.

Window D — Late Morning

11:00 AM – 12:00 PM ET

* Observation only.
* No new live positions.
* Log all qualifying or potentially qualifying PDL support-reclaim setups.

No live position may be initiated outside Window C.

⸻

5. Purpose of Shadow Observation

Shadow observation is used to determine whether the approved strategy performs differently depending on time of day.

A shadow trade must follow the SAME setup logic used for any future live trade.

Agent Nickel must NOT loosen, alter, reinterpret, or optimize the strategy simply because the trade is hypothetical.

For each qualifying shadow setup, calculate the theoretical:

* Entry
* Stop
* Target
* Position risk
* Outcome
* Maximum Favorable Excursion
* Maximum Adverse Excursion
* R multiple

Shadow trades must be clearly marked:

SHADOW — NOT EXECUTED

Shadow results must never be represented as actual Robinhood trades or actual portfolio performance.

⸻

6. Reference Support Level

Version 0.2 uses ONE primary support reference:

Previous Trading Day Low — PDL

Before the market opens, record when available:

* Previous trading day’s low.
* Previous trading day’s close.
* Current premarket price.
* Current premarket low.

Only the Previous Trading Day Low is an authorized entry reference in Version 0.2.

Premarket low and previous close are collected for research purposes only.

⸻

7. Support Zone

Define the PDL support zone as:

PDL ± 0.10%

Example:

If PDL = $600.00:

* Upper boundary = $600.60
* Lower boundary = $599.40

A support test occurs when SPY trades inside this zone during the Research Observation Window.

Touching the zone alone is NOT an entry signal.

⸻

8. Required Support Test

For a setup to become eligible:

1. SPY must trade inside the PDL support zone.
2. Price must subsequently trade at or below the exact PDL.
3. Price must NOT fall more than 0.15% below PDL before reclaiming it.

If price trades more than 0.15% below PDL before a valid reclaim:

THE SETUP IS INVALIDATED.

Do not execute or record a successful theoretical entry for that occurrence.

The invalidated occurrence should still be logged for research.

⸻

9. Reclaim Confirmation

After testing PDL, SPY must reclaim the level.

A valid reclaim requires:

1. A completed 1-minute candle CLOSE above the exact PDL.

AND

2. The following completed 1-minute candle must NOT close below PDL.

The second candle serves as confirmation that the reclaim was not immediately rejected.

Do NOT evaluate an incomplete candle as complete.

Do NOT predict that a candle will close above PDL.

Wait for completed data.

This same reclaim definition must be used for both shadow and future live setups.

⸻

10. Proposed Live Entry

Live entry may eventually be permitted ONLY during:

9:45 AM – 11:00 AM ET

Live execution remains disabled until every Technical Precondition in README.md has been verified.

After a valid reclaim confirmation:

Place a LIMIT BUY order.

Initial permitted limit price:

No higher than 0.05% above the confirmed reclaim price.

Do not chase price beyond this threshold.

If SPY moves beyond the permitted entry range before the order fills:

Cancel the unfilled order.

Record:

QUALIFIED LIVE SETUP — NO FILL

Do not increase the limit price simply to obtain execution.

Missing the trade is acceptable.

⸻

11. Shadow Entry

For qualifying setups outside the authorized live window, or while Agent Nickel remains in Research Mode:

Calculate a theoretical limit entry using the SAME rule:

No higher than 0.05% above the confirmed reclaim price.

If price moves beyond the theoretical permitted entry range before a hypothetical fill would have occurred:

Record:

QUALIFIED SHADOW SETUP — NO FILL

Do not assume a favorable fill merely because the trade is hypothetical.

Shadow execution assumptions must remain conservative and consistent.

⸻

12. Stop Loss

Every live or shadow trade must have a predetermined invalidation point BEFORE entry.

Initial stop:

0.15% below PDL

The stop level must be calculated before entry.

Agent Nickel may NEVER:

* Move the stop farther away after entry.
* Remove the stop because price may recover.
* Average down.
* Add to a losing position.

For shadow trades, record the trade as stopped if price reaches the theoretical stop.

For future live trades, exits must follow CLAUDE.md.

⸻

13. Profit Target

Version 0.2 requires a minimum:

2:1 reward-to-risk ratio

Calculate:

Entry price − Stop price = 1R

Profit target:

Entry price + (2 × 1R)

Example:

Entry = $600.40
Stop = $599.50
Risk = $0.90/share
2R target = $602.20

The trade may NOT be entered or counted as a qualifying shadow trade unless a valid 2R target can be calculated.

⸻

14. Position Risk

Version 0.2 maximum risk per future live trade:

0.50% of total Agent Nickel account equity

Example:

Account equity = $50

Maximum permitted theoretical loss:

$0.25

Position quantity must be sized so that the theoretical loss from entry to stop does not exceed the maximum permitted account risk.

Fractional shares may be used only if supported and verified through the connected Robinhood MCP.

All future live position sizing remains subject to the stricter capital and position limits in CLAUDE.md.

The most restrictive rule always wins.

For shadow trades, calculate theoretical quantity using the same account-equity and risk-percentage framework.

⸻

15. Maximum Live Trades

Maximum completed live entries:

2 trades per trading day

Maximum live attempts at the same PDL setup:

2 per trading day

After two stopped-out live trades:

STOP LIVE TRADING FOR THE DAY.

Do not attempt a third live entry even if another valid reclaim occurs.

Shadow observation must continue through 12:00 PM.

⸻

16. Daily Loss Circuit Breaker

Maximum realized LIVE trading loss per day:

1.0% of beginning-of-day Agent Nickel account equity

Example:

Beginning equity = $50

Maximum daily realized loss:

$0.50

Once live realized losses equal or exceed this amount:

NO NEW LIVE POSITIONS MAY BE OPENED THAT DAY.

Shadow observation may continue.

The circuit breaker resets on the next trading day based on that day’s beginning account equity.

Shadow losses do NOT count toward the live-account daily-loss circuit breaker.

They must still be recorded separately for research.

⸻

17. No-Trade Conditions

Agent Nickel must NOT initiate a live trade when:

* Live Trading has not been explicitly authorized.
* Any Technical Precondition in README.md remains unverified.
* Current time is outside 9:45 AM–11:00 AM ET.
* SPY has not tested the PDL support zone.
* SPY violated the 0.15% downside invalidation threshold before reclaim.
* A completed 1-minute candle has not closed above PDL.
* The confirmation candle closes below PDL.
* Required account information is unavailable.
* Required market data is unavailable.
* Position sizing cannot satisfy risk limits.
* A 2R target cannot be established.
* Daily live-trade limit has been reached.
* Daily live-loss circuit breaker has been reached.
* Robinhood indicates an account restriction.
* Market data required to evaluate the setup is missing, stale, contradictory, or unreliable.

When uncertain:

NO LIVE TRADE.

For shadow observation, missing or unreliable market data means:

DO NOT FABRICATE THE SETUP OR RESULT.

Log the data issue instead.

⸻

18. Volume

Volume is NOT an entry requirement in Version 0.2.

However, Agent Nickel should record when available:

* Volume on the support-test candle.
* Volume on the reclaim candle.
* Volume on the confirmation candle.

This information is collected for later analysis.

Do NOT reject or approve a trade based on volume in Version 0.2.

⸻

19. Time-Window Classification

Every live or shadow setup must be assigned to exactly ONE time bucket based on the time of reclaim confirmation:

* Window A: 8:00–9:30 AM
* Window B: 9:30–9:45 AM
* Window C: 9:45–11:00 AM
* Window D: 11:00 AM–12:00 PM

The time bucket must be recorded before evaluating the outcome.

Never reclassify a setup after seeing whether it won or lost.

⸻

20. Trade and Shadow Logging

For every valid or invalidated setup, record when available:

Market Context

* Date
* PDL
* Previous close
* Premarket low
* SPY price at 8:00 AM
* SPY price at 9:30 AM
* SPY price at 9:45 AM
* SPY price at 11:00 AM

Setup Classification

* Live or Shadow
* Time bucket: A, B, C, or D
* Time PDL zone was first tested
* Lowest price during test
* Maximum penetration below PDL
* Reclaim candle time
* Reclaim candle close
* Confirmation candle time
* Confirmation candle close
* Valid or invalidated setup

Trade

* Entry price
* Quantity or theoretical quantity
* Dollar position size
* Stop price
* Target price
* Dollar risk
* Account risk percentage
* Exit price
* Exit time
* Exit reason
* Realized or theoretical P/L
* R multiple

Excursion Data

Record when market data allows:

* Maximum Favorable Excursion — MFE
* Maximum Adverse Excursion — MAE

Volume Research

* Test candle volume
* Reclaim candle volume
* Confirmation candle volume

Execution Classification

Use one of:

* LIVE — FILLED
* LIVE — PARTIALLY FILLED
* LIVE — QUALIFIED / NO FILL
* LIVE — CANCELED
* SHADOW — THEORETICAL FILL
* SHADOW — QUALIFIED / NO FILL
* INVALIDATED SETUP
* DATA INSUFFICIENT

⸻

21. Research Metrics

Agent Nickel should maintain separate statistics for each time bucket.

At minimum, track:

* Number of qualifying setups
* Number of fills or theoretical fills
* Wins
* Losses
* Win rate
* Average winning R
* Average losing R
* Average R per trade
* Expectancy
* Maximum consecutive losses
* Percentage reaching +1R
* Percentage reaching +2R
* Average MFE
* Average MAE

Live and shadow performance must also be reported separately.

Do NOT combine actual Robinhood P/L with theoretical shadow P/L.

⸻

22. Strategy Evaluation

Do not change the proposed trading window because of a small number of observations.

Time-window performance should be evaluated only after a meaningful sample has accumulated.

Agent Nickel may report observations such as:

* One window appears cleaner.
* One window produces more invalidations.
* One window reaches 2R more frequently.
* One window experiences greater adverse excursion.
* One window produces substantially more setups.

These observations are NOT authorization to modify the strategy.

Any change to the trading window requires explicit user approval and a new strategy version.

⸻

23. Strategy Modification

Agent Nickel may NOT modify this strategy during market operation.

Agent Nickel may identify observations or potential improvements but must record them separately.

Potential improvements must NOT affect execution until explicitly approved by the user and incorporated into a new strategy version.

Examples include:

* Different support-zone width.
* Different reclaim confirmation.
* Volume requirements.
* Different authorized trading window.
* Premarket live execution.
* Opening-bell execution.
* Premarket-low setups.
* VWAP.
* QQQ.
* Trailing stops.
* Partial profit taking.
* Different reward/risk targets.

These are research questions, NOT current trading authority.

⸻

24. Technical Capability Dependency

This strategy depends on technical capabilities that must be verified through the connected Robinhood MCP.

Required capabilities include:

* SPY market data.
* Historical OHLCV data.
* 1-minute candle availability.
* Ability to distinguish completed candles from currently forming candles.
* Previous-day price data.
* Required premarket data.
* Current quotes.
* Buying power.
* Account equity.
* Positions.
* Open orders.
* Order status and fill status.
* Fractional SPY trading.
* Fractional SPY LIMIT BUY orders.
* Fractional SPY LIMIT SELL orders.
* Fractional-order precision compatible with Agent Nickel’s account size and risk limits.

If any single required Technical Precondition cannot be verified:

AGENT NICKEL REMAINS IN RESEARCH MODE IN FULL.

There is no partial authorization for live trading.

Research Mode may continue to include:

* Observation.
* Shadow trading.
* Data collection.
* Strategy analysis.
* Reporting.

Research Mode may NOT include:

* Live order submission.
* Modification of live positions.
* Management of real trading capital.

⸻

25. Core Principle

Agent Nickel does not predict what SPY will do.

Agent Nickel waits for a predefined market condition and responds according to predefined rules.

Agent Nickel observes more than it trades.

Agent Nickel does not need to trade every day.

Agent Nickel does not chase missed trades.

Agent Nickel does not change rules because of fear, excitement, previous losses, or previous gains.

Agent Nickel treats live trades and shadow trades according to the same setup logic.

THE SETUP EITHER QUALIFIES OR IT DOES NOT.

If it qualifies during Window C and Live Trading has been authorized:

Execute according to this strategy and the Constitution.

If it qualifies outside Window C, or Agent Nickel remains in Research Mode:

Record it as a shadow setup.

If it does not qualify:

DO NOTHING.
