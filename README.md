# Technical Delivery Case Study

### Technical PMO / Agile Delivery for a Data & Machine Learning Initiative

This portfolio project demonstrates how I approach the **planning, coordination, documentation, validation, and delivery of a technical analytics and machine learning initiative** from a Technical PMO / Technical Delivery perspective.

The technical implementation uses the **Kedro Spaceflights project as the foundation** and extends it with delivery-focused documentation and project-management artifacts.

### Use Case

The case study uses an **assumed business scenario**:

> Predict shuttle ticket prices using historical shuttle, company, and review data.

The ML implementation provides technical context and demonstrates my ability to understand and coordinate technical work across a data and ML delivery lifecycle.

---

## ⚠️ Case Study Context & Intended Use

**This is a portfolio case study based on an assumed analytics use case. It is not an actual client project and does not represent the PMO, Agile, engineering, data science, or governance standards of any specific company.**

The documentation structure used here — including requirements, backlog, acceptance criteria, technical design, risks and dependencies, release readiness, and retrospective — is an **illustrative example** of how technical delivery work could be organized.

In a real organization, documentation, terminology, approval processes, governance standards, tools, and delivery practices will vary based on the company's:

* PMO and governance standards
* Agile methodology or framework
* Engineering and data science practices
* Regulatory and compliance requirements
* Project complexity and organizational structure
* Existing tools and documentation standards

Therefore, these artifacts **are not intended to be a fixed template or universal PMO format**. They represent one possible approach for demonstrating Technical PMO / Technical Delivery capabilities.

---

## 🎯 What This Project Demonstrates

* Translating a business problem into technical delivery requirements
* Structuring Epics, Stories, and Tasks
* Defining acceptance criteria and requirements traceability
* Understanding technical architecture and data workflows
* Coordinating technical activities across a delivery lifecycle
* Identifying risks, dependencies, and delivery considerations
* Supporting technical evaluation and decision-making
* Assessing release readiness
* Conducting retrospectives and identifying improvements

The project demonstrates **technical understanding for delivery leadership**, rather than positioning me as the sole developer or technical decision-maker.

---

## 🔄 Delivery Lifecycle

```text
Business Problem -> Requirements -> Data Assessment -> Planning & Backlog -> Technical Design -> Development -> QA & Validation -> Model Evaluation -> Release Readiness -> Retrospective
```

---

## 🧩 Technical Architecture

  ```text
  Source Data
      ↓
  Data Processing
      ↓
  Model Input Dataset
      ↓
  Model Training
      ↓
  Model Evaluation
      ↓
  Candidate Comparison
  ```

### Technology Stack

| Area             | Technology   |
| ---------------- | ------------ |
| Programming      | Python       |
| Data Analysis    | Pandas       |
| Pipeline         | Kedro        |
| Machine Learning | Scikit-learn |
| Exploration      | Jupyter      |
| Version Control  | Git / GitHub |
| Documentation    | Markdown     |

---

## 📂 Repository Structure

```text
Technical-Delivery-Case-Study/
│
├── README.md
├── docs/
│   ├── project-overview.md
│   ├── requirements.md
│   ├── delivery-backlog.md
│   ├── acceptance-criteria.md
│   ├── technical-design.md
│   ├── risks-and-dependencies.md
│   ├── release-readiness.md
│   └── retrospective.md
│
└── spaceflights/
    ├── data/
    ├── notebooks/
    ├── src/
    └── tests/
```

---

## 📚 Project Documentation

| Document                                               | Purpose                                 |
| ------------------------------------------------------ | --------------------------------------- |
| [Project Overview](01_project-overview.md)             | Project purpose and delivery approach   |
| [Requirements](02_requirements.md)                     | Business and functional requirements    |
| [Delivery Backlog](03_delivery-backlog.md)             | Epics, Stories, Tasks, and traceability |
| [Acceptance Criteria](04_acceptance-criteria.md)       | Expected Story outcomes                 |
| [Technical Design](05_technical-design.md)             | Architecture, data flow, and modeling   |
| [Risks & Dependencies](06_risks-and-dependencies.md)   | Delivery risks and dependencies         |
| [Release Readiness](07_release-readiness.md)           | Readiness assessment                    |
| [Retrospective](08_delivery-retrospective.md)          | Lessons learned and improvements        |

---

## 👤 Role Perspective

This case study is presented from a **Technical PMO / Technical Delivery perspective**.

The focus is on:

**Understand → Plan → Coordinate → Track → Validate → Communicate → Improve**

Technical teams and stakeholders remain responsible for their respective technical and business decisions. My role in this case study is to demonstrate the ability to understand technical work, coordinate delivery, identify risks and dependencies, facilitate technical discussions, and support informed decision-making.

---

## 📖 Project Origin

The technical implementation is based on the **Kedro Spaceflights tutorial**.

The [original tutorial](https://docs.kedro.org/en/stable/tutorials/spaceflights_tutorial/) provides the foundation for the data science pipeline. This repository extends that foundation with additional delivery documentation and Technical PMO practices created for this portfolio case study.

---

## ⚠️ Limitations

This is a **portfolio-scale case study**, not an enterprise production implementation.

It uses non-production data and does not include proprietary or confidential business information. Production deployment, automated retraining, enterprise MLOps, comprehensive model validation, security implementation, and infrastructure planning are outside the initial scope.

A production implementation would require additional technical, security, infrastructure, operational, compliance, and stakeholder considerations.

---

## 🎯 Key Takeaway

This project demonstrates a **Technical PMO / Technical Delivery approach to a data and machine learning initiative** while showing enough technical depth to understand the work being coordinated.

**Requirements → Planning → Technical Understanding → Coordination → Quality → Evaluation → Release Readiness → Continuous Improvement**
