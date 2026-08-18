"""Reference implementation of the equations documented in the project report.

This module is not the original experimental pipeline and does not reproduce the
reported grid search without the underlying chronological match and odds data.
"""

from __future__ import annotations

from math import exp, log
from typing import Iterable


def expected_home_score(home_rating: float, away_rating: float, home_advantage: float) -> float:
    return 1.0 / (1.0 + 10.0 ** ((away_rating - (home_rating + home_advantage)) / 400.0))


def update_ratings(
    home_rating: float,
    away_rating: float,
    home_score: float,
    update_factor: float,
    home_advantage: float,
) -> tuple[float, float]:
    """Update ratings after a win (1), draw (0.5), or loss (0)."""
    expected_home = expected_home_score(home_rating, away_rating, home_advantage)
    expected_away = 1.0 - expected_home
    away_score = 1.0 - home_score
    return (
        home_rating + update_factor * (home_score - expected_home),
        away_rating + update_factor * (away_score - expected_away),
    )


def calibrated_home_probability(rating_difference: float, intercept: float, slope: float) -> float:
    linear_predictor = intercept + slope * rating_difference
    if linear_predictor >= 0:
        return 1.0 / (1.0 + exp(-linear_predictor))
    exponential = exp(linear_predictor)
    return exponential / (1.0 + exponential)


def implied_probability(decimal_odds: float) -> float:
    if decimal_odds <= 1.0:
        raise ValueError("decimal odds must exceed one")
    return 1.0 / decimal_odds


def qualifies_as_value_bet(model_probability: float, decimal_odds: float, edge_threshold: float) -> bool:
    return model_probability - implied_probability(decimal_odds) > edge_threshold


def brier_score(probabilities: Iterable[float], outcomes: Iterable[int]) -> float:
    pairs = list(zip(probabilities, outcomes, strict=True))
    if not pairs:
        raise ValueError("at least one prediction is required")
    return sum((probability - outcome) ** 2 for probability, outcome in pairs) / len(pairs)


def log_loss(probabilities: Iterable[float], outcomes: Iterable[int], epsilon: float = 1e-15) -> float:
    pairs = list(zip(probabilities, outcomes, strict=True))
    if not pairs:
        raise ValueError("at least one prediction is required")
    total = 0.0
    for probability, outcome in pairs:
        clipped = min(max(probability, epsilon), 1.0 - epsilon)
        total -= outcome * log(clipped) + (1 - outcome) * log(1.0 - clipped)
    return total / len(pairs)


def flat_stake_profit(won: bool, decimal_odds: float, stake: float) -> float:
    if stake <= 0.0:
        raise ValueError("stake must be positive")
    return (decimal_odds - 1.0) * stake if won else -stake
