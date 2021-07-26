<script lang="ts">
	import tokenStore from '$lib/stores/tokenStore';
	import { API_BASE_URL } from '../lib/Env';
	import { goto } from '$app/navigation';
	import { base } from '$app/paths';
	import { page } from '$app/stores';
	import Alert from '../lib/util/Alert.svelte';
	import Spinner from '../lib/util/Spinner.svelte';
	import { onMount } from 'svelte';

	enum Status {
		IDLE,
		LOADING,
		INVALID_CREDENTIALS,
		ERROR,
		SUCCESS,
		LOGGED_IN
	}

	const SUBMITTABLE_WHEN = [Status.IDLE, Status.INVALID_CREDENTIALS, Status.ERROR];

	const TARGETS = {
		checkout: `${base}/checkout`,
		home: `${base}/`
	};
	const DEFAULT_TARGET = 'home';

	let username;
	let password;
	let currentStatus = Status.LOADING;

	function redirectToTarget(fallback?: string) {
		const target = TARGETS[$page.query.get('target')] || fallback;
		if (target) {
			goto(target);
		}
	}

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
			redirectToTarget(DEFAULT_TARGET);
		} else if (res.status === 401) {
			currentStatus = Status.INVALID_CREDENTIALS;
		} else {
			currentStatus = Status.ERROR;
		}
	}

	onMount(async () => {
		if (!$tokenStore) {
			currentStatus = Status.IDLE;
		} else {
			const res = await fetch(`${API_BASE_URL}/users/me`, {
				headers: {
					Authorization: `Bearer ${$tokenStore.access_token}`
				}
			});
			if (res.ok) {
				currentStatus = Status.LOGGED_IN;
				redirectToTarget();
			} else {
				tokenStore.set(null);
				currentStatus = Status.IDLE;
			}
		}
	});
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
			disabled={!SUBMITTABLE_WHEN.includes(currentStatus)}>Sign in</button
		>
	</form>

	{#if currentStatus === Status.INVALID_CREDENTIALS}
		<Alert message="Invalid username or password." />
	{:else if currentStatus === Status.ERROR}
		<Alert message="Connection error or service interruption. Please try it again later." />
	{:else if currentStatus === Status.SUCCESS}
		<Alert message="Login successful." type="success" />
	{:else if currentStatus === Status.LOGGED_IN}
		<Alert message="You are already logged in." type="success" />
	{:else if currentStatus === Status.LOADING}
		<Spinner />
	{/if}
</div>

<style>
	form {
		margin-bottom: 2rem;
	}
</style>
