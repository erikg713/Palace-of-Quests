import { createGlobalStyle } from "styled-components";

export const GlobalStyle = createGlobalStyle`
  /* Reset Styles */
  *, *::before, *::after {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
  }

  /* CSS Variables */
  :root {
      --background-color: #f4f4f4;
      --font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      --focus-color: #4a90e2;
  }

  /* Global Styles */
  body {
      font-family: var(--font-family);
      margin: 0;
      padding: 0;
      background-color: var(--background-color);
      color: #333;
  }

  /* Accessibility Enhancements */
  a:focus, button:focus {
      outline: 2px solid var(--focus-color);
  }

  /* Dark Mode Support */
  @media (prefers-color-scheme: dark) {
      :root {
          --background-color: #222;
          --focus-color: #90caf9;
      }
      body {
          background-color: var(--background-color);
          color: #eee;
      }
  }
`;
