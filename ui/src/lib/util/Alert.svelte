<script lang="ts">
	export let type: 'error' | 'success' = 'error';
</script>

<div class="alert alert-{type}" role="alert"><slot /></div>

<style lang="postcss">
	.alert {
		padding: 1rem;
		border-width: 1px;
		border-style: solid;
	}

	.alert-error {
		border-color: var(--error-color);
	}

	.alert-success {
		border-color: var(--success-color);
	}
</style>
