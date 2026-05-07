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

const RiskBreakdown = ({ factor}) => {
  return (
    <div className="max-w-4xl mx-auto mt-8 space-y-6">
      
      {/* Five Reason Boxes */}
      <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
        {factor?.map((item, index) => {
        
        const iconName = featureIconMap[item.feature] || "AlertTriangle";
        const IconComponent = LucideIcons[iconName];

        return (
          <RiskFactorCard
            key={index}
            icon={IconComponent}
            label={item.feature}
            value={`${item.impact_score > 0 ? '+' : ''}${(
              item.impact_score * 100
            ).toFixed(1)}%`}
            trend={item.effect}
          />
        );
      })}
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