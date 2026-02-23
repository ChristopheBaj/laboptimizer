from fastapi import FastAPI

from app.core.random_search import random_search

app = FastAPI(title="LabOptimizer")


@app.get("/")
def root():
    return {"service": "LabOptimizer", "docs": "/docs", "health": "/health"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/optimize/random")
def optimize_random():
    # Objective “toy” : minimum at x=2
    def f(x: float) -> float:
        return (x - 2) ** 2

    result = random_search(f, x_min=-10, x_max=10, n_trials=200, seed=0)
    return {"best_x": result.best_x, "best_y": result.best_y}
