# Problem Statement

## Context

Teams running AI-assisted development often accumulate duplicated guidance, drift between execution platforms, and completion claims without verifiable evidence. Over time, this reduces trust in process outcomes and increases rework.

## Core Problems

1. Rule duplication creates conflicting sources of truth.
2. Process definitions and delivery-specific instructions are mixed together.
3. Verification practices are inconsistent, so "done" cannot be audited reliably.
4. Legacy artifacts remain in active paths and blur what is current policy.

## Constraints

1. A single canonical workflow source must exist in the repository.
2. Core principles and process rules must stay platform-agnostic.
3. Delivery-specific guidance must live in adapter documents.
4. Repository HEAD should contain active materials only; history provides traceability.

## Objectives

1. Define one authoritative workflow structure covering principles, lifecycle, and governance.
2. Keep quality gates explicit and evidence-oriented.
3. Support multiple execution environments through mapping adapters, not rule forks.
4. Make onboarding concise: active entry points only, no legacy-first navigation.

## Non-Goals

1. Rewriting historical commits.
2. Preserving obsolete docs in active paths.
3. Building a separate product outside repository governance.
