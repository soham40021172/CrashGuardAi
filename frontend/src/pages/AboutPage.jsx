import React from "react";

export default function AboutPage() {
  const videoUrl = "https://youtu.be/YOUR_VIDEO_LINK";

  const getEmbedUrl = (url) => {
    const videoId = url.split("/").pop();
    return `https://www.youtube.com/embed/${videoId}`;
  };

  return (
    <div className="min-h-screen bg-gray-50 px-6 py-10">

      {/* 🔥 Header */}
      <div className="max-w-5xl mx-auto text-center mb-10">
        <h1 className="text-4xl font-bold text-gray-800">
          🚗 About CrashGuard AI
        </h1>
        <p className="text-gray-600 mt-3 text-lg">
          A Machine Learning system for predicting vehicle crash injury risk
        </p>
      </div>

      {/* 🎥 Video Section */}
      <div className="max-w-5xl mx-auto bg-white rounded-2xl shadow-xl p-6 mb-10">
        <h2 className="text-2xl font-semibold mb-3 text-gray-800">
          🎬 Project Demo & Explanation
        </h2>

        <p className="text-gray-600 mb-4">
          This video walks through the complete system including the machine learning model,
          backend API, and frontend interface. It demonstrates how predictions are generated
          and how users interact with the application.
        </p>

        <div className="aspect-video">
          <iframe
            className="w-full h-full rounded-xl"
            src={getEmbedUrl(videoUrl)}
            title="Project Demo"
            frameBorder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
          />
        </div>
      </div>

      {/* 🧠 Project Overview */}
      <div className="max-w-5xl mx-auto grid md:grid-cols-3 gap-6">

        <div className="bg-blue-50 p-5 rounded-xl">
          <h3 className="text-lg font-semibold text-blue-700">
            🧠 ML System
          </h3>
          <p className="text-sm text-gray-600 mt-2">
            Uses a trained Random Forest model to predict injury probability based on crash conditions.
          </p>
        </div>

        <div className="bg-green-50 p-5 rounded-xl">
          <h3 className="text-lg font-semibold text-green-700">
            ⚙️ Backend API
          </h3>
          <p className="text-sm text-gray-600 mt-2">
            Flask-based REST API serves predictions using pre-trained model pipelines.
          </p>
        </div>

        <div className="bg-purple-50 p-5 rounded-xl">
          <h3 className="text-lg font-semibold text-purple-700">
            💻 Frontend UI
          </h3>
          <p className="text-sm text-gray-600 mt-2">
            Built with React (Vite) for an interactive and user-friendly prediction interface.
          </p>
        </div>

      </div>

      {/* 💼 Real-World Impact */}
      <div className="max-w-5xl mx-auto mt-10 bg-white p-6 rounded-2xl shadow-lg">
        <h2 className="text-2xl font-semibold text-gray-800 mb-3">
          💼 Why This Project Matters
        </h2>

        <ul className="list-disc list-inside text-gray-600 space-y-2">
          <li>Helps identify high-risk crash scenarios</li>
          <li>Supports data-driven road safety decisions</li>
          <li>Demonstrates production-level ML architecture</li>
          <li>Bridges data engineering, ML, and frontend systems</li>
        </ul>
      </div>

      {/* 👨‍💻 Footer */}
      <div className="max-w-5xl mx-auto mt-10 text-center text-gray-500 text-sm">
        Developed as a complete end-to-end Machine Learning project for real-world applications.
      </div>

    </div>
  );
}