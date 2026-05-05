import React from 'react';
import { Shield, Settings, FileText, ChevronDown } from 'lucide-react';
import { Link, useLocation } from 'react-router-dom';

const Navbar = () => {
  const location = useLocation();

  return (
    <nav className="bg-[#2d3e50] text-white px-6 py-3 flex items-center justify-between shadow-lg border-b border-slate-700/50">
      {/* Left: Logo and Brand */}
      <div className="flex items-center gap-3">
        <div className="bg-white/10 p-2 rounded-lg border border-white/20">
          <Shield className="w-6 h-6 text-white" />
        </div>
        <div>
          <h1 className="text-xl font-bold tracking-tight leading-tight">
            CrashGuard AI
          </h1>
          <p className="text-[10px] text-slate-400 uppercase tracking-widest font-semibold">
            Predictive Safety System
          </p>
        </div>
      </div>

      {/* Middle: Navigation Links */}
      <div className="flex items-center gap-6">

        <Link
          to="/"
          className={`flex items-center gap-2 px-4 py-2 rounded-full text-sm font-medium transition-all ${
            location.pathname === '/'
              ? 'bg-slate-800/80 border border-slate-600 shadow-inner'
              : 'text-slate-400 hover:text-white'
          }`}
        >
          <Shield className="w-4 h-4" />
          DASHBOARD
        </Link>

        <Link
          to="/analytics"
          className={`flex items-center gap-2 text-sm font-medium transition-colors ${
            location.pathname === '/analytics'
              ? 'text-white'
              : 'text-slate-400 hover:text-white'
          }`}
        >
          <Settings className="w-4 h-4" />
          Analytics
        </Link>

        <button className="flex items-center gap-2 text-slate-400 hover:text-white transition-colors text-sm font-medium">
          <FileText className="w-4 h-4" />
          Reports
        </button>
      </div>

      {/* Right: User Profile */}
      <div className="flex items-center gap-2 bg-slate-800/50 pr-2 pl-1 py-1 rounded-full border border-slate-700 hover:border-slate-500 cursor-pointer transition-all">

      </div>
    </nav>
  );
};

export default Navbar;