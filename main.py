from mylib.lib import (
    extract,
    load_data,
    describe,
    query,
    example_transform,
    start_spark,
    end_spark,
)


def main():
    # Extract the data
    extract()  # This downloads the medical dataset CSV

    # Start Spark
    spark = start_spark("HeartData")

    # Load the data
    df = load_data(
        spark, data="data/heart_attack_prediction_dataset.csv", name="HeartData"
    )

    # Describe the data
    describe(df)

    # Run a sample query: for example, average Cholesterol by Country
    query(
        spark,
        df,
        """
        SELECT Country, AVG(Cholesterol) as avg_cholesterol
        FROM HeartData
        GROUP BY Country
        ORDER BY avg_cholesterol DESC
        """,
        "HeartData",
    )

    # Transformation: Add a "RiskCategory" column
    example_transform(df)

    # End Spark Session
    end_spark(spark)


if __name__ == "__main__":
    main()
