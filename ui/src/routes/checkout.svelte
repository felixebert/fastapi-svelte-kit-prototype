<script lang="ts">
	import { goto } from '$app/navigation';
	import { base } from '$app/paths';
	import RequireAuth from '$lib/util/RequireAuth.svelte';
	import CartProvider from '$lib/cart/CartProvider.svelte';
	import { formatPrice } from '$lib/util/money';
	import { API_BASE_URL } from '$lib/Env';
	import type { Cart } from '$lib/cart/Cart';

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

	async function placeOrder(e: Event, cart: Cart) {
		e.preventDefault();
		currentStatus = Status.LOADING;

		const res = await fetch(`${API_BASE_URL}/orders`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				shippingAddress: {
					fullname,
					addressLine1,
					addressLine2,
					zip,
					city,
					country
				},
				products: cart.products
			})
		});

		if (res.ok) {
			const order = await res.json();
			orderNumber = order.label;
			currentStatus = Status.SUCCESS;
		} else {
			if (res.status === 401) {
				goto(`${base}/login?target=checkout`);
			}
			currentStatus = Status.ERROR;
		}
	}
</script>

<svelte:head>
	<title>Climate trees - Checkout</title>
</svelte:head>

<div class="content-container">
	<h1>Checkout</h1>

	<RequireAuth>
		<CartProvider let:cart>
			<form class="pure-form pure-form-stacked" on:submit={(e) => placeOrder(e, cart)}>
				<fieldset>
					<legend>Shipping & Invoice address</legend>
					<p>
						<label for="fullname">Full name</label>
						<input type="text" id="fullname" required bind:value={fullname} />
					</p>

					<p>
						<label for="addressLine1">Address line 1</label>
						<input type="text" id="addressLine1" required bind:value={addressLine1} />
					</p>
					<p>
						<label for="addressLine2">Address line 2</label>
						<input type="text" id="addressLine2" required bind:value={addressLine2} />
					</p>

					<p>
						<label for="zip">Zip</label>
						<input type="text" id="zip" required bind:value={zip} />
					</p>

					<p>
						<label for="city">City</label>
						<input type="text" id="city" required bind:value={city} />
					</p>

					<p>
						<label for="country">Country</label>
						<input type="text" id="country" required bind:value={country} />
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
		</CartProvider>
	</RequireAuth>
</div>
