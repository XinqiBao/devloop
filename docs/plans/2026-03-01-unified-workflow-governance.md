# Unified Workflow Governance Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Rebuild `devloop` into a clean-HEAD, single-source workflow system with platform-agnostic core/process docs and adapter-specific Claude/Codex deployment docs.

**Architecture:** Keep one canonical workflow source inside `devloop/docs` with three layers: `core`, `process`, `adapters`. Keep `plugins/xdev` as Claude delivery, add Codex deployment adapter, and remove obsolete legacy/archive content from HEAD while relying on Git history for traceability.

**Tech Stack:** Markdown, shell scripts, Claude plugin structure, Codex skill discovery (`~/.agents/skills`), Git.

---

### Task 1: Create New Documentation Skeleton

**Files:**
- Create: `docs/core/.gitkeep`
- Create: `docs/process/.gitkeep`
- Create: `docs/adapters/claude/.gitkeep`
- Create: `docs/adapters/codex/.gitkeep`
- Create: `docs/governance/.gitkeep`

**Step 1: Create directory skeleton**

Run: `mkdir -p docs/core docs/process docs/adapters/claude docs/adapters/codex docs/governance`
Expected: command succeeds with no error.

**Step 2: Add keep files so paths exist in git**

Run:
```bash
touch docs/core/.gitkeep docs/process/.gitkeep docs/adapters/claude/.gitkeep docs/adapters/codex/.gitkeep docs/governance/.gitkeep
```
Expected: files exist and are tracked.

**Step 3: Verify skeleton**

Run: `find docs -maxdepth 3 -type d | sort`
Expected: output includes all 5 new directories.

**Step 4: Commit**

```bash
git add docs/core/.gitkeep docs/process/.gitkeep docs/adapters/claude/.gitkeep docs/adapters/codex/.gitkeep docs/governance/.gitkeep
git commit -m "docs: add unified workflow documentation skeleton"
```

---

### Task 2: Migrate Governance Documents

**Files:**
- Create: `docs/governance/status.md`
- Create: `docs/governance/decisions.md`
- Create: `docs/governance/changelog.md`
- Modify: `docs/xdev-workflow/STATUS.md`
- Modify: `docs/xdev-workflow/decisions.md`
- Modify: `docs/xdev-workflow/history.md`

**Step 1: Write new governance files with current structure**

Copy and normalize:
- `docs/xdev-workflow/STATUS.md` -> `docs/governance/status.md`
- `docs/xdev-workflow/decisions.md` -> `docs/governance/decisions.md`
- `docs/xdev-workflow/history.md` -> `docs/governance/changelog.md`

Expected: new files contain current canonical governance content.

**Step 2: Add short migration pointers in old files**

Replace old files with 3-8 line notices that point to the new locations.
Expected: old files no longer duplicate canonical content.

**Step 3: Verify no duplicate governance source**

Run: `rg -n "Current Phase: v2 Core Complete|Design Decisions — xdev Workflow|Design History — xdev Workflow" docs`
Expected: canonical content appears in `docs/governance/*`; old files are pointer stubs only.

**Step 4: Commit**

```bash
git add docs/governance/status.md docs/governance/decisions.md docs/governance/changelog.md docs/xdev-workflow/STATUS.md docs/xdev-workflow/decisions.md docs/xdev-workflow/history.md
git commit -m "docs(governance): migrate status decisions and changelog"
```

---

### Task 3: Build Platform-Agnostic Core and Process Documents

**Files:**
- Create: `docs/core/principles.md`
- Create: `docs/core/problem-statement.md`
- Create: `docs/process/lifecycle.md`
- Create: `docs/process/quality-gates.md`

**Step 1: Write core principles**

Create `docs/core/principles.md` with enforceable rules:
- quality-first
- evidence-before-claim
- context-budget
- parallel-when-safe
- self-improvement-loop

Expected: no Claude/Codex-specific terms in rule definitions.

**Step 2: Write problem statement**

Create `docs/core/problem-statement.md` from current requirements with platform-neutral language.
Expected: documents intent and constraints without implementation details.

**Step 3: Write lifecycle process**

Create `docs/process/lifecycle.md` with phases:
- clarify -> design -> plan -> execute -> verify -> improve
Each phase must define inputs, outputs, acceptance criteria.

**Step 4: Write quality gates**

Create `docs/process/quality-gates.md` describing hard completion gates and verification evidence format.

**Step 5: Verify platform neutrality**

Run: `rg -n "Claude|Codex" docs/core docs/process`
Expected: no matches in `docs/core/*`; process docs only mention platform-specific terms in adapter references, not rule definitions.

**Step 6: Commit**

```bash
git add docs/core/principles.md docs/core/problem-statement.md docs/process/lifecycle.md docs/process/quality-gates.md
git commit -m "docs: add platform-agnostic core and process specs"
```

---

### Task 4: Build Adapter Documents (Claude + Codex)

**Files:**
- Create: `docs/adapters/claude/overview.md`
- Create: `docs/adapters/claude/plugin-stack.md`
- Create: `docs/adapters/codex/overview.md`
- Create: `docs/adapters/codex/setup.md`
- Modify: `docs/xdev-workflow/plugin-inventory.md`

**Step 1: Create Claude adapter overview**

Document:
- marketplace install flow
- plugin responsibilities (`plugins/xdev`)
- what remains in dotfiles vs plugin layer

**Step 2: Move plugin inventory into adapter**

Port key content from `docs/xdev-workflow/plugin-inventory.md` to `docs/adapters/claude/plugin-stack.md`.
Expected: adapter doc is canonical; old file becomes pointer stub.

**Step 3: Create Codex adapter overview**

Document mapping rules:
- where Codex consumes shared rules
- how Codex-specific instructions map to core/process

**Step 4: Create Codex setup doc**

Include exact install/update commands for `~/.agents/skills` and required local config references.

**Step 5: Verify adapter boundaries**

Run: `rg -n "quality-first|evidence-before-claim" docs/adapters`
Expected: adapters reference, not redefine, these principles.

**Step 6: Commit**

```bash
git add docs/adapters/claude/overview.md docs/adapters/claude/plugin-stack.md docs/adapters/codex/overview.md docs/adapters/codex/setup.md docs/xdev-workflow/plugin-inventory.md
git commit -m "docs(adapters): add claude and codex mapping docs"
```

---

### Task 5: Update Root Entry Points and Install Guidance

**Files:**
- Modify: `README.md`
- Modify: `CLAUDE.md`
- Modify: `docs/plans/2026-03-01-unified-workflow-governance-design.md`
- Create: `scripts/install-codex.sh`

**Step 1: Rewrite README navigation**

Update README to point only to active docs:
- core
- process
- adapters
- governance

Expected: README no longer lists old iterative paths as primary entry points.

**Step 2: Align project CLAUDE.md pointers**

Update `CLAUDE.md` so it points to canonical docs and avoids duplicate policy text.

**Step 3: Add codex install script**

Create `scripts/install-codex.sh` to:
- ensure `~/.agents/skills` exists
- install/update symlink(s) from local repo
- print verification checks

**Step 4: Verify onboarding path**

Run:
```bash
rg -n "docs/xdev-workflow|archive/devloop-scheduler" README.md CLAUDE.md
```
Expected: no primary guidance depends on old paths.

**Step 5: Commit**

```bash
git add README.md CLAUDE.md scripts/install-codex.sh docs/plans/2026-03-01-unified-workflow-governance-design.md
git commit -m "docs: unify onboarding and add codex installer"
```

---

### Task 6: Remove Legacy and Obsolete Content from HEAD

**Files:**
- Delete: `archive/devloop-scheduler/` (all files)
- Delete: `docs/xdev-workflow/research-notes.md`
- Delete: `docs/xdev-workflow/implementation-plan.md`
- Delete: `docs/plans/2026-02-23-xdev-v2-design.md`

**Step 1: Remove legacy archive directory**

Run: `git rm -r archive/devloop-scheduler`
Expected: all scheduler legacy content staged for deletion.

**Step 2: Remove obsolete iterative docs**

Run:
```bash
git rm docs/xdev-workflow/research-notes.md docs/xdev-workflow/implementation-plan.md docs/plans/2026-02-23-xdev-v2-design.md
```
Expected: removed files are not referenced by active onboarding docs.

**Step 3: Validate clean-head policy**

Run:
```bash
test ! -d archive || true
rg -n "devloop-scheduler|2026-02-23-xdev-v2-design|research-notes|implementation-plan" README.md docs || true
```
Expected: no active path depends on removed legacy docs.

**Step 4: Commit**

```bash
git add -A
git commit -m "docs: remove legacy and obsolete workflow artifacts from head"
```

---

### Task 7: End-to-End Verification and Final Documentation Consistency

**Files:**
- Modify (if needed): `docs/governance/status.md`
- Modify (if needed): `docs/governance/changelog.md`

**Step 1: Run consistency checks**

Run:
```bash
git status --short
find docs -type f | sort
rg -n "TODO|TBD|FIXME" docs README.md CLAUDE.md
```
Expected:
- working tree clean or only intentional final edits
- no unresolved placeholder markers

**Step 2: Verify Claude and Codex instructions are actionable**

Run:
```bash
rg -n "install|setup|verify" docs/adapters/claude docs/adapters/codex scripts/install-codex.sh
```
Expected: both adapters include concrete installation and verification commands.

**Step 3: Update governance status**

Record completed governance migration in `docs/governance/status.md` and add changelog entry.

**Step 4: Commit**

```bash
git add docs/governance/status.md docs/governance/changelog.md
git commit -m "docs(governance): record unified workflow governance rollout"
```

