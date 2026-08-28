import pandas as pd
from pathlib import Path

from models.bug import Bug


def load_historical_bugs() -> pd.DataFrame:
    """
    Load historical bug records from the CSV file.
    """

    file_path = Path(__file__).parent.parent / "data" / "historical_bugs.csv"

    bugs = pd.read_csv(file_path)

    return bugs


def load_historical_bug_models() -> list[Bug]:
    """
    Load historical bugs and convert each record into a Bug model.
    """

    bugs = load_historical_bugs()

    bug_models = [
        Bug(**row.to_dict())
        for _, row in bugs.iterrows()
    ]

    return bug_models