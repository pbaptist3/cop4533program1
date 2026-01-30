# **Stable Matching**
Implementation of Gale-Shapely algorithm involving hospital-student prefreences
## **Description**
This project implements the Gale-Shapely algorithm for solving the hospital-student assignment problem. Given preference lists from both hospitals and students, the algorithm finds a stable matching where no hospital-student pair would prefer each other over their current assignments.
The project includes three main components:
- **Matching Engine** - Implements hospital-proposing deferred acceptance
- **Verifier** - Validates that a matching is both valid and stable
- **Scalability Analysis** - Measures and graphs algorithm performance
## **Getting Started**
### **Dependencies**
- Python 3.6 or higher
- matplotlib (for scalability graphing)
