<script lang="ts">
	import { goto } from '$app/navigation';
	import { base } from '$app/paths';
	import RequireAuth from '$lib/util/RequireAuth.svelte';
	import CartProvider from '$lib/cart/CartProvider.svelte';
	import { formatPrice } from '$lib/util/money';
	import { API_BASE_URL } from '$lib/Env';
	import tokenStore from '$lib/stores/tokenStore';
	import cartStore from '$lib/stores/cartStore';
	import Alert from '../lib/util/Alert.svelte';
	import { onMount } from 'svelte';

	enum Status {
		IDLE,
		LOADING,
		ERROR,
		SUCCESS
	}

	let fullname;
	let addressLine1;
	let addressLine2;
	let zip;
	let city;
	let country;
	let orderNumber;
	let currentStatus = Status.IDLE;

	async function placeOrder(e: Event) {
		e.preventDefault();
		currentStatus = Status.LOADING;

		try {
			const res = await fetch(`${API_BASE_URL}/orders`, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
					Authorization: `Bearer ${$tokenStore.access_token}`
				},
				body: JSON.stringify({
					order_request: {
						shipping_address: {
							fullname,
							address_line1: addressLine1,
							address_line2: addressLine2,
							zip,
							city,
							country
						},
						items: $cartStore
					}
				})
			});

			if (res.ok) {
				const order = await res.json();
				orderNumber = order.label;
				cartStore.set([]);
				currentStatus = Status.SUCCESS;
			} else {
				if (res.status === 401) {
					goto(`${base}/login?target=checkout`);
				}
				currentStatus = Status.ERROR;
			}
		} catch (e) {
			console.error('send order error', e);
			currentStatus = Status.ERROR;
		}
	}

	onMount(() => {
		if ($cartStore.length <= 0) {
			goto(`${base}/`);
		}
	});
</script>

<svelte:head>
	<title>Climate trees - Checkout</title>
</svelte:head>

<div class="content-container">
	<h1>Checkout</h1>

	{#if currentStatus === Status.SUCCESS}
		<Alert type="success">
			<p>Order completed.</p>
			<p>Your order number for further reference: {orderNumber}</p>
		</Alert>
	{:else if $cartStore.length > 0}
		<RequireAuth>
			<CartProvider let:cart>
				<form class="pure-form pure-form-stacked" on:submit={placeOrder}>
					<fieldset>
						<legend>Shipping & Invoice address</legend>
						<p>
							<label for="fullname">Full name</label>
							<input
								type="text"
								id="fullname"
								autocomplete="shipping name"
								required
								bind:value={fullname}
							/>
						</p>

						<p>
							<label for="addressLine1">Address line 1</label>
							<input
								type="text"
								id="addressLine1"
								autocomplete="shipping address-line1"
								required
								bind:value={addressLine1}
							/>
						</p>
						<p>
							<label for="addressLine2">Address line 2</label>
							<input
								type="text"
								id="addressLine2"
								autocomplete="shipping address-line2"
								bind:value={addressLine2}
							/>
						</p>

						<p>
							<label for="zip">Zip</label>
							<input
								type="text"
								id="zip"
								autocomplete="shipping postal-code"
								required
								bind:value={zip}
							/>
						</p>

						<p>
							<label for="city">City</label>
							<input
								type="text"
								id="city"
								autocomplete="shipping address-level2"
								required
								bind:value={city}
							/>
						</p>

						<p>
							<label for="country">Country</label>
							<input
								type="text"
								id="country"
								autocomplete="shipping country"
								required
								bind:value={country}
							/>
						</p>
					</fieldset>
					<fieldset>
						<legend>Products</legend>
						<ul>
							{#each cart.products as product}
								<li>{product.quantity}x {product.title}: {formatPrice(product.total)}</li>
							{/each}
						</ul>
					</fieldset>

					<p><strong>{formatPrice(cart.total)}</strong></p>

					<button
						type="submit"
						class="pure-button pure-button-primary"
						disabled={currentStatus !== Status.IDLE && currentStatus !== Status.ERROR}
						>Complete order
					</button>
				</form>

				{#if currentStatus === Status.ERROR}
					<Alert>Could not complete order. Please try again later.</Alert>
				{/if}
			</CartProvider>
		</RequireAuth>
	{/if}
</div>

<style>
	form {
		margin-bottom: 2rem;
	}
</style>
