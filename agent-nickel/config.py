# Agent Nickel Configuration
# All trading parameters live here — edit before running

CONFIG = {
    # Account
    "account_budget": 50,
    "max_risk_per_trade": 0.01,

    # Crypto pairs
    "active_pair": "BTC",
    "pairs": ["BTC", "ETH"],

    # Strategy parameters
    "ema_period": 50,
    "timeframe": "4h",
    "min_zone_touches": 2,
    "min_rr_ratio": 2.0,
    "fib_level": 0.382,

    # Trade management
    "max_open_trades": 1,
    "phase": "alert",  # "alert" or "autonomous"

    # Circuit breakers
    "daily_loss_limit": 0.03,
    "weekly_loss_limit": 0.06,
    "consecutive_loss_limit": 3,
    "volatility_threshold": 0.05,

    # Notifications
    "notification_method": "print",
    "your_email": "",
}
