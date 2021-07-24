describe('header', () => {
	describe('brand', () => {
		it('should link to root base path', () => {
			cy.visit('/');
			cy.get('.brand').should('have.attr', 'href').and('equal', '/');
		});
	});

	describe('nav items', () => {
		it('should start with root base path', () => {
			cy.visit('/');
			cy.get('nav li').first().children('a').should('have.attr', 'href').and('match', /^\/.+/);
		});

		it('should highlight when active', () => {
			cy.visit('/');
			cy.get('nav li').first().children('a').click();
			cy.get('nav li').first().should('have.class', 'pure-menu-selected');
		});
	});
});
