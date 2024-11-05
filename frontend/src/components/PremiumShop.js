import React, { useState, useEffect } from "react";
import { getPremiumBenefits, initiatePayment } from "../api/premiumAPI";

const PremiumShop = () => {
  const [benefits, setBenefits] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchBenefits = async () => {
      const data = await getPremiumBenefits();
      setBenefits(data);
      setLoading(false);
    };
    fetchBenefits();
  }, []);

  const handlePurchase = async (benefitId) => {
    const result = await initiatePayment(benefitId);
    if (result.error) {
      alert(result.error);
    } else {
      alert("Payment initiated. Complete in the Pi app.");
    }
  };

  if (loading) return <p>Loading premium shop...</p>;

  return (
    <div className="container">
      <h2>Premium Shop</h2>
      <ul>
        {benefits.map(benefit => (
          <li key={benefit.id}>
            <h3>{benefit.name}</h3>
            <p>{benefit.description}</p>
            <p>Price: {benefit.price_pi} Pi</p>
            <button onClick={() => handlePurchase(benefit.id)}>Purchase</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PremiumShop;
