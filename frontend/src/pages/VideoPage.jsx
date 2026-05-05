import React from "react";

export default function VideoPage() {
  const videos = [
    "https://youtu.be/a0pc44KEHp0",
    "https://youtu.be/t2-qywa1io8",
  ];

  // Helper to convert watch URLs to embed URLs
  const getEmbedUrl = (url) => {
    const videoId = url.split("/").pop();
    return `https://www.youtube.com/embed/${videoId}`;
  };

  return (
    <div className="max-w-5xl mx-auto p-6 space-y-6">
      <h1 className="text-3xl font-bold mb-6">Analytics Videos</h1>

      {videos.map((url, index) => (
        <div key={index} className="aspect-video">
          <iframe
            className="w-full h-full rounded-lg shadow-lg"
            src={getEmbedUrl(url)}
            title={`Video ${index + 1}`}
            frameBorder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
          />
        </div>
      ))}
    </div>
  );
}