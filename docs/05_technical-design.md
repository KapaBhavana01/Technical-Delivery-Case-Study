# Technical Design

## 1. Solution Overview
This solution implements a structured analytics and machine learning workflow for shuttle price prediction.

The project initially uses exploratory analysis to understand the available data and assess the feasibility of the use case. Following requirements and initial analytical direction confirmation, the workflow is structured into reusable Kedro pipelines for data processing and machine learning.

The solution separates data preparation from model development and evaluation, enabling the workflow to be organized, repeatable, and easier to validate and maintain.

The overall solution flow is:

Exploratory Data Assessment
→ Data Processing
→ Model Input Dataset
→ Model Training
→ Model Evaluation
→ Candidate Model Comparison

## 2. Technical Architecture
The solution is organized into separate stages for data processing and data science/modeling. Kedro provides the pipeline structure used to organize and execute these stages.

### Architecture Flow


                                                ┌─────────────────────────┐
                                                │   Source Datasets       │
                                                │ Companies / Shuttles /  │
                                                │ Reviews                 │
                                                └────────────┬────────────┘
                                                             │
                                                             ▼
                                                ┌─────────────────────────┐
                                                │ Data Processing Pipeline│
                                                │                         │
                                                │ • Data preprocessing   │
                                                │ • Data transformation   │
                                                │ • Dataset integration   │
                                                └────────────┬────────────┘
                                                             │
                                                             ▼
                                                ┌─────────────────────────┐
                                                │ Model Input Dataset     │
                                                └────────────┬────────────┘
                                                             │
                                                             ▼
                                                ┌─────────────────────────┐
                                                │ Data Science Pipeline   │
                                                │                         │
                                                │ • Train/test split      │
                                                │ • Model training        │
                                                │ • Model evaluation      │
                                                └────────────┬────────────┘
                                                             │
                                                             ▼
                                                ┌─────────────────────────┐
                                                │ Model Evaluation Results│
                                                │                         │
                                                │ Baseline & Candidates  │
                                                └─────────────────────────┘ 

## 3. Data Flow
The data flow begins with exploratory analysis and progresses through data preparation, model input creation, and machine learning evaluation.

### Data Flow


                                          Companies Data ───────┐
                                                                │
                                          Shuttles Data ────────┼──→ Data Preprocessing
                                                                │
                                          Reviews Data ─────────┘
                                                                        │
                                                                        ▼
                                                              Model Input Dataset
                                                                        │
                                                                        ▼
                                                               Feature / Target Split
                                                                        │
                                                                        ▼
                                                               Train / Test Split
                                                                   │          │
                                                                   ▼          ▼
                                                              Training       Testing
                                                                   │          │
                                                                   └────┬─────┘
                                                                        ▼
                                                                 Model Evaluation
                                                                        │
                                                                        ▼
                                                            Candidate Model Comparison

## 4. Pipeline Structure
The Kedro implementation separates data preparation from data science activities through dedicated pipelines.

### Data Processing Pipeline

The data processing pipeline prepares the source datasets for machine learning.

The workflow includes:

1. **Preprocess company data**
   - Transforms relevant company attributes into usable formats.

2. **Preprocess shuttle data**
   - Transforms relevant shuttle attributes and prepares the price field.

3. **Create model input table**
   - Combines the processed shuttle, review, and company datasets.
   - Removes records with missing values required for the modeling workflow.

The output of this pipeline is the prepared dataset used by the data science pipeline.

### Data Science Pipeline

The data science pipeline uses the prepared model input dataset for model development and evaluation.

The workflow includes:

1. **Split data**
   - Separates the feature variables from the target variable.
   - Divides the data into training and test datasets.

2. **Train model**
   - Trains the selected modeling approach using the training dataset.

3. **Evaluate model**
   - Generates predictions using the test dataset.
   - Calculates the model evaluation metric.

### Pipeline Organization

The data science workflow is structured to support both the baseline modeling workflow and candidate modeling experimentation.

This structure allows different modeling approaches to be evaluated within a consistent pipeline framework without changing the upstream data preparation process.

### Delivery Perspective

From a delivery perspective, the pipeline structure creates separable areas of work for:

- Data preparation
- Feature and target preparation
- Model development
- Model evaluation
- Candidate model experimentation
- Validation and future enhancements

This separation also provides clearer boundaries for identifying dependencies, risks, technical changes, and validation activities during the delivery lifecycle.

## 5. Modeling Approach
The modeling workflow uses a baseline model followed by evaluation of alternative candidate approaches. The purpose of the initial modeling phase is to establish a performance baseline and provide a consistent basis for comparing alternative approaches.

### Baseline Model

Linear Regression is used as the initial baseline model.

The baseline establishes a reference point against which alternative modeling approaches can be evaluated.

### Candidate Models

Additional candidate models are evaluated using the same prepared dataset and evaluation methodology.

The initial evaluation includes:

- Linear Regression — baseline
- Random Forest — candidate
- Gradient Boosting — candidate

### Initial Evaluation

The initial model evaluation produced the following results:

| Model | R² | Role |
|---|---:|---|
| Linear Regression | ~0.390 | Baseline |
| Random Forest | ~0.423 | Candidate |
| Gradient Boosting | ~0.437 | Candidate / best observed |

Gradient Boosting achieved the highest observed R² among the initially evaluated approaches, followed by Random Forest and Linear Regression.

These results represent an initial model comparison rather than a production model selection.

### Technical Delivery Perspective

The modeling workflow supports structured technical decision-making by providing a common evaluation approach for comparing candidate models.

From a Technical PMO perspective, the focus is on facilitating evaluation, documenting findings and limitations, and ensuring that technical recommendations are supported by documented evidence.

Further technical investigation may include feature engineering, hyperparameter tuning, cross-validation, additional evaluation metrics, and error analysis before considering production readiness.
## 6. Technology Stack
The project uses a focused technical stack to support data exploration, reusable analytics pipelines, machine learning, and delivery documentation.

| Area | Technology | Purpose |
|---|---|---|
| Programming | Python | Data processing and machine learning implementation |
| Data Analysis | Pandas | Data manipulation and analysis |
| Data Science Workflow | Kedro | Structuring reusable data science pipelines |
| Machine Learning | Scikit-learn | Model development and evaluation |
| Exploratory Analysis | Jupyter Notebooks | Initial data assessment and analytical exploration |
| Version Control | Git / GitHub | Source control and project collaboration |
| Testing | Python testing framework | Validation of pipeline and implementation behavior |
| Documentation | Markdown | Requirements, delivery, technical, and governance documentation |

### Technology Selection Considerations

The technology stack was kept intentionally focused on the requirements of the use case.

Kedro provides the structure for converting exploratory data science work into reusable pipelines, while Python and Scikit-learn support the modeling workflow.

GitHub provides version control and serves as the central location for both the technical implementation and delivery documentation.
## 7. Technical Considerations
The following considerations were identified during the development and evaluation of the solution.

### Reusability

The initial exploratory analysis was performed in Jupyter notebooks to understand the data and assess the use case. The workflow was subsequently structured into reusable Kedro pipelines to improve organization, repeatability, and maintainability.

### Data Quality

The quality of the model depends on the quality and completeness of the input data. Missing values and required data transformations need to be addressed before the data can be used for modeling.

### Model Performance

Initial model evaluation provides a basis for comparison but does not establish production readiness. The observed performance should be further investigated through additional experimentation and validation.

### Pipeline Maintainability

Separating data processing from model development helps isolate changes and makes future enhancements easier to manage.

### Validation

Pipeline outputs and model evaluation results should be validated consistently when changes are introduced to the workflow.

### Scalability

The current implementation is intended as a portfolio case study and is not designed as an enterprise-scale production system. Additional engineering and infrastructure considerations would be required for production deployment.

### Data & Security

The case study uses non-confidential data. No proprietary business data, credentials, or client-specific implementation details are included in the repository.
## 8. Assumptions & Constraints
The following assumptions and constraints define the boundaries of the initial case study.

### Assumptions

- The available datasets contain sufficient information to demonstrate the proposed price prediction use case.
- The exploratory analysis provides an appropriate starting point for defining the initial analytics workflow.
- The prepared model input dataset is suitable for the initial modeling exercise.
- R² is used as the initial metric for comparing model performance.
- The initial model comparison is sufficient to demonstrate the evaluation workflow, but not to establish production readiness.

### Constraints

- The project uses a limited, non-production dataset.
- The implementation is intended as a portfolio case study rather than an enterprise production solution.
- The initial modeling workflow does not include comprehensive hyperparameter optimization or production-scale model validation.
- Production deployment, automated retraining, and enterprise MLOps infrastructure are outside the initial scope.
- The project does not use proprietary or confidential business data.

### Delivery Implications

These assumptions and constraints should be considered when interpreting the model results and evaluating potential future iterations.

Any transition toward production would require additional technical validation, data assessment, security considerations, infrastructure planning, and stakeholder review.
