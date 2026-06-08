"""
Data preprocessing utilities.

Phase 4:
- Missing value handling
- Duplicate analysis
- Leakage removal
"""

from typing import List

import numpy as np
import pandas as pd


MISSING_VALUE_TOKEN = "?"


def replace_question_marks(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Replace '?' with NaN.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """
    df = df.copy()

    df.replace(
        MISSING_VALUE_TOKEN,
        np.nan,
        inplace=True
    )

    return df


def remove_leakage_columns(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Remove identifier columns.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """
    leakage_columns: List[str] = [
        "encounter_id",
        "patient_nbr"
    ]

    return df.drop(
        columns=leakage_columns,
        errors="ignore"
    )