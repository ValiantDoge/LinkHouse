/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../templates/**/*.{html,js}",
  ],
  purge: {
    enabled: false, //true for production build
    content: [
        '../**/templates/*.html',
        '../**/templates/**/*.html'
    ]
  },
  // darkMode: 'dark',
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
       'cam-blue': "#242056",
       'cam-red': "#e10110",
       'cam-gold': "#d6a53f",

       'bg-color': '#d1e2ef',
      },

      fontFamily: {
       
      Barlow: ['Barlow', 'sans-serif'],
      Lora: ['Lora', 'serif'],
      Mulish: ['Mulish', 'sans-serif'],
      ching: ['Noto Sans JP', 'sans-serif'],


       },

       fontSize: {
        'xxs': '0.3rem',
      },

      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
      }

    },

  },
  plugins: [require('@tailwindcss/line-clamp')],


}