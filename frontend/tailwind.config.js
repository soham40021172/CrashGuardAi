/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Adding safety/industrial colors for your CrashGuard theme
        brand: {
          dark: "#0f172a",    // Deep Navy
          accent: "#0ea5e9",  // Safety Blue
          danger: "#ef4444",  // Alert Red
          success: "#22c55e", // Safe Green
        }
      }
    },
  },
  plugins: [],
}