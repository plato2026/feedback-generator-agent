#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════════
# run.sh — Quick Start Script
# ═══════════════════════════════════════════════════════════════
# Usage:  chmod +x run.sh && ./run.sh
# ═══════════════════════════════════════════════════════════════

set -e

echo "📝 Student Feedback Generator Agent"
echo "════════════════════════════════════"

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not found. Please install Python 3.10+."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
echo "✅ Python $PYTHON_VERSION detected"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
fi

# Activate virtual environment
source venv/bin/activate 2>/dev/null || source venv/Scripts/activate 2>/dev/null
echo "✅ Virtual environment activated"

# Install dependencies
echo "📦 Installing dependencies..."
pip install -q -r requirements.txt
echo "✅ Dependencies installed"

# Check for secrets
if [ ! -f ".streamlit/secrets.toml" ]; then
    echo ""
    echo "⚠️  No secrets.toml found."
    echo "   You can enter your API key in the sidebar when the app opens,"
    echo "   or create .streamlit/secrets.toml from the template:"
    echo "   cp .streamlit/secrets.toml.example .streamlit/secrets.toml"
    echo ""
fi

# Launch
echo ""
echo "🚀 Launching Feedback Generator Agent..."
echo "   Open: http://localhost:8501"
echo "   Press Ctrl+C to stop"
echo ""
streamlit run app.py
