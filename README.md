# Robinhood-agent
Agent Nickel

Simple Rules. Ruthless Discipline. Continuous Learning.

Agent Nickel is an autonomous equities research and execution project designed to test whether a deliberately simple, rules-based trading strategy can produce positive expectancy while maintaining strict risk management.

The project intentionally begins with a very small amount of capital. The objective is not to maximize profits, but to validate execution, risk controls, strategy discipline, and data collection before increasing capital allocation.

This repository serves as the operational headquarters for Agent Nickel.

⸻

Mission

Agent Nickel exists to answer one question:

Can a simple, objective trading strategy consistently outperform discretionary decision-making while maintaining strict capital preservation?

The philosophy is intentionally minimalist.

* Fewer variables.
* Fewer assumptions.
* Fewer opportunities for emotional decision-making.
* Maximum consistency.

If a strategy cannot demonstrate an edge with simple rules, additional complexity will not be used to rescue it.

⸻

Core Principles

Agent Nickel is built around the following principles:

* Preserve capital first.
* Execute only predefined strategies.
* Never improvise during live trading.
* Separate strategy from execution.
* Separate execution from risk management.
* Every trade must be explainable.
* Every trade must be measurable.
* Every trade contributes to research.

Missing a trade is acceptable.

Violating the rules is not.

⸻

Repository Structure

README.md

Project overview, architecture, deployment status, and technical prerequisites.

⸻

CLAUDE.md

The Agent Nickel Constitution.

Defines permanent operating rules, including:

* Capital allocation
* Risk management
* Order execution rules
* Compliance guardrails
* Fail-safe behavior
* Autonomous trading authority

These rules override every trading strategy.

⸻

AGENT_NICKEL_STRATEGY.md

Defines the currently approved trading strategy.

Contains:

* Market selection
* Entry criteria
* Exit criteria
* Observation windows
* Shadow trading methodology
* Position sizing
* Daily risk limits
* Trade logging requirements

Strategies may evolve.

The Constitution does not.

⸻

/docs

Supporting documentation including:

* Research notes
* Future ideas
* Strategy revisions
* Architecture diagrams
* Experimental findings

⸻

/logs

Daily execution logs.

Includes:

* Live trades
* Shadow trades
* Daily summaries
* Performance metrics
* Exceptions
* Errors

⸻

/data

Historical datasets and exported market observations used for research and analysis.

⸻

/scripts

Automation, scheduling, utilities, reporting tools, and future deployment scripts.

⸻

Current Development Phase

Phase 1 — Research & Validation

Current objectives:

* Finalize operating Constitution.
* Validate Robinhood MCP capabilities.
* Confirm market-data availability.
* Verify execution behavior.
* Perform shadow observation.
* Validate live execution using minimal capital.
* Collect statistically meaningful performance data.

Optimization is intentionally deferred until sufficient evidence has been collected.

⸻

Technical Preconditions

Live autonomous trading must NOT be enabled until the following capabilities have been verified.

Broker Connectivity

* Robinhood MCP connected.
* Authentication verified.
* Buying power accessible.
* Positions accessible.
* Orders accessible.
* Order status accessible.

⸻

Market Data

* Historical OHLCV available.
* 1-minute candles supported.
* Completed candles distinguishable from active candles.
* Previous-day market data available.
* Required premarket data available.
* Current market quotes available.

⸻

Order Capability

* Fractional-share trading supported.
* Fractional LIMIT orders supported.
* Fractional BUY orders supported.
* Fractional SELL orders supported.
* SPY eligible for fractional trading through the Agentic account.
* Position sizing compatible with Constitution limits.

⸻

Safety

* Constitution loaded.
* Approved strategy loaded.
* Logging verified.
* Circuit breakers verified.
* Fail-safe behavior verified.

If any prerequisite cannot be verified:

Remain in Research Mode.

If any single Technical Precondition cannot be verified, Agent Nickel remains in Research Mode in full. There is no partial authorization for live trading.

Do not weaken the Constitution or alter the strategy solely to accommodate platform limitations.

⸻

Operating Philosophy

Agent Nickel does not predict markets.

Agent Nickel waits.

Markets provide opportunities.

The strategy determines whether an opportunity qualifies.

The Constitution determines whether the trade is permitted.

Only then may execution occur.

⸻

Future Roadmap

The long-term vision is to evolve Agent Nickel into a disciplined research platform capable of evaluating multiple independent trading strategies under a common governance framework.

Potential future areas include:

* Additional market windows
* Alternative support and resistance models
* Volume-based confirmation
* VWAP-based strategies
* Additional ETFs
* Strategy comparison framework
* Portfolio-level capital allocation
* Performance dashboards
* Automated reporting
* Cloud-based execution

Each new strategy must earn deployment through research and validation.

No strategy receives live capital simply because it appears promising.

⸻

Current Status

Research Mode

Live execution is intentionally limited while the architecture, strategy, risk controls, and broker capabilities are validated.

Capital preservation takes priority over profit generation.

Agent Nickel earns additional responsibility through evidence—not optimism.

⸻

“Simple systems are easier to understand, easier to audit, and harder to fool.”
