"""
Healthcare feature engineering utilities.

Phase 5:
- Clinical features
- Utilization features
- Risk indicators
- Interaction features
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def create_total_visits(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Total healthcare utilization.
    """
    df = df.copy()

    df["total_visits"] = (
        df["number_outpatient"]
        + df["number_emergency"]
        + df["number_inpatient"]
    )

    return df


def create_total_meds_ratio(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Medication intensity relative to stay length.
    """
    df = df.copy()

    df["total_meds_ratio"] = (
        df["num_medications"]
        / (df["time_in_hospital"] + 1)
    )

    return df


def create_prior_visits_flag(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Previous healthcare interaction indicator.
    """
    df = df.copy()

    df["prior_visits_flag"] = np.where(
        (
            df["number_outpatient"]
            + df["number_emergency"]
        ) > 0,
        1,
        0
    )

    return df


def create_high_glucose_flag(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Severe glucose indicator.
    """
    df = df.copy()

    df["high_glucose_flag"] = np.where(
        df["max_glu_serum"].isin(
            [">200", ">300"]
        ),
        1,
        0
    )

    return df


def create_polypharmacy_flag(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Excessive medication burden.
    """
    df = df.copy()

    df["polypharmacy"] = np.where(
        df["num_medications"] > 15,
        1,
        0
    )

    return df


def create_meds_per_day(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Daily medication burden.
    """
    df = df.copy()

    df["meds_per_day"] = (
        df["num_medications"]
        / (df["time_in_hospital"] + 1)
    )

    return df


def create_long_stay_flag(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Long hospitalization indicator.
    """
    df = df.copy()

    df["long_stay_flag"] = np.where(
        df["time_in_hospital"] > 7,
        1,
        0
    )

    return df


def create_chronic_patient_flag(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Frequent inpatient care indicator.
    """
    df = df.copy()

    df["chronic_patient_flag"] = np.where(
        df["number_inpatient"] > 2,
        1,
        0
    )

    return df


def create_frequent_visitor_flag(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Frequent healthcare utilization.
    """
    df = df.copy()

    df["frequent_visitor_flag"] = np.where(
        df["total_visits"] > 3,
        1,
        0
    )

    return df


def create_utilization_score(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Combined healthcare usage score.
    """
    df = df.copy()

    df["utilization_score"] = (
        df["number_outpatient"]
        + df["number_emergency"] * 2
        + df["number_inpatient"] * 3
    )

    return df


def create_clinical_complexity_score(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Overall disease burden score.
    """
    df = df.copy()

    df["clinical_complexity_score"] = (
        df["num_medications"]
        + df["number_diagnoses"]
    )

    return df


def create_interaction_features(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Clinical interaction features.
    """
    df = df.copy()

    df["stay_medication_interaction"] = (
        df["time_in_hospital"]
        * df["num_medications"]
    )

    df["diagnosis_medication_interaction"] = (
        df["number_diagnoses"]
        * df["num_medications"]
    )

    df["inpatient_emergency_interaction"] = (
        df["number_inpatient"]
        * df["number_emergency"]
    )

    return df