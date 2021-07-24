<script>
	import { page } from '$app/stores';
	import { base } from '$app/paths';
	import cartStore from '$lib/stores/cartStore';

	let totalQuantityInCart;
	$: totalQuantityInCart = $cartStore.reduce((accumulator, p) => accumulator + p.quantity, 0);
</script>

<nav>
	<ul class="pure-menu-list">
		<li class="pure-menu-item" class:pure-menu-selected={$page.path === `${base}/cart`}>
			<a href={`${base}/cart`} class="pure-menu-link">
				Cart
				{#if totalQuantityInCart > 0}
					<span class="badge">{totalQuantityInCart}</span>
				{/if}
			</a>
		</li>
		<li class="pure-menu-item" class:pure-menu-selected={$page.path === `${base}/login`}>
			<a href={`${base}/login`} class="pure-menu-link">Login</a>
		</li>
	</ul>
</nav>

<style>
	nav {
		flex: 1 1 auto;
		text-align: right;
	}

	.badge {
		background: var(--secondary-color);
		padding: 3px 8px;
		border-radius: 50%;
	}
</style>
