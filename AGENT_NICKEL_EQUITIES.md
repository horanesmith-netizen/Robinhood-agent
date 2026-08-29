# Agent Nickel Equities Strategy
## Version 1.0

This document defines equities and ETF-specific trading rules for
Agent Nickel (Track 1 — Smitty, NY).

This document is governed by the Agent Nickel Constitution (CLAUDE.md)
and by AGENT_NICKEL_CORE.md. Both override this document in any conflict.

Effective on commit, this document formally supersedes
AGENT_NICKEL_STRATEGY.md v0.2 for all risk-sizing and grading rules.
The reclaim mechanics defined in AGENT_NICKEL_STRATEGY.md (PDL zone,
breach threshold, reclaim confirmation, entry/stop/target calculation)
remain in force and are incorporated here by reference — they are not
being rewritten, only re-graded and re-sized under the new
percentage-based risk framework. The daily realized-loss circuit
breaker from AGENT_NICKEL_STRATEGY.md v0.2 also remains in force
unchanged (see TRADE FREQUENCY AND DAILY LIMITS below) — it is
stricter than the Constitution's default ceiling, and per Constitution
Section 9 the stricter limit governs.

---

## SCOPE

- Asset class: Equities and ETFs only.
- Authorized instrument: SPY only. No other symbol is authorized
  under this version. Trading or evaluating another symbol requires
  explicit user authorization per Constitution Section 4.
- Direction: LONG ONLY. No shorting, no puts, no inverse ETFs, no
  margin, no leverage.

---

## REGIME INSTRUMENT

Per CORE.md Step 1, the primary trend instrument for equities regime
classification is SPY itself, measured on the Daily chart 50 EMA.

- Aggressive: SPY above Daily 50 EMA, higher highs/higher lows, no
  extreme volatility event active.
- Selective: SPY near Daily 50 EMA, mixed structure.
- Defensive: SPY below Daily 50 EMA, lower lows. No new positions.
- No Trade: extreme volatility event, major news imminent/breaking,
  account restriction, or capability verification incomplete.

Per CORE.md, Defensive and No Trade regimes are an absolute bar on new
positions — see the baseline qualification gate below. This is
independent of, and takes priority over, the grade-scoring conditions.

---

## APPROVED SETUP: PDL SUPPORT RECLAIM (Setup EQ-1)

Edge source: institutional re-entry after a reclaim of the previous
trading day's low — the same setup defined in AGENT_NICKEL_STRATEGY.md
v0.2, re-graded under this file.

### Mechanics (incorporated from AGENT_NICKEL_STRATEGY.md — unchanged)

- **PDL support zone:** PDL ± 0.10%.
- **Max breach before invalidation:** price must not trade more than
  0.15% below PDL before reclaiming it. Breach beyond that
  invalidates the setup.
- **Reclaim confirmation:** a completed 1-minute candle closes above
  PDL, AND the following completed 1-minute candle does not close
  back below PDL. No incomplete candle may be evaluated as complete.
  No candle close may be predicted in advance.
- **Entry:** limit buy no higher than 0.05% above the confirmed
  reclaim price. If price moves beyond this range before fill,
  cancel the order — do not chase. This is a passive limit order,
  not a marketable limit — see ORDER TYPE below.
- **Stop loss:** 0.15% below PDL, set before entry. Never widened
  after entry.

### Order type (clarification — not a deviation)

Constitution V1.2 Section 3 permits marketable limit orders ONLY for
breakout entries (CORE.md Setup 2 and Setup 3) and time-stop exits.
Setup EQ-1 is a standard zone entry (CORE.md Setup 1 pattern), not a
breakout, so it does not qualify for marketable-limit entry even
though CORE.md's generic Step 8 execution table lists "Marketable
limit" as the default for "Standard entry at zone." Where CORE.md's
generic table and the Constitution's narrower, setup-specific list
disagree, the Constitution governs. EQ-1 entries therefore use a
passive limit order as defined in Mechanics above. Time-stop exits
(see POSITION MANAGEMENT) do use a marketable limit, per the
Constitution's explicit exception for that scenario.

### Baseline qualification gate (required for ANY grade)

All of the following must be true before Setup EQ-1 qualifies at any
grade. If any is false: NO TRADE.

1. Valid PDL reclaim confirmed per the mechanics above.
2. Confirmed uptrend per CORE.md Step 2a (higher highs AND higher
   lows on the primary timeframe). A reclaim without a confirmed
   uptrend does not qualify at any grade.
3. Regime is Aggressive or Selective. Defensive and No Trade regimes
   are an absolute bar on new positions per CORE.md's regime
   definitions ("No new positions" / "Full stop") — this holds
   regardless of how the reclaim otherwise looks, and regardless of
   the grade-scoring conditions below.

### Additional conditions (grade-determining)

With the baseline gate satisfied, count how many of the following
two conditions are also met:

1. **50 EMA confluence** — SPY's 50 EMA (Daily) is within 1% of the
   PDL zone price, per CORE.md's confluence definition.
2. **Aggressive regime** — regime classification (above) is
   specifically Aggressive at time of confirmation, not just
   Selective. (Selective satisfies the baseline gate but does not
   earn this point.)

**Volume upgrade (separate from the count above):** per CORE.md Step
4's Volume Upgrade rule, if the reclaim or confirmation candle's
volume exceeds 1.3x the 20-period average, upgrade the grade
determined below by one level (B→A, A→A+). A+ cannot be upgraded
further. Volume is a post-grade bonus, not one of the counted
conditions — this matches CORE.md's actual mechanic.

> **Flagged deviation:** an earlier draft of this document counted
> volume as a third, equally-weighted condition alongside EMA
> confluence and regime (requiring 1-of-3 / 2-of-3 / 3-of-3 for
> B/A/A+). That is not what CORE.md Step 4 specifies — CORE.md treats
> volume as a one-level upgrade applied after the base grade is set,
> not a base-grade input. This version corrects that: the base grade
> comes from the 2-condition count below, and volume can only bump it
> up one level afterward. This changes some grade outcomes relative
> to the earlier draft (e.g., a reclaim with only volume confirmation
> and neither EMA confluence nor Aggressive regime is now baseline-B
> with no upgrade available, rather than an automatic B under the old
> 1-of-3 count — same result here, but the two mechanics diverge in
> other combinations). Confirm this is the intended mechanic before
> relying on it for sizing.

### Grading and risk allocation

| Grade | Requirement | Risk Allocation | Min R:R |
|-------|-------------|-----------------|---------|
| A+ | Baseline gate + both additional conditions, OR baseline gate + 1 condition + volume upgrade | 5% of equity | 3:1 |
| A | Baseline gate + 1 of 2 additional conditions, OR baseline gate + 0 conditions + volume upgrade | 3% of equity | 2.5:1 |
| B | Baseline gate + 0 of 2 additional conditions | 1.5% of equity | 2:1 |
| No Trade | Baseline gate not satisfied | 0% | — |

Risk allocation and R:R minimums follow Constitution Section 2 and
CORE.md Step 5 — the most restrictive limit between this table, the
Constitution, and CORE.md always applies.

### Zone validation exemption (deviation from CORE.md — flagged)

CORE.md Step 2c requires a zone to be validated by 2+ prior touches
or a >2% move on a prior test before it may be traded. **PDL is
exempt from this test.** It is treated as inherently valid because it
is a fixed, universally-watched daily reference level, not a
discretionarily-identified structure zone. This is a deliberate
deviation from the generic CORE zone-validation rule, carried over
unchanged from AGENT_NICKEL_STRATEGY.md v0.2. Flagging it here so it
isn't mistaken for an oversight.

---

## TRADING WINDOW

Unchanged from AGENT_NICKEL_STRATEGY.md v0.2:

- **Window A (8:00–9:30 AM ET):** Observation/shadow only.
- **Window B (9:30–9:45 AM ET):** Observation/shadow only.
- **Window C (9:45–11:00 AM ET):** Live trading window. Shadow
  logging also required.
- **Window D (11:00 AM–12:00 PM ET):** Observation/shadow only.

No live position may be initiated outside Window C. Shadow logging
is required for all qualifying/invalidated setups in Windows A, B,
C, and D.

---

## POSITION MANAGEMENT

Per CORE.md Step 5, applied to Setup EQ-1:

- **Partial exit:** at 1.5R, move stop to breakeven (no partial
  exit). At 2R, exit 50% of position at limit. Trail the remaining
  50% to the prior swing low on the timeframe below primary.
- **Time stop:** if the trade has not moved 0.5R in either direction
  after 3 primary-timeframe candles, exit via marketable limit
  (permitted for time-stop exits per Constitution Section 3). This
  is thesis expiration, not failure.
- **Take profit:** TP = Entry + (Stop Distance × R:R multiple per
  grade table above).

---

## TRADE FREQUENCY AND DAILY LIMITS

- **Maximum live trades per day:** 2 completed entries. After 2
  stopped-out live trades, stop live trading for the remainder of
  the day; shadow observation continues through 12:00 PM.
- **Daily loss circuit breaker:** 1.0% of Agent Nickel account equity
  at the start of the trading day, per AGENT_NICKEL_STRATEGY.md v0.2
  Section 16. This remains in force unchanged. The Constitution's
  Section 9 default is 10% of starting equity, but Section 9 itself
  states that asset-class files may set a stricter limit and the
  stricter limit governs — so the existing 1.0% figure is not
  superseded by the Constitution's looser default. Selling an
  existing position does not reset or restore this allowance.
- **Max concurrent positions:** 1, per Constitution Section 7. Once
  closed, Agent Nickel may propose another qualifying setup the same
  day if the daily loss limit hasn't been reached and a live trade
  slot remains.

---

## AUTONOMY GATE — EQUITIES

Per CORE.md's universal minimums, applied specifically to this
asset class:

- 20 completed trades in equities (Setup EQ-1).
- Expectancy > 0.3R.
- Profit factor > 1.3.
- Zero constitutional violations in the last 10 trades.
- Zero execution errors in the last 10 trades.
- At least one losing trade handled correctly (stop honored, no
  averaging down, no widened stop).
- Performance observed across at least 2 market regimes (e.g.
  Aggressive and Selective).

Passing this gate does not grant crypto autonomy (Constitution /
CORE.md — gates are independent per asset class).

Until this gate is passed, Agent Nickel operates in **Alert Phase**
for equities: every qualifying Setup EQ-1 trade is proposed via the
CORE.md Step 6 proposal format and requires explicit YES from Smitty
before execution. No response within 30 minutes is treated as NO.

---

## RESEARCH / LOGGING CARRYOVER

All logging fields defined in AGENT_NICKEL_STRATEGY.md v0.2 Section 20
(market context, setup classification, trade data, excursion data,
volume research, execution classification) remain required, combined
with the CORE.md Step 9 journal schema. Where the two overlap, use
the CORE.md field names; where STRATEGY.md v0.2 has a field CORE.md
doesn't (e.g. time-window bucket A/B/C/D), keep it.

Live and shadow performance must be reported separately per
STRATEGY.md v0.2 Section 21. Do not combine actual P/L with
theoretical shadow P/L.

---

## STATUS

Live Trading: Not Authorized until every Technical Precondition in
README.md is verified via the Robinhood capability check
(capability_check.py — not yet built). Until then, Agent Nickel
remains in Research Mode for equities: observation, shadow trading,
and data collection only. No live order submission.

---

## VERSION HISTORY
- v1.0: Initial release. Formally supersedes AGENT_NICKEL_STRATEGY.md
  v0.2 risk-sizing and grading (flat 0.50%/trade) with grade-based
  percentage risk (5%/3%/1.5%) per Constitution V1.2. The 1.0%/day
  circuit breaker from STRATEGY.md v0.2 remains in force unchanged
  (it is stricter than the Constitution's 10%/day default, and
  Constitution Section 9 specifies the stricter limit governs).
  Reclaim mechanics unchanged. PDL exempted from CORE.md Step 2c zone
  validation (deliberate deviation, documented above). Volume treated
  as a post-grade upgrade per CORE.md Step 4, not a base-grade
  condition (corrected from an earlier draft — documented above).
  Added explicit baseline-gate exclusion for Defensive/No Trade
  regimes per CORE.md's regime definitions.
