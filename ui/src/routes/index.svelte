<script context="module" lang="ts">
	import type { Product } from '$lib/home/Product';

	export async function load({ fetch }) {
		const url = `http://localhost:8000/products`;
		const res = await fetch(url);
		const products: Product[] = await res.json();

		if (res.ok) {
			return {
				props: {
					products
				}
			};
		}

		return {
			status: res.status,
			error: new Error(`Could not load ${url}`)
		};
	}
</script>

<script lang="ts">
	import Banner from '$lib/home/Banner.svelte';
	import ProductList from '$lib/home/ProductList.svelte';

	export let products: Product[];
</script>

<svelte:head>
	<title>Rapid-growing, co2-saving trees</title>
</svelte:head>

<Banner />
<ProductList {products} />
