import os
import pytest
from mylib.lib import (
    extract,
    load_data,
    example_transform,
    start_spark,
    end_spark,
)

@pytest.fixture(scope="module")
def spark():
    spark = start_spark("TestMedicalData")
    yield spark
    end_spark(spark)


def test_extract():
    """Test that the extract function downloads or provides the medical data file."""
    file_path = extract()
    assert os.path.exists(file_path) is True, \
        "The data file should exist after extraction."


def test_load_data(spark):
    """Test that load_data correctly loads the medical dataset into a DataFrame."""
    df = load_data(spark)
    assert df is not None, \
        "DataFrame should not be None."
    assert df.count() > 0, \
        "DataFrame should have at least one row."
    assert "Patient ID" in df.columns, \
        "Expected 'Patient ID' column to be present."


def test_example_transform(spark):
    """Test that example_transform adds the 'RiskCategory' column based on Heart Attack Risk."""
    df = load_data(spark)
    transformed_df = example_transform(df)  
    assert "RiskCategory" in transformed_df.columns, \
        "Expected 'RiskCategory' column after transformation."
    #check that values in 'RiskCategory' are as expected (e.g., 'High Risk' or 'Low Risk').
    sample = transformed_df.select("RiskCategory").head(1)
    assert len(sample) > 0, "Should have at least one row after transformation."
