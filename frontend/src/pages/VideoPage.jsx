import React from "react";

export default function VideoPage() {
  const videos = [
    {
      url: "https://youtu.be/a0pc44KEHp0",
      title: "Power BI Dashboard Walkthrough",
      description:
        "Explore insights from vehicle crash data including trends, risk factors, and injury analysis using interactive dashboards.",
    },
  ];

  const getEmbedUrl = (url) => {
    const videoId = url.split("/").pop();
    return `https://www.youtube.com/embed/${videoId}`;
  };

  return (
    <div className="min-h-screen bg-gray-50 px-6 py-10">
      
      {/* 🔥 Header Section */}
      <div className="max-w-5xl mx-auto mb-10 text-center">
        <h1 className="text-4xl font-bold text-gray-800">
          📊 Analytics Dashboard
        </h1>
        <p className="text-gray-600 mt-3 text-lg">
          Interactive insights and visual storytelling powered by Power BI
        </p>
      </div>

      {/* 🎥 Video Section */}
      <div className="max-w-5xl mx-auto space-y-10">
        {videos.map((video, index) => (
          <div
            key={index}
            className="bg-white rounded-2xl shadow-xl p-6"
          >
            <h2 className="text-2xl font-semibold mb-2 text-gray-800">
              {video.title}
            </h2>

            <p className="text-gray-600 mb-4">
              {video.description}
            </p>

            {/* Video */}
            <div className="aspect-video mb-6">
              <iframe
                className="w-full h-full rounded-xl"
                src={getEmbedUrl(video.url)}
                title={video.title}
                frameBorder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
              />
            </div>

            {/* 📊 Insights Section */}
            <div className="grid md:grid-cols-3 gap-4 mt-4">
              <div className="bg-blue-50 p-4 rounded-xl">
                <h3 className="font-semibold text-blue-700">Crash Trends</h3>
                <p className="text-sm text-gray-600 mt-1">
                  Identify peak accident times and seasonal patterns.
                </p>
              </div>

              <div className="bg-green-50 p-4 rounded-xl">
                <h3 className="font-semibold text-green-700">Risk Factors</h3>
                <p className="text-sm text-gray-600 mt-1">
                  Analyze how weather, speed, and road type affect injuries.
                </p>
              </div>

              <div className="bg-red-50 p-4 rounded-xl">
                <h3 className="font-semibold text-red-700">Injury Insights</h3>
                <p className="text-sm text-gray-600 mt-1">
                  Understand conditions leading to high injury probability.
                </p>
              </div>
            </div>

            {/* 💡 Footer Note */}
            <div className="mt-6 text-sm text-gray-500 italic">
              This dashboard complements the ML model by providing human-readable insights for decision-making.
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}