""" Tries in python 
Methods -  insert_key(k, v)
           has_key(k)
           retrie_val(k)
           start_with_prefix(prefix)
"""
# HELPERS #


def _get_child_branches(tr):
    return tr[1:]


def _get_child_branch(tr, c):
    """
    Find matching branch with the character
    """
    for branch in _get_child_branches(tr):
        if branch[0] == c:
            return branch

    return None


def _retrive_branch(k, trie_list):
    if not k:
        return None
    tr = trie_list
    for c in k:
        child_branch = _get_child_branch(tr, c)
        if not child_branch:
            return None
        tr = child_branch

    return tr


def _is_trie_bucket(bucket):
    if len(bucket) != 2:
        return False

    return type(bucket[1]) is tuple


def _get_bucket_key(bucket):
    if not _is_trie_bucket(bucket):
        return None

    return bucket[1][0]

# HAS_KEY #


def has_key(k, tr):
    return _retrive_branch(k, tr) is not None

# RETRIE_VAL


def retrie_val(k, tr):
    key_tuple = _retrive_branch(k, tr)
    if not key_tuple:
        return None

    return key_tuple[1]


def insert_key(key, v, trie_list):
    if not key or has_key(key, trie_list):
        return

    tr = trie_list
    for char in key:
        branch = _get_child_branch(tr, char)
        if not branch:
            new_branch = [char]
            tr.append(new_branch)
            tr = new_branch
        else:
            tr = branch
    tr.append((key, v))


def start_with_prefix(prefix, trie):
    branch = _retrive_branch(prefix, trie)
    if not branch:
        return []
    prefix_list = []
    q = branch[1:]
    while q:
        curr_branch = q.pop(0)
        if _is_trie_bucket(curr_branch):
            prefix_list.append(_get_bucket_key(curr_branch))
        else:
            q.extend(curr_branch[1:])
    return prefix_list

if __name__ == "__main__":
    trie = [[]]
    states = """
            Alabama
            Alaska
            Arizona
            Arkansas
            California
            Colorado
            Connecticut
            Delaware
            Florida
            Georgia
            Hawaii
            Idaho
            Illinois
            Indiana
            Iowa
            Kansas
            Kentucky
            Louisiana
            Maine
            Maryland
            Massachusetts
            Michigan
            Minnesota
            Mississippi
            Missouri
            Montana
            Nebraska
            Nevada
            New Hampshire
            New Jersey
            New Mexico
            New York
            North Carolina
            North Dakota
            Ohio
            Oklahoma
            Oregon
            Pennsylvania
            Rhode Island
            South Carolina
            South Dakota
            Tennessee
            Texas
            Utah
            Vermont
            Virginia
            Washington
            West Virginia
            Wisconsin
            Wyoming"""
    states_list = [w.strip().lower() for w in states.splitlines() if w]
    for state in states_list:
        insert_key(state, True, trie)
    print start_with_prefix("new", trie)
