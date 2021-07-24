describe('productList', () => {
	it('should show at least one product', () => {
		cy.visit('/');
		cy.get('.product').should('have.length.gte', 1);
	});

	it('should show at least one product when loaded client-side', () => {
		cy.visit('/');
		cy.get('nav a').first().click();
		cy.get('a.brand').click();
		cy.get('.product').should('have.length.gte', 1);
	});

	describe('add to cart button', () => {
		beforeEach(function () {
			cy.window().then((win) => {
				win.sessionStorage.clear();
			});
		});

		it('should show current quantity in button', () => {
			cy.visit('/');
			cy.get('.add-to-cart button').first().click();
			cy.get('.current-quantity').should('have.text', '1');
		});

		it('should show total cart quantity in nav', () => {
			cy.visit('/');
			cy.get('.add-to-cart').first().children('button').click();
			cy.get('.add-to-cart').last().children('button').click();
			cy.get('nav .cart-link').should('have.text', 'Cart (2)');
		});

		it('should increase quantity on plus click', () => {
			cy.visit('/');
			cy.get('.add-to-cart').first().children('button').click();
			cy.get('.add-to-cart').first().find('button').last().click();
			cy.get('.current-quantity').should('have.text', '2');
		});

		it('should decrease quantity on minus click', () => {
			cy.visit('/');
			cy.get('.add-to-cart').first().children('button').click();
			cy.get('.add-to-cart').first().find('button').first().click();
			cy.get('.current-quantity').should('not.exist');
		});
	});
});
