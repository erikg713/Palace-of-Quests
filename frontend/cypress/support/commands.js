# Cypress support codes
Cypress.Commands.add('mockAPIs', () => {
  cy.intercept('/api/user/*/profile', { fixture: 'profile.json' }).as('getProfile');
  cy.intercept('/api/user/*/quests', { fixture: 'quests.json' }).as('getQuests');
  cy.intercept('/api/user/*/inventory', { fixture: 'inventory.json' }).as('getInventory');
});
