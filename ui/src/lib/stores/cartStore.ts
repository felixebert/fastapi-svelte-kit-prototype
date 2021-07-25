import { browser } from '$app/env';
import { writable } from 'svelte/store';

const STORAGE_KEY = 'cart';

type CartStoreProduct = {
	id: number;
	quantity: number;
};

export type CartStore = [CartStoreProduct?];

const storedValueRaw = browser ? window.sessionStorage.getItem(STORAGE_KEY) : null;
const { subscribe, set, update } = writable<CartStore>(
	storedValueRaw ? JSON.parse(storedValueRaw) : []
);

export default {
	subscribe,
	set: (value: CartStore) => {
		window.sessionStorage.setItem(STORAGE_KEY, JSON.stringify(value));
		return set(value);
	},
	update
};
