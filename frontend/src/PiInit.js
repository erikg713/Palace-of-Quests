import { useEffect } from 'react';

export default function PiInit() {
  useEffect(() => {
    if (window.Pi) {
      window.Pi.init({ version: "2.0", sandbox: process.env.NODE_ENV !== "developement" });
    }
  }, []);
  return null;
}
