import React, { useState, useEffect } from 'react';

const HeroSection = () => {
  const [offsetY, setOffsetY] = useState(0);

  // Listener to track page scroll
  const handleScroll = () => setOffsetY(window.pageYOffset);

  useEffect(() => {
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <section className="relative h-[70vh] w-full overflow-hidden flex items-center justify-center border-b border-slate-800">
      {/* The Background Image 
          transform: translateY moves the image. 
          The '*' multiplier determines speed. 
          Positive value moves it DOWN when scrolling DOWN.
      */}
      <div 
        className="absolute inset-0 z-0 w-full h-[200%] bg-cover bg-center"
        style={{ 
          backgroundImage: `url('/header.jpg')`, // Use your uploaded world map image
          transform: `translateY(${(offsetY * 0.3) - 100}px)`, // Adjust 0.4 for "faster" or "slower" feel
          filter: 'brightness(0.7) contrast(1)'
        }}
      />

      {/* Dark Overlay for Text Readability */}
      <div className="absolute inset-0 bg-linear-to-b from-[#0f172a]/80 via-transparent to-[#0f172a] z-10" />

      {/* The Text Content - Stays in normal flow */}
      <div className="relative z-20 max-w-4xl px-8 text-center">
        <h1 className="text-4xl md:text-5xl font-extrabold text-white mb-6 leading-tight tracking-tight">
          Quantifying Roadway Risk: <br />
          <span className="text-sky-400 font-medium">A Predictive Analysis of FARS Data</span>
        </h1>
        <p className="text-lg md:text-xl text-slate-300 font-light max-w-2xl mx-auto leading-relaxed">
          Estimate the risk of roadway collisions based on weather conditions, 
          traffic density, time of day, and roadway type.
        </p>
        
        <div className="mt-8 flex gap-4 justify-center">
          <div className="h-1 w-20 bg-sky-500 rounded-full"></div>
          <div className="h-1 w-20 bg-slate-700 rounded-full"></div>
        </div>
      </div>
    </section>
  );
};

export default HeroSection;