#ifndef GAME_LAUNCHER_H
#define GAME_LAUNCHER_H

#include <string>
#include <vector>

class GameLauncher {
public:
    GameLauncher();
    void launchGame(const std::string& gameName);
    void addGame(const std::string& gameName);
    void displayGames() const;

private:
    std::vector<std::string> games;
};

#endif // GAME_LAUNCHER_H