<script lang="ts">
	import { goto } from '$app/navigation';
	import { base } from '$app/paths';
	import tokenStore from '$lib/stores/tokenStore';
	import { onMount } from 'svelte';
	import Spinner from './Spinner.svelte';

	enum Status {
		LOADING,
		DONE
	}

	let currentStatus = Status.LOADING;

	onMount(() => {
		if ($tokenStore) {
			currentStatus = Status.DONE;
		} else {
			goto(`${base}/`);
		}
	});
</script>

{#if currentStatus === Status.LOADING}
	<Spinner />
{:else}
	<slot />
{/if}
