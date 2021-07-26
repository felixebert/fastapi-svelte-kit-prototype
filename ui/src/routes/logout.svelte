<script lang="ts">
	import tokenStore from '$lib/stores/tokenStore';
	import Alert from '../lib/util/Alert.svelte';
	import { onMount } from 'svelte';
	import Spinner from '../lib/util/Spinner.svelte';

	onMount(() => {
		tokenStore.set(null);
	});
</script>

<svelte:head>
	<title>Climate trees - Logout</title>
</svelte:head>

<div class="content-container">
	<h1>Logout</h1>

	{#if $tokenStore}
		<Spinner />
	{:else}
		<Alert type="success">Logout successful.</Alert>
	{/if}
</div>
