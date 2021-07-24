describe('productList', () => {
	it('should show at least one product', () => {
		cy.visit('http://localhost:3000');
		cy.get('.product').should('have.length.gte', 1);
	});

	it('should show at least one product when loaded client-side', () => {
		cy.visit('http://localhost:3000');
		cy.get('nav a').first().click();
		cy.get('a.brand').click();
		cy.get('.product').should('have.length.gte', 1);
	});
});
