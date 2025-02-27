#include "GameLauncher.h"
#include <iostream>

void GameLauncher::launchGame(const std::string& gameName) {
    std::cout << "Launching game: " << gameName << std::endl;
    // Logic to launch the game
}

void GameLauncher::addGame(const std::string& gameName) {
    games.push_back(gameName);
    std::cout << "Added game: " << gameName << std::endl;
}

void GameLauncher::displayGames() const {
    std::cout << "Available games:" << std::endl;
    for (const auto& game : games) {
        std::cout << "- " << game << std::endl;
    }
}