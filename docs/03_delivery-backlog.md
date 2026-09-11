# Delivery Backlog

The backlog is organized using an Agile delivery hierarchy of **Epics → Stories → Tasks**.

Stories represent meaningful deliverables or outcomes, while Tasks represent the work required to complete each Story. Requirements are mapped at the Story level to maintain traceability between the business/functional requirements and planned delivery work.

## Epic 1: Data Assessment & Requirements

| ID       | Work Item                                            | Type  | Requirements |
| -------- | ---------------------------------------------------- | ----- | ------------ |
| DA-01    | Understand available data and analytics objective    | Story | FR-00        |
| DA-01-T1 | Explore available datasets using Jupyter notebooks   | Task  | —            |
| DA-01-T2 | Assess data quality and relevant attributes          | Task  | —            |
| DA-01-T3 | Confirm analytics objective and initial requirements | Task  | —            |
| DA-01-T4 | Document initial findings and assumptions            | Task  | —            |

## Epic 2: Data Pipeline

| ID       | Work Item                                           | Type  | Requirements |
| -------- | --------------------------------------------------- | ----- | ------------ |
| DP-01    | Establish a reusable data processing workflow       | Story | FR-01, FR-02 |
| DP-01-T1 | Define data processing workflow                     | Task  | —            |
| DP-01-T2 | Preprocess company data                             | Task  | —            |
| DP-01-T3 | Preprocess shuttle data                             | Task  | —            |
| DP-01-T4 | Create model input dataset                          | Task  | —            |
| DP-01-T5 | Structure the workflow as a reusable Kedro pipeline | Task  | —            |

## Epic 3: Predictive Modeling

| ID       | Work Item                                             | Type  | Requirements |
| -------- | ----------------------------------------------------- | ----- | ------------ |
| ML-01    | Develop and evaluate a baseline prediction model      | Story | FR-03, FR-04 |
| ML-01-T1 | Define baseline modeling approach                     | Task  | —            |
| ML-01-T2 | Split data into training and test datasets            | Task  | —            |
| ML-01-T3 | Train baseline model                                  | Task  | —            |
| ML-01-T4 | Evaluate baseline model                               | Task  | —            |
| ML-02    | Evaluate alternative modeling approaches              | Story | FR-04        |
| ML-02-T1 | Implement candidate models                            | Task  | —            |
| ML-02-T2 | Evaluate candidate models using a consistent approach | Task  | —            |
| ML-02-T3 | Compare model performance                             | Task  | —            |
| ML-02-T4 | Document model evaluation findings and limitations    | Task  | —            |

## Epic 4: Quality & Validation

| ID       | Work Item                                       | Type  | Requirements         |
| -------- | ----------------------------------------------- | ----- | -------------------- |
| QA-01    | Establish quality and validation checks         | Story | Quality Requirements |
| QA-01-T1 | Validate data processing outputs                | Task  | —                    |
| QA-01-T2 | Validate pipeline execution                     | Task  | —                    |
| QA-01-T3 | Validate model evaluation workflow              | Task  | —                    |
| QA-01-T4 | Document quality considerations and limitations | Task  | —                    |

## Epic 5: Technical Delivery & Governance

| ID       | Work Item                                                | Type  | Requirements             |
| -------- | -------------------------------------------------------- | ----- | ------------------------ |
| TD-01    | Document the technical solution and delivery approach    | Story | Quality Requirements     |
| TD-01-T1 | Document technical workflow and architecture             | Task  | —                        |
| TD-01-T2 | Document technical decisions and assumptions             | Task  | —                        |
| TD-02    | Establish delivery risk and dependency tracking          | Story | —                        |
| TD-02-T1 | Identify technical and delivery dependencies             | Task  | —                        |
| TD-02-T2 | Identify potential delivery risks                        | Task  | —                        |
| TD-02-T3 | Document mitigation considerations                       | Task  | —                        |
| TD-03    | Define release readiness considerations                  | Story | Initial Success Criteria |
| TD-03-T1 | Define release readiness criteria                        | Task  | —                        |
| TD-03-T2 | Identify outstanding technical considerations            | Task  | —                        |
| TD-04    | Define future enhancements and improvement opportunities | Story | Future Considerations    |
| TD-04-T1 | Document potential technical enhancements                | Task  | —                        |
| TD-04-T2 | Document next-iteration opportunities                    | Task  | —                        |
| TD-05    | Conduct a delivery retrospective                         | Story | —                        |
| TD-05-T1 | Review delivery workflow                                 | Task  | —                        |
| TD-05-T2 | Identify process improvement opportunities               | Task  | —                        |
| TD-05-T3 | Document lessons learned                                 | Task  | —                        |

## Requirements Traceability

The backlog provides the following high-level traceability:

**FR-00 → DA-01 → Data Assessment**

**FR-01, FR-02 → DP-01 → Reusable Data Pipeline**

**FR-03, FR-04 → ML-01 → Baseline Model**

**FR-04 → ML-02 → Candidate Model Evaluation**

**Quality Requirements → QA-01 → Quality & Validation**

**Initial Success Criteria → TD-03 → Release Readiness**

**Future Considerations → TD-04 → Next Iteration**
