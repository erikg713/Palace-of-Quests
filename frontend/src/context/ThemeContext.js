// context/ThemeContext.js
import React, { createContext, useContext, useState, useEffect } from 'react';

// Define available themes
const themes = {
  light: {
    '--primary-color': '#ffffff',
    '--secondary-color': '#f5f5f5',
    '--text-color': '#000000',
  },
  dark: {
    '--primary-color': '#2d2d2d',
    '--secondary-color': '#1c1c1c',
    '--text-color': '#ffffff',
  },
};

const ThemeContext = createContext();

export const useTheme = () => useContext(ThemeContext);

export const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState('light');

  // Update CSS variables dynamically based on theme
  useEffect(() => {
    const currentTheme = themes[theme];
    Object.keys(currentTheme).forEach((key) => {
      document.documentElement.style.setProperty(key, currentTheme[key]);
    });
  }, [theme]);

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};
