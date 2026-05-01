import React, { useState } from 'react';
import { Gauge, ChevronRight, Info } from 'lucide-react';

const RiskCalculator = ({ onPredict }) => {
  // 1. Updated Options Keys to match Backend Expectations
  const options = {
    collision_type_clean: ['REAR_END', 'SIDESWIPE', 'SINGLE_VEHICLE', 'HEAD_ON', 'ANGLE', 'OTHER'],
    crash_dayofweek_clean: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    crash_location_type: ['ON_ROAD', 'OFF_ROAD'],
    crash_season_clean: ['Spring', 'Summer', 'Fall', 'Winter'],
    cross_road_category_clean: ['UNKNOWN', 'ARTERIAL', 'RESIDENTIAL', 'LOCAL', 'HIGH_SPEED', 'RAMP'],
    driver_distracted_by_clean: ['NO_DISTRACTION', 'ATTENTION_RELATED', 'DISTRACTION', 'UNKNOWN', 'NO_DRIVER'],
    drivers_license_state_clean: ['IN_STATE_MD', 'OUT_STATE_US', 'UNKNOWN', 'OTHER'],
    driver_substance_abuse_clean: ['NONE', 'ALCOHOL', 'DRUG', 'UNKNOWN'],
    light_clean: ['DAY', 'DARK_LIGHTED', 'DARK_NOT_LIGHTED', 'TWILIGHT', 'UNKNOWN'],
    road_category_clean: ['LOCAL', 'ARTERIAL', 'HIGH_SPEED', 'RESIDENTIAL', 'RAMP', 'UNKNOWN'],
    route_type_clean: ['Highway/Main', 'Local/Municipal', 'Gov/Private/Special', 'Other/Unknown'],
    surface_condition_clean: ['DRY', 'WET', 'WINTER', 'OTHER', 'UNKNOWN'],
    time_of_day_clean: ['Morning Rush', 'Mid-Day', 'Evening Rush', 'Night', 'Late Night'],
    traffic_control_clean: ['NO_CONTROL', 'TRAFFIC_SIGNAL', 'STOP_YIELD', 'WARNING_SIGN', 'OTHER'],
    vehicle_body_type_clean: ['PASSENGER_VEHICLE', 'SUV_PICKUP_LIGHT_TRUCK', 'HEAVY_TRUCK', 'BUS', 'TWO_WHEELER', 'EMERGENCY_VEHICLE'],
    vehicle_first_impact_location_clean: ['FRONT', 'SIDE', 'REAR', 'REAR_SIDE', 'ROLLOVER_TOP', 'NON_COLLISION'],
    vehicle_going_dir_clean: ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UNKNOWN'],
    vehicle_movement_clean: ['STRAIGHT_DRIVING', 'TURNING', 'SLOWING_OR_STOPPED', 'LANE_CHANGE', 'HIGH_RISK_MANEUVER'],
    weather_clean: ['CLEAR', 'CLOUDY', 'RAIN', 'FOG', 'WINTER', 'UNKNOWN']
  };

  // 2. State initialized with exact Backend Key Names
  const [formData, setFormData] = useState({
    speed_limit: 38,
    vehicle_age: 5,
    collision_type_clean: 'REAR_END',
    crash_dayofweek_clean: 'Friday',
    crash_location_type: 'ON_ROAD',
    crash_season_clean: 'Spring',
    cross_road_category_clean: 'ARTERIAL',
    driver_distracted_by_clean: 'NO_DISTRACTION',
    drivers_license_state_clean: 'IN_STATE_MD',
    driver_substance_abuse_clean: 'NONE',
    driverless_vehicle: 0,
    is_incorporated: 1,
    is_weekend: 0,
    light_clean: 'DAY',
    location_cluster_clean: 5, // Static or hidden input
    non_motorist_substance_abuse_clean: 0,
    parked_vehicle_clean: 0,
    related_non_motorist_clean: 0,
    road_category_clean: 'ARTERIAL',
    route_type_clean: 'Highway/Main',
    surface_condition_clean: 'WET',
    time_of_day_clean: 'Evening Rush',
    traffic_control_clean: 'TRAFFIC_SIGNAL',
    vehicle_body_type_clean: 'PASSENGER_VEHICLE',
    vehicle_first_impact_location_clean: 'FRONT',
    vehicle_going_dir_clean: 'NORTH',
    vehicle_movement_clean: 'STRAIGHT_DRIVING',
    weather_clean: 'RAIN'
  });

  const handleChange = (key, value) => {
    setFormData(prev => ({ ...prev, [key]: value }));
  };

  // Helper to make backend keys look pretty in the UI
  const formatLabel = (key) => {
    return key
      .replace(/_clean/g, '')
      .replace(/_/g, ' ')
      .replace(/\b\w/g, l => l.toUpperCase());
  };

  return (
    <div className="bg-[#f3f0eb] rounded-3xl p-6 md:p-10 shadow-2xl border border-white/60">
      {/* Header */}
      <div className="mb-10 flex flex-col md:flex-row md:items-end justify-between gap-4">
        <div>
          <div className="flex items-center gap-3 mb-2">
            <div className="p-2 bg-slate-800 rounded-lg"><Gauge className="w-5 h-5 text-white" /></div>
            <h2 className="text-sm font-black uppercase tracking-[0.2em] text-slate-800">Risk Calculator</h2>
          </div>
          <p className="text-slate-500 text-sm font-medium ml-12">Data structured for API integration</p>
        </div>
      </div>

      {/* 1. NUMERIC SLIDERS */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12 bg-white/60 p-8 rounded-3xl border border-slate-200">
        <div className="space-y-5">
          <div className="flex justify-between items-center">
            <label className="text-xs font-bold uppercase text-slate-600">Speed Limit (MPH)</label>
            <span className="bg-[#b49b7e] px-4 py-1.5 rounded-lg text-white text-xs font-black">{formData.speed_limit}</span>
          </div>
          <input type="range" min="5" max="70" step="5" value={formData.speed_limit} onChange={(e) => handleChange('speed_limit', parseInt(e.target.value))} className="w-full accent-[#b49b7e]" />
        </div>

        <div className="space-y-5">
          <div className="flex justify-between items-center">
            <label className="text-xs font-bold uppercase text-slate-600">Vehicle Age (Years)</label>
            <span className="bg-slate-700 px-4 py-1.5 rounded-lg text-white text-xs font-black">{formData.vehicle_age}</span>
          </div>
          <input type="range" min="0" max="40" step="1" value={formData.vehicle_age} onChange={(e) => handleChange('vehicle_age', parseInt(e.target.value))} className="w-full accent-slate-800" />
        </div>
      </div>

      {/* 2. DROPDOWN GRID */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-6">
        {Object.keys(options).map((key) => (
          <div key={key} className="space-y-2">
            <label className="text-[10px] font-bold text-slate-500 uppercase tracking-widest ml-1">{formatLabel(key)}</label>
            <select 
              value={formData[key]} 
              onChange={(e) => handleChange(key, e.target.value)}
              className="w-full bg-white/90 border border-slate-200 rounded-2xl p-4 text-sm font-bold text-slate-700 outline-none"
            >
              {options[key].map(opt => <option key={opt} value={opt}>{opt.replace(/_/g, ' ')}</option>)}
            </select>
          </div>
        ))}

        {/* Binary Toggles */}
        {[
          { label: 'Driverless Vehicle', key: 'driverless_vehicle' },
          { label: 'Is Weekend', key: 'is_weekend' },
          { label: 'Parked Vehicle', key: 'parked_vehicle_clean' },
          { label: 'Non-Motorist Involved', key: 'related_non_motorist_clean' }
        ].map((bool) => (
          <div key={bool.key} className="space-y-2">
             <label className="text-[10px] font-bold text-slate-500 uppercase tracking-widest ml-1">{bool.label}</label>
             <div className="flex bg-slate-200/50 p-1.5 rounded-2xl">
                <button onClick={() => handleChange(bool.key, 0)} className={`flex-1 py-3 text-xs font-black rounded-xl ${formData[bool.key] === 0 ? 'bg-white shadow-md text-slate-800' : 'text-slate-400'}`}>NO</button>
                <button onClick={() => handleChange(bool.key, 1)} className={`flex-1 py-3 text-xs font-black rounded-xl ${formData[bool.key] === 1 ? 'bg-white shadow-md text-slate-800' : 'text-slate-400'}`}>YES</button>
             </div>
          </div>
        ))}
      </div>

      <button onClick={() => onPredict(formData)} className="w-full mt-12 bg-[#4a6b8a] text-white py-6 rounded-3xl font-black text-xl uppercase tracking-widest hover:bg-[#3a5670] transition-all">
        Run AI Risk Prediction
      </button>
    </div>
  );
};

export default RiskCalculator;