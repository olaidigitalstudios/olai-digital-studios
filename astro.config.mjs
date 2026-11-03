import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
export default defineConfig({
  site: 'https://olaidigitalstudios.netlify.app',
  base: '/',
  trailingSlash: 'never',
  integrations: [
    tailwind({
      applyBaseStyles: false
    })
  ],
  image: {
    service: {
      entrypoint: 'astro/assets/services/sharp'
    }
  }
});
