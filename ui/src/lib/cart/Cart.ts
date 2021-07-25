import type { Product } from '$lib/home/Product';
import type { CartStore } from '$lib/stores/cartStore';
import { calculateTotal } from '$lib/util/money';

export type CartProduct = Product & {
	quantity: number;
	total: number;
};

export type Cart = {
	products: CartProduct[];
	total: number;
};

export function convertToCart(cartStore: CartStore, allProducts: Product[]): Cart {
	const cartProducts = cartStore
		.map((cartStoreEntry) => {
			const product = allProducts.find((p) => p.id === cartStoreEntry.id);
			if (!product) return null;
			const total = calculateTotal(product.price, cartStoreEntry.quantity);
			return { ...product, quantity: cartStoreEntry.quantity, total };
		})
		.filter((e) => e);

	const total = cartProducts.reduce((result, product) => result + product.total, 0);

	return {
		products: cartProducts,
		total
	};
}
