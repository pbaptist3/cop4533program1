import sys

def read_input():
    """
    format:
    n lines of hospital preferences
    n lines of student preferences
    n lines of matching (h, s)

    """

    n = int(input())
    h_pref = []
    for _ in range(n):
        h_pref.append([int(x) for x in input().split()])
    s_pref = []
    for _ in range(n):
        s_pref.append([int(x) for x in input().split()])
    
    matching = {}
    for _ in range(n):
        parts = input().split()
        h, s = int(parts[0]), int(parts[1])
        matching[h] = s

    return n, h_pref, s_pref, matching

def read_from_files(input_file, matching_file):
    """Read problem instance from input file and matching from matching file."""
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    n = int(lines[0])

    h_pref = []
    for i in range(1, n+1):
        h_pref.append([int(x) for x in lines[i].split()])

    s_pref = []
    for i in range(n+1, 2*n+1):
        s_pref.append([int(x) for x in lines[i].split()])

    matching = {}
    with open(matching_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                parts = line.split()
                if (len(parts) >= 2):
                    h, s = int(parts[0]), int(parts[1])
                    matching[h] = s

    return n, h_pref, s_pref, matching

def check_validity(n, matching):
    """
    Check that matching is valid:
    Each hospital matched to exactly one student and vice versa.

    """
    
    if len(matching) != n:
        return False, f"INVALID: Expected {n} pairs, found {len(matching)}"
    
    # check all hospitals 1 .. n present
    for h in range(1, n+1):
        if h not in matching:
            return False, f"INVALID: Hospital {h} is unmatched"
    
    # check hospital indices are in valid range
    for h in matching:
        if h < 1 or h > n:
            return False, f"INVALID: Hospital {h} out of range"
        
    # check student indices are in valid range
    matched_students = list(matching.values())
    for s in matched_students:
        if s < 1 or s > n:
            return False, f"INVALID: Student {s} out of range"
        
    # check for duplicate students
    if len(matched_students) != len(set(matched_students)):
        seen = set()
        for s in matched_students:
            if s in seen:
                return False, f"INVALID: Student {s} matched multiple times"
            seen.add(s)

    # check all students 1 .. n are matched
    if set(matched_students) != set(range(1, n+1)):
        missing = set(range(1, n+1)) - set(matched_students)
        return False, f"INVALID: Students {missing} are unmatched"
    
    return True, "Valid"

def check_stability(n, h_pref, s_pref, matching):
    """
    Check that there are no blocking pairs

    A blocking pair (h, s) exists if:
    - h prefers s over h's current match, AND
    - s prefers h over s's current match
    """
    # reverse matching: student -> hospital
    reverse_matching = {s: h for h, s in matching.items()}

    hospital_rank = {}
    for h in range(n):
        hospital_rank[h+1] = {}
        for rank, s in enumerate(h_pref[h]):
            hospital_rank[h+1][s] = rank
    
    # student ranking: student_rank[s][h] = rank of hospital h for student s
    student_rank = {}
    for s in range(n):
        student_rank[s+1] = {}
        for rank, h in enumerate(s_pref[s]):
            student_rank[s+1][h] = rank

    # check for blocking pairs
    for h in range(1, n+1):
        current_student = matching[h]
        # check all students that h prefers over current student
        for s in h_pref[h-1]:
            # stop when we reach current match
            if s == current_student:
                break
            
            # h prefers s over current student
            # Check if s prefers h over s's current match
            s_current_hospital = reverse_matching[s]
            if student_rank[s][h] < student_rank[s][s_current_hospital]:
                return False, f"UNSTABLE: Blocking pair (Hospital {h}, Student {s})"
            
    return True, "Stable"

def verify(n, h_pref, s_pref, matching):
    """
    Main verification function returning appropriate message based on validity and stability.
    """
    is_valid, validity_msg = check_validity(n, matching)
    if not is_valid:
        return validity_msg
    
    is_stable, stability_msg = check_stability(n, h_pref, s_pref, matching)
    if not is_stable:
        return stability_msg
    
    return "VALID AND STABLE"

def main():
    if len(sys.argv) == 1:
        n, h_pref, s_pref, matching = read_input()
    elif len(sys.argv) == 3:
        input_file = sys.argv[1]
        matching_file = sys.argv[2]
        n, h_pref, s_pref, matching = read_from_files(input_file, matching_file)
    else:
        print("Usage:")
        print("  python verifier.py               # read from stdin")
        print("  python verifier.py <input_file> <matching_file>  # read from files")
        sys.exit(1)
    result = verify(n, h_pref, s_pref, matching)
    print(result)

if __name__ == "__main__":
    main()
        