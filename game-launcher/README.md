# Game Launcher

## Overview
This project is a game launcher application designed to manage and launch games efficiently. It provides a user-friendly interface to add games, display the list of available games, and launch them directly from the launcher.

## Project Structure
```
game-launcher
├── src
│   ├── main.cpp          # Entry point of the application
│   ├── GameLauncher.h    # Header file for the GameLauncher class
│   ├── GameLauncher.cpp  # Implementation of the GameLauncher class
│   └── resources
│       └── resource.h    # Resource definitions (icons, images, etc.)
├── CMakeLists.txt        # CMake configuration file
├── README.md             # Documentation for the project
└── LICENSE               # Licensing information
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/game-launcher.git
   ```
2. Navigate to the project directory:
   ```
   cd game-launcher
   ```
3. Create a build directory:
   ```
   mkdir build && cd build
   ```
4. Run CMake to configure the project:
   ```
   cmake ..
   ```
5. Build the project:
   ```
   cmake --build .
   ```

## Usage
- After building the project, you can run the game launcher executable.
- Use the interface to add games to your library.
- Select a game from the list and click the launch button to start playing.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.