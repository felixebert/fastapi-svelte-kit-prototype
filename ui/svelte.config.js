import preprocess from 'svelte-preprocess';
import autoprefixer from 'autoprefixer';
import postcssNested from 'postcss-nested';
import adapter from '@sveltejs/adapter-static';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://github.com/sveltejs/svelte-preprocess
	// for more information about preprocessors
	preprocess: preprocess({
		postcss: {
			plugins: [postcssNested(), autoprefixer()]
		}
	}),

	kit: {
		// hydrate the <div id="svelte"> element in src/app.html
		target: '#svelte',
		adapter: adapter(),
		paths: {
			base: process.env.BASE_PATH || ''
		}
	}
};

export default config;
