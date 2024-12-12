[![Python 3.11.9](https://github.com/syedhumarahim/scaffold/actions/workflows/main.yml/badge.svg)](https://github.com/syedhumarahim/scaffold/actions/workflows/main.yml)
## Medical Data Analysis

This project loads, processes, and analyzes medical patient data using PySpark. It provides operations for loading, describing, querying, and transforming the dataset, enabling insights into patient demographics, health indicators, and heart attack risk factors.

## Project Overview

The dataset contains records of patients along with various health metrics such as Age, Cholesterol, Blood Pressure, Heart Rate, Lifestyle Factors, and a computed Heart Attack Risk. The project demonstrates loading this data into Spark, generating basic summary statistics, executing SQL-like queries, and performing transformations (e.g., categorizing patients by risk level).

## Setting Up Your Spark Environment

There are several ways to prepare a Spark environment:

1. **Install Apache Spark Locally**:  
   - Download the latest version of [Apache Spark](https://spark.apache.org/downloads.html).
   - Unzip and set your `SPARK_HOME` environment variable.
   - Add `SPARK_HOME/bin` to your PATH, so you can run `spark-submit` and `pyspark` from the terminal.

2. **Use a Pre-configured Environment**:  
   - Leverage platforms that provide managed Spark clusters, such as Databricks, AWS EMR, or Google Dataproc.
   - These platforms handle setup and scaling, letting you focus on writing PySpark code.

3. **Run Spark in Containers**:  
   - Use Docker images that have Spark pre-installed.
   - Run containers locally or in a CI/CD pipeline environment for quick testing.

4. **Use GitHub Codespaces or Other Cloud IDEs**:  
   - Some cloud-based IDEs offer Spark-ready environments or allow you to install Spark easily.
   - This setup is convenient for development without local installations.


## Data Loading

The dataset provides comprehensive patient health records. After extracting the CSV file, it is loaded into a Spark DataFrame for analysis.

**Sample Structure:**

| Patient ID | Age | Sex    | Cholesterol | Blood Pressure | Heart Rate | Diabetes | Smoking | ... | Country    | Continent       | Hemisphere           | Heart Attack Risk |
|------------|-----|--------|-------------|----------------|------------|----------|----------|-----|------------|-----------------|----------------------|------------------|
| BMW7812    | 67  | Male   | 208         | 158/88         | 72         | 0        | 1        | ... | Argentina  | South America   | Southern Hemisphere  | 0                |
| CZE1114    | 21  | Male   | 389         | 165/93         | 98         | 1        | 1        | ... | Canada     | North America   | Northern Hemisphere  | 0                |
| BNI9906    | 21  | Female | 324         | 174/99         | 72         | 1        | 0        | ... | France     | Europe          | Northern Hemisphere  | 0                |

(Additional columns available in the dataset not shown in this truncated table.)

### Operations
- **Extract**: Downloads or reads the medical dataset CSV into the `data` directory.
- **Load Data**: Loads the CSV into a Spark DataFrame, ready for analysis.
- **Display Sample**: Shows the first few rows to verify successful loading.

## Data Description

After loading, summary statistics are generated to provide a quick overview of numeric columns. This helps understand distributions of values like Age, Cholesterol, BMI, and others.

| Summary | Age  | Cholesterol | BMI   | ... |
|---------|------|-------------|-------|-----|
| Count   | 100  | 100         | 100   | ... |
| Mean    | 54.3 | 250.7       | 28.5  | ... |
| Stddev  | 22.4 | 65.5        | 5.3   | ... |
| Min     | 18   | 120         | 18.0  | ... |
| Max     | 90   | 398         | 39.9  | ... |

*(Note: Values are illustrative.)*

## Data Querying

You can run Spark SQL queries on the DataFrame. For example, to find the countries with the highest average Cholesterol levels:

```sql
SELECT Country, AVG(Cholesterol) AS avg_cholesterol
FROM HeartData
GROUP BY Country
ORDER BY avg_cholesterol DESC
LIMIT 3;

| Country | avg_cholesterol |
|---------|-----------------|
| Canada  | 320.5           |
| Brazil  | 310.2           |
| France  | 299.8           |


## Data Transformation

A transformation step can add new columns or categorize patients. For example, a **"RiskCategory"** column can be derived from the **"Heart Attack Risk"** column:

| Patient ID | Age | Cholesterol | Heart Attack Risk | RiskCategory |
|------------|-----|-------------|------------------|--------------|
| BMW7812    | 67  | 208         | 0                | Low Risk     |
| CZE1114    | 21  | 389         | 0                | Low Risk     |
| BNI9906    | 21  | 324         | 0                | Low Risk     |

## Outputs and Logs

All operation outputs and queries can be logged to **final_pyspark_output.md**, providing a record of the transformations, queries, and results performed during analysis.

## Testing

Basic tests (in **test_main.py**) verify:

- Data extraction and file creation
- Data loading integrity
- Transformations adding expected columns

These tests help ensure the reliability of data processing steps.
