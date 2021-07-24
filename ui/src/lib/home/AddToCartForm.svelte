<script lang="ts">
	import cartStore from '$lib/stores/cartStore';

	export let id: number;

	$: cart = [...$cartStore];
	$: cartEntry = cart.find((p) => p.id === id);

	$: addToCart = () => {
		if (!cartEntry) {
			cart.push({ id, quantity: 1 });
		} else {
			cartEntry.quantity = 1;
		}
		cartStore.set(cart);
	};

	$: updateQuantity = (qty: number) => {
		cartEntry.quantity = qty;
		cartStore.set(cart);
	};

	$: incQuantity = () => updateQuantity(cartEntry.quantity + 1);
	$: decQuantity = () => updateQuantity(cartEntry.quantity - 1);
</script>

<form class="add-to-cart">
	{#if !cartEntry || cartEntry.quantity <= 0}
		<button type="button" class="pure-button" on:click={addToCart}>Add to cart</button>
	{:else}
		<div class="pure-button">
			<button type="button" on:click={decQuantity}>-</button>
			<span class="current-quantity">{cartEntry.quantity}</span>
			<button type="button" on:click={incQuantity} disabled={cartEntry.quantity >= 20}>+</button>
		</div>
	{/if}
</form>

<style lang="postcss">
	.add-to-cart {
		margin-bottom: 1rem;
		text-align: center;
	}
</style>
