# Operations Log

## Operation: Load Data

The operation is **load data**

The truncated output is:

| Patient ID | Age | Sex    | Cholesterol | Blood Pressure | Heart Rate | Diabetes | Family History | Smoking | Obesity | Alcohol Consumption | Exercise Hours Per Week | Diet      | Previous Heart Problems | Medication Use | Stress Level | Sedentary Hours Per Day | Income  | BMI       | Triglycerides | Physical Activity Days Per Week | Sleep Hours Per Day | Country       | Continent       | Hemisphere           | Heart Attack Risk |
|------------|-----|--------|-------------|----------------|------------|----------|----------------|---------|---------|---------------------|--------------------------|-----------|------------------------|----------------|--------------|--------------------------|---------|-----------|--------------|--------------------------------|--------------------|---------------|-----------------|----------------------|------------------|
| BMW7812    | 67  | Male   | 208         | 158/88         | 72         | 0        | 0              | 1       | 0       | 0                   | 4.168188835442079       | Average   | 0                      | 0              | 9            | 6.6150014529140595      | 261404  | 31.251233 | 286          | 0                              | 6                  | Argentina     | South America   | Southern Hemisphere  | 0                |
| CZE1114    | 21  | Male   | 389         | 165/93         | 98         | 1        | 1              | 1       | 1       | 1                   | 1.8132416178634458      | Unhealthy | 1                      | 0              | 1            | 4.963458839757678       | 285768  | 27.194973 | 235          | 1                              | 7                  | Canada        | North America   | Northern Hemisphere  | 0                |
| BNI9906    | 21  | Female | 324         | 174/99         | 72         | 1        | 0              | 0       | 0       | 0                   | 2.0783529861178884      | Healthy   | 1                      | 1              | 9            | 9.463425838029828       | 235282  | 28.176571 | 587          | 4                              | 4                  | France        | Europe          | Northern Hemisphere  | 0                |

---

## Operation: Describe Data

The operation is **describe data**

The truncated output is:

| Summary | Age        | Cholesterol  | Heart Rate  | Diabetes | Smoking  | 
|---------|------------|-------------|------------|----------|----------|
| count   | 100        | 100          | 100        | 100      | 100      | 
| mean    | 54.3       | 250.7        | 78.2       | 0.7      | 0.8      | 
| std     | 22.4       | 65.5         | 20.1       | 0.4      | 0.4      | 
| min     | 18         | 120          | 40         | 0        | 0        | 
| max     | 90         | 398          | 110        | 1        | 1        | 



---

## Operation: Query Data

The operation is **query data**

The query is:
```
SELECT Country, AVG(Cholesterol) AS avg_cholesterol
FROM HeartData
GROUP BY Country
ORDER BY avg_cholesterol DESC
LIMIT 3
```

The truncated output is:

| Country | avg_cholesterol |
|---------|-----------------|
| Canada  | 320.5           |
| Brazil  | 310.2           |
| France  | 299.8           |



## Operation: Transform Data

The operation is **transform data**

The truncated output is:

| Patient ID | Age | Sex    | Cholesterol | Blood Pressure | Heart Rate | Diabetes | Family History | Smoking | Obesity | Alcohol Consumption | Exercise Hours Per Week | Diet      | Previous Heart Problems | Medication Use | Stress Level | Sedentary Hours Per Day | Income  | BMI       | Triglycerides | Physical Activity Days Per Week | Sleep Hours Per Day | Country       | Continent       | Hemisphere           | Heart Attack Risk |
|------------|-----|--------|-------------|----------------|------------|----------|----------------|---------|---------|---------------------|--------------------------|-----------|------------------------|----------------|--------------|--------------------------|---------|-----------|--------------|--------------------------------|--------------------|---------------|-----------------|----------------------|------------------|
| BMW7812    | 67  | Male   | 208         | 158/88         | 72         | 0        | 0              | 1       | 0       | 0                   | 4.168188835442079       | Average   | 0                      | 0              | 9            | 6.6150014529140595      | 261404  | 31.251233 | 286          | 0                              | 6                  | Argentina     | South America   | Southern Hemisphere  | 0                |
| CZE1114    | 21  | Male   | 389         | 165/93         | 98         | 1        | 1              | 1       | 1       | 1                   | 1.8132416178634458      | Unhealthy | 1                      | 0              | 1            | 4.963458839757678       | 285768  | 27.194973 | 235          | 1                              | 7                  | Canada        | North America   | Northern Hemisphere  | 0                |
| BNI9906    | 21  | Female | 324         | 174/99         | 72         | 1        | 0              | 0       | 0       | 0                   | 2.0783529861178884      | Healthy   | 1                      | 1              | 9            | 9.463425838029828       | 235282  | 28.176571 | 587          | 4                              | 4                  | France        | Europe          | Northern Hemisphere  | 0                |
