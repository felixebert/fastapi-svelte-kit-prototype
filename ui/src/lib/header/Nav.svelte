<script>
	import { page } from '$app/stores';
	import { base } from '$app/paths';
	import cartStore from '$lib/stores/cartStore';
	import tokenStore from '$lib/stores/tokenStore';

	let totalQuantityInCart;
	$: totalQuantityInCart = $cartStore.reduce((accumulator, p) => accumulator + p.quantity, 0);

	const cartPath = `${base}/cart`;
	const loginPath = `${base}/login`;
	const logoutPath = `${base}/logout`;
</script>

<nav>
	<ul class="pure-menu-list">
		<li class="pure-menu-item" class:pure-menu-selected={$page.path === cartPath}>
			<a href={cartPath} class="pure-menu-link cart-link">
				Cart {#if totalQuantityInCart > 0}({totalQuantityInCart}){/if}
			</a>
		</li>
		<li class="pure-menu-item" class:pure-menu-selected={$page.path === loginPath}>
			{#if $tokenStore}
				<a href={logoutPath} class="pure-menu-link">Logout</a>
			{:else}
				<a href={loginPath} class="pure-menu-link">Login</a>
			{/if}
		</li>
	</ul>
</nav>

<style>
	nav {
		flex: 1 1 auto;
		text-align: right;
	}
</style>
