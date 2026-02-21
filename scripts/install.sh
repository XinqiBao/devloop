#!/usr/bin/env bash
set -euo pipefail

echo "=== devloop installation ==="

# Check prerequisites
missing=()

command -v python3 >/dev/null || missing+=("python3 (3.10+)")
command -v git >/dev/null || missing+=("git")
command -v gh >/dev/null || missing+=("gh (GitHub CLI)")
command -v node >/dev/null || missing+=("node (18+)")

if [ ${#missing[@]} -gt 0 ]; then
    echo "ERROR: Missing prerequisites:"
    printf '  - %s\n' "${missing[@]}"
    echo "Install them and re-run this script."
    exit 1
fi

# Check gh auth
if ! gh auth status &>/dev/null; then
    echo "WARNING: gh is not authenticated. Run: gh auth login"
fi

# Check Claude Code CLI
if ! command -v claude &>/dev/null; then
    echo "Installing Claude Code CLI..."
    npm install -g @anthropic-ai/claude-code
fi

# Install Python package
echo "Installing devloop..."
pip install -e ".[dev]"

# Create config directory
config_dir="$HOME/.config/devloop"
mkdir -p "$config_dir"

if [ ! -f "$config_dir/config.yaml" ]; then
    cp configs/config.example.yaml "$config_dir/config.yaml"
    echo "Created config at $config_dir/config.yaml"
    echo "IMPORTANT: Edit this file with your settings before running."
else
    echo "Config already exists at $config_dir/config.yaml"
fi

echo ""
echo "=== Installation complete ==="
echo "Next steps:"
echo "  1. Edit $config_dir/config.yaml"
echo "  2. Set environment variables: TG_BOT_TOKEN, TG_CHAT_ID"
echo "  3. Run: python -m src.scheduler --once"
