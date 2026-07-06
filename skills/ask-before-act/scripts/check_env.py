#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

with open('SKILL.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. SKILL.md line count
lines = content.count('\n') + 1
line_status = 'PASS' if lines <= 500 else 'FAIL'
print(f'SKILL.md lines: {lines} (limit 500): {line_status}')

# 2. frontmatter
fm_name = re.search(r'^name:\s*(.+)', content, re.M)
fm_desc = re.search(r'^description:\s*(.+)', content, re.M)
name_val = fm_name.group(1) if fm_name else 'FAIL'
desc_val = fm_desc.group(1)[:50] if fm_desc else 'FAIL'
print(f'Frontmatter name: {name_val}')
print(f'Frontmatter desc: {desc_val}...')

# 3. Gotchas
gotchas = re.findall(r'\*\*\d+\.', content)
gotchas_status = 'PASS' if len(gotchas) >= 5 else 'FAIL'
print(f'Gotchas: {len(gotchas)} (min 5): {gotchas_status}')

# 4. HARD-GATE
has_hard_gate = '<HARD-GATE>' in content and '</HARD-GATE>' in content
hg_status = 'PASS' if has_hard_gate else 'FAIL'
print(f'HARD-GATE: {hg_status}')

# 5. AskUserQuestion
aqr = len(re.findall(r'AskUserQuestion', content))
aqr_status = 'PASS' if aqr >= 1 else 'FAIL'
print(f'AskUserQuestion refs: {aqr} (min 1): {aqr_status}')

# 6. Spec mode
esm = 'EnterSpecMode' in content or 'ExitSpecMode' in content
print(f'Spec mode: {esm}')

# 7. Self-iteration hook
has_hook = '执行后复盘' in content
hook_status = 'PASS' if has_hook else 'FAIL'
print(f'Self-iteration hook: {hook_status}')

# 8. Secrets
secrets = re.findall(r'(password|secret|token|api_key)\s*[:=]', content, re.IGNORECASE)
sec_status = 'PASS' if len(secrets) == 0 else 'FAIL'
print(f'Secrets: {len(secrets)} (should be 0): {sec_status}')

# 9. Evals
with open('evals/evals.json', 'r', encoding='utf-8') as f:
    evals = json.load(f)
eval_status = 'PASS' if len(evals) >= 3 else 'FAIL'
print(f'Eval cases: {len(evals)} (min 3): {eval_status}')

# 10. Eval queries
with open('evals/eval_queries.json', 'r', encoding='utf-8') as f:
    queries = json.load(f)
trigger_true = sum(1 for q in queries if q['should_trigger'])
trigger_false = sum(1 for q in queries if not q['should_trigger'])
near_miss = sum(1 for q in queries if 'near-miss' in q.get('reason', '').lower())

q_total_status = 'PASS' if len(queries) >= 16 else 'FAIL'
q_true_status = 'PASS' if trigger_true >= 8 else 'FAIL'
q_false_status = 'PASS' if trigger_false >= 8 else 'FAIL'
q_near_status = 'PASS' if near_miss >= 4 else 'FAIL'

print(f'Queries: {len(queries)} total (min 16): {q_total_status}')
print(f'  Should-trigger: {trigger_true} (min 8): {q_true_status}')
print(f'  Should-not-trigger: {trigger_false} (min 8): {q_false_status}')
print(f'  Near-miss: {near_miss} (min 4): {q_near_status}')

# Summary
all_pass = all([
    lines <= 500, fm_name and fm_desc, len(gotchas) >= 5, has_hard_gate,
    aqr >= 1, has_hook, len(secrets) == 0, len(evals) >= 3,
    len(queries) >= 16, trigger_true >= 8, trigger_false >= 8, near_miss >= 4
])
print()
overall_text = 'ALL PASS' if all_pass else 'SOME FAILED'
print(f'Overall: {overall_text}')
