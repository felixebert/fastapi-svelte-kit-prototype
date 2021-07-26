<script lang="ts">
	import tokenStore from '$lib/stores/tokenStore';
	import { API_BASE_URL } from '../lib/Env';
	import { goto } from '$app/navigation';
	import { base } from '$app/paths';
	import Alert from '../lib/util/Alert.svelte';
	import Spinner from '../lib/util/Spinner.svelte';

	enum Status {
		IDLE,
		LOADING,
		INVALID_CREDENTIALS,
		ERROR,
		SUCCESS
	}

	let username;
	let password;
	let currentStatus = Status.IDLE;

	async function login(e: Event) {
		e.preventDefault();
		currentStatus = Status.LOADING;

		const res = await fetch(`${API_BASE_URL}/token`, {
			method: 'POST',
			body: new URLSearchParams({
				username,
				password
			})
		});

		if (res.ok) {
			const token = await res.json();
			tokenStore.set(token);
			currentStatus = Status.SUCCESS;
			goto(`${base}/`);
		} else if (res.status === 401) {
			currentStatus = Status.INVALID_CREDENTIALS;
		} else {
			currentStatus = Status.ERROR;
		}
	}
</script>

<svelte:head>
	<title>Climate trees - Login</title>
</svelte:head>

<div class="content-container">
	<h1>Login</h1>

	<form class="pure-form pure-form-stacked" on:submit={login}>
		<p>
			<label for="username">Email</label>
			<input type="email" id="username" required autocomplete="username" bind:value={username} />
		</p>

		<p>
			<label for="current-password">Password</label>
			<input
				type="password"
				id="current-password"
				required
				autocomplete="current-password"
				bind:value={password}
			/>
		</p>

		<button
			type="submit"
			class="pure-button pure-button-primary"
			disabled={currentStatus === Status.LOADING || currentStatus === Status.SUCCESS}
			>Sign in</button
		>
	</form>

	{#if currentStatus === Status.INVALID_CREDENTIALS}
		<Alert message="Invalid username or password." />
	{:else if currentStatus === Status.ERROR}
		<Alert message="Connection error or service interruption. Please try it again later." />
	{:else if currentStatus === Status.SUCCESS}
		<Alert message="Login successful." type="success" />
	{:else if currentStatus === Status.LOADING}
		<Spinner />
	{/if}
</div>

<style>
	form {
		margin-bottom: 2rem;
	}
</style>
