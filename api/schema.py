from pydantic import BaseModel


class InputMetrics(BaseModel):
    error_count: int
    log_level_score: float
    event_density: float
