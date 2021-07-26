<script lang="ts">
	import { API_BASE_URL } from '../lib/Env';
	import Alert from '../lib/util/Alert.svelte';
	import Spinner from '../lib/util/Spinner.svelte';

	enum Status {
		IDLE,
		LOADING,
		INVALID_CREDENTIALS,
		ERROR
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
			// store
			currentStatus = Status.IDLE;
			let message = await res.json();
			console.log(message);
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
			disabled={currentStatus === Status.LOADING}>Sign in</button
		>
	</form>

	{#if currentStatus === Status.INVALID_CREDENTIALS}
		<Alert message="Invalid username or password." />
	{:else if currentStatus === Status.ERROR}
		<Alert message="Connection error or service interruption. Please try it again later." />
	{:else if currentStatus === Status.LOADING}
		<Spinner />
	{/if}
</div>

<style>
	form {
		margin-bottom: 2rem;
	}
</style>
