import React, { useState } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import Navbar from './components/Navbar';
import StatusBar from './components/StatusBar';
import HeroSection from './components/HeroSection';
import RiskCalculator from './components/RiskCalculator';
import RiskMeter from './components/RiskMeter';
import RiskBreakdown from './components/RiskBreakdown';
import VideoPage from './pages/VideoPage';
import AboutPage from './pages/AboutPage';

import { getRiskPrediction } from './services/api';

function HomePage({
  handlePredict,
  probability,
  injuryType,
  safetyScore,
  factors
}) {
  return (
    <>
      <StatusBar />
      <HeroSection />

      <main className="max-w-6xl mx-auto px-6 mt-\[-50px\] relative z-30">
        <RiskCalculator onPredict={handlePredict} />

        <RiskMeter
          score={probability}
          type={injuryType}
          safetyScore={safetyScore}
        />

        <RiskBreakdown factor={factors} />
      </main>
    </>
  );
}

function App() {
  const [safetyScore, setSafetyScore] = useState(0);
  const [probability, setProbablity] = useState(0);
  const [injuryType, setInjuryType] = useState([]);
  const [factors, setFactors] = useState('');

  const handlePredict = async (data) => {
    try {
      const response = await getRiskPrediction(data);

      if (response.status === 'success') {
        setProbablity(response.data.probability * 100);
        setInjuryType(response.data.injury_type);
        setSafetyScore(response.data.safety_score);
        setFactors(response.data.top_factors);
      }
    } catch (error) {
      console.log("Connection Failed");
    }
  };

  return (
    <BrowserRouter>
      <div className="min-h-screen bg-[#fcfcfc] pb-20">
        <Navbar />

        <Routes>
          <Route
            path="/"
            element={
              <HomePage
                handlePredict={handlePredict}
                probability={probability}
                injuryType={injuryType}
                safetyScore={safetyScore}
                factors={factors}
              />
            }
          />

          <Route path="/analytics" element={<VideoPage />} />
          <Route path="/about" element={<AboutPage />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;