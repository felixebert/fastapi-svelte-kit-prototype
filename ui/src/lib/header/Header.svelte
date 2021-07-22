<script>
	import { base } from '$app/paths';
	import Nav from '$lib/header/Nav.svelte';
</script>

<header class="pure-menu pure-menu-horizontal">
	<a href={base} class="pure-menu-heading">Climate trees</a>
	<Nav />
</header>

<style>
	header {
		display: flex;
	}
</style>
