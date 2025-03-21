# Pygame Space Shooter 🚀☄️

A classic space shooter game built with Pygame as a capstone project for the Boot.Dev Python OOP course.

## Description

This game is a tribute to classic space shooter arcade games where players control a spaceship and navigate through an asteroid field. The game showcases object-oriented programming principles with a clean, modular structure.

## Features

- Player-controlled spaceship
- Asteroid field with collision detection
- Circle-based hit detection system
- Object-oriented design with inheritance and encapsulation

## Project Structure
```
pygame-space-shooter/
├── Makefile               # Build automation
├── requirements.txt       # Project dependencies
└── src/                   # Source code
├── core/                  # Core game functionality
│   ├── constants.py       # Game constants and settings
│   └── main.py            # Main game loop
└── entities/              # Game entities
├── asteroid.py            # Asteroid class
├── asteroidfield.py       # Field of asteroids manager
├── circleshape.py         # Base circle collision class
└── player.py              # Player spaceship class
```
## Installation

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Setup

1. Clone this repository:
```
git clone https://github.com/yourusername/pygame-space-shooter.git
cd pygame-space-shooter
```
2. Set up the development environment and run the game using the provided Makefile:
```
make all
```
This will:
- Create a virtual environment
- Install required dependencies
- Run the game

## Usage

### Running the Game

After installation, you can run the game at any time with:
```
make run
```
### Game Controls

- **WSAD Keys**: Move the spaceship
- **Space**: Shoot
- **Esc**: Exit the game

## Development

### Available Makefile Commands

The project includes a Makefile with several useful commands:

- `make dev` - Set up the development environment
- `make run` - Run the game
- `make all` - Set up environment and run the game
- `make drop-dev` - Remove the virtual environment
- `make clean` - Remove virtual environment and all Python cache files
- `make help` - Show help message with available commands

### Adding New Features

To extend the game with new features:

1. Add new entity classes in the `src/entities/` directory
2. Update the main game loop in `src/core/main.py`
3. Add any new constants to `src/core/constants.py`

## Learning Outcomes

This project demonstrates proficiency in:

- Object-oriented programming in Python
- Game development fundamentals with Pygame
- Software design patterns
- Clean code architecture
- Build automation with Makefiles

## Acknowledgments
- Boot.Dev Python OOP course https://www.boot.dev/tracks/backend
- Pygame community
