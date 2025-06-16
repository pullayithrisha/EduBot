import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Home from './Home'; 
import './App.css'; 

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={
            <div style={{ 
              textAlign: 'center', 
              padding: '50px',
              minHeight: '100vh',
              backgroundColor: '#0F1D3D',
              color: 'white'
            }}>
              <h1>Welcome</h1>
              <p>Generate questions from your PDFs!</p>

              <Link to="/home">
                <button style={{
                  padding: '6px',
                  borderRadius: '8px',
                  width: '100px',
                  backgroundColor: '#ffffff',
                  color: '#131A81',
                  border: 'none',
                  fontWeight: 'bold',
                  cursor: 'pointer'
                }}>
                  Try it Now
                </button>
              </Link>
            </div>
          }
        />
        <Route path="/home" element={<Home />} />
      </Routes>
    </Router>
  );
}

export default App;
