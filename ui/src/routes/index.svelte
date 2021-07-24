<script context="module" lang="ts">
	import type { Product } from '$lib/home/Product';
	import { API_BASE_URL } from '../lib/Env';

	export async function load({ fetch }) {
		const url = `${API_BASE_URL}/products`;
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
