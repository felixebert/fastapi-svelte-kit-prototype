import { writableSessionStore } from '$lib/util/writableSessionStore';

const STORAGE_KEY = 'cart';

type CartStoreProduct = {
	id: number;
	quantity: number;
};

export type CartStore = [CartStoreProduct?];

export default writableSessionStore<CartStore>(STORAGE_KEY, []);
