<script lang="ts">
	import type { Product } from '$lib/home/Product';

	export let products: Product[];
</script>

<div>
	{#each products as product}
		{product.title}
	{/each}
</div>
