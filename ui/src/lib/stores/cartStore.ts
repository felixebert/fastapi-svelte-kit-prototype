import { browser } from '$app/env';
import { writable } from 'svelte/store';

const STORAGE_KEY = 'cart';

type CartProduct = {
	id: number;
	quantity: number;
};

type Cart = [CartProduct?];

const storedValueRaw = browser ? window.sessionStorage.getItem(STORAGE_KEY) : null;
const { subscribe, set, update } = writable<Cart>(storedValueRaw ? JSON.parse(storedValueRaw) : []);

export default {
	subscribe,
	set: (value: Cart) => {
		window.sessionStorage.setItem(STORAGE_KEY, JSON.stringify(value));
		return set(value);
	},
	update
};
