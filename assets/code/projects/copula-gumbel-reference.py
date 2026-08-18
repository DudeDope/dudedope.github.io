"""Reference implementation of the selected Gumbel-copula workflow.

This is a transparent reconstruction from the public methodology, not the
unavailable original six-family fitting pipeline.
"""

from __future__ import annotations

import argparse

import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar


def extract_events(frame: pd.DataFrame, threshold: float = 100.0) -> pd.DataFrame:
    ordered = frame.sort_values("Datetime").copy()
    ordered["Datetime"] = pd.to_datetime(ordered["Datetime"], errors="raise")
    ordered["AQI"] = pd.to_numeric(ordered["AQI"], errors="raise")

    above = ordered["AQI"] > threshold
    consecutive = ordered["Datetime"].diff().eq(pd.Timedelta(hours=1))
    starts_new_event = above & (~above.shift(fill_value=False) | ~consecutive)
    event_id = starts_new_event.cumsum()

    events = (
        ordered.loc[above]
        .assign(event_id=event_id[above].to_numpy())
        .groupby("event_id", sort=True)
        .agg(duration=("AQI", "size"), severity=("AQI", "sum"))
        .reset_index(drop=True)
    )
    return events


def pseudo_observations(values: pd.Series) -> np.ndarray:
    return values.rank(method="average").to_numpy(dtype=float) / (len(values) + 1.0)


def gumbel_cdf(u: np.ndarray, v: np.ndarray, theta: float) -> np.ndarray:
    if theta < 1.0:
        raise ValueError("the Gumbel parameter must be at least one")
    u = np.clip(u, 1e-12, 1.0 - 1e-12)
    v = np.clip(v, 1e-12, 1.0 - 1e-12)
    exponent = ((-np.log(u)) ** theta + (-np.log(v)) ** theta) ** (1.0 / theta)
    return np.exp(-exponent)


def finite_difference_density(u: np.ndarray, v: np.ndarray, theta: float, step: float = 2e-4) -> np.ndarray:
    lower_u = np.clip(u - step, 1e-9, 1.0 - 1e-9)
    upper_u = np.clip(u + step, 1e-9, 1.0 - 1e-9)
    lower_v = np.clip(v - step, 1e-9, 1.0 - 1e-9)
    upper_v = np.clip(v + step, 1e-9, 1.0 - 1e-9)
    numerator = (
        gumbel_cdf(upper_u, upper_v, theta)
        - gumbel_cdf(upper_u, lower_v, theta)
        - gumbel_cdf(lower_u, upper_v, theta)
        + gumbel_cdf(lower_u, lower_v, theta)
    )
    denominator = (upper_u - lower_u) * (upper_v - lower_v)
    return np.maximum(numerator / denominator, 1e-300)


def fit_gumbel(u: np.ndarray, v: np.ndarray) -> float:
    def negative_log_likelihood(theta: float) -> float:
        density = finite_difference_density(u, v, theta)
        return -float(np.log(density).sum())

    result = minimize_scalar(negative_log_likelihood, bounds=(1.000001, 30.0), method="bounded")
    if not result.success:
        raise RuntimeError(result.message)
    return float(result.x)


def conditional_exceedance(
    events: pd.DataFrame,
    theta: float,
    duration_threshold: int,
    severity_threshold: float,
) -> float:
    f_duration_left = float((events["duration"] < duration_threshold).mean())
    f_severity = float((events["severity"] <= severity_threshold).mean())
    joint_cdf = float(gumbel_cdf(np.array([f_duration_left]), np.array([f_severity]), theta)[0])
    numerator = 1.0 - f_duration_left - f_severity + joint_cdf
    return numerator / (1.0 - f_duration_left)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path")
    parser.add_argument("--city", default="Bangalore")
    parser.add_argument("--duration-threshold", type=int, default=12)
    parser.add_argument("--severity-threshold", type=float, default=2000.0)
    arguments = parser.parse_args()

    data = pd.read_csv(arguments.csv_path, usecols=["City", "Datetime", "AQI"])
    city_data = data.loc[data["City"].eq(arguments.city), ["Datetime", "AQI"]].dropna()
    events = extract_events(city_data)
    u = pseudo_observations(events["duration"])
    v = pseudo_observations(events["severity"])
    theta = fit_gumbel(u, v)
    probability = conditional_exceedance(
        events,
        theta,
        arguments.duration_threshold,
        arguments.severity_threshold,
    )

    print(f"events={len(events)}")
    print(f"theta={theta:.6f}")
    print(f"upper_tail_dependence={2.0 - 2.0 ** (1.0 / theta):.6f}")
    print(f"conditional_exceedance={probability:.6f}")


if __name__ == "__main__":
    main()
