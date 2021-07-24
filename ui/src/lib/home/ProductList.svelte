<script lang="ts">
	import type { Product } from '$lib/home/Product';
	import AddToCartForm from '$lib/home/AddToCartForm.svelte';

	export let products: Product[];
</script>

<main class="pure-g product-list content-container">
	{#each products as product}
		<div class="product pure-u-1 pure-u-md-1-3">
			<div class="product-header">
				<h2>{product.title}</h2>

				<span class="product-price">
					{product.price}€
				</span>
			</div>

			<div class="product-description">
				{product.description}
			</div>

			<AddToCartForm id={product.id} />
		</div>
	{/each}
</main>

<style lang="postcss">
	.product {
		border: 1px solid var(--secondary-color);
		margin-bottom: 1rem;
	}

	.product-header {
		display: flex;
		flex-direction: column;
		justify-content: center;
		padding: 3rem 0;
		background: var(--secondary-color);
		color: var(--on-secondary-color);
		text-align: center;

		h2 {
			font-size: 3.5rem;
			margin: 0;
			text-transform: uppercase;
			font-weight: normal;
		}
	}

	.product-price {
		letter-spacing: 0.25em;
		font-size: 1.25rem;
	}

	.product-description {
		padding: 2rem 1rem;
	}
</style>
