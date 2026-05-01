import React from 'react';

const StatusBar = () => {
  return (
    <div className="bg-[#f8f9fa] border-b border-slate-200 py-2 px-6 flex items-center gap-4 text-xs font-medium text-slate-500">
      <div className="flex items-center gap-1">
        <span>Project:</span>
        <span className="font-bold text-slate-800">Crash-Predict v2.1</span>
      </div>
      
      <span className="text-slate-300">|</span>
      
      <div className="flex items-center gap-1">
        <span>Data Version:</span>
        <span className="text-slate-800">FARS 2025 Update</span>
      </div>

      <span className="text-slate-300">|</span>

      <div className="flex items-center gap-2">
        <span>Status:</span>
        <span className="bg-slate-200 text-slate-700 px-2 py-0.5 rounded border border-slate-300 shadow-sm text-[10px] uppercase tracking-wider font-bold">
          Deployed
        </span>
      </div>
    </div>
  );
};

export default StatusBar;