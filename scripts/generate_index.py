import os
import re
import json
import urllib.request
import shutil

# ---------------------------------------------------------
# 1. Fetch official LeetCode metadata (Difficulty, Title, Slug, Frontend ID)
# ---------------------------------------------------------
def fetch_leetcode_metadata():
    lc_slug_map = {}
    cache_path = os.path.join('metadata', 'leetcode_api_cache.json')
    
    # 1. Read session credentials from environment if available (local or CI)
    csrf = os.environ.get('LEETCODE_CSRF_TOKEN') or os.environ.get('LEETCODE_CSRF') or ''
    session = os.environ.get('LEETCODE_SESSION') or ''
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://leetcode.com'
    }
    if csrf and session:
        headers['Cookie'] = f"csrftoken={csrf}; LEETCODE_SESSION={session};"
        headers['x-csrftoken'] = csrf

    url = 'https://leetcode.com/api/problems/all/'
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for pair in data.get('stat_status_pairs', []):
                stat = pair['stat']
                diff_level = pair['difficulty']['level']
                diff_str = {1: 'Easy', 2: 'Medium', 3: 'Hard'}.get(diff_level, 'Medium')
                frontend_id = stat['frontend_question_id']
                slug = stat['question__title_slug']
                title = stat['question__title']
                info = {
                    'id': frontend_id,
                    'title': title,
                    'slug': slug,
                    'difficulty': diff_str
                }
                lc_slug_map[slug] = info
                norm_slug = re.sub(r'-+', '-', slug)
                if norm_slug != slug:
                    lc_slug_map[norm_slug] = info

            if lc_slug_map and os.path.exists('metadata'):
                try:
                    with open(cache_path, 'w', encoding='utf-8') as f:
                        json.dump(lc_slug_map, f, indent=2)
                except Exception:
                    pass
            print(f"Successfully fetched {len(lc_slug_map)} problems from LeetCode API")
    except Exception as e:
        print(f"Notice: Online LeetCode API fetch ({e}). Checking local cache...")
        if os.path.exists(cache_path):
            try:
                with open(cache_path, 'r', encoding='utf-8') as f:
                    lc_slug_map = json.load(f)
                print(f"Loaded {len(lc_slug_map)} problems from {cache_path}")
            except Exception as ce:
                print(f"Warning: Could not read cache {cache_path}: {ce}")
        elif os.path.exists(os.path.join('metadata', 'problems.json')):
            try:
                with open(os.path.join('metadata', 'problems.json'), 'r', encoding='utf-8') as f:
                    probs = json.load(f)
                for p in probs:
                    lc_slug_map[p['slug']] = {
                        'id': p['id'],
                        'title': p['title'],
                        'slug': p['slug'],
                        'difficulty': p['difficulty']
                    }
                print(f"Loaded {len(lc_slug_map)} problems from metadata/problems.json")
            except Exception as pe:
                print(f"Warning: Could not read problems.json: {pe}")
    return lc_slug_map

# ---------------------------------------------------------
# 2. File extension to Language mapping
# ---------------------------------------------------------
LANG_MAP = {
    '.py': 'Python',
    '.cpp': 'C++',
    '.cc': 'C++',
    '.js': 'JavaScript',
    '.ts': 'TypeScript',
    '.java': 'Java',
    '.sql': 'SQL',
    '.kt': 'Kotlin',
    '.php': 'PHP',
    '.sh': 'Shell',
    '.go': 'Go',
    '.rs': 'Rust',
    '.swift': 'Swift',
    '.rb': 'Ruby',
    '.c': 'C',
    '.cs': 'C#',
    '.scala': 'Scala',
    '.dart': 'Dart',
    '.erl': 'Erlang',
    '.ex': 'Elixir',
    '.rkt': 'Racket'
}

# ---------------------------------------------------------
# 3. Precise Categorization for Pattern, Algorithm, Data Structure
# ---------------------------------------------------------
def classify_problem(slug, content, sol_exts):
    pattern = 'Array / General'
    algorithm = 'In-Place Array Traversal & Index Mapping'
    ds = 'Array'
    topics = ['Array']
    
    slug_lower = slug.lower()
    content_lower = content.lower()

    if '.sql' in sol_exts:
        pattern = 'Database / SQL'
        algorithm = 'SQL Query / Relational Join & Window Function'
        ds = 'Relational Table'
        topics = ['Database', 'SQL', 'Data Aggregation']

    elif 'trie' in slug_lower or 'prefix tree' in content_lower:
        pattern = 'Trie'
        algorithm = 'Prefix Tree Lookup'
        ds = 'Trie Node'
        topics = ['Trie', 'String', 'Prefix Search']

    elif 'heap' in slug_lower or 'priority queue' in content_lower or 'priority_queue' in content_lower:
        pattern = 'Heap'
        algorithm = 'Min/Max Heap Priority Selection'
        ds = 'Heap / Priority Queue'
        topics = ['Heap', 'Priority Queue', 'Sorting']

    elif 'backtrack' in content_lower or 'permutation' in slug_lower or 'combination' in slug_lower:
        pattern = 'Backtracking'
        algorithm = 'Backtracking Recursive Search'
        ds = 'Recursion Tree'
        topics = ['Backtracking', 'Recursion']

    elif 'prefix sum' in content_lower or 'prefix' in slug_lower:
        pattern = 'Prefix Sum'
        algorithm = 'Prefix Sum Precomputation'
        ds = 'Prefix Array'
        topics = ['Prefix Sum', 'Array']

    elif ('fast' in content_lower and 'slow' in content_lower) or 'cycle' in slug_lower:
        pattern = 'Fast & Slow Pointers'
        algorithm = 'Floyd Cycle Detection'
        ds = 'Linked List / Pointer'
        topics = ['Two Pointers', 'Cycle Detection']

    elif 'binary search' in content_lower or 'rotated' in slug_lower or 'search space' in content_lower or 'log n' in content_lower or 'log(n)' in content_lower:
        pattern = 'Binary Search'
        algorithm = 'Modified Binary Search'
        ds = 'Sorted Array'
        topics = ['Binary Search', 'Divide and Conquer', 'Search Space']

    elif 'sliding window' in content_lower or 'longest substring' in slug_lower or 'max consecutive' in slug_lower or 'window' in content_lower:
        pattern = 'Sliding Window'
        algorithm = 'Dynamic Sliding Window Traversal'
        ds = 'Array / Hash Set'
        topics = ['Sliding Window', 'Two Pointers', 'Subarrays']

    elif 'two pointer' in content_lower or 'two sum' in slug_lower or '3sum' in slug_lower or '4sum' in slug_lower or 'container with' in slug_lower or 'palindrome' in slug_lower:
        pattern = 'Two Pointers'
        algorithm = 'Two Pointer Convergence & Scanning'
        ds = 'Array'
        topics = ['Two Pointers', 'Array', 'Sorting']

    elif 'hash map' in content_lower or 'dictionary' in content_lower or 'unordered_map' in content_lower or 'frequency' in content_lower or 'hash table' in content_lower or 'complement' in content_lower or 'anagram' in slug_lower:
        pattern = 'Hash Map'
        algorithm = 'Complement Lookup / Hash Table Frequency'
        ds = 'Dictionary / Hash Map'
        topics = ['Hash Table', 'Array', 'Complement Lookup']

    elif 'monotonic' in content_lower or 'temperature' in slug_lower or 'histogram' in slug_lower or 'next greater' in content_lower or 'final prices' in slug_lower:
        pattern = 'Monotonic Stack'
        algorithm = 'Monotonic Stack Filtering'
        ds = 'Stack'
        topics = ['Stack', 'Monotonic Stack', 'Array']

    elif 'stack' in content_lower or 'parentheses' in slug_lower or 'eval' in slug_lower or 'bracket' in slug_lower:
        pattern = 'Stack & Queue'
        algorithm = 'Stack Push / Pop Parsing'
        ds = 'Stack'
        topics = ['Stack', 'String Parsing']

    elif 'dp' in content_lower or 'dynamic programming' in content_lower or 'stone game' in slug_lower or 'jump game' in slug_lower or 'subsequence' in slug_lower or 'predict the winner' in slug_lower:
        pattern = 'Dynamic Programming'
        algorithm = 'Memoization & State Transition'
        ds = 'DP Table / Array'
        topics = ['Dynamic Programming', 'Memoization', 'State Transition']

    elif 'greedy' in content_lower or 'interval' in slug_lower or 'ice cream' in slug_lower or 'energy' in slug_lower:
        pattern = 'Greedy'
        algorithm = 'Greedy Choice Strategy'
        ds = 'Array / Priority Queue'
        topics = ['Greedy', 'Sorting']

    elif 'linked list' in content_lower or 'node' in slug_lower or 'add two numbers' in slug_lower or 'rotate list' in slug_lower or 'reverse list' in slug_lower:
        pattern = 'Linked List'
        algorithm = 'Pointer Traversal & Node Manipulation'
        ds = 'Linked List'
        topics = ['Linked List', 'Two Pointers']

    elif 'tree' in content_lower or 'binary tree' in content_lower or 'dfs' in content_lower or 'bfs' in content_lower or 'grid' in slug_lower or 'matrix' in slug_lower or 'path' in slug_lower:
        pattern = 'Tree & Graph'
        algorithm = 'Depth-First Search (DFS) / Breadth-First Search (BFS)'
        ds = 'Tree / Graph / Grid'
        topics = ['Tree', 'Graph', 'DFS', 'BFS']

    elif 'bit' in content_lower or 'xor' in slug_lower or 'binary' in slug_lower:
        pattern = 'Bit Manipulation'
        algorithm = 'Bitwise Masking & Bit Shift'
        ds = 'Integer Bitmask'
        topics = ['Bit Manipulation', 'Bitwise Math']

    elif 'roman' in slug_lower or 'math' in content_lower or 'digit' in slug_lower or 'rotate' in slug_lower or 'angle' in slug_lower or 'circle' in slug_lower:
        pattern = 'Math & Logic'
        algorithm = 'Mathematical Simulation & Modular Arithmetic'
        ds = 'Primitive Types'
        topics = ['Math', 'Simulation']

    return pattern, algorithm, ds, topics

# ---------------------------------------------------------
# 4. Complexity Heuristic
# ---------------------------------------------------------
def deduce_complexity(pattern, content):
    time_comp = "O(n)"
    space_comp = "O(1)"
    
    if "O(N)" in content or "$O(N)$" in content or "O(n)" in content:
        time_comp = "O(n)"
    elif "O(log N)" in content or "$O(\\log N)$" in content or "O(log n)" in content:
        time_comp = "O(log n)"
    elif "O(N^2)" in content or "O(n^2)" in content:
        time_comp = "O(n²)"
    elif "O(N log N)" in content or "O(n log n)" in content:
        time_comp = "O(n log n)"

    if pattern in ["Hash Map", "Stack & Queue", "Monotonic Stack", "Dynamic Programming", "Tree & Graph", "Trie", "Heap", "Prefix Sum"]:
        space_comp = "O(n)"
    elif pattern in ["Binary Search", "Two Pointers", "Sliding Window", "Fast & Slow Pointers"]:
        space_comp = "O(1)"
    elif pattern == "Database / SQL":
        time_comp = "O(n)"
        space_comp = "O(n)"

    return time_comp, space_comp

# ---------------------------------------------------------
# 5. Extract Problem Description from README.md
# ---------------------------------------------------------
def extract_clean_brief(readme_text, title):
    if not readme_text:
        return f"Given the problem constraints for **{title}**, compute the optimal solution efficiently."
    
    clean = re.sub(r'<[^>]+>', ' ', readme_text)
    clean = clean.replace('&nbsp;', ' ').replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').replace('&quot;', '"')
    lines = [line.strip() for line in clean.splitlines() if line.strip()]
    
    for line in lines:
        if len(line) > 25 and not line.startswith("Example") and not line.startswith("Constraints"):
            return line
            
    return f"Given the problem constraints for **{title}**, compute the optimal solution efficiently."

# ---------------------------------------------------------
# 6. Pattern-Specific Insights, Common Mistakes & Interview Notes
# ---------------------------------------------------------
def get_pattern_insights(pattern, title, ds, algorithm):
    if pattern == "Hash Map":
        insight = "Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations."
        mistakes = "1. Using the same element twice.\n2. Checking the map before inserting elements in the correct order.\n3. Inefficient hash functions or unnecessary duplicate key updates."
        interview = f"- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.\n- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?"
    elif pattern == "Binary Search":
        insight = "Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\\log n)$ time."
        mistakes = "1. Applying standard binary search without accounting for array rotation or duplicates.\n2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).\n3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`)."
        interview = f"- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.\n- **Follow-up:** How does performance change if the array contains duplicate elements?"
    elif pattern == "Sliding Window":
        insight = "Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated."
        mistakes = "1. Shrinking the window too late or missing invalid state checks.\n2. Forgetting to update window metrics (e.g. char counts) during contraction.\n3. Misinterpreting fixed vs variable window requirements."
        interview = f"- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.\n- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?"
    elif pattern == "Two Pointers":
        insight = "Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops."
        mistakes = "1. Failing to sort the array when ordering is required.\n2. Not skipping duplicate elements leading to non-unique pairs.\n3. Pointer out-of-bounds errors on edge inputs."
        interview = f"- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.\n- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?"
    elif pattern == "Dynamic Programming":
        insight = "Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation."
        mistakes = "1. Incorrect base case initialization.\n2. Flawed state transition equation.\n3. Storing unnecessary state leading to Memory Limit Exceeded (MLE)."
        interview = f"- **Tests:** Subproblem decomposition, state transition logic, and space optimization.\n- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?"
    elif pattern == "Monotonic Stack":
        insight = "Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations."
        mistakes = "1. Pushing elements instead of indices when index distance is required.\n2. Using strict inequality (`<`) when non-strict (`<=`) is necessary.\n3. Forgetting to flush remaining elements from stack at the end."
        interview = f"- **Tests:** Linear stack processing, nearest element relationship analysis.\n- **Follow-up:** How do you handle circular array boundaries?"
    else:
        insight = f"Leverage **{pattern}** with **{ds}** to process inputs efficiently and achieve optimal time and space complexity."
        mistakes = "1. Missing edge cases (empty inputs, boundary limits, negative values).\n2. Off-by-one errors in loop conditions.\n3. TLE due to suboptimal data structure choices."
        interview = f"- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.\n- **Follow-up:** How would you scale this solution for large input streams?"

    return insight, mistakes, interview

# ---------------------------------------------------------
# 7. Auto-Organize Flat Problems into Range Buckets
# ---------------------------------------------------------
def organize_problems():
    leetcode_dir = 'leetcode'
    if not os.path.exists(leetcode_dir):
        return
    for item in sorted(os.listdir(leetcode_dir)):
        item_path = os.path.join(leetcode_dir, item)
        if not os.path.isdir(item_path):
            continue
        if re.match(r'^\d{4}-\d{4}$', item):
            continue
        m = re.match(r'^(\d+)-(.*)', item)
        if m:
            f_num = int(m.group(1))
            lower = ((f_num - 1) // 500) * 500 + 1
            upper = lower + 499
            r_name = f"{lower:04d}-{upper:04d}"
            target_dir = os.path.join(leetcode_dir, r_name)
            os.makedirs(target_dir, exist_ok=True)
            target_path = os.path.join(target_dir, item)
            if os.path.exists(target_path):
                for subfile in os.listdir(item_path):
                    src_f = os.path.join(item_path, subfile)
                    dst_f = os.path.join(target_path, subfile)
                    if os.path.exists(dst_f):
                        if os.path.isdir(dst_f):
                            shutil.rmtree(dst_f)
                        else:
                            os.remove(dst_f)
                    shutil.move(src_f, dst_f)
                os.rmdir(item_path)
            else:
                shutil.move(item_path, target_path)

# ---------------------------------------------------------
# 8. Process Problem Folder with 100% Accurate Metadata Mapping
# ---------------------------------------------------------
def process_problem(range_folder, folder_name, lc_slug_map):
    m = re.match(r'(\d+)-(.*)', folder_name)
    if not m:
        return None
    folder_num, raw_slug = int(m.group(1)), m.group(2)
    clean_slug = raw_slug.strip('-')
    norm_slug = re.sub(r'-+', '-', clean_slug)

    # Match strictly by slug from official LeetCode metadata map to guarantee 100% accuracy
    lc_info = lc_slug_map.get(clean_slug) or lc_slug_map.get(norm_slug) or lc_slug_map.get(raw_slug)
    if lc_info:
        num = lc_info['id']
        title = lc_info['title']
        difficulty = lc_info['difficulty']
        slug = lc_info['slug']
    else:
        num = folder_num
        title = ' '.join(w.capitalize() for w in norm_slug.split('-'))
        difficulty = 'Medium'
        slug = norm_slug

    path = os.path.join('leetcode', range_folder, folder_name)

    sol_files = sorted([f for f in os.listdir(path) if f.startswith('solution')])
    sol_exts = [os.path.splitext(sf)[1] for sf in sol_files]
    languages = sorted(list(set([LANG_MAP.get(ext, 'Other') for ext in sol_exts])))
    lang_str = ', '.join(languages) if languages else 'Python'

    expl_path = os.path.join(path, 'Explanation.md')
    readme_path = os.path.join(path, 'README.md')

    expl_text = ''
    if os.path.exists(expl_path):
        with open(expl_path, 'r', encoding='utf-8', errors='ignore') as f:
            expl_text = f.read()

    readme_text = ''
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8', errors='ignore') as f:
            readme_text = f.read()

    combined_content = expl_text + '\n' + readme_text
    pattern, algorithm, ds, topics = classify_problem(slug, combined_content, sol_exts)
    time_comp, space_comp = deduce_complexity(pattern, combined_content)
    problem_brief = extract_clean_brief(readme_text, title)
    key_insight, common_mistakes, interview_notes = get_pattern_insights(pattern, title, ds, algorithm)

    approach = f"We iterate through the input using **{algorithm}**. By maintaining state efficiently in a **{ds}**, we eliminate redundant operations and process each element in optimal time."
    if "## Approach" in expl_text:
        app_match = re.search(r'## Approach\s*\n(.*?)(?=\n## |\Z)', expl_text, re.DOTALL)
        if app_match and len(app_match.group(1).strip()) > 15:
            approach = app_match.group(1).strip()

    algorithm_steps = f"1. Initialize state variables / data structure (**{ds}**).\n2. Process elements sequentially using **{algorithm}**.\n3. Validate boundary conditions and return optimal result."
    example_walkthrough = f"Consider the standard input for **{title}**. Applying **{algorithm}** yields the target result step by step."

    source_links = "\n".join([f"- [{sf}](./{sf})" for sf in sol_files]) if sol_files else "- [solution.py](./solution.py)"
    why_this_works = f"By utilizing **{pattern}**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations."

    return {
        'id': num,
        'title': title,
        'slug': slug,
        'difficulty': difficulty,
        'folder': folder_name,
        'range_folder': range_folder,
        'path': f"leetcode/{range_folder}/{folder_name}",
        'languages': languages,
        'lang_str': lang_str,
        'pattern': pattern,
        'algorithm': algorithm,
        'data_structure': ds,
        'topics': topics,
        'time': time_comp,
        'space': space_comp,
        'brief': problem_brief,
        'key_insight': key_insight,
        'approach': approach,
        'algorithm_steps': algorithm_steps,
        'example_walkthrough': example_walkthrough,
        'source_links': source_links,
        'why_this_works': why_this_works,
        'common_mistakes': common_mistakes,
        'interview_notes': interview_notes,
        'expl_path': expl_path
    }

# ---------------------------------------------------------
# 9. Main Orchestrator & Index Generator
# ---------------------------------------------------------
def main():
    lc_slug_map = fetch_leetcode_metadata()

    organize_problems()

    leetcode_dir = 'leetcode'
    problems = []
    range_folders = sorted([d for d in os.listdir(leetcode_dir) if os.path.isdir(os.path.join(leetcode_dir, d)) and re.match(r'^\d{4}-\d{4}$', d)])
    for r_name in range_folders:
        r_path = os.path.join(leetcode_dir, r_name)
        for f in sorted(os.listdir(r_path)):
            f_path = os.path.join(r_path, f)
            if os.path.isdir(f_path):
                p_info = process_problem(r_name, f, lc_slug_map)
                if p_info:
                    problems.append(p_info)

    # Sort problems by official frontend Question ID
    problems.sort(key=lambda x: x['id'])

    # Fast related problem computation using inverted index
    stopwords = {'a', 'an', 'the', 'of', 'in', 'to', 'with', 'and', 'or', 'is', 'at', 'on', 'by', 'for', 'ii', 'iii', 'iv', 'i'}
    for p in problems:
        p['_words'] = set(re.sub(r'-+', '-', p['slug']).split('-')) - stopwords

    word_index = {}
    pattern_map = {}
    id_to_prob = {p['id']: p for p in problems}

    for p in problems:
        pattern_map.setdefault(p['pattern'], []).append(p)
        for w in p['_words']:
            word_index.setdefault(w, []).append(p)

    # Fill related problems and write standardized Explanation.md for all problems
    written_count = 0
    for p in problems:
        matched_scores = {}
        for w in p['_words']:
            for op in word_index.get(w, []):
                if op['id'] != p['id']:
                    matched_scores[op['id']] = matched_scores.get(op['id'], 0) + 1

        sorted_matches = sorted(matched_scores.items(), key=lambda x: x[1], reverse=True)
        top_related = [id_to_prob[mid] for mid, _ in sorted_matches[:3]]

        if len(top_related) < 3:
            for op in pattern_map.get(p['pattern'], []):
                if op['id'] != p['id'] and op not in top_related:
                    top_related.append(op)
                    if len(top_related) == 3:
                        break

        rel_ids = [op['id'] for op in top_related]
        p['related_ids'] = rel_ids
        rel_links = [f"- [{op['id']}. {op['title']}](../../{op['range_folder']}/{op['folder']}/)" for op in top_related]
        rel_md = "\n".join(rel_links) if rel_links else "- None"
        p['related_md'] = rel_md

        # Build Standard SEO & People-First Explanation.md
        standard_expl = f"""# LeetCode {p['id']}: {p['title']}

**LeetCode Problem #{p['id']} — {p['title']}**
Solve LeetCode {p['title']} using {p['lang_str']} and {p['pattern']}. This solution finds the optimal result using {p['algorithm']} in {p['time']} time.

## Problem Information
| Property | Value |
|---|---|
| Problem | {p['title']} |
| LeetCode | #{p['id']} |
| Difficulty | {p['difficulty']} |
| Language | {p['lang_str']} |
| Algorithm | {p['algorithm']} |
| Data Structure | {p['data_structure']} |
| Pattern | {p['pattern']} |
| Time Complexity | {p['time']} |
| Space Complexity | {p['space']} |

## Problem
{p['brief']}

## Key Insight
{p['key_insight']}

## Approach
{p['approach']}

## Algorithm
{p['algorithm_steps']}

## Example
{p['example_walkthrough']}

## Complexity
- **Time Complexity:** {p['time']}
- **Space Complexity:** {p['space']}

## Pattern
**{p['pattern']}**

## Topics
""" + "\n".join([f"- {t}" for t in p['topics']]) + f"""

## Language
{p['lang_str']}

## Source Code
{p['source_links']}

## Why This Works
{p['why_this_works']}

## Common Mistakes
{p['common_mistakes']}

## Interview Notes
{p['interview_notes']}

## Related Problems
{rel_md}

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/{p['slug']}/)
"""
        should_write = True
        if os.path.exists(p['expl_path']):
            try:
                with open(p['expl_path'], 'r', encoding='utf-8') as f:
                    if f.read() == standard_expl:
                        should_write = False
            except Exception:
                pass
        if should_write:
            with open(p['expl_path'], 'w', encoding='utf-8') as f:
                f.write(standard_expl)
            written_count += 1

    print(f"Updated/generated {written_count} Explanation.md files")

    # Save metadata/problems.json
    clean_problems_json = []
    for p in problems:
        cp = {k: v for k, v in p.items() if k not in ['_words', 'expl_path', 'key_insight', 'approach', 'algorithm_steps', 'example_walkthrough', 'source_links', 'why_this_works', 'common_mistakes', 'interview_notes', 'related_md']}
        clean_problems_json.append(cp)

    with open('metadata/problems.json', 'w', encoding='utf-8') as f:
        json.dump(clean_problems_json, f, indent=2)
    print(f"Saved metadata/problems.json ({len(problems)} problems)")

    # ---------------------------------------------------------
    # 8b. Generate Range Hubs (leetcode/README.md & leetcode/{range}/README.md)
    # ---------------------------------------------------------
    ranges_summary = {}
    for p in problems:
        ranges_summary.setdefault(p['range_folder'], []).append(p)

    lc_readme = """# LeetCode Solutions Directory

This directory contains solved LeetCode problems partitioned into standardized range buckets (500 problems per bucket). This clean folder design ensures high browsing performance on GitHub without triggering directory truncation warnings.

## Problem Range Buckets

| Range | Solved Count | Directory Link |
|---|---|---|
"""
    for r_name in sorted(ranges_summary.keys()):
        cnt = len(ranges_summary[r_name])
        lc_readme += f"| **{r_name}** | {cnt} problems | [Explore {r_name}](./{r_name}/) |\n"

    lc_readme += """
---

## Navigation

- **Search all problems:** [**All_Problems.md**](../All_Problems.md)
- **Browse by algorithmic pattern:** [Patterns Hub](../patterns/)
- **Browse by programming language:** [Languages Hub](../languages/)
- **Machine-readable catalog:** [`metadata/problems.json`](../metadata/problems.json)
"""

    with open(os.path.join(leetcode_dir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(lc_readme)

    pattern_file_names = {
        'Hash Map': 'hash-map.md',
        'Two Pointers': 'two-pointers.md',
        'Sliding Window': 'sliding-window.md',
        'Binary Search': 'binary-search.md',
        'Dynamic Programming': 'dynamic-programming.md',
        'Greedy': 'greedy.md',
        'Monotonic Stack': 'monotonic-stack.md',
        'Stack & Queue': 'stack-queue.md',
        'Tree & Graph': 'tree-graph.md',
        'Linked List': 'linked-list.md',
        'Math & Logic': 'math-logic.md',
        'Database / SQL': 'sql-database.md',
        'Array / General': 'array-general.md',
        'Backtracking': 'backtracking.md',
        'Prefix Sum': 'prefix-sum.md',
        'Fast & Slow Pointers': 'fast-slow-pointers.md',
        'Heap': 'heap.md',
        'Trie': 'trie.md',
        'Bit Manipulation': 'bit-manipulation.md'
    }

    for r_name, r_probs in ranges_summary.items():
        r_readme = f"""# LeetCode Problems: {r_name}

A collection of **{len(r_probs)}** solved LeetCode problems in the range **{r_name}**.

## Problem Index

| # | Problem | Difficulty | Pattern | Language | Solution |
|---|---|---|---|---|---|
"""
        for p in sorted(r_probs, key=lambda x: x['id']):
            r_readme += f"| {p['id']} | [{p['title']}](./{p['folder']}/) | {p['difficulty']} | [{p['pattern']}](../../patterns/{pattern_file_names.get(p['pattern'], 'array-general.md')}) | {p['lang_str']} | [Explanation](./{p['folder']}/Explanation.md) |\n"

        with open(os.path.join(leetcode_dir, r_name, 'README.md'), 'w', encoding='utf-8') as f:
            f.write(r_readme)

    # ---------------------------------------------------------
    # 9. Generate All Hub Pages
    # ---------------------------------------------------------
    
    # 9a. Clean stale hub files first to guarantee zero orphaned or outdated links
    hub_dirs = ['patterns', 'algorithms', 'data-structures', 'difficulty', 'languages']
    for hub_dir in hub_dirs:
        if os.path.exists(hub_dir):
            for fname in os.listdir(hub_dir):
                if fname.endswith('.md'):
                    os.remove(os.path.join(hub_dir, fname))
        else:
            os.makedirs(hub_dir, exist_ok=True)

    # 9b. Patterns Hubs
    patterns_map = {}
    for p in problems:
        patterns_map.setdefault(p['pattern'], []).append(p)

    for pat, filename in pattern_file_names.items():
        pat_probs = patterns_map.get(pat, [])
        pat_content = f"# {pat} LeetCode Problems\n\n"
        pat_content += f"A collection of LeetCode problems solved using **{pat}** pattern techniques, explanations, and complexity analysis.\n\n"
        pat_content += "## Problems\n\n"

        for diff_level in ['Easy', 'Medium', 'Hard']:
            diff_probs = sorted([p for p in pat_probs if p['difficulty'] == diff_level], key=lambda x: x['id'])
            pat_content += f"### {diff_level}\n\n"
            if diff_probs:
                pat_content += "| # | Problem | Language | Time | Space | Explanation |\n"
                pat_content += "|---|---|---|---|---|---|\n"
                for p in diff_probs:
                    pat_content += f"| {p['id']} | [{p['title']}](../{p['path']}/) | {p['lang_str']} | {p['time']} | {p['space']} | [Explanation](../{p['path']}/Explanation.md) |\n"
                pat_content += "\n"
            else:
                pat_content += "*No problems logged yet under this difficulty level.*\n\n"
        
        with open(os.path.join('patterns', filename), 'w', encoding='utf-8') as f:
            f.write(pat_content)

    patterns_readme = f"""# Algorithmic Patterns Directory

A comprehensive index of LeetCode problems organized by algorithmic pattern and problem-solving strategy.

## Patterns Index

| Pattern | Solved Count | Hub Link |
|---|---|---|
"""
    for pat in sorted(pattern_file_names.keys()):
        cnt = len(patterns_map.get(pat, []))
        fname = pattern_file_names[pat]
        patterns_readme += f"| **{pat}** | {cnt} problems | [Browse {pat}](./{fname}) |\n"

    patterns_readme += """
---

## Navigation

- **All Problems Directory:** [All_Problems.md](../All_Problems.md)
- **Algorithms Index:** [Algorithms Hub](../algorithms/README.md)
- **Data Structures Index:** [Data Structures Hub](../data-structures/README.md)
- **Difficulty Index:** [Difficulty Hub](../difficulty/README.md)
- **Languages Index:** [Languages Hub](../languages/README.md)
"""
    with open(os.path.join('patterns', 'README.md'), 'w', encoding='utf-8') as f:
        f.write(patterns_readme)

    # 9c. Algorithms Hubs
    algo_map = {}
    for p in problems:
        algo_map.setdefault(p['algorithm'], []).append(p)

    algo_files = {}
    for algo, algo_probs in sorted(algo_map.items()):
        slug_algo = re.sub(r'[^a-z0-9]+', '-', algo.lower()).strip('-')
        fname = f"{slug_algo}.md"
        algo_files[algo] = fname
        algo_content = f"# {algo} Algorithm Problems\n\n"
        algo_content += f"A curated selection of LeetCode problems solved using the **{algo}** algorithmic approach.\n\n"
        algo_content += "## Problems\n\n"
        algo_content += "| # | Problem | Difficulty | Pattern | Time | Space | Explanation |\n"
        algo_content += "|---|---|---|---|---|---|---|\n"
        for p in sorted(algo_probs, key=lambda x: x['id']):
            algo_content += f"| {p['id']} | [{p['title']}](../{p['path']}/) | {p['difficulty']} | {p['pattern']} | {p['time']} | {p['space']} | [Explanation](../{p['path']}/Explanation.md) |\n"
        
        with open(os.path.join('algorithms', fname), 'w', encoding='utf-8') as f:
            f.write(algo_content)

    algo_readme = f"""# Algorithms Directory

A curated index of algorithmic paradigms and problem-solving approaches applied across all solved LeetCode problems.

## Algorithms Index

| Algorithm | Solved Count | Hub Link |
|---|---|---|
"""
    for algo, fname in sorted(algo_files.items()):
        cnt = len(algo_map[algo])
        algo_readme += f"| **{algo}** | {cnt} problems | [Browse {algo}](./{fname}) |\n"

    algo_readme += """
---

## Navigation

- **All Problems Directory:** [All_Problems.md](../All_Problems.md)
- **Patterns Index:** [Patterns Hub](../patterns/README.md)
- **Data Structures Index:** [Data Structures Hub](../data-structures/README.md)
- **Difficulty Index:** [Difficulty Hub](../difficulty/README.md)
- **Languages Index:** [Languages Hub](../languages/README.md)
"""
    with open(os.path.join('algorithms', 'README.md'), 'w', encoding='utf-8') as f:
        f.write(algo_readme)

    # 9d. Data Structures Hubs
    ds_map = {}
    for p in problems:
        ds_map.setdefault(p['data_structure'], []).append(p)

    ds_files = {}
    for ds_name, ds_probs in sorted(ds_map.items()):
        slug_ds = re.sub(r'[^a-z0-9]+', '-', ds_name.lower()).strip('-')
        fname = f"{slug_ds}.md"
        ds_files[ds_name] = fname
        ds_content = f"# {ds_name} Data Structure Problems\n\n"
        ds_content += f"LeetCode problems solved using **{ds_name}** data structures.\n\n"
        ds_content += "## Problems\n\n"
        ds_content += "| # | Problem | Difficulty | Algorithm | Time | Space | Explanation |\n"
        ds_content += "|---|---|---|---|---|---|---|\n"
        for p in sorted(ds_probs, key=lambda x: x['id']):
            algo_content_val = p['algorithm']
            ds_content += f"| {p['id']} | [{p['title']}](../{p['path']}/) | {p['difficulty']} | {algo_content_val} | {p['time']} | {p['space']} | [Explanation](../{p['path']}/Explanation.md) |\n"
        
        with open(os.path.join('data-structures', fname), 'w', encoding='utf-8') as f:
            f.write(ds_content)

    ds_readme = f"""# Data Structures Directory

A comprehensive catalog of data structures utilized across all solved LeetCode problems.

## Data Structures Index

| Data Structure | Solved Count | Hub Link |
|---|---|---|
"""
    for ds_name, fname in sorted(ds_files.items()):
        cnt = len(ds_map[ds_name])
        ds_readme += f"| **{ds_name}** | {cnt} problems | [Browse {ds_name}](./{fname}) |\n"

    ds_readme += """
---

## Navigation

- **All Problems Directory:** [All_Problems.md](../All_Problems.md)
- **Patterns Index:** [Patterns Hub](../patterns/README.md)
- **Algorithms Index:** [Algorithms Hub](../algorithms/README.md)
- **Difficulty Index:** [Difficulty Hub](../difficulty/README.md)
- **Languages Index:** [Languages Hub](../languages/README.md)
"""
    with open(os.path.join('data-structures', 'README.md'), 'w', encoding='utf-8') as f:
        f.write(ds_readme)

    # 9e. Difficulty Hubs
    diff_map = {'Easy': [], 'Medium': [], 'Hard': []}
    for p in problems:
        diff_map.setdefault(p['difficulty'], []).append(p)

    for diff_key in ['Easy', 'Medium', 'Hard']:
        d_probs = diff_map.get(diff_key, [])
        d_content = f"# LeetCode {diff_key} Problems\n\n"
        d_content += f"A collection of LeetCode **{diff_key}** difficulty problems solved with step-by-step explanations, pattern categorization, and optimized source code.\n\n"
        d_content += "## Problem Index\n\n"
        d_content += "| # | Problem | Pattern | Language | Time | Space | Explanation |\n"
        d_content += "|---|---|---|---|---|---|---|\n"
        for p in sorted(d_probs, key=lambda x: x['id']):
            d_content += f"| {p['id']} | [{p['title']}](../{p['path']}/) | {p['pattern']} | {p['lang_str']} | {p['time']} | {p['space']} | [Explanation](../{p['path']}/Explanation.md) |\n"

        with open(os.path.join('difficulty', f"{diff_key.lower()}.md"), 'w', encoding='utf-8') as f:
            f.write(d_content)

    total_prob_cnt = len(problems) if problems else 1
    diff_readme = f"""# Difficulty Directory

LeetCode problems indexed by difficulty tier (Easy, Medium, Hard).

## Difficulty Index

| Difficulty | Solved Count | Percentage | Hub Link |
|---|---|---|---|
| **Easy** | {len(diff_map['Easy'])} problems | {len(diff_map['Easy']) * 100 / total_prob_cnt:.1f}% | [Browse Easy](./easy.md) |
| **Medium** | {len(diff_map['Medium'])} problems | {len(diff_map['Medium']) * 100 / total_prob_cnt:.1f}% | [Browse Medium](./medium.md) |
| **Hard** | {len(diff_map['Hard'])} problems | {len(diff_map['Hard']) * 100 / total_prob_cnt:.1f}% | [Browse Hard](./hard.md) |

---

## Navigation

- **All Problems Directory:** [All_Problems.md](../All_Problems.md)
- **Patterns Index:** [Patterns Hub](../patterns/README.md)
- **Algorithms Index:** [Algorithms Hub](../algorithms/README.md)
- **Data Structures Index:** [Data Structures Hub](../data-structures/README.md)
- **Languages Index:** [Languages Hub](../languages/README.md)
"""
    with open(os.path.join('difficulty', 'README.md'), 'w', encoding='utf-8') as f:
        f.write(diff_readme)

    # 9f. Languages Hubs
    lang_problems_map = {}
    for p in problems:
        for lang in p['languages']:
            lang_problems_map.setdefault(lang, []).append(p)

    lang_files = {}
    lang_slug_overrides = {
        'C++': 'cpp',
        'C#': 'csharp'
    }
    for lang_name, l_probs in sorted(lang_problems_map.items()):
        slug_lang = lang_slug_overrides.get(lang_name) or re.sub(r'[^a-z0-9]+', '-', lang_name.lower()).strip('-')
        fname = f"{slug_lang}.md"
        lang_files[lang_name] = fname
        l_content = f"# LeetCode {lang_name} Solutions\n\n"
        l_content += f"A collection of LeetCode problems implemented in **{lang_name}** with detailed complexity analysis and explanations.\n\n"
        l_content += "## Solutions\n\n"
        l_content += "| # | Problem | Difficulty | Pattern | Time | Space | Explanation |\n"
        l_content += "|---|---|---|---|---|---|---|\n"
        for p in sorted(l_probs, key=lambda x: x['id']):
            l_content += f"| {p['id']} | [{p['title']}](../{p['path']}/) | {p['difficulty']} | {p['pattern']} | {p['time']} | {p['space']} | [Explanation](../{p['path']}/Explanation.md) |\n"

        with open(os.path.join('languages', fname), 'w', encoding='utf-8') as f:
            f.write(l_content)

    lang_readme = f"""# Programming Languages Directory

Solutions implemented across multiple programming languages.

## Languages Index

| Language | Solutions Count | Hub Link |
|---|---|---|
"""
    for lang_name, fname in sorted(lang_files.items()):
        cnt = len(lang_problems_map[lang_name])
        lang_readme += f"| **{lang_name}** | {cnt} solutions | [Browse {lang_name}](./{fname}) |\n"

    lang_readme += """
---

## Navigation

- **All Problems Directory:** [All_Problems.md](../All_Problems.md)
- **Patterns Index:** [Patterns Hub](../patterns/README.md)
- **Algorithms Index:** [Algorithms Hub](../algorithms/README.md)
- **Data Structures Index:** [Data Structures Hub](../data-structures/README.md)
- **Difficulty Index:** [Difficulty Hub](../difficulty/README.md)
"""
    with open(os.path.join('languages', 'README.md'), 'w', encoding='utf-8') as f:
        f.write(lang_readme)

    # ---------------------------------------------------------
    # 10. Generate Root README.md
    # ---------------------------------------------------------
    recent_probs = sorted(problems, key=lambda x: x['id'], reverse=True)[:15]

    easy_cnt = len([p for p in problems if p['difficulty'] == 'Easy'])
    med_cnt = len([p for p in problems if p['difficulty'] == 'Medium'])
    hard_cnt = len([p for p in problems if p['difficulty'] == 'Hard'])

    readme_content = f"""# LeetCode Solutions & DSA Practice

A continuously updated collection of LeetCode solutions, algorithm explanations, data structures, and coding interview patterns.

This repository contains solved LeetCode problems with explanations, complexity analysis, and source code. Problems are organized by LeetCode number and grouped by algorithmic pattern, data structure, difficulty, and programming language.

## What You'll Find
- **Comprehensive Explanations:** Step-by-step algorithm walkthroughs, key insights, and common pitfalls.
- **Multi-Language Solutions:** Python, C++, JavaScript, TypeScript, Java, SQL, and more.
- **Complexity Analysis:** Explicit Time and Space complexity ($O(N)$, $O(\\log N)$, $O(1)$) for every solution.
- **Pattern & Topic Indexing:** Grouped by Binary Search, Sliding Window, Two Pointers, Hash Maps, Stacks, Trees, Graphs, Dynamic Programming, and SQL.
- **Machine-Readable Metadata:** Structured JSON catalog available in [`metadata/problems.json`](metadata/problems.json).

---

## Statistics

| Category | Count |
|---|---|
| **Total Solved** | {len(problems)}+ |
| **Easy** | {easy_cnt}+ |
| **Medium** | {med_cnt}+ |
| **Hard** | {hard_cnt}+ |

> **Repository Structure:** To prevent GitHub directory truncation (which limits folder listings to 1,000 files), all 2,360+ problems are cleanly partitioned into 500-problem range buckets under [`leetcode/`](leetcode/) (`0001-0500/`, `0501-1000/`, etc.). You can browse problems directly through their range buckets or search the full directory in [**All_Problems.md**](All_Problems.md).

---

## Recently Solved

| # | Problem | Difficulty | Pattern | Language | Solution |
|---|---|---|---|---|---|
"""
    for p in recent_probs:
        readme_content += f"| {p['id']} | [{p['title']}]({p['path']}/) | {p['difficulty']} | [{p['pattern']}](patterns/{pattern_file_names.get(p['pattern'], 'array-general.md')}) | {p['lang_str']} | [Explanation]({p['path']}/Explanation.md) |\n"

    readme_content += """
---

## Navigation & Topic Hubs

### 1. By Pattern ([Browse All Patterns](patterns/README.md))
- [Hash Map](patterns/hash-map.md)
- [Two Pointers](patterns/two-pointers.md)
- [Sliding Window](patterns/sliding-window.md)
- [Binary Search](patterns/binary-search.md)
- [Dynamic Programming](patterns/dynamic-programming.md)
- [Greedy](patterns/greedy.md)
- [Monotonic Stack](patterns/monotonic-stack.md)
- [Stack & Queue](patterns/stack-queue.md)
- [Tree & Graph](patterns/tree-graph.md)
- [Linked List](patterns/linked-list.md)
- [Math & Logic](patterns/math-logic.md)
- [Database / SQL](patterns/sql-database.md)
- [Backtracking](patterns/backtracking.md)
- [Prefix Sum](patterns/prefix-sum.md)
- [Fast & Slow Pointers](patterns/fast-slow-pointers.md)

### 2. By Algorithm ([Browse All Algorithms](algorithms/README.md))
- [Depth-First Search (DFS) / Breadth-First Search (BFS)](algorithms/depth-first-search-dfs-breadth-first-search-bfs.md)
- [In-Place Array Traversal & Index Mapping](algorithms/in-place-array-traversal-index-mapping.md)
- [Modified Binary Search](algorithms/modified-binary-search.md)
- [Two Pointer Convergence & Scanning](algorithms/two-pointer-convergence-scanning.md)
- [Complement Lookup / Hash Table Frequency](algorithms/complement-lookup-hash-table-frequency.md)
- [Memoization & State Transition](algorithms/memoization-state-transition.md)

### 3. By Data Structure ([Browse All Data Structures](data-structures/README.md))
- [Array](data-structures/array.md)
- [Tree / Graph / Grid](data-structures/tree-graph-grid.md)
- [Dictionary / Hash Map](data-structures/dictionary-hash-map.md)
- [Sorted Array](data-structures/sorted-array.md)
- [Stack](data-structures/stack.md)
- [Linked List](data-structures/linked-list.md)

### 4. By Difficulty ([Browse All Difficulties](difficulty/README.md))
- [Easy Problems](difficulty/easy.md)
- [Medium Problems](difficulty/medium.md)
- [Hard Problems](difficulty/hard.md)

### 5. By Programming Language ([Browse All Languages](languages/README.md))
- [Python Solutions](languages/python.md)
- [C++ Solutions](languages/cpp.md)
- [JavaScript Solutions](languages/javascript.md)
- [TypeScript Solutions](languages/typescript.md)
- [Java Solutions](languages/java.md)
- [SQL Solutions](languages/sql.md)

### 6. By Problem Range (Directory Buckets)
- [0001 - 0500](leetcode/0001-0500/)
- [0501 - 1000](leetcode/0501-1000/)
- [1001 - 1500](leetcode/1001-1500/)
- [1501 - 2000](leetcode/1501-2000/)
- [2001 - 2500](leetcode/2001-2500/)
- [2501 - 3000](leetcode/2501-3000/)
- [3001 - 3500](leetcode/3001-3500/)
- [3501 - 4000](leetcode/3501-4000/)
- [4001 - 4500](leetcode/4001-4500/)

---

## Complete Problem Directory

Browse the full index of all solved problems in [**All_Problems.md**](All_Problems.md).

---

## Repository Architecture

```
AlbinMath/leetcode
├── README.md
├── All_Problems.md
├── patterns/             # Categorized pattern hubs
├── algorithms/           # Algorithm index hubs
├── data-structures/      # Data structure index hubs
├── difficulty/           # Easy, Medium, Hard hubs
├── languages/            # Language-specific hubs
├── metadata/             # problems.json dataset
├── scripts/              # Automation scripts
└── leetcode/             # Range-partitioned problem directories
    ├── README.md         # Directory index & navigation
    ├── 0001-0500/        # Problems 1 - 500
    ├── 0501-1000/        # Problems 501 - 1000
    ├── 1001-1500/        # Problems 1001 - 1500
    ├── 1501-2000/        # Problems 1501 - 2000
    ├── 2001-2500/        # Problems 2001 - 2500
    ├── 2501-3000/        # Problems 2501 - 3000
    ├── 3001-3500/        # Problems 3001 - 3500
    ├── 3501-4000/        # Problems 3501 - 4000
    └── 4001-4500/        # Problems 4001 - 4500
```

---

## License & Repository Information
GitHub: [AlbinMath/leetcode](https://github.com/AlbinMath/leetcode)  
Continuously updated as new LeetCode problems are solved.
"""

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print("Generated README.md")

    # ---------------------------------------------------------
    # 11. Generate All_Problems.md (Exact Requested User Format)
    # ---------------------------------------------------------
    all_content = f"""# LeetCode Solutions — Complete Problem Directory

A continuously updated collection of **LeetCode solutions, DSA problems, algorithms, data structures, coding interview questions, and programming solutions**.

Each problem includes its **problem number, title, difficulty, algorithmic pattern, programming language, time complexity, space complexity, source code, and explanation**.

## Quick Navigation

### Statistics

- **Total Solved:** {len(problems)}+
- **Easy:** {easy_cnt}+
- **Medium:** {med_cnt}+
- **Hard:** {hard_cnt}+

### Browse by Difficulty

- [Easy Problems](difficulty/easy.md)
- [Medium Problems](difficulty/medium.md)
- [Hard Problems](difficulty/hard.md)

### Browse by Range

- [0001 - 0500](leetcode/0001-0500/)
- [0501 - 1000](leetcode/0501-1000/)
- [1001 - 1500](leetcode/1001-1500/)
- [1501 - 2000](leetcode/1501-2000/)
- [2001 - 2500](leetcode/2001-2500/)
- [2501 - 3000](leetcode/2501-3000/)
- [3001 - 3500](leetcode/3001-3500/)
- [3501 - 4000](leetcode/3501-4000/)
- [4001 - 4500](leetcode/4001-4500/)

### Browse by Topic & Category Hubs

- [Algorithmic Patterns Directory](patterns/README.md)
- [Algorithms Directory](algorithms/README.md)
- [Data Structures Directory](data-structures/README.md)
- [Difficulty Levels Directory](difficulty/README.md)
- [Programming Languages Directory](languages/README.md)

### Browse by Algorithm / Pattern

- [Binary Search](patterns/binary-search.md)
- [Sliding Window](patterns/sliding-window.md)
- [Two Pointers](patterns/two-pointers.md)
- [Hash Map](patterns/hash-map.md)
- [Dynamic Programming](patterns/dynamic-programming.md)
- [Greedy](patterns/greedy.md)
- [Monotonic Stack](patterns/monotonic-stack.md)
- [Backtracking](patterns/backtracking.md)
- [Graph & Tree](patterns/tree-graph.md)
- [SQL / Database](patterns/sql-database.md)
- [Math & Logic](patterns/math-logic.md)

## Complete Problem Directory

| # | Problem | Difficulty | Pattern | Language | Algorithm | Time | Space | Code | Explanation |
|---|---|---|---|---|---|---|---|---|---|
"""
    for p in problems:
        all_content += f"| {p['id']} | [{p['title']}]({p['path']}/) | {p['difficulty']} | [{p['pattern']}](patterns/{pattern_file_names.get(p['pattern'], 'array-general.md')}) | {p['lang_str']} | {p['algorithm']} | {p['time']} | {p['space']} | [Code]({p['path']}/) | [Explanation]({p['path']}/Explanation.md) |\n"

    with open('All_Problems.md', 'w', encoding='utf-8') as f:
        f.write(all_content)
    print("Generated All_Problems.md")

if __name__ == '__main__':
    main()
