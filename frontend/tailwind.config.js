/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#3498DB',
          light: '#5DADE2',
          dark: '#2980B9',
          50: '#EBF5FB',
          100: '#D6EAF8',
          200: '#AED6F1',
          300: '#85C1E9',
          400: '#5DADE2',
          500: '#3498DB', // Our main blue
          600: '#2980B9',
          700: '#216A9D',
          800: '#1A5276',
          900: '#154360',
        },
        gray: {
          50: '#F8FAFC',
          100: '#F1F5F9',
          200: '#E2E8F0',
          300: '#CBD5E1',
          400: '#94A3B8',
          500: '#64748B',
          600: '#475569',
          700: '#334155',
          800: '#1E293B',
          900: '#0F172A',
        },
        accent: {
          light: '#FFF9C4', // Very light yellow accent
          DEFAULT: '#FFF176',
        }
      },
      fontFamily: {
        sans: ['Roboto', 'ui-sans-serif', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Arial', 'sans-serif'],
        display: ['Roboto', 'ui-sans-serif', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Arial', 'sans-serif'],
      },
      borderRadius: {
        'xl': '1rem',
        '2xl': '1.5rem',
        'squircle': '2rem',
      },
      boxShadow: {
        'soft': '0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03)',
        'card': '0 10px 15px -3px rgba(0, 0, 0, 0.04), 0 4px 6px -2px rgba(0, 0, 0, 0.02)',
      },
      spacing: {
        '18': '4.5rem',
      },
      animation: {
        'slide-in': 'slideIn 0.5s ease-out',
      },
      keyframes: {
        slideIn: {
          '0%': { transform: 'translateY(10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        }
      }
    },
  },
  corePlugins: {
    container: false
  },
  plugins: [
    function({ addComponents }) {
      addComponents({
        '.container': {
          maxWidth: '100%',
          '@screen sm': {
            maxWidth: '640px',
          },
          '@screen md': {
            maxWidth: '768px',
          },
          '@screen lg': {
            maxWidth: '1024px',
          },
          '@screen xl': {
            maxWidth: '1280px',
          },
          marginLeft: 'auto',
          marginRight: 'auto',
          paddingLeft: '1rem',
          paddingRight: '1rem',
        },
        '.container-narrow': {
          maxWidth: '100%',
          '@screen sm': {
            maxWidth: '640px',
          },
          '@screen md': {
            maxWidth: '768px',
          },
          '@screen lg': {
            maxWidth: '896px',
          },
          marginLeft: 'auto',
          marginRight: 'auto',
          paddingLeft: '1rem',
          paddingRight: '1rem',
        },
        '.btn': {
          borderRadius: '0.5rem',
          fontWeight: '500',
          display: 'inline-flex',
          alignItems: 'center',
          justifyContent: 'center',
          transition: 'all 150ms ease',
          cursor: 'pointer',
          '&:disabled': {
            opacity: '0.65',
            pointerEvents: 'none'
          }
        },
        '.btn-primary': {
          backgroundColor: '#3498DB',
          color: 'white',
          '&:hover': {
            backgroundColor: '#2980B9'
          },
          '&:focus': {
            boxShadow: '0 0 0 3px rgba(52, 152, 219, 0.5)'
          }
        },
        '.btn-secondary': {
          backgroundColor: '#E2E8F0',
          color: '#475569',
          '&:hover': {
            backgroundColor: '#CBD5E1',
            color: '#334155'
          },
          '&:focus': {
            boxShadow: '0 0 0 3px rgba(226, 232, 240, 0.5)'
          }
        },
        '.section': {
          paddingTop: '4rem',
          paddingBottom: '4rem',
          '@screen md': {
            paddingTop: '6rem',
            paddingBottom: '6rem',
          }
        },
        '.card': {
          backgroundColor: 'white',
          borderRadius: '0.75rem',
          padding: '1.5rem',
          boxShadow: '0 10px 15px -3px rgba(0, 0, 0, 0.04), 0 4px 6px -2px rgba(0, 0, 0, 0.02)',
          transition: 'all 150ms ease',
        }
      })
    }
  ]
}
