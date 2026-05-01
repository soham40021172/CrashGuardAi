import React, { useEffect } from 'react';
import { motion, useAnimation } from 'framer-motion';
import { AlertTriangle, Activity, ShieldAlert,ShieldCheck } from 'lucide-react';

const SafetyScore = ({ score = 0 }) => {
    const Safety_colour = (s) => s < 50 ? "text-red-600" : "text-emerald-500";

    return (
      <div className="bg-white rounded-3xl p-8 shadow-2xl border border-slate-100 mt-12 flex flex-col justify-center items-center h-full w-full">
        <div className="flex items-center gap-2 mb-6">
          <ShieldCheck className="w-5 h-5 text-emerald-500" />
          <h2 className="text-sm font-black uppercase tracking-widest text-slate-800">Safety Score</h2>
        </div>
        <div className="flex flex-col items-center">
          <div className={`text-6xl font-black ${Safety_colour(score)} tracking-tighter`}>
            {score}<span className="text-4xl text-slate-400">/100</span>
          </div>
          <div className={`mt-4 px-4 py-1 bg-emerald-50 rounded-full text-[10px] font-black ${Safety_colour(score)} uppercase tracking-widest`}>
            Secure Status
          </div>
        </div>
      </div>
    );
  };

const RiskMeter = ({ score = 0, type = "Injury Type", safetyScore = 0 }) => {
  const controls = useAnimation();

  useEffect(() => {
    controls.set({ rotate: -90 });
    controls.start({
      rotate: (score / 100) * 180 - 90,
      transition: { duration: 1.5, ease: "backOut" }
    });
  }, [score, controls]);

  const getRiskColor = (s) => {
    if (s < 30) return 'text-emerald-500';
    if (s < 60) return 'text-amber-500';
    return 'text-red-600';
  };

  return (
    /* 1. Use max-w-none to let it fill the screen width */
    /* 2. Increased gap to 10 for better separation */
    <div className="flex flex-col md:flex-row gap-10 justify-center items-stretch w-full max-w-none mx-auto px-10">
      
      {/* 3. LEFT BOX: 70% Ratio using flex-[7] */}
      <div className="flex-/[7/] bg-white rounded-3xl p-8 shadow-2xl border border-slate-100 mt-12 overflow-hidden flex flex-col justify-between">
        <div className="flex items-center justify-between mb-10">
          <div>
            <div className="flex items-center gap-2 mb-1">
              <Activity className="w-5 h-5 text-slate-700" />
              <h2 className="text-sm font-black uppercase tracking-widest text-slate-800">
                Injury Severity Projection
              </h2>
            </div>
            <p className="text-slate-500 text-xs font-bold uppercase tracking-tighter">
              Probability of Severe/Fatal Outcome
            </p>
          </div>
          <div className={`text-3xl font-black ${getRiskColor(score)} tabular-nums`}>
            {score.toFixed(1)}%
          </div>
        </div>

        {/* This div contains the gauge; w-full allows it to scale with the box */}
        <div className="relative flex justify-center items-end h-64">
          <svg viewBox="0 0 200 100" className="w-full max-w-2xl drop-shadow-sm">
            <path
              d="M20,100 A80,80 0 0,1 180,100"
              fill="none"
              stroke="#f1f5f9"
              strokeWidth="12"
              strokeLinecap="round"
            />
            <path
              d="M20,100 A80,80 0 0,1 180,100"
              fill="none"
              stroke="url(#riskGradient)"
              strokeWidth="12"
              strokeLinecap="round"
              strokeDasharray="251.2"
              strokeDashoffset={251.2 - (score / 100) * 251.2}
              className="transition-all duration-1000 ease-out"
            />
            <defs>
              <linearGradient id="riskGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stopColor="#10b981" />
                <stop offset="50%" stopColor="#f59e0b" />
                <stop offset="100%" stopColor="#dc2626" />
              </linearGradient>
            </defs>
          </svg>

          <motion.div
            animate={controls}
            className="absolute bottom-0 w-1.5 h-44 origin-bottom rounded-full z-20 shadow-lg"
            style={{ backgroundColor: '#1e293b', marginBottom: '-2px' }}
          >
            <div className="absolute top-0 left-1/2 -translate-x-1/2 -mt-2 w-4 h-4 bg-slate-800 rotate-45 rounded-sm" />
            <div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-6 h-6 bg-slate-800 rounded-full border-4 border-white shadow-md" />
          </motion.div>

          <div className="absolute bottom-4 flex flex-col items-center">
            <span className={`text-7xl font-black tabular-nums tracking-tighter ${getRiskColor(score)}`}>
              {Math.round(score)}
            </span>
            <div className="flex items-center gap-1 text-slate-400 font-black text-[10px] uppercase tracking-widest mt-1">
              <AlertTriangle className="w-3 h-3" />
              Risk Index
            </div>
          </div>
          
          <div className="absolute bottom-0 left-4 text-[10px] font-black text-emerald-500 uppercase">Safe</div>
          <div className="absolute bottom-0 right-4 text-[10px] font-black text-red-600 uppercase">Critical</div>
        </div>
        
        <div className="mt-10 grid grid-cols-2 gap-4 pt-6 border-t border-slate-100">
           <div className="bg-slate-50 p-4 rounded-2xl border border-slate-100">
              <p className="text-[10px] font-black text-slate-400 uppercase mb-1">Severity Level</p>
              <div className="flex items-center gap-2">
                 <ShieldAlert className={`w-4 h-4 ${getRiskColor(score)}`} />
                 <p className={`text-sm font-black uppercase ${getRiskColor(score)}`}>{type}</p>
              </div>
           </div>
           <div className="bg-slate-50 p-4 rounded-2xl border border-slate-100 text-right">
              <p className="text-[10px] font-black text-slate-400 uppercase mb-1">Prediction Confidence</p>
              <p className="text-sm font-black text-slate-700 uppercase tracking-tighter">High (RandomForest)</p>
           </div>
        </div> 
      </div>

      {/* 4. RIGHT BOX: 30% Ratio using flex-[3] */}
      <div className="flex-/[3/] flex flex-col">
          <SafetyScore score={safetyScore} />
      </div>

    </div>
  );
};

export default RiskMeter;