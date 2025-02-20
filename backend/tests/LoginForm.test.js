import { render, screen, fireEvent } from "@testing-library/react";
import LoginForm from "./LoginForm";

test("renders login form", () => {
  render(<LoginForm />);
  
  const usernameInput = screen.getByPlaceholderText(/username/i);
  const passwordInput = screen.getByPlaceholderText(/password/i);
  const loginButton = screen.getByText(/login/i);
  
  expect(usernameInput).toBeInTheDocument();
  expect(passwordInput).toBeInTheDocument();
  expect(loginButton).toBeInTheDocument();
});

test("submits login form", () => {
  render(<LoginForm />);
  
  const usernameInput = screen.getByPlaceholderText(/username/i);
  const passwordInput = screen.getByPlaceholderText(/password/i);
  const loginButton = screen.getByText(/login/i);
  
  fireEvent.change(usernameInput, { target: { value: "testuser" } });
  fireEvent.change(passwordInput, { target: { value: "password123" } });
  fireEvent.click(loginButton);
  
  // Add assertions based on expected behavior after submission.
});
