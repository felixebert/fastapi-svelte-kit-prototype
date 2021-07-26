<script lang="ts">
	import { base } from '$app/paths';
	import CartProvider from '$lib/cart/CartProvider.svelte';
	import CartContent from '$lib/cart/CartContent.svelte';
	import { formatPrice } from '$lib/util/money';
</script>

<svelte:head>
	<title>Climate trees - Cart</title>
</svelte:head>

<div class="content-container">
	<h1>Cart</h1>

	<CartProvider let:cart>
		{#if cart}
			<CartContent {cart} />

			<div class="total">
				{formatPrice(cart.total)}
			</div>

			<form action={`${base}/checkout/auth`}>
				<button>Order now</button>
			</form>
		{/if}
	</CartProvider>
</div>

<style lang="postcss">
</style>
