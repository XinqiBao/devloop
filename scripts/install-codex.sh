#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "${SCRIPT_DIR}/.." && pwd)"
SOURCE_DIR="${REPO_ROOT}/docs"
TARGET_DIR="${HOME}/.agents/skills"
TARGET_LINK="${TARGET_DIR}/devloop"

if [[ ! -d "${SOURCE_DIR}" ]]; then
  echo "error: source docs directory not found: ${SOURCE_DIR}" >&2
  exit 1
fi

mkdir -p "${TARGET_DIR}"
ln -sfn "${SOURCE_DIR}" "${TARGET_LINK}"

echo "Installed Codex workflow link:"
echo "  ${TARGET_LINK} -> $(readlink "${TARGET_LINK}")"
echo
echo "Verification commands:"
echo "  test -L \"${TARGET_LINK}\" && echo link-ok"
echo "  readlink \"${TARGET_LINK}\""
echo "  find \"${TARGET_LINK}\" -maxdepth 2 -type d | sort"
echo
echo "Canonical docs source: ${SOURCE_DIR}"
echo "Project guide: ${REPO_ROOT}/CLAUDE.md"
echo "Runtime instructions: AGENTS.md (if provided by your Codex environment)"
