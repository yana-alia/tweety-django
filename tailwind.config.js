/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './templates/*.html',
    './social/templates/social/*.html',
    './landing/templates/landing/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
  prefix: "tw-",
  important: true,
  corePlugins: {
      preflight: false,
  }
}