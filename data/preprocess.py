import pandas as pd
from sklearn.preprocessing import LabelEncoder


def preprocess():
    df = pd.read_csv("data/logs.csv")  # Kaggle dataset
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df["error_count"] = df["message"].str.contains("error", case=False).astype(int)
    df["log_level_score"] = LabelEncoder().fit_transform(df["level"])
    df["event_density"] = df.groupby(df["timestamp"].dt.date)["message"].transform(
        "count"
    )
    df["anomaly"] = df["anomaly"].astype(int)

    df[["error_count", "log_level_score", "event_density", "anomaly"]].to_csv(
        "data/preprocessed_logs.csv", index=False
    )


if __name__ == "__main__":
    preprocess()
