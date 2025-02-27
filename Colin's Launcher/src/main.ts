import React from 'react';
import ReactDOM from 'react-dom';
import FancyDesign from './components/FancyDesign';
import './assets/styles.css';

const App = () => {
    return (
        <div>
            <FancyDesign />
        </div>
    );
};

ReactDOM.render(<App />, document.getElementById('root'));