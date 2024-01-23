# Data Backend Challenge

## Task Description

The goal is to estimate the combinatorial complexity of the Mercedes EQS,
focusing on calculating the number of possible vehicle configurations. This
involves analyzing the options provided in the table while considering the
constraints outlined in the fine print of the attached PDF.

## Getting Started

### Installation

```bash
python -m pip install -r requirements.txt
```

## Approach

1. **Data Extraction**:

   - Extract relevant data from the PDF file, and identify constraints mentioned
     in the fine print regarding how different equipment codes relate to the
     described options. Refer to [visualization.ipynb](./visualization.ipynb)
     for a visualization of the data extraction process. The current
     implementation only extracts data from `Serienausstattungen` section (page
     7-17).

2. **Combination Calculation**:

   - Develop algorithms to calculate the number of possible vehicle
     configurations, taking into account the identified constraints. Refer to
     [combinations.py](./combinations.py) for the calculation of the possible
     combinations.

   - We compute the combinations for each vehicle type ("EQS 350", "EQS 450+",
     "EQS 580 4MATIC", "Mercedes-AMG EQS 53 4MATIC+"), considering certain
     configurations may not be feasible for specific vehicle types.

   - In the sections like `Serienausstattungen` and `Einzelausstattungen`, the
     configurations are largely independent, allowing each configuration to be
     either enabled or disabled. Only combinations with constrained
     configurations are not allowed. However, for categories like `Polster`,
     `Lacke`, `Zierelemente`, `Innenhimmel`, and `Räder`, buyers are constrained
     to selecting only one option from each category. In addition, combinations
     involving `Polster` and `Lacke` must align with the valid combinations
     outlined in the table on page 44.
