<script lang="ts">
	import type { Product } from '$lib/home/Product';

	export let products: Product[];
</script>

<div class="pure-g product-list">
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

			<form class="product-actions pure-form">
				<div class="product-quantity">
					<label for="quantity-{product.id}">Quantity</label>
					<input type="number" id="quantity-{product.id}" value="1" min="1" max="20" required />
				</div>
				<div class="button-container">
					<button type="submit" class="button-choose pure-button">Add to cart</button>
				</div>
			</form>
		</div>
	{/each}
</div>

<style lang="postcss">
	.product-list {
		max-width: var(--content-width);
		margin: 0 auto;
	}

	.product {
		border: 1px solid var(--secondary-color);
		margin: 0 0.5rem 2rem;
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

	.product-actions {
		margin-bottom: 1rem;
		display: flex;
		justify-content: center;
		align-items: center;

		input {
			width: 62px;
			margin-bottom: 0;
			&:invalid {
				border: 1px solid var(--error-color);
			}
		}

		.button-container {
			align-self: flex-end;
		}

		.product-quantity {
			flex: 0 1 auto;
			padding-right: 0.5rem;
		}
	}
</style>
