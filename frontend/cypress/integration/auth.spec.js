describe("Pi Network Authentication Flow", () => {
  it("should authenticate user with Pi Network", () => {
    // Visit the app's main page where the sign-in button is located
    cy.visit("http://localhost:3000");

    // Mock Pi.authenticate() in the browser
    cy.window().then((win) => {
      win.Pi = {
        authenticate: (scopes, onIncompletePaymentFound) => {
          return new Promise((resolve) => {
            const fakeAuthResult = {
              user: { username: "test_user" },
              accessToken: "fake_access_token"
            };
            resolve(fakeAuthResult);
          });
        }
      };
    });

    // Simulate clicking the "Sign In with Pi" button
    cy.get("button").contains("Sign In with Pi").click();

    // Verify that the backend received the access token
    cy.intercept("POST", "/signin", (req) => {
      expect(req.body.authResult.accessToken).to.equal("fake_access_token");
      req.reply({ statusCode: 200, body: { message: "User authenticated" } });
    });

    // Check that the user sees a success message or their username
    cy.contains("Welcome, test_user").should("exist");
  });
});
