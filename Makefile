.PHONY: all dev run drop-dev clean help

# Default target
all: dev run

# Virtual environment directory and activation script paths
VENV_DIR := .venv
VENV_BIN := $(VENV_DIR)/bin
VENV_ACTIVATE := $(VENV_BIN)/activate
PYTHON := $(VENV_BIN)/python

# Set up development environment
dev: $(VENV_ACTIVATE)

$(VENV_ACTIVATE):
	@echo "Setting up development environment..."
	@python3 -m venv $(VENV_DIR)
	@. $(VENV_ACTIVATE) && pip install --upgrade pip
	@. $(VENV_ACTIVATE) && pip install -r requirements.txt
	@echo "Development environment ready!"

# Run the game
run: $(VENV_ACTIVATE)
	@echo "Running the game..."
	@. $(VENV_ACTIVATE) && python -m src.core.main

# Remove development environment
drop-dev:
	@echo "Removing development environment..."
	@if [ -d "$(VENV_DIR)" ]; then \
		rm -rf $(VENV_DIR); \
		echo "Virtual environment removed."; \
	else \
		echo "Virtual environment not found."; \
	fi

# Clean up Python cache files and virtual environment
clean: drop-dev
	@echo "Cleaning up Python cache files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.pyo" -delete
	@find . -type f -name "*.pyd" -delete
	@find . -name '*.egg-info' -exec rm -rf {} +
	@find . -name '*.egg' -exec rm -rf {} +
	@find . -name '.pytest_cache' -exec rm -rf {} +
	@echo "Cleanup complete!"

# Help message
help:
	@echo "Available commands:"
	@echo "  make dev      - Set up development environment (create venv and install dependencies)"
	@echo "  make run      - Run the game"
	@echo "  make all      - Set up environment and run the game"
	@echo "  make drop-dev - Remove the virtual environment"
	@echo "  make clean    - Remove virtual environment and all Python cache files"
	@echo "  make help     - Show this help message"
