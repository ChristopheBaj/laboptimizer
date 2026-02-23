from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Callable


@dataclass
class RandomSearchResult:
    best_x: float
    best_y: float


def random_search(
    f: Callable[[float], float],
    x_min: float,
    x_max: float,
    n_trials: int = 50,
    seed: int | None = 0,
) -> RandomSearchResult:
    rng = random.Random(seed)
    best_x: float | None = None
    best_y: float | None = None

    for _ in range(n_trials):
        x = rng.uniform(x_min, x_max)
        y = f(x)
        if best_y is None or y < best_y:
            best_x, best_y = x, y

    assert best_x is not None and best_y is not None
    return RandomSearchResult(best_x=best_x, best_y=best_y)
