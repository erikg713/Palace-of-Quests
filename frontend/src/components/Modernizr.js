import React from "react";

const FeatureTest = () => {
  const supportsFlexbox = Modernizr.flexbox ? "Yes" : "No";

  return (
    <div className="text-center">
      <h3>Feature Detection</h3>
      <p>Does your browser support Flexbox? {supportsFlexbox}</p>
    </div>
  );
};

export default FeatureTest;
