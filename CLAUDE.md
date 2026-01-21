# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Anki Card Generator is a tool for generating Japanese language learning content using Claude AI. It integrates with Anki flashcard system to help users learn Japanese vocabulary and grammar based on their existing knowledge level.

## Tech Stack

- Python 3.13
- uv package manager
- Flask (planned)

## Common Commands

```bash
# Install dependencies
uv sync

# Run the application
uv run python src/main.py

# Add a dependency
uv add <package-name>
```

## Project Structure

```
anki-card-generator/
├── src/               # Main source code
│   ├── main.py        # Application entry point
│   └── pyproject.toml # Project configuration
├── resources/         # Reference materials
│   └── grammar.md     # Japanese grammar reference (N5-N3 JLPT levels)
└── README.md          # Project documentation (Chinese)
```

## Key Concepts

- The project uses a Claude Project workflow where user background, known vocabulary, and grammar patterns are stored as context
- `resources/grammar.md` contains Japanese grammar patterns organized by JLPT level (N5, N4, N3) in the format `【Ｎx文法】`
- The goal is to generate Japanese learning content that builds on the user's existing knowledge
