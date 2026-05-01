import React from 'react';
import * as LucideIcons from 'lucide-react'


const featureIconMap = {
    "Collision Type": "CarFront",
    "Crash Dayofweek": "CalendarDays",
    "Crash Location Type": "MapPin",
    "Crash Season": "Leaf",
    "Cross Road Category": "GitFork",
    "Driver Distracted By": "SmartphoneOff",
    "Drivers License State": "IdCard",
    "Driver Substance Abuse": "Beer",
    "Driverless Vehicle": "Cpu",
    "Is Incorporated": "Landmark",
    "Is Weekend": "GlassWater",
    "Light": "SunMoon",
    "Location Cluster": "Layers",
    "Non Motorist Substance Abuse": "PersonStanding",
    "Parked Vehicle": "Circle",
    "Related Non Motorist": "Bike",
    "Road Category": "Road",
    "Route Type": "Route",
    "Speed Limit": "Gauge",
    "Surface Condition": "Waves",
    "Time Of Day": "Clock",
    "Traffic Control": "TrafficCone",
    "Vehicle Age": "History",
    "Vehicle Body Type": "Truck",
    "Vehicle First Impact Location": "Zap",
    "Vehicle Going Dir": "Compass",
    "Vehicle Movement": "MoveUpRight",
    "Weather": "CloudRain"
  };

const RiskFactorCard = ({ icon: Icon, label, value, trend }) => {
  const isNegative = value.startsWith('-');
  return (
    <div className="bg-white p-4 rounded-2xl border border-slate-100 shadow-sm">
      <div className="flex items-center gap-2 mb-3 text-slate-500">
        <Icon className="w-4 h-4" />
        <span className="text-[10px] font-bold uppercase tracking-tight">{label}</span>
      </div>
      <div className="flex items-center gap-2">
        <span className={`text-xl font-black ${isNegative ? 'text-emerald-500' : 'text-amber-600'}`}>
          {isNegative ? '↓' : '↑'} {value}
        </span>
      </div>
      {/* Progress bar visual */}
      <div className="mt-3 h-1 w-full bg-slate-100 rounded-full overflow-hidden">
        <div 
          className={`h-full rounded-full ${isNegative ? 'bg-emerald-400' : 'bg-amber-400'}`} 
          style={{ width: `${Math.abs(parseInt(value))}%` }}
        />
      </div>
    </div>
  );
};

const RiskBreakdown = ({ factor, recommendation }) => {
  return (
    <div className="max-w-4xl mx-auto mt-8 space-y-6">
      
      {/* Five Reason Boxes */}
      <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
        <RiskFactorCard icon={LucideIcons.CloudRain} label="Weather Impact" value="+22%" />
        <RiskFactorCard icon={LucideIcons.Gauge} label="Speed Factor" value="+15%" />
        <RiskFactorCard icon={LucideIcons.AlertTriangle} label="Road Friction" value="-18%" />
        <RiskFactorCard icon={LucideIcons.Users} label="Driver State" value="+12%" />
        <RiskFactorCard icon={LucideIcons.Calendar} label="Temporal Risk" value="-08%" />
      </div>

      {/* Safety Recommendation Panel */}
      <div className="bg-[#fcfbf9] border border-slate-200 rounded-3xl p-6 flex flex-col md:flex-row items-center gap-6">
        <div className="bg-amber-100 p-4 rounded-full">
          <LucideIcons.Lightbulb className="w-8 h-8 text-amber-600" />
        </div>
        
        <div className="flex-1 space-y-2 text-center md:text-left">
          <h3 className="text-sm font-black text-slate-800 uppercase tracking-widest">Safety Recommendation</h3>
          <p className="text-slate-600 text-sm leading-relaxed">
            Reduce speed by <span className="font-bold text-amber-700">10-15 km/h</span> and maintain safe distance. 
            Wet roads combined with speed violations pose a pronounced risk.
          </p>
        </div>

        <button className="flex items-center gap-2 bg-white border border-slate-300 px-6 py-3 rounded-xl text-xs font-bold text-slate-700 hover:bg-slate-50 transition-all shadow-sm">
          <LucideIcons.Download className="w-4 h-4" />
          Download Report
        </button>
      </div>

      {/* Footer Branding */}
      <div className="flex flex-wrap items-center justify-between px-2 gap-4">
        <div className="flex items-center gap-2">
           <div className="w-4 h-4 bg-slate-800 rounded-sm flex items-center justify-center">
              <div className="w-2 h-2 bg-white rounded-full" />
           </div>
           <span className="text-[10px] font-bold text-slate-400 uppercase tracking-widest">NHTSA Crash Dataset</span>
        </div>
        <div className="flex gap-6 text-[10px] font-bold text-slate-400 uppercase tracking-widest">
           <span>Federal Auto Safety Standards</span>
           <span>Crash Predict Model Documentation</span>
        </div>
      </div>
    </div>
  );
};

export default RiskBreakdown;