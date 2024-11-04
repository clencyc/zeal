/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',  // Adjust this path to match your Django templates
    './static/**/*.js',       // Include any JavaScript files if needed
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};