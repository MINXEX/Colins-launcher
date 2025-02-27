import React from 'react';
import './styles.css';

const FancyDesign: React.FC = () => {
    return (
        <div className="fancy-launcher">
            <header className="launcher-header">
                <h1>Colin's Launcher</h1>
            </header>
            <main className="launcher-main">
                <button className="launcher-button">Play Game 1</button>
                <button className="launcher-button">Play Game 2</button>
                <button className="launcher-button">Settings</button>
            </main>
            <footer className="launcher-footer">
                <p>© 2023 Colin's Launcher. All rights reserved.</p>
            </footer>
        </div>
    );
};

export default FancyDesign;