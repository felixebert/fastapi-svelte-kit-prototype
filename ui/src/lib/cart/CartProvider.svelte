<script lang="ts">
	import cartStore from '$lib/stores/cartStore';
	import type { CartStore } from '$lib/stores/cartStore';
	import { convertToCart } from '$lib/cart/Cart';
	import type { Cart } from '$lib/cart/Cart';
	import { onMount } from 'svelte';
	import { API_BASE_URL } from '$lib/Env';
	import type { Product } from '$lib/home/Product';
	import Spinner from '$lib/util/Spinner.svelte';
	import Alert from '$lib/util/Alert.svelte';

	enum Status {
		LOADING,
		ERROR,
		DONE
	}

	let currentStatus = Status.LOADING;
	let cart: Cart;

	onMount(async () => {
		const res = await fetch(`${API_BASE_URL}/products`);
		if (res.ok) {
			currentStatus = Status.DONE;
			const products: Product[] = await res.json();
			const cartStoreProducts = $cartStore as CartStore;
			cart = convertToCart(cartStoreProducts, products);
		} else {
			currentStatus = Status.ERROR;
		}
	});
</script>

{#if currentStatus === Status.LOADING}
	<Spinner />
{:else if currentStatus === Status.ERROR}
	<Alert message="Connection error. Please try it again" />
{:else}
	<slot {cart} />
{/if}
