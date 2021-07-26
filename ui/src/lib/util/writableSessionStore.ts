import { browser } from '$app/env';
import { writable } from 'svelte/store';
import type { Writable } from 'svelte/types/runtime/store';

export interface WritableSessionStore<T> extends Writable<T> {}

export function writableSessionStore<T>(
	storageKey: string,
	defaultValue?: T
): WritableSessionStore<T> {
	const storedValueRaw = browser ? window.sessionStorage.getItem(storageKey) : null;
	const initialValue = storedValueRaw ? JSON.parse(storedValueRaw) : defaultValue;
	const { subscribe, set, update } = writable<T>(initialValue);

	return {
		subscribe,
		set: (value: T) => {
			window.sessionStorage.setItem(storageKey, JSON.stringify(value));
			return set(value);
		},
		update
	};
}
