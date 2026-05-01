import React from "react";

export default function VideoPage() {
  const videos = [
    "VIDEO_ID_1",
    "VIDEO_ID_2",
  ];

  return (
    <div className="max-w-5xl mx-auto p-6 space-y-6">
      <h1 className="text-3xl font-bold mb-6">Analytics Videos</h1>

      {videos.map((videoId, index) => (
        <iframe
          key={index}
          className="w-full rounded-lg"
          height="450"
          src={`https://www.youtube.com/embed/${videoId}`}
          title={`Video ${index + 1}`}
          frameBorder="0"
          allowFullScreen
        />
      ))}
    </div>
  );
}
