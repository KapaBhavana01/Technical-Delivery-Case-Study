# Delivery Retrospective

## 1. Purpose

This retrospective reviews the delivery approach used throughout the technical analytics case study and identifies lessons learned and opportunities for improvement.

## 2. What Worked Well

* Exploratory analysis provided an initial understanding of the data and use case.
* Transitioning the exploratory workflow into Kedro pipelines improved structure and repeatability.
* Separating data processing from model development created clear technical work boundaries.
* A baseline model provided a reference point for evaluating alternative approaches.
* Requirements, acceptance criteria, risks, and technical decisions were documented alongside the implementation.
* The delivery backlog provided traceability between requirements and planned technical work.

## 3. Lessons Learned

* Early data assessment helps identify data-quality considerations before pipeline development.
* Clear requirements and acceptance criteria improve alignment between business objectives and technical implementation.
* Separating technical work into distinct pipeline areas makes dependencies and validation activities easier to identify.
* Model performance should be evaluated using a consistent methodology before comparing candidate approaches.
* Technical decision-making benefits from documented evidence, assumptions, and known limitations.

## 4. Improvement Opportunities

Future iterations could improve the solution through:

* Additional feature engineering
* Hyperparameter tuning
* Cross-validation
* Expanded model evaluation metrics
* Error and residual analysis
* Additional data validation
* More comprehensive release-readiness assessment

## 5. Delivery Recommendations

For a future iteration, the delivery process should continue to maintain clear traceability between requirements, technical work, validation results, decisions, and release readiness.

As the solution moves closer to production, technical stakeholders should additionally assess data quality, security, infrastructure, scalability, model performance, and operational requirements.
