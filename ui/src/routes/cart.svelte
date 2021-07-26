<script lang="ts">
	import { base } from '$app/paths';
	import { browser } from '$app/env';
	import CartProvider from '$lib/cart/CartProvider.svelte';
	import CartContent from '$lib/cart/CartContent.svelte';
	import cartStore from '$lib/stores/cartStore';
	import { formatPrice } from '$lib/util/money';
</script>

<svelte:head>
	<title>Climate trees - Cart</title>
</svelte:head>

<div class="content-container">
	<h1>Cart</h1>

	{#if $cartStore.length > 0}
		<CartProvider let:cart>
			<CartContent {cart} />

			<div class="total">
				{formatPrice(cart.total)}
			</div>

			<form action={`${base}/checkout/auth`}>
				<button>Order now</button>
			</form>
		</CartProvider>
	{:else if browser}
		<p>Cart is empty.</p>
	{/if}
</div>

<style lang="postcss">
</style>
