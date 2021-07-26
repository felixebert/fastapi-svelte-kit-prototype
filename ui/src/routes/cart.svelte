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
				<h2>Total</h2>
				<strong>{formatPrice(cart.total)}</strong>
			</div>

			<form action={`${base}/login`} method="GET">
				<input type="hidden" name="target" value="checkout" />
				<button>Order now</button>
			</form>
		</CartProvider>
	{:else if browser}
		<p>Cart is empty.</p>
	{/if}
</div>

<style lang="postcss">
	.total {
		border-top: 1px solid var(--on-primary-color);
		margin-top: 3rem;
		padding-top: 1rem;
		display: grid;
		grid-template-columns: 1fr 1fr;

		h2 {
			margin: 0;
		}

		:last-child {
			text-align: right;
		}
	}

	form {
		margin-top: 4rem;
	}
</style>
