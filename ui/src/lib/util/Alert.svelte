<script lang="ts">
	export let message: string;
</script>

<div class="alert alert-error" role="alert">{message}</div>

<style lang="postcss">
	.alert {
		padding: 1rem;
	}

	.alert-error {
		border: 1px solid var(--error-color);
	}
</style>
