const formatter = new Intl.NumberFormat('de-DE', {
	style: 'currency',
	currency: 'EUR',
	minimumFractionDigits: 2,
	maximumFractionDigits: 2
});

export function calculateTotal(price: number, quantity: number): number {
	const priceInCent = Math.round(price * 100);
	const totalInCent = priceInCent * quantity;
	return totalInCent / 100;
}

export function formatPrice(price: number) {
	return formatter.format(price);
}
