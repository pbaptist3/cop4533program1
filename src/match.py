def match(source=input, sink=print):
    # take inputs
    n = int(source())
    h_pref = []
    s_pref = []
    for _ in range(n):
       h_pref.append([int(i) for i in source().split(' ')])
    for _ in range(n):
       s_pref.append([int(i) for i in source().split(' ')])

    # make reverse lookup for student preferences
    rev_s = [[-1]*n for i in range(n)]
    for i, s_list in enumerate(s_pref):
        for j, h in enumerate(s_list):
            rev_s[h-1][i] = j

    # initialize objects for tracking matches
    unvisited = [0]*n
    unmatched = set(range(n))
    matches = {}
    # matching loop
    while len(unmatched) > 0:
        h = next(iter(unmatched))
        
        s = h_pref[h][unvisited[h]] - 1
        unvisited[h] += 1
        # unmatched so far
        if not (s in matches):
            unmatched.remove(h)
            matches[s] = h
        # s prefers h to current match h'
        elif rev_s[h][s] < rev_s[matches[s]][s]:
            h_prime = matches[s]
            matches[s] = h
            unmatched.remove(h)
            unmatched.add(h_prime)
        # rejected otherwise
    
    for (s, h) in matches.items():
        sink(f"{h+1} {s+1}")

if __name__=="__main__":
    match()
