import { writableSessionStore } from '$lib/util/writableSessionStore';

const STORAGE_KEY = 'token';

export type Token = {
	access_token: string;
	token_type: string;
};

export default writableSessionStore<Token>(STORAGE_KEY);
