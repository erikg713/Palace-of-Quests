import React from 'react';

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  // Triggered when an error occurs in a child component
  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  // Logs the error, e.g., to an external monitoring service
  componentDidCatch(error, errorInfo) {
    console.error("Logged from ErrorBoundary:", error, errorInfo);
    // Example: Send the error to a service
    // logErrorToService(error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div>
          <h1>Something went wrong.</h1>
          <p>We’re working to fix this issue. Please try again later.</p>
        </div>
      );
    }

    return this.props.children;
  }
}

export default ErrorBoundary;
