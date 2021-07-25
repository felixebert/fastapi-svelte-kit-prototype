<script lang="ts">
	import type { Cart } from '$lib/cart/Cart';
	import { formatPrice } from '$lib/util/money';

	export let cart: Cart;
</script>

<section class="cart-products">
	{#each cart.products as product}
		<div class="cart-product">
			{product.title}:
			{formatPrice(product.total)}
		</div>
	{/each}
</section>
