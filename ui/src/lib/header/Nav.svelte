<script>
	import { page } from '$app/stores';
	import { base } from '$app/paths';

	const menuItems = [
		{
			path: `${base}/cart`,
			label: 'Cart'
		},
		{
			path: `${base}/login`,
			label: 'Login'
		}
	];
</script>

<nav>
	<ul class="pure-menu-list">
		{#each menuItems as menuItem}
			<li class="pure-menu-item" class:pure-menu-selected={$page.path === menuItem.path}>
				<a href={menuItem.path} class="pure-menu-link">{menuItem.label}</a>
			</li>
		{/each}
	</ul>
</nav>

<style>
	nav {
		flex: 1 1 auto;
		text-align: right;
	}
</style>
