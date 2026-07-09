#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""skill-env-setup 格式预检脚本——检测 SKILL.md 和 eval 资产的完整性。"""
import sys, re, json, os

sys.stdout.reconfigure(encoding='utf-8')

script_dir = os.path.dirname(os.path.abspath(__file__))
skill_dir = os.path.dirname(script_dir)
os.chdir(skill_dir)

errors = []
checks = []

# 1. SKILL.md line count
with open('SKILL.md', 'r', encoding='utf-8') as f:
    content = f.read()
lines = content.count('\n') + 1
line_ok = lines <= 500
checks.append(f'SKILL.md lines: {lines} (limit 500): {"PASS" if line_ok else "FAIL"}')
if not line_ok:
    errors.append(f'SKILL.md exceeds 500 lines ({lines})')

# 2. frontmatter
fm_name = re.search(r'^name:\s*(.+)', content, re.M)
fm_desc = re.search(r'^description:\s*(.+)', content, re.M)
name_val = fm_name.group(1).strip() if fm_name else None
desc_val = fm_desc.group(1).strip() if fm_desc else None
checks.append(f'Frontmatter name: {name_val or "FAIL"}')
checks.append(f'Frontmatter desc: {(desc_val or "FAIL")[:60]}...')
if not name_val:
    errors.append('Missing frontmatter name')
if not desc_val:
    errors.append('Missing frontmatter description')

# 3. description length
if desc_val:
    desc_ok = len(desc_val) <= 1024
    checks.append(f'Description length: {len(desc_val)} (limit 1024): {"PASS" if desc_ok else "FAIL"}')
    if not desc_ok:
        errors.append(f'Description too long ({len(desc_val)})')

# 4. name matches directory
dir_name = os.path.basename(skill_dir)
name_match = name_val == dir_name if name_val else False
checks.append(f'Name matches dir: {name_val} == {dir_name}: {"PASS" if name_match else "FAIL"}')
if not name_match:
    errors.append(f'Name ({name_val}) does not match directory ({dir_name})')

# 5. Gotchas count
gotchas = re.findall(r'\*\*\d+\.', content)
gotchas_ok = len(gotchas) >= 5
checks.append(f'Gotchas: {len(gotchas)} (min 5): {"PASS" if gotchas_ok else "FAIL"}')
if not gotchas_ok:
    errors.append(f'Not enough Gotchas ({len(gotchas)}, need 5)')

# 6. HARD-GATE
has_hard_gate = '<HARD-GATE>' in content and '</HARD-GATE>' in content
checks.append(f'HARD-GATE: {"PASS" if has_hard_gate else "FAIL"}')
if not has_hard_gate:
    errors.append('Missing HARD-GATE')

# 7. AskUserQuestion
aqr_count = len(re.findall(r'AskUserQuestion', content))
aqr_ok = aqr_count >= 1
checks.append(f'AskUserQuestion refs: {aqr_count} (min 1): {"PASS" if aqr_ok else "FAIL"}')
if not aqr_ok:
    errors.append('No AskUserQuestion references')

# 8. Spec mode
has_spec = 'EnterSpecMode' in content and 'ExitSpecMode' in content
checks.append(f'Spec mode (Enter/Exit): {"PASS" if has_spec else "FAIL"}')
if not has_spec:
    errors.append('Missing EnterSpecMode/ExitSpecMode')

# 9. Self-iteration hook
has_hook = '执行后复盘' in content
checks.append(f'Self-iteration hook: {"PASS" if has_hook else "FAIL"}')
if not has_hook:
    errors.append('Missing self-iteration hook')

# 10. Secrets check
secrets = re.findall(r'(password|secret|token|api_key)\s*[:=]', content, re.IGNORECASE)
secrets_ok = len(secrets) == 0
checks.append(f'Secrets: {len(secrets)} (should be 0): {"PASS" if secrets_ok else "FAIL"}')
if not secrets_ok:
    errors.append(f'Found {len(secrets)} potential secrets')

# 11. Evals
with open('evals/evals.json', 'r', encoding='utf-8') as f:
    evals = json.load(f)
evals_ok = len(evals) >= 3
checks.append(f'Eval cases: {len(evals)} (min 3): {"PASS" if evals_ok else "FAIL"}')
if not evals_ok:
    errors.append(f'Not enough eval cases ({len(evals)}, need 3)')

# Check assertions in each eval
for ev in evals:
    assert_count = len(ev.get('assertions', []))
    if assert_count < 2:
        errors.append(f'Eval {ev.get("id", "?")} has only {assert_count} assertions (need 2)')

# 12. Eval queries
with open('evals/eval_queries.json', 'r', encoding='utf-8') as f:
    queries = json.load(f)
trigger_true = sum(1 for q in queries if q['should_trigger'])
trigger_false = sum(1 for q in queries if not q['should_trigger'])
near_miss = sum(1 for q in queries if 'near-miss' in q.get('reason', '').lower())

q_total_ok = len(queries) >= 16
q_true_ok = trigger_true >= 8
q_false_ok = trigger_false >= 8
q_near_ok = near_miss >= 4

checks.append(f'Queries: {len(queries)} total (min 16): {"PASS" if q_total_ok else "FAIL"}')
checks.append(f'  Should-trigger: {trigger_true} (min 8): {"PASS" if q_true_ok else "FAIL"}')
checks.append(f'  Should-not-trigger: {trigger_false} (min 8): {"PASS" if q_false_ok else "FAIL"}')
checks.append(f'  Near-miss: {near_miss} (min 4): {"PASS" if q_near_ok else "FAIL"}')

if not q_total_ok:
    errors.append(f'Not enough queries ({len(queries)}, need 16)')
if not q_true_ok:
    errors.append(f'Not enough should-trigger ({trigger_true}, need 8)')
if not q_false_ok:
    errors.append(f'Not enough should-not-trigger ({trigger_false}, need 8)')
if not q_near_ok:
    errors.append(f'Not enough near-miss ({near_miss}, need 4)')

# 13. references
has_refs = 'references/' in content and 'Read references/' in content
checks.append(f'References loading: {"PASS" if has_refs else "FAIL"}')
if not has_refs:
    errors.append('Missing references loading instructions')

# Summary
for c in checks:
    print(c)

print()
if errors:
    print(f'Overall: SOME FAILED ({len(errors)} errors)')
    for e in errors:
        print(f'  - {e}')
    sys.exit(1)
else:
    print(f'Overall: ALL PASS ({len(checks)} checks)')
    sys.exit(0)
