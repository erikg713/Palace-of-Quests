// context/LocaleContext.js
import React, { createContext, useContext, useState } from 'react';
import { IntlProvider } from 'react-intl';

// Supported languages and translations
const messages = {
  en: {
    greeting: "Hello, {name}!",
    login: "Login",
  },
  es: {
    greeting: "¡Hola, {name}!",
    login: "Iniciar sesión",
  },
};

const LocaleContext = createContext();

export const useLocale = () => useContext(LocaleContext);

export const LocaleProvider = ({ children }) => {
  const [locale, setLocale] = useState('en');

  return (
    <LocaleContext.Provider value={{ locale, setLocale }}>
      <IntlProvider locale={locale} messages={messages[locale]}>
        {children}
      </IntlProvider>
    </LocaleContext.Provider>
  );
};
