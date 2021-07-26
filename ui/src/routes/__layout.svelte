<script>
	import Header from '$lib/header/Header.svelte';
</script>

<Header />
<slot />

<style global lang="postcss">
	@import 'purecss/build/pure.css';

	:root {
		/* naming is inspired by material ui color system */
		--content-width: 800px;
		--primary-color: #fff;
		--secondary-color: #c8e6c9;
		--error-color: #ff0000;
		--on-primary-color: #000;
		--on-secondary-color: var(--on-primary-color);
	}

	.content-container {
		max-width: var(--content-width);
		margin: 0 auto;
		padding: 0 1rem;

		h1 {
			margin: 3rem 0;
		}
	}

	.pure-button {
		background-color: var(--secondary-color);
		color: var(--on-secondary-color);
	}

	.pure-form input[type] {
		border-color: var(--secondary-color);
		padding: calc(0.5em - 1px) 0.6em;
	}

	.pure-menu-link,
	.pure-menu-heading {
		color: var(--on-primary-color);
	}

	.pure-menu-active > .pure-menu-link,
	.pure-menu-link:hover,
	.pure-menu-link:focus,
	.pure-menu-selected > .pure-menu-link {
		background-color: var(--secondary-color);
	}
</style>
