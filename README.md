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
### **Installing**
1. Download all Python files to the same directory:
   - match.py
   - verifier.py
   - time_match
   - time_verify
## **Executing program**
- Run the matching algorithm:
  '''python match.py < input.in'''
- Save output to a file:
  '''python match.py < input.in > output.out'''
- Verify a matching:
  '''python verifier.py input.in output.out'''
- Run scalability analysis:
  '''python scalability.py'''
# **Help**
Ensure input files follow the correct format:
- First line: integer n
- Next n lines: hospital preference lists (permutations of 1..n)
- Next n lines: student preference lists (permutations of 1..n)
To test the full pipeline:
'''python match.py < example.in >
result.out && python verifier.py
example.in result.out'''
## **Authors**
Philip A. Baptist 
Ansh Gupta
