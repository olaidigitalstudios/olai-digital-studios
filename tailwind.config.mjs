/** @type {import('tailwindcss').Config} */
export default {
  future: {
    hoverOnlyWhenSupported: true
  },
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        void: '#0C0D0E',
        surface: {
          DEFAULT: '#141518',
          elevated: '#1C1E22',
          highlight: '#262930'
        },
        accent: {
          gold: '#E5B869',
          terracotta: '#E07A5F',
          amber: '#F59E0B'
        }
      },
      fontFamily: {
        display: ['"Manrope"', 'system-ui', 'sans-serif'],
        sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
        brand: ['"Bodoni Moda"', 'Georgia', 'serif']
      },
      boxShadow: {
        'glow-gold': '0 0 24px -4px rgba(229, 184, 105, 0.35)',
        'card-hover': '0 12px 30px -10px rgba(0, 0, 0, 0.8), 0 0 20px -5px rgba(229, 184, 105, 0.15)'
      },
      aspectRatio: {
        'card-art': '16 / 9'
      },
      transitionDuration: {
        stagger: 'var(--duration-stagger)',
        micro: 'var(--duration-micro)',
        quick: 'var(--duration-quick)',
        fast: 'var(--duration-fast)',
        medium: 'var(--duration-medium)',
        slow: 'var(--duration-slow)',
        'very-slow': 'var(--duration-very-slow)',
      },
      transitionTimingFunction: {
        'smooth-out': 'var(--ease-smooth-out)',
        'spring-soft': 'var(--ease-spring-soft)',
      }
    }
  },
  plugins: []
};
