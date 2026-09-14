#!/bin/bash
echo "🤖 Installing JARVIS AI Assistant..."
echo ""
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi
echo "✓ Python 3 found"
echo ""
echo "Creating virtual environment..."
python3 -m venv venv
echo "Activating virtual environment..."
source venv/bin/activate
echo "Upgrading pip..."
pip install --upgrade pip
echo "Installing dependencies..."
pip install -r requirements.txt
if [ ! -f .env ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo ""
    echo "⚠️  IMPORTANT: Edit .env file with your credentials:"
    echo "   - GITHUB_TOKEN: Your GitHub personal access token"
    echo "   - GEMINI_API_KEY: Your Google Gemini API key"
    echo ""
fi
echo ""
echo "✓ Installation complete!"
echo ""
echo "To start JARVIS:"
echo "  1. Edit .env with your API keys"
echo "  2. Run: python app.py"
echo "  3. Say 'Hey Jarvis' if voice is enabled"
