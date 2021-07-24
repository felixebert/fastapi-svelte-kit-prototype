<script>
	import { assets } from '$app/paths';
</script>

<div class="banner">
	<picture>
		<source srcset="{assets}/home/banner-medium.jpg" media="(min-width: 641px)" />
		<source srcset="{assets}/home/banner-large.jpg" media="(min-width: 1921px)" />
		<img src="{assets}/home/banner-small.jpg" alt="A full-grown tree" />
	</picture>
	<h1 class="banner-head">
		Buy fast growing trees.<br />
		Save the planet!
	</h1>
</div>

<style>
	.banner {
		position: relative;
		display: flex;
		justify-content: center;
		align-items: center;
		text-align: center;
		color: #fff;
		height: 33vh;
		background: rgba(0, 0, 0, 0.2);
		margin-bottom: 1rem;
	}

	.banner img {
		position: absolute;
		inset: 0;
		z-index: -1;
		width: 100%;
		height: 100%;
		object-fit: cover;
	}

	.banner-head {
		font-weight: 500;
		text-shadow: 0 1px 1px #000;
	}
</style>
