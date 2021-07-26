<script lang="ts">
	import type { Cart } from '$lib/cart/Cart';
	import { formatPrice } from '$lib/util/money';

	export let cart: Cart;
</script>

<section class="cart-products">
	{#each cart.products as product}
		<div class="cart-product">
			<h2>{product.title}</h2>
			<div class="cart-quantity">
				{product.quantity}x
			</div>
			<div class="cart-price">
				{formatPrice(product.total)}
			</div>
		</div>
	{/each}
</section>

<style>
	.cart-product {
		display: grid;
		grid-template:
			'title title' auto
			'quantity price' auto / 1fr 1fr;
		padding-bottom: 1rem;
		margin-bottom: 2rem;
	}

	h2 {
		grid-column-end: span 2;
		font-weight: normal;
	}

	.cart-price {
		text-align: right;
	}
</style>
